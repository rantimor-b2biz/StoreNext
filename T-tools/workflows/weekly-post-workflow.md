# Weekly Post Workflow

> The end-to-end process for creating a weekly Pilgrim Prayers blog post + newsletter — from topic to published content.

---

## Process Overview

```
[Content Calendar] → This week's topic
         ↓
[Research Agent] → Researches site, trends, audience pulse → research-brief.md
         ↓
[Storyteller Agent] → Writes the blog post draft (reads research-brief.md)
         ↓
[Gatekeeper Agent] → Reviews and approves / sends back
         ↓
[Storyteller Agent] → Revises (if needed)
         ↓
[Gatekeeper Agent] → Final approval of blog post
         ↓
    ┌────────────────┴────────────────┐
    ↓                                 ↓
[Visual Agent]                 [Newsletter Agent]
Creates image brief            Adapts for email
& AI prompts                   newsletter
    ↓                                 ↓
    └────────────────┬────────────────┘
         ↓
[Gatekeeper Agent] → Reviews visuals + newsletter
         ↓
[You] → Generate images, publish blog + send newsletter
         ↓
    ┌────────────────┴────────────────┐
    ↓                                 ↓
[Paid Search Agent]           [Research Agent]
Extracts ad hooks             Tracks performance
from published post           Updates M-memory
```

---

## Step 1: Preparation

### Before Starting

All agents MUST read:
- `C-core/project-brief.md` — Who we are
- `C-core/voice-dna.md` — How we speak
- `C-core/icp-profile.md` — Who we serve
- `M-memory/learning-log.md` — What we've learned
- `B-brain/content-calendar.md` — This week's topic

### Set Up the Project Folder

Create a new folder in `O-output/` with the week number and topic:

```
O-output/
└── [number]-weekly-post-[slug]/
    ├── research-brief.md        ← Research Agent's intel for the Storyteller
    ├── storyteller-draft.md     ← Storyteller's blog post draft
    ├── gatekeeper-review.md     ← Gatekeeper's review
    ├── final-post.md            ← Approved blog post
    ├── visual-brief.md          ← Visual Agent's image direction & AI prompts
    └── newsletter-version.md    ← Newsletter adaptation
```

**Example:** `O-output/14-weekly-post-easter-garden-tomb/`

---

## Step 2: Research Agent Prepares the Brief

### What the Research Agent Does

1. **Reads the content calendar** — What's this week's topic, structure, and site?
2. **Reads the research-skill** — `T-tools/skills/research-skill/research-skill.md`
3. **Researches the site** — Current season, weather, events, sensory details
4. **Checks the Evangelical pulse** — What believers are talking about, feeling, praying about
5. **Finds story hooks** — Scripture connections, historical moments, surprise facts
6. **Saves the brief** — `research-brief.md` in the project folder

### File Format: `research-brief.md`

See `T-tools/skills/research-skill/research-skill.md` for the full template.

The brief includes: site intelligence, scripture connections, story hooks, trending context, visual suggestions, and a recommended emotional angle.

---

## Step 3: Storyteller Writes the Blog Post

### What the Storyteller Does

1. **Reads the research brief** — `O-output/[this-week]/research-brief.md` (site intel, trends, story hooks)
2. **Checks the content calendar** — What's this week's topic, structure, and site?
3. **Reads the weekly-post-skill** — `T-tools/skills/weekly-post-skill/weekly-post-skill.md`
4. **Reads C-core files** — Voice, audience, brand
5. **Writes the draft** — Following the assigned post structure, informed by the research brief
6. **Self-checks** — Against the quality checklist

### File Format: `storyteller-draft.md`

```markdown
# Weekly Post: [Title]

**Week:** [Week number from calendar]
**Date:** [Publication date]
**Topic:** [From content calendar]
**Structure:** [Which of the 6 structures]
**Holy Land Site:** [Featured location]
**Version:** v1

---

## The Post

[Full blog post text — 500-800 words]

---

## Storyteller Notes

### Why This Angle
- [Reasoning for the approach]

### Scripture Used
- [Book Chapter:Verse — and why]

### Emotional Target
- [What should the reader feel?]

### Suggested Imagery
- [Photo ideas for the web team]

### Questions for the Gatekeeper
- [Any uncertainties or alternatives considered]
```

---

## Step 4: Gatekeeper Reviews the Blog Post

### What the Gatekeeper Does

