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

### Branch Policy — 3 ענפים בלבד

| ענף | מטרה | מי דוחף |
|-----|------|---------|
| `main` | ברירת מחדל. תוכן מאושר + תשתית. GitHub Actions רצים מכאן. | merge מ-routine-drafts |
| `routine-drafts` | כל דראפט תוכן שבועי. | Claude בסיום כל סבב |
| `claude/*` | ענפי עבודה זמניים של Claude Code web — תשתית בלבד. | נמחקים אחרי merge |

### ⚠️ CONTENT MUST GO TO routine-drafts — NOT TO claude/* BRANCHES

**כלל קריטי:** כל קובץ O-output/ חייב להידחף ל-`routine-drafts`. לעולם לא ל-`claude/*`.

סשן ROUTINE פותח אוטומטית ענף `claude/*`. זה בסדר לשינויי תשתית.
אבל **תוכן שבועי (O-output/)** חייב תמיד לעבור דרך:

```bash
git checkout routine-drafts 2>/dev/null || git checkout -b routine-drafts origin/main
git add O-output/W[NN]/
git commit -m "W[NN] draft: [topic]"
git push origin routine-drafts
git checkout main
```

אם דחפת בטעות ל-`claude/*` — העבר ידנית:
```bash
git checkout routine-drafts
git cherry-pick <commit-hash>
git push origin routine-drafts
```

### Push תוכן שבועי — תמיד ל-routine-drafts
```bash
git checkout routine-drafts 2>/dev/null || git checkout -b routine-drafts origin/main
git add O-output/W[NN]/
git commit -m "W[NN] draft: [topic]"
git push origin routine-drafts
git checkout main
```
→ פותח PR לאישור Ran לפני שתוכן מגיע ל-main.
→ Merge ל-main מפעיל GitHub Action לשליחת אימייל אוטומטית.

### NEVER push directly to main
תשתית (CLAUDE.md, A-agents, C-core) — PR מענף claude/* → main.

---

## Session Start Protocol (MANDATORY)

When starting ANY new conversation from this folder, ALWAYS read these files first before responding:

### 1. Core Files (C-core/) - WHO IS STORENEXT?
- `C-core/project-brief.md` - What StoreNext does, who they serve, business goals
- `C-core/voice-dna.md` - **CRITICAL** - How StoreNext speaks (formal, data-driven, CFO-focused)
- `C-core/icp-profile.md` - Who we're targeting (CFOs, Procurement Directors, CIOs) — StoreNext core platform
- `C-core/icp-profile-meteor.md` - ICP for Meteor (fintech division) — separate buyer personas, Israeli market, English content
- `C-core/brand-standards.md` - Visual and tone guidelines

### 2. Planning & Memory Files - WHAT WAS PUBLISHED / WHAT HAVE WE LEARNED?
- `B-brain/content-calendar.md` - **Source of truth for publication status** (✅ פורסם rows = what ran, which category, which week). Use this for variety checks.
- `B-brain/linkedin-content-plan.md` - 47-week strategic roadmap. Use this to find this week's planned topic.
- `M-memory/learning-log.md` - Patterns and performance insights (what worked, what didn't). NOT a publication log.
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

*Last updated: 2026-05-26*
