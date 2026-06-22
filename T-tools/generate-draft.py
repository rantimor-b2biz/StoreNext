#!/usr/bin/env python3
"""
StoreNext Weekly LinkedIn Draft Generator
Runs inside GitHub Actions on Friday 09:00 UTC.
Calls Claude API with the full agent pipeline and saves draft to drafts/W[NN]-draft.md
"""

import os
import datetime
import anthropic

# ── Config ────────────────────────────────────────────────────────────────────
REPO_ROOT   = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRAFTS_DIR  = os.path.join(REPO_ROOT, "drafts")
MODEL       = "claude-sonnet-4-6"

# ── Helpers ───────────────────────────────────────────────────────────────────
def read(path):
    full = os.path.join(REPO_ROOT, path)
    try:
        with open(full, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"[FILE NOT FOUND: {path}]"

def iso_week(date=None):
    d = date or datetime.date.today()
    return f"W{d.isocalendar()[1]:02d}"

def current_date():
    override = os.environ.get("OVERRIDE_DATE", "").strip()
    if override:
        return datetime.date.fromisoformat(override)
    return datetime.date.today()

# ── Context loader ─────────────────────────────────────────────────────────────
def build_context():
    return {
        "voice_dna":        read("C-core/voice-dna.md"),
        "icp_profile":      read("C-core/icp-profile.md"),
        "brand_standards":  read("C-core/brand-standards.md"),
        "content_calendar": read("B-brain/content-calendar.md"),
        "content_plan":     read("B-brain/linkedin-content-plan.md"),
        "learning_log":     read("M-memory/learning-log.md"),
        "decisions":        read("M-memory/decisions.md"),
    }

# ── Prompt ────────────────────────────────────────────────────────────────────
def build_prompt(ctx, week, today):
    return f"""You are running the StoreNext weekly LinkedIn content pipeline for {week} (date: {today}).

You have the full authority of the Researcher, Strategist, Copywriter, and Gatekeeper agents.
Run the complete pipeline in one pass and output a publish-ready LinkedIn post.

## Context

### Voice & Tone (voice-dna.md)
{ctx['voice_dna']}

### ICP Profile
{ctx['icp_profile']}

### Brand Standards
{ctx['brand_standards']}

### Content Calendar (publication history + variety rules)
{ctx['content_calendar']}

### 47-Week Content Plan
{ctx['content_plan']}

### Learning Log (what worked)
{ctx['learning_log']}

### Strategic Decisions
{ctx['decisions']}

## Your Task

**Step 1 — Context Check (Track D)**
- Check: is there a Jewish holiday or Israeli national event this week ({today})?
- Check: is there breaking procurement/supply chain news relevant to StoreNext?
- Decision: proceed as planned, or flag a deviation with recommendation.

**Step 2 — Topic Selection**
- Check the content calendar: what categories were used in the last 2 weeks?
- Apply variety rule: do not repeat the same category 3 times in a row.
- Find the current week's slot in the 47-week content plan.
- Select the best topic for {week} and explain why.

**Step 3 — Write the LinkedIn Post**
- Language: English (default)
- Format: follow StoreNext voice standards exactly (no hype, no em-dashes, data-backed, short sentences)
- Length: 150-250 words
- Structure: Hook (2 lines max) → Problem/insight → Data point with source → StoreNext angle → Engagement question
- Hashtags: 3-4 relevant enterprise hashtags at the end

**Step 4 — Gatekeeper Check**
Self-review the post against voice-dna.md before outputting. Fix any violations.

## Output Format

Output ONLY the following markdown. No preamble, no explanation outside the template.

---
# LinkedIn Draft — {week}
**Date generated:** {today}
**Category:** [category name]
**Topic:** [topic]
**Language:** English
**Status:** DRAFT — pending Ran's review

---

[POST TEXT HERE — ready to copy-paste to LinkedIn]

---

## Generation Notes
- Context check: [result]
- Category used: [category] | Last 2 weeks: [categories]
- Variety rule: [pass/flag]
- Topic source: [line from content plan or rationale]
- Gatekeeper flags: [none / list any]
"""

# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    today  = current_date()
    week   = iso_week(today)
    outdir = DRAFTS_DIR
    os.makedirs(outdir, exist_ok=True)
    outfile = os.path.join(outdir, f"{week}-draft.md")

    print(f"Generating draft for {week} ({today})")

    ctx    = build_context()
    prompt = build_prompt(ctx, week, today)

    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    message = client.messages.create(
        model=MODEL,
        max_tokens=2048,
        messages=[{"role": "user", "content": prompt}],
    )

    draft = message.content[0].text

    with open(outfile, "w", encoding="utf-8") as f:
        f.write(draft)

    print(f"Draft saved: {outfile}")

    # Also save to weekly O-output folder (source of truth for content history)
    weekly_dir = os.path.join(REPO_ROOT, "O-output", week, "final")
    os.makedirs(weekly_dir, exist_ok=True)
    weekly_file = os.path.join(weekly_dir, "final-post.md")
    with open(weekly_file, "w", encoding="utf-8") as f:
        f.write(draft)

    print(f"Also saved to: {weekly_file}")
    print(f"Tokens used: input={message.usage.input_tokens}, output={message.usage.output_tokens}")

if __name__ == "__main__":
    main()