1. **First read** — Initial impression: Does it transport me?
2. **Voice check** — Does it sound like Pilgrim Prayers?
3. **Audience check** — Would an Evangelical Christian feel moved?
4. **Structure check** — Does it follow the assigned structure?
5. **Quality check** — Against the weekly post checklist
6. **Decision** — APPROVE / REVISIONS NEEDED / ESCALATE

### File Format: `gatekeeper-review.md`

```markdown
# Gatekeeper Review: [Title]

**Date:** [Date]
**Version Reviewed:** v1

---

## Status: [APPROVED / REVISIONS NEEDED / ESCALATE]

---

## What's Working
- [Specific strength 1]
- [Specific strength 2]

## What Needs Work
1. **[Issue]** — [How to fix it]
2. **[Issue]** — [How to fix it]

## Evangelical Alignment Check
- [ ] No Catholic-specific references
- [ ] Scripture used naturally (not as sermon)
- [ ] Faith expressed warmly, not preachy
- [ ] No political messaging

## Next Step
[What the Storyteller should do now]
```

---

## Step 5: Revision (If Needed)

If the Gatekeeper sends it back:

1. **Storyteller reads the feedback** — Understands what to fix
2. **Updates `storyteller-draft.md`** — Changes version to `v2`
3. **Gatekeeper reviews again** — Updates `gatekeeper-review.md`
4. **Repeat until approved** — Usually 1-2 rounds max

---

## Step 6: Final Blog Post

When the Gatekeeper approves:

### File Format: `final-post.md`

```markdown
# [Post Title]

**Status:** Approved for publication
**Approved date:** [Date]
**Week:** [Week number]

---

[Clean post text — no notes, no markup, ready to publish]

---

*Created by: Storyteller Agent*
*Reviewed by: Gatekeeper Agent*
```

---

## Step 7: Visual Agent Creates Image Direction

### What the Visual Agent Does

1. **Reads the approved `final-post.md`** and the Storyteller's "Suggested Imagery" notes
2. **Reads `C-core/voice-dna.md`** — Visual Voice section
3. **Creates a visual brief** — Hero image, inline images, newsletter header, social sharing image
4. **Writes AI image prompts** — Ready to use in any image generation tool
5. **Delivers for Gatekeeper review**

### File Format: `visual-brief.md`

```markdown
# Visual Brief: [Post Title]

**Week:** [Number]
**Post Structure:** [Which of the 6]
**Holy Land Site:** [Location]

---

## Hero Image
**Description:** [What the image shows]
**Mood:** [Emotional feeling]
**AI Prompt:** [Full prompt ready to use]

## Inline Image
**Description:** [What it shows]
**Placement:** [After which section]
**AI Prompt:** [Full prompt]

## Newsletter Header
**Description:** [Simplified version for email]
**AI Prompt:** [Adapted prompt]

## Social Sharing Image
**Text Overlay:** [Title text]
**AI Prompt:** [Full prompt]

---

## Visual Agent Notes
- **Color focus:** [Which palette colors]
- **Evangelical check:** [No Catholic/Orthodox iconography]
```

> **Note:** The Visual Agent and Newsletter Agent can work **in parallel** — both start from the approved `final-post.md`.

---

## Step 8: Newsletter Agent Adapts

### What the Newsletter Agent Does

1. **Reads the approved `final-post.md`**
2. **Reads the newsletter-skill** — `T-tools/skills/newsletter-skill/newsletter-skill.md`
3. **Adapts the post** — Subject line, preview text, condensed body, CTA
4. **Delivers for Gatekeeper review**

### File Format: `newsletter-version.md`

```markdown
# Newsletter: [Title]

**Based on:** final-post.md
**Send date:** [Planned date]

---

## Subject Line
[Subject line — max 50 characters]

## Preview Text
[Preview text — 40-90 characters]

---

## Email Body

[Full email text, formatted as it would appear]

---

## Newsletter Agent Notes

### Subject Line Alternatives
1. [Backup option 1]
2. [Backup option 2]

### CTA Chosen
[Which CTA and why]

### What Was Cut
[What was shortened from the blog post and why]
```

---

## Step 9: Gatekeeper Reviews Newsletter + Visuals

Quick review of the newsletter version:

- [ ] Subject line under 50 characters?
- [ ] Preview text complements the subject?
- [ ] Under 500 words?
- [ ] One CTA only?
- [ ] Feels like a letter, not marketing?
- [ ] Warm and personal?

