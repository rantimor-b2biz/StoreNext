# StoreNext - AI Agent Team for Enterprise B2B Marketing

---

## ⚠️ FILE STRUCTURE RULES — READ THIS BEFORE CREATING ANY FILE

The auto-sync script pushes local changes to GitHub automatically.
Your job: write files to the correct local location. Do NOT git push.

### Root folder — only these items allowed:
```
A-agents/   B-brain/   C-core/   M-memory/   O-output/   T-tools/
CLAUDE.md   README.md
```
NEVER create any file directly at the StoreNext project root.

### O-output — strict structure:
```
O-output/
└── W[NN]/           ← ISO week number ONLY (e.g. W24, W25)
    ├── final/       ← final-post.md (triggers GitHub Action email when synced)
    └── process/     ← research-brief.md, copywriter-draft.md, gatekeeper-review.md
```

NAMING — no exceptions:
- ✅ O-output/W24/
- ❌ O-output/04-linkedin-topic-name/
- ❌ O-output/W24-topic-name/
- ❌ O-output/week4/

Get current ISO week number: `date +%V`

### Push to routine-drafts — NEVER to master directly
```bash
git checkout routine-drafts 2>/dev/null || git checkout -b routine-drafts
git add O-output/W[NN]/
git commit -m "W[NN] draft: [topic]"
git push origin routine-drafts
git checkout master
```
→ This opens a PR for Ran to review before content reaches master.
→ Merge to master triggers email + visual generation automatically.

---

## Session Start Protocol (MANDATORY)

When starting ANY new conversation from this folder, ALWAYS read these files first before responding:

### 1. Core Files (C-core/) - WHO IS STORENEXT?
- `C-core/project-brief.md` - What StoreNext does, who they serve, business goals
- `C-core/voice-dna.md` - **CRITICAL** - How StoreNext speaks (formal, data-driven, CFO-focused)
- `C-core/icp-profile.md` - Who we're targeting (CFOs, Procurement Directors, CIOs) — StoreNext core platform
- `C-core/icp-profile-meteor.md` - ICP for Meteor (fintech division) — separate buyer personas, Israeli market, English content
- `C-core/brand-standards.md` - Visual and tone guidelines

