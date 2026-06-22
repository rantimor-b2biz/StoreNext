#!/usr/bin/env python3
"""
StoreNext Weekly Topic Proposals — GitHub Action
Runs every Sunday 06:00 UTC (09:00 IST).

Pipeline:
  Researcher  → research-brief.md   (web search enabled)
  Strategist  → 2 topic options     (with hooks + rationale)

Output: email with 2 options for Ran to choose/edit.
Full post writing happens in ROUTINE after approval.
"""

import os, datetime
import anthropic

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL     = "claude-sonnet-4-6"

# ── Helpers ───────────────────────────────────────────────────────────────────

def read(path):
    try:
        with open(os.path.join(REPO_ROOT, path), encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"[FILE NOT FOUND: {path}]"

def save(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Saved: {path}")

def iso_week(date=None):
    d = date or datetime.date.today()
    return f"W{d.isocalendar()[1]:02d}"

def current_date():
    override = os.environ.get("OVERRIDE_DATE", "").strip()
    return datetime.date.fromisoformat(override) if override else datetime.date.today()

def call(client, system, user, tools=None, max_tokens=2048):
    kwargs = dict(
        model=MODEL,
        max_tokens=max_tokens,
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    if tools:
        kwargs["tools"] = tools
    response = client.messages.create(**kwargs)
    parts = [b.text for b in response.content if b.type == "text"]
    return "\n".join(parts)

# ── Context ───────────────────────────────────────────────────────────────────

def load_context():
    return {
        "voice_dna":  read("C-core/voice-dna.md"),
        "icp":        read("C-core/icp-profile.md"),
        "calendar":   read("B-brain/content-calendar.md"),
        "plan_47":    read("B-brain/linkedin-content-plan.md"),
        "learning":   read("M-memory/learning-log.md"),
        "researcher": read("A-agents/researcher-agent.md"),
        "strategist": read("A-agents/strategist-agent.md"),
    }

# ── Agent 1: Researcher ───────────────────────────────────────────────────────

def run_researcher(client, ctx, week, today, process_dir):
    print(f"\n[1/2] Researcher — {week}...")

    web_search_tool = [{
        "type": "web_search_20250305",
        "name": "web_search",
        "max_uses": 5,
    }]

    system = f"You are the StoreNext Researcher agent.\n{ctx['researcher']}\nToday: {today} | Week: {week}"

    user = f"""Run the research pipeline for {week}.

## Track D — Context Check
- Date: {today}. Any Israeli/Jewish holiday or national event this week?
- Any breaking procurement/supply chain news worth a realtime marketing angle?

## Track A — Industry Research (use web_search)
Find 2-3 current stats on enterprise procurement, supplier portals, or CFO challenges (2025-2026).

## Track B — Competitor Intelligence (use web_search)
What are Coupa, Basware, or Tipalti posting on LinkedIn this week? What gaps exist?

## Track C — Israeli Context (use web_search)
Any recent Israeli finance or procurement news relevant to CFOs?

## Content Calendar
{ctx['calendar']}

## 47-Week Plan
{ctx['plan_47']}

Output a concise Research Brief: context check, 2-3 stats with sources, competitor gaps, 3 content angles.
"""

    result = call(client, system, user, tools=web_search_tool, max_tokens=2500)
    save(os.path.join(process_dir, "research-brief.md"), f"# Research Brief — {week}\n\n{result}")
    return result

# ── Agent 2: Strategist ───────────────────────────────────────────────────────

def run_strategist(client, ctx, research_brief, week, process_dir):
    print(f"\n[2/2] Strategist — proposing 2 options...")

    system = (
        f"You are the StoreNext Strategist agent.\n{ctx['strategist']}\n\n"
        "HARD RULE: Write the ENTIRE output in English. "
        "All hooks, topic names, categories, and rationale must be in English. "
        "LinkedIn content at StoreNext is English only. No Hebrew anywhere."
    )

    user = f"""Based on the research brief, propose exactly 2 topic options for {week}.

LANGUAGE: Write everything in English. The hooks especially must be in English,
because they become the opening lines of the LinkedIn post. No Hebrew.

## Research Brief
{research_brief}

## Content Calendar (variety rules — do not repeat category 3x in a row)
{ctx['calendar']}

## Voice DNA
{ctx['voice_dna']}

## Format for each option:

### Option [A/B]: [Topic name]
**Hook:** [Opening 2 lines of the post — stops scroll, no hype]
**Category:** [from the 6 content categories]
**Format:** [data-led / narrative / case study / quote-driven]
**Why this week:** [1-2 sentences — timing, variety, ICP fit]
**Key stat to use:** [the main data point from research + source]

Keep each option concise. Ran will choose one and run the full ROUTINE session.
"""

    result = call(client, system, user, max_tokens=1000)
    save(os.path.join(process_dir, "weekly-content-plan.md"), f"# Weekly Options — {week}\n\n{result}")
    return result

# ── Email ─────────────────────────────────────────────────────────────────────

def send_email(week, today, options, research_brief):
    import smtplib
    from email.mime.text      import MIMEText
    from email.mime.multipart import MIMEMultipart

    password = os.environ.get("GMAIL_APP_PASS", "")
    if not password:
        print("No GMAIL_APP_PASS — skipping email")
        return

    sender = "rantimor@gmail.com"
    sep    = "=" * 60

    body = "\n".join([
        f"StoreNext {week} — 2 topic options ready for your choice.",
        "",
        "Reply or open a ROUTINE session with your selection.",
        "The ROUTINE will handle full research, writing, Gatekeeper review, and visual.",
        "",
        sep,
        "",
        options,
        "",
        sep,
        "",
        "── Research Brief (background) ──",
        "",
        research_brief,
    ])

    msg = MIMEMultipart()
    msg["Subject"] = f"StoreNext {week} — בחר נושא לפוסט הלינקדאין"
    msg["From"]    = sender
    msg["To"]      = sender
    msg.attach(MIMEText(body, "plain", "utf-8"))

    with smtplib.SMTP("smtp.gmail.com", 587) as s:
        s.starttls()
        s.login(sender, password)
        s.sendmail(sender, sender, msg.as_string())

    print(f"Email sent: StoreNext {week}")

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    today       = current_date()
    week        = iso_week(today)
    process_dir = os.path.join(REPO_ROOT, "O-output", week, "process")
    os.makedirs(process_dir, exist_ok=True)

    print(f"StoreNext topic proposal pipeline — {week} ({today})")

    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    ctx    = load_context()

    research_brief = run_researcher(client, ctx, week, today, process_dir)
    options        = run_strategist(client, ctx, research_brief, week, process_dir)

    send_email(week, today, options, research_brief)
    print(f"\nDone. 2 options sent for {week}.")

if __name__ == "__main__":
    main()