Quick review of the visual brief:

- [ ] Hero image matches the post's story and emotion?
- [ ] Color palette within brand guidelines?
- [ ] No political, violent, or stock-photo elements?
- [ ] Evangelical-appropriate (no Catholic/Orthodox iconography)?
- [ ] AI prompts detailed enough for consistent results?
- [ ] Newsletter header works at small mobile size?

---

## Step 10: Publish & Send

Once all versions are approved:

1. **Generate images** → Use AI prompts from `visual-brief.md`
2. **Blog post** → Publish on pilgrimprayers.org with images
3. **Newsletter** → Send to subscriber list with newsletter header image
4. **Social media** → Share with social sharing image (optional)

---

## Step 11: Paid Search Agent Extracts Ad Hooks (Optional)

After the blog post is published, the **Paid Search Agent** scans it for ad opportunities:

1. **Reads `final-post.md`** -- Looks for phrases that work as search ad headlines or descriptions
2. **Reads `research-brief.md`** -- Cross-references trending keywords and audience pulse
3. **Creates ad copy variants** -- New RSA headlines/descriptions inspired by the post's language
4. **Updates keyword map** -- Adds any new keyword ideas from the post's topic and scripture references
5. **Saves to** -- `O-output/ads/search/[date]-ad-copy.md`

This step runs in parallel with publishing and is optional (not every post generates new ads).

---

## Step 12: Track Performance & Update Memory

After publishing, the **Research Agent** tracks content performance, the **Paid Search Agent** tracks ad performance, and the **Gatekeeper** updates `M-memory/learning-log.md`:

```markdown
## [Date] — Weekly Post: [Title]

**Week:** [Number]
**Structure used:** [Which of the 6]
**Site featured:** [Location]

### What Worked
- [What resonated]

### What We'd Do Differently
- [Lesson for next time]

### Audience Signals
- [Any feedback, shares, replies, prayer submissions]

### Pattern Discovered
- [Any new insight for future posts]
```

---

## Weekly Checklist

### Sunday: Research
- [ ] Research Agent reads content calendar for this week's topic
- [ ] Research Agent researches site, trends, audience pulse
- [ ] Research Agent saves `research-brief.md` to project folder

### Monday: Preparation
- [ ] Create project folder in O-output (if not already created)
- [ ] All agents read C-core and M-memory files
- [ ] Storyteller reads `research-brief.md`

### Tuesday-Wednesday: Writing
- [ ] Storyteller writes draft (informed by research brief)
- [ ] Storyteller self-checks and delivers

### Thursday: Review + Visuals
- [ ] Gatekeeper reviews blog post
- [ ] Revisions if needed
- [ ] Blog post approved → `final-post.md`
- [ ] Visual Agent creates image brief → `visual-brief.md`

### Friday: Newsletter + Visual Review
- [ ] Newsletter Agent adapts the post
- [ ] Gatekeeper reviews newsletter + visual brief
- [ ] Newsletter approved → `newsletter-version.md`
- [ ] Visual brief approved → `visual-brief.md`

### Weekend/Monday: Publish
- [ ] Generate images from AI prompts
- [ ] Blog post published with images
- [ ] Newsletter sent with header image
- [ ] Paid Search Agent extracts ad hooks from published post (optional)
- [ ] Research Agent tracks performance
- [ ] Paid Search Agent reviews weekly ad performance (Friday)
- [ ] Learning log updated

### First of Month: Strategic
- [ ] Research Agent creates monthly trend report → `B-brain/monthly-trends/`
- [ ] Review calendar for next 4-8 weeks based on trend report
- [ ] Adjust topics if trends suggest better opportunities

---

## Tips for Success

1. **Real stories always win** — If something real happened this week, lead with that
2. **Don't force the calendar** — If the planned topic doesn't feel right, swap it
3. **Keep the rotation varied** — Don't do 3 "Believer's Story" posts in a row
4. **Log everything** — The learning log is what makes this system get better over time
5. **One feeling per post** — Don't try to make the reader feel everything at once

---

*This workflow turns a blank page into a published blog post and newsletter, every single week.*

---

> **© Tom Even**
> Workshops & future dates: [www.getagents.today](https://www.getagents.today)
> Newsletter: [www.agentsandme.com](https://www.agentsandme.com)
