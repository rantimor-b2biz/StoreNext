#!/usr/bin/env python3
"""
StoreNext Weekly LinkedIn Draft Generator — Full Multi-Agent Pipeline
Each agent runs as a separate Claude API call with its own role and context.

Pipeline:
  Researcher  → research-brief.md      (web search enabled)
  Strategist  → weekly-content-plan.md (picks best topic)
  Copywriter  → copywriter-draft.md    (writes post)
  Gatekeeper  → gatekeeper-review.md   (reviews + fixes)
  Artist      → visual-data.json + PNG

Output: drafts/W[NN]-draft.md + O-output/W[NN]/final/ + email with PNG
"""

import os, json, datetime, subprocess
import anthropic

REPO_ROOT  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL      = "claude-sonnet-4-6"

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
    """Single Claude API call. Returns text response."""
    kwargs = dict(
        model=MODEL,
        max_tokens=max_tokens,
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    if tools:
        kwargs["tools"] = tools

    response = client.messages.create(**kwargs)

    # Collect text + tool results
    text_parts = []
    tool_results = []
    for block in response.content:
        if block.type == "text":
            text_parts.append(block.text)
        elif block.type == "tool_use" and block.name == "web_search":
            tool_results.append(f"[Web search: {block.input.get('query','')}]")

    return "\n".join(text_parts + tool_results)

# ── Context ───────────────────────────────────────────────────────────────────

def load_context():
    return {
        "voice_dna":       read("C-core/voice-dna.md"),
        "icp":             read("C-core/icp-profile.md"),
        "brand":           read("C-core/brand-standards.md"),
        "calendar":        read("B-brain/content-calendar.md"),
        "plan_47":         read("B-brain/linkedin-content-plan.md"),
        "learning":        read("M-memory/learning-log.md"),
        "decisions":       read("M-memory/decisions.md"),
        "researcher_role": read("A-agents/researcher-agent.md"),
        "strategist_role": read("A-agents/strategist-agent.md"),
        "copywriter_role": read("A-agents/copywriter-agent.md"),
        "gatekeeper_role": read("A-agents/gatekeeper-agent.md"),
    }

# ── Agent 1: Researcher ───────────────────────────────────────────────────────

def run_researcher(client, ctx, week, today, process_dir):
    print(f"\n[1/5] Researcher running for {week}...")

    web_search_tool = [{
        "type": "web_search_20250305",
        "name": "web_search",
        "max_uses": 5,
    }]

    system = f"""You are the StoreNext Researcher agent.
{ctx['researcher_role']}

Today: {today} | Week: {week}
"""

    user = f"""Run the full research pipeline for {week}.

## Track D — Context Check (do this first, no search needed)
- Date: {today}
- Check: Jewish holidays or Israeli national events this week?
- Flag if content plan should deviate.

## Track A — Industry Research (use web_search)
Search for: recent enterprise procurement trends, CFO supply chain challenges, supplier portal ROI data (2025-2026).
Find at least 2 statistics with sources.

## Track B — Competitor Intelligence (use web_search)
Search LinkedIn posts from: Coupa, Basware, Tipalti, Tradeshift — what are they posting this week?
Identify gaps StoreNext can own.

## Track C — Israeli Context (use web_search)
Search for: recent Israeli procurement or finance news relevant to CFOs.

## Content Calendar Context
{ctx['calendar']}

## 47-Week Plan
{ctx['plan_47']}

## Learning Log
{ctx['learning']}

Output a structured Research Brief covering:
1. Context check result
2. Key industry stats (with sources)
3. Competitor gaps
4. Israeli context
5. 3 recommended content angles for {week} (respecting variety rules from calendar)
"""

    result = call(client, system, user, tools=web_search_tool, max_tokens=3000)
    save(os.path.join(process_dir, "research-brief.md"), f"# Research Brief — {week}\n\n{result}")
    return result

# ── Agent 2: Strategist ───────────────────────────────────────────────────────

def run_strategist(client, ctx, research_brief, week, today, process_dir):
    print(f"\n[2/5] Strategist running...")

    system = f"""You are the StoreNext Strategist agent.
{ctx['strategist_role']}
"""

    user = f"""Based on the research brief below, select the BEST topic for {week}.

## Research Brief
{research_brief}

## Content Calendar (variety rules)
{ctx['calendar']}

## Your task
1. Check variety: what categories ran last 2 weeks? Do not repeat 3 in a row.
2. Pick ONE topic from the 3 angles in the research brief.
3. Write a clear recommendation with:
   - Selected topic
   - Hook (opening 2 lines of the post)
   - Why this topic, why this week
   - Category
   - Format: data-led / narrative / case study / quote-driven

Output: Weekly Content Plan (short, decisive — one recommendation only).
"""

    result = call(client, system, user, max_tokens=1000)
    save(os.path.join(process_dir, "weekly-content-plan.md"), f"# Weekly Content Plan — {week}\n\n{result}")
    return result

# ── Agent 3: Copywriter ───────────────────────────────────────────────────────

def run_copywriter(client, ctx, research_brief, content_plan, week, today, process_dir):
    print(f"\n[3/5] Copywriter running...")

    system = f"""You are the StoreNext Copywriter agent.
{ctx['copywriter_role']}

HARD RULES:
- Language: English only
- No em dashes (—) anywhere
- No exclamation marks
- Short sentences (10-14 words)
- 150-250 words total
"""

    user = f"""Write the LinkedIn post for {week}.

## Strategist's Plan
{content_plan}

## Research Brief (use the stats)
{research_brief}

## Voice & Tone
{ctx['voice_dna']}

## ICP
{ctx['icp']}

## Post structure:
Hook (2 lines, stops scroll) →
Problem or insight (2-3 sentences) →
Stat with source (1 sentence) →
StoreNext angle (2-3 sentences) →
Engagement question (1 sentence) →
3-4 hashtags

Output ONLY the post text + hashtags. No metadata, no explanation.
"""

    result = call(client, system, user, max_tokens=800)
    save(os.path.join(process_dir, "copywriter-draft.md"), f"# Copywriter Draft — {week}\n\n{result}")
    return result

# ── Agent 4: Gatekeeper ───────────────────────────────────────────────────────

def run_gatekeeper(client, ctx, draft, week, process_dir):
    print(f"\n[4/5] Gatekeeper reviewing...")

    system = f"""You are the StoreNext Gatekeeper agent.
{ctx['gatekeeper_role']}
"""

    user = f"""Review and fix this LinkedIn post for {week}.

## Post to review
{draft}

## Voice DNA (check against this)
{ctx['voice_dna']}

## Check for:
- [ ] No em dashes (—) — replace with periods or commas
- [ ] No exclamation marks
- [ ] No hype words (revolutionary, transformative, disruptive)
- [ ] Short sentences (10-14 words)
- [ ] Data claim has source
- [ ] Ends with engagement question
- [ ] 3-4 hashtags, enterprise-relevant
- [ ] English only
- [ ] 150-250 words

Output TWO sections:
1. REVIEW NOTES (bullet list of issues found and fixes applied)
2. APPROVED POST (the final, corrected post text — ready to publish)
"""

    result = call(client, system, user, max_tokens=1000)
    save(os.path.join(process_dir, "gatekeeper-review.md"), f"# Gatekeeper Review — {week}\n\n{result}")

    # Extract approved post (everything after "APPROVED POST")
    if "APPROVED POST" in result:
        approved = result.split("APPROVED POST", 1)[1].strip().lstrip(":").strip()
    else:
        approved = draft  # fallback: use draft if no clear separation
    return approved, result

# ── Agent 5: Artist ───────────────────────────────────────────────────────────

def run_artist(client, approved_post, week, process_dir, final_dir):
    print(f"\n[5/5] Artist generating visual...")

    system = "You are the StoreNext Artist agent producing visual-data.json for the PNG generator."

    user = f"""Given this approved LinkedIn post, produce visual-data.json.

Rules:
- All fields in English
- visual_type: stat_card (metric-led) | process_flow (sequence) | quote_card (bold statement)
- key_metric: dominant number, short (e.g. "73% fewer exceptions")
- hook: opening line, max 12 words
- visual_direction: one sentence for layout

Output ONLY valid JSON, no markdown fences.

{{
  "week": "{week}",
  "generated": "{datetime.date.today()}",
  "posts": [
    {{
      "post_id": "{week}-01",
      "topic": "...",
      "category": "...",
      "key_metric": "...",
      "hook": "...",
      "visual_type": "stat_card",
      "visual_direction": "...",
      "dimensions": "1080x1350",
      "output_file": "O-output/{week}/final/{week}-01-visual.png"
    }}
  ]
}}

Post:
{approved_post}
"""

    json_text = call(client, system, user, max_tokens=512)
    json_text = json_text.strip()
    if json_text.startswith("```"):
        json_text = "\n".join(l for l in json_text.splitlines() if not l.startswith("```")).strip()

    json_path = os.path.join(process_dir, "visual-data.json")
    save(json_path, json_text)

    generator = os.path.join(os.path.dirname(__file__), "generate-visual.py")
    result = subprocess.run(["python3", generator, json_path], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"Visual error: {result.stderr}")
        return None

    png_path = os.path.join(final_dir, f"{week}-01-visual.png")
    return png_path if os.path.exists(png_path) else None

# ── Email ─────────────────────────────────────────────────────────────────────

def send_email(week, approved_post, png_path, gatekeeper_notes):
    import smtplib
    from email.mime.text      import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.image     import MIMEImage

    password = os.environ.get("GMAIL_APP_PASS", "")
    if not password:
        print("No GMAIL_APP_PASS — skipping email")
        return

    sender = "rantimor@gmail.com"
    sep    = "=" * 60

    body = "\n".join([
        f"StoreNext {week} — LinkedIn post ready for your review.",
        "",
        "To publish: copy the post text below to LinkedIn.",
        "The visual is attached as PNG.",
        "",
        sep,
        "",
        approved_post,
        "",
        sep,
        "",
        "── Gatekeeper Notes ──",
        gatekeeper_notes,
    ])

    msg = MIMEMultipart()
    msg["Subject"] = f"StoreNext {week} — LinkedIn post ready"
    msg["From"]    = sender
    msg["To"]      = sender
    msg.attach(MIMEText(body, "plain", "utf-8"))

    if png_path and os.path.exists(png_path):
        with open(png_path, "rb") as f:
            img = MIMEImage(f.read(), name=os.path.basename(png_path))
        msg.attach(img)
        print(f"Visual attached: {png_path}")

    with smtplib.SMTP("smtp.gmail.com", 587) as s:
        s.starttls()
        s.login(sender, password)
        s.sendmail(sender, sender, msg.as_string())

    print(f"Email sent: StoreNext {week}")

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    today = current_date()
    week  = iso_week(today)

    process_dir = os.path.join(REPO_ROOT, "O-output", week, "process")
    final_dir   = os.path.join(REPO_ROOT, "O-output", week, "final")
    drafts_dir  = os.path.join(REPO_ROOT, "drafts")
    os.makedirs(process_dir, exist_ok=True)
    os.makedirs(final_dir, exist_ok=True)
    os.makedirs(drafts_dir, exist_ok=True)

    print(f"Starting StoreNext content pipeline for {week} ({today})")

    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    ctx    = load_context()

    # Run pipeline
    research_brief  = run_researcher(client, ctx, week, today, process_dir)
    content_plan    = run_strategist(client, ctx, research_brief, week, today, process_dir)
    draft           = run_copywriter(client, ctx, research_brief, content_plan, week, today, process_dir)
    approved, notes = run_gatekeeper(client, ctx, draft, week, process_dir)
    png_path        = run_artist(client, approved, week, process_dir, final_dir)

    # Build final post file
    final_md = f"""# LinkedIn Post — {week}
**Date generated:** {today}
**Status:** DRAFT — pending Ran's review

---

{approved}
"""
    save(os.path.join(final_dir, "final-post.md"), final_md)
    save(os.path.join(drafts_dir, f"{week}-draft.md"), final_md)

    # Send email
    send_email(week, approved, png_path, notes)
    print(f"\nPipeline complete for {week}.")

if __name__ == "__main__":
    main()