### 2. Memory Files (M-memory/) - WHAT HAVE WE LEARNED?
- `M-memory/learning-log.md` - What content has worked (and what hasn't)
- `M-memory/decisions.md` - Strategic choices made (why we prioritize certain topics)
- `M-memory/feedback.md` - Audience signals (engagement patterns, lead generation)

### 3. Agent Definitions (A-agents/) - HOW DO WE WORK?
- Review agent roles when you need to coordinate multi-agent workflows

---

## How This System Works

**StoreNext** is a multi-agent content system designed to position StoreNext as an enterprise B2B thought leader targeting CFOs, Procurement Directors, and CIOs.

**Goal:** Generate LinkedIn posts and long-form articles in StoreNext's professional, data-driven voice, driving enterprise inbound leads.

**The agents (8 active):**
1. **Researcher** - Research enterprise procurement trends and CFO challenges
2. **Copywriter** - Write articles and LinkedIn posts in StoreNext's formal voice
3. **Artist** - Create professional B2B visual assets
4. **Gatekeeper** - Quality control (reviews all content before publication)
5. **Analyst** - Turn messy enterprise inputs into structured documents
6. **Strategist** - Strategic analysis for enterprise marketing decisions
7. **Devil's Advocate** - Challenge assumptions before committing
8. **Chief of Staff** - Synthesize Strategist + Devil's Advocate into one decision brief

---

## Quick Commands

### 📝 Content Creation
- **"Create a LinkedIn post about [topic]"**
  → Researcher → Copywriter → Gatekeeper

- **"Write an article about [topic]"**
  → Researcher → Copywriter → Gatekeeper

- **"Create content about [enterprise trend]"**
  → Researcher → Copywriter → Gatekeeper

### 📊 Strategic Analysis
- **"Should we focus on [topic/angle]?"**
  → Strategist → Devil's Advocate → Chief of Staff (decision brief)

- **"Analyze this decision: [X]"**
  → Chief of Staff (synthesis)

### ✅ Quality Control
- **"Review this post against brand standards"**
  → Gatekeeper (checks: voice, ICP relevance, data accuracy, enterprise tone)

- **"Does this sound like StoreNext?"**
  → Gatekeeper compares to C-core/voice-dna.md

---

## StoreNext Voice Standards

**Always use:**
- Professional, formal tone (8/10)
- Data-backed claims with metrics
- Short sentences (10-14 words)
- Enterprise terminology (procurement, vendor, supply chain, ROI)
- Solution-focused messaging
- Specific call-to-actions

**Never use:**
- "Revolutionary," "Transformative," "Disruptive"
- Hype language or marketing fluff
- Em dashes (use periods instead)
- Exclamation marks (use periods)
- Casual language ("touch base," "synergy")

---

## LinkedIn Best Practices (B2B Enterprise)

- ✅ First 2 lines must stop scroll (hook before truncation)
- ✅ One main idea per post
- ✅ Specific numbers and metrics beat generic claims
- ✅ No external links in caption (put in first comment)
- ✅ Trigger engagement question at end
- ❌ Generic hooks
- ❌ Multiple ideas in one post
- ❌ Stock photography

---

## Content Quality Standards

**Every piece must:**
1. ✅ Sound like StoreNext (read C-core/voice-dna.md first)
2. ✅ Serve the ICP (CFOs, Procurement Directors, CIOs)
3. ✅ Be specific (numbers, examples, not vague claims)
4. ✅ Pass Gatekeeper review before publication

---

## File Organization

### O-output/ (Generated Content)
Save all content in week folders:

```
O-output/
├── 2026-W11/
│   ├── process/    ← drafts, research, notes
│   └── final/      ← approved, ready to publish
```

**Rules:**
- Split into `/final/` (published/approved) and `/process/` (drafts/research)
- Every production cycle must include `process/content-process-log.md`

---

## Weekly Content Session — Full Cycle

> NEVER spread the weekly content process across multiple days. Run start-to-finish in one session.

The entire content cycle runs in ONE session, from research to final approved posts. Total time required from Ran: approximately 10 minutes.

### The 6-Step Single-Session Workflow

**Step 1 — Researcher scans sources**
Reads `B-brain/research-sources.md` and current trends. Produces `O-output/W[NN]/process/intelligence-brief.md`.

**Step 2 — Strategist proposes 2-3 topics**
Based on the intelligence brief, proposes 2-3 topic options with a suggested hook for each. Produces `O-output/W[NN]/process/weekly-content-plan.md`.
- **PAUSE HERE: Ran approves one or more topics before proceeding.**

**Step 3 — Copywriter writes all approved posts**
Writes every post that was approved in Step 2. Saves drafts to `O-output/W[NN]/process/copywriter-draft.md`.

**Step 4 — Gatekeeper reviews all posts**
Checks every draft against `C-core/voice-dna.md` and brand standards. Approves or returns with specific revision notes. Saves to `O-output/W[NN]/process/gatekeeper-review.md`.

**Step 5 — Artist creates visuals (אוטומטי לחלוטין)**
For each Gatekeeper-approved post, Artist runs autonomously — no user input required:
1. Reads `O-output/W[NN]/process/visual-data.json` (populated by Copywriter in Step 3)
2. Reads `C-core/visual-design-language.md` + `C-core/brand-standards.md`
3. Reads `C-core/storenext-logo.svg` — embedded in every visual
4. Selects visual type per post: `stat_card` / `process_flow` / `quote_card`
5. Generates HTML visual → saves to `O-output/W[NN]/final/post-[NN]-visual.html`

**Logo rules (mandatory):**
- Light background visuals: logo as-is (dark wordmark + red icon)
- Dark/navy background visuals: wordmark fill changed to `#FFFFFF`, red icon `#ee404a` unchanged
- Logo always top-left, minimum clear space 16px

**Step 6 — Final posts delivered**
All approved posts + visuals in `O-output/W[NN]/final/`:
- `final-post.md` — all post texts ready to publish
- `post-[NN]-visual.html` — matching visual per post

**Step 7 — Content calendar updated**
`B-brain/content-calendar.md` updated: new entries with status `📋 מאושר`, visual column `🎨 נוצר`.
`M-memory/learning-log.md` updated after publication.

### Time Summary

| Who | When | Time Required |
|-----|------|---------------|
| Ran | Step 2: approve topics | ~5 minutes |
| Ran | Step 6: collect final posts + visuals | ~2 minutes |
| Agents | Steps 1, 3, 4, 5, 7 | Automated |

**Total Ran time per week: ~7 minutes.**

### Key Rules
- Do NOT initiate Step 3 (Copywriter) before receiving topic approval from Ran at Step 2.
- Step 5 (Artist) runs immediately after Gatekeeper — no approval gate needed.
- Copywriter MUST populate `visual-data.json` as part of Step 3 — Artist cannot run without it.

---

## Auto-Learning Protocol

After completing significant work, update the relevant memory file:

### When to Update M-memory/learning-log.md
- After publishing content → Record performance (likes, comments, DMs)
- When noticing patterns → What formats drive CFO engagement

### When to Update M-memory/decisions.md
- When making strategic choices → Topic prioritization
- When adjusting approach → Format or angle changes

---

## Critical Reminders

### ALWAYS Read C-core/ First
Before writing ANY content, read:
- `C-core/voice-dna.md` - How StoreNext speaks
- `C-core/icp-profile.md` - Who we're serving (StoreNext core platform)
- `C-core/icp-profile-meteor.md` - If content is for Meteor (fintech division), use this ICP instead

### NEVER Skip Gatekeeper Review
All content goes through Gatekeeper before publication.

### UPDATE M-memory After Publishing
Capture learnings so the system gets smarter over time.

### NEVER Use Worktree Isolation
Do NOT use `isolation: "worktree"` when calling agents. All work goes directly on the main branch. Worktrees are a developer tool — using them in content workflows causes files to get lost in `.claude/worktrees/`.

---

*Last updated: 2026-06-08*
