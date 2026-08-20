# Learning Log

This is the team's collective memory. Every agent reads this before working. Every review adds to it. We get better together.

---

## How This Works

**Before working:** Every agent reads the relevant sections
**After working:** Gatekeeper logs patterns from each review session
**Periodically:** Consolidate insights into agent instruction files

---

## Ran's Feedback — Copywriting for CFO/AP (2026-07-07)

Real feedback from Ran on the W27 e-invoicing post. Applies to ALL future posts.
The goal is to open conversations with CFOs, Finance and AP leaders. Optimize for that.

1. **Lead with pain, not the topic.** Never open with the regulation, announcement, or
   timeline. Open with the consequence the reader feels. The trigger goes in line 2-3 as proof.
   - Weak: "Israel's Tax Authority planned this rollout for 2028. Now it lands by June 2026."
   - Strong: "Thousands of invoices that never required validation before will require it in
     less than six months." / "The real challenge isn't the regulation. It's the volume."

2. **Translate mechanisms into business consequences.** A CFO does not care about an
   "allocation number." Convert every mechanism to: payment delays, exceptions, audit,
   manual work, VAT/tax risk, cash flow.
   - "Every invoice above NIS 5,000 becomes a compliance checkpoint. If validation happens
     too late, payments are delayed. If it doesn't happen at all, VAT recovery is at risk."

3. **Add a "most / very few" contrast** to expose the size of the change:
   - "Most organizations already have a process for high-value invoices. Very few have a
     process for validating every invoice above NIS 5,000."

4. **Close with a question that demands a real answer** (name a number, a role, or a
   readiness gap), not a generic professional question.
   - Weak: "How are you sizing invoice volume at the NIS 5,000 threshold?"
   - Strong: "How many invoices will cross the NIS 5,000 threshold every month, and who is
     validating them today?" / "Are your AP processes ready for a 3x to 5x increase in
     invoices requiring validation?"

Embedded in `A-agents/copywriter-agent.md` → "Lead With Pain" section.

---

## Ran's Feedback — Cross-Brand Topic Collision (W30, 2026-07-23)

Ran caught that the W30 StoreNext post ("The Governance Gap... Agentic AI") landed
3 days after the W30 Meteor post ("The AI Performance Gap in Treasury") — same
"AI + Gap + Finance" theme and title formula, to the same CFO audience. Zooming
out further: 4 posts in a row across both brands (W28, W29, W30 Meteor, W30
StoreNext) all centered on AI-in-finance, and 3 of the last 4 titles used "The
[X] Gap" as the headline formula.

Root cause: topic dedup in `generate_article_and_post.py` was per-brand only —
the StoreNext researcher never saw what Meteor published that same week, so it
could not detect the collision even though both brands publish 3 days apart to
overlapping readers.

Fix: `stage1_research` now also passes the last 8 posts across BOTH brands as a
"cross-brand check" the researcher must actively avoid echoing — same theme,
same headline formula ("The [X] Gap"), or the same macro-topic (AI adoption/
governance in finance) more than 2-3 weeks running. When AI-in-finance has
dominated recently, the researcher is told to prefer pillar 1 (Supplier Portal
core) or pillar 3 (procurement/CFO agenda, non-AI) instead, even if an AI
angle is trending — variety across pillars beats chasing the same macro-theme.

---

## Ran's Feedback — Post Structure + Correctness (W30, 2026-07-23)

Ran scored the fully-automated W30 StoreNext post 8.5/10 — the auto-pipeline is
working well, but flagged real issues plus one bug found independently in review:

1. **Correctness bug (Gatekeeper miss):** the post/article used Meteor's approved
   numbers (1,000+ ERP integrations / 400+ clients) for a Supplier Portal post.
   Root cause: `C-core/product-capabilities.md` only listed approved numbers for
   Meteor, so the model borrowed them by proximity. Fixed by adding Supplier
   Portal's own numbers (300+ clients / 3M transactions/day) to that file, plus a
   hard rule that numbers never cross products.
2. **False attribution:** "The insight Gartner drew but did not name" attributed
   the author's own conclusion to the cited source. Say "Our takeaway is simple"
   instead — never imply a source said something it did not say.
3. **Abrupt product pivot:** jumping straight from the macro insight to "This is
   exactly where [product] becomes critical" reads as a pitch on cue. Bridge with:
   name the reader-facing question the insight implies -> name the strongest
   general candidate -> only then the product.
4. **State the business-value thesis as a sentence**, not just an implication
   (e.g. "AI creates value only when every autonomous decision can be trusted,
   explained, and audited").
5. **Bullets in business-outcome language**, not mechanism language (translate
   "OCR validation" -> "every invoice validated before it reaches the ERP", etc).
6. **Strategic positioning:** when relevant, close by pointing to StoreNext's
   broader "trusted business context" thesis with the specific product as one
   proof point, not the whole pitch — before the tactical closing question.

Embedded in `A-agents/copywriter-agent.md` → "Your Interpretation Is Not Their
Quote" and "Bridge Before the Product, Don't Jump" sections, plus the Gatekeeper
checklist. Root-cause fix in `C-core/product-capabilities.md`.

---

## Ran's Feedback — No Overstated Tech Claims (2026-07-13)

From the W28 Meteor post review: do not repeat "real-time" for capabilities that are
not literally real-time. Precise alternatives Ran approved:
- "Automated, continuously updated bank connectivity"
- "Up-to-date financial visibility across banks and systems"

Third-party quotes (surveys, analysts) that say "real-time" may stay, clearly attributed.
The rule applies to OUR capability claims (StoreNext / Meteor). When unsure what the
product actually delivers, ask Ran before publishing.

Embedded in `A-agents/copywriter-agent.md` → "No Overstated Technology Claims" section.

---

## Why Memory Matters

> "Brain is what you feed the system. Memory is what the system learns."

Most AI systems are stateless — every conversation starts from zero. This file is what makes your system **compound over time**.

Every pattern logged here makes future work better.

---

## Active Patterns (Apply These Now)

### Copy Patterns

**What Works:**
| Do This | Not This |
|---------|----------|
| Start with a specific moment or action | Start with a generic statement |
| Use contrast frames: "Old way... New way..." | Use abstract explanations |
| Include numbers that can be visualized | Use vague claims |
| Write short lines. Punchy rhythm. | Write long flowing paragraphs |

**Voice Markers (Must Be Present):**
- Personal pronouns (I, my, me, you)
- Specific numbers (20 hours → 7 hours)
- Sensory/visual details
- Conversational tone

**Voice Violations (Must Be Absent):**
- Corporate jargon (leverage, optimize, synergy)
- Vague superlatives (best, leading, top-tier)
- Generic claims that competitors could use
- Passive voice overuse
- Long explanatory sentences

---

## Common Mistakes to Avoid

### Copy Mistakes
1. Opening with a lesson instead of a moment
2. Using "best" or "leading" without proof
3. Writing headlines that could apply to any competitor
4. Over-explaining the insight (let it land)
5. Missing the natural brand callback

---

## Quality Shortcuts

**Copy Quick Checks:**
1. Read it aloud — does it flow?
2. Count specific numbers — aim for 2+ per piece
3. Check first line — is it a moment or an explanation?
4. Check last line — is it memorable standalone?
5. Apply the test: Visual? Provable? Unique?

---

## Iteration Log

*Add entries below after each review session*

<!--
Template for new entries:

## [Date] - [Content Type]: [Brief Description]

### Gatekeeper Review
**Status:** [Approved / Sent Back / Escalated]

### What Worked Well
- [Specific pattern that succeeded]

### What Needed Improvement
- [Specific issue that needed fixing]

### Pattern Discovered
- [Reusable insight for future work]

### Updates Made
- [ ] Added to Active Patterns
- [ ] Updated agent instructions
- [ ] Flagged for human

-->

---

## 2025-02-03 - LinkedIn Post: איך להגדיל את הסיכוי לגייס

### Gatekeeper Review
**Status:** ✅ Approved

### What Worked Well
- **Hook עם הכחשה:** "אמרתי לו שאין לי מושג" — עוצר גלילה כי מפתיע
- **כנות עצמית:** לא הבטיח שום דבר, אמר בפירוש "זה לא אומר שיצליח"
- **סיום אופייני:** "וזה שווה משהו. גם אם זה לא הכל" — ביטוי מהכתיבה האמיתית
- **נקי מניו אייג׳:** לא הוזכרו כוכבים/אנרגיות/יקום — רק "תזמון"

### What Needed Improvement
- המטאפורה "דוחף סלע על הר" קצת שחוקה — אפשר היה למצוא משהו יותר מקורי (לא תוקן, לא קריטי)

### Pattern Discovered
- **הכחשה ב-hook עובדת:** כשפותחים עם "אין לי מושג" או "אני לא יודע" — זה יוצר סקרנות
- **לא חייבים שאלה בסוף:** הסגנון של אסטרו הוא "לא מנסה לשכנע", אז סיום בתובנה שקטה מתאים
- **"וזה שווה משהו"** — ביטוי חתימה שכדאי להשתמש בו

### Files Created
- `O-output/01-linkedin-post-giyus/copywriter-draft.md`
- `O-output/01-linkedin-post-giyus/gatekeeper-review.md`
- `O-output/01-linkedin-post-giyus/final-post.md`

---

## 2025-02-03 - System Sync: All Agents Grounded in Brand Context

### What Happened
סנכרון מלא של כל הסוכנים עם קבצי הליבה של המותג. כל סוכן עכשיו מכיר את:
- **אסטרו** — אסטרולוגיה עסקית ליזמים
- **הקהל** — מייסדים רציונליים שניסו הכל ומוכנים לנסות משהו מוזר
- **הקול** — עסקי, ישיר, כנה, עם אירוניה עצמית

### Agent Status

| Agent | Core Files | Brand Context | Writing Style |
|-------|-----------|---------------|---------------|
| Copywriter | ✅ Points to all C-core files | ✅ Has Owner's Writing Style section | ✅ Full patterns documented |
| Gatekeeper | ✅ Points to all C-core files | ✅ Knows brand standards | ⚠️ Generic (needs brand-specific criteria) |

### What's Working
- Copywriter agent has detailed Owner's Writing Style section with do/don't examples
- Both agents point to correct C-core files in Required Reading
- Voice DNA has full patterns from actual writing

### What Needs Attention
- Gatekeeper agent still has generic review criteria — could be enhanced with אסטרו-specific checkpoints
- Writing samples folder is empty — when samples are added, re-analyze

### Files Verified
- `C-core/project-brief.md` — ✅ Filled with אסטרו specifics
- `C-core/voice-dna.md` — ✅ Filled with voice attributes + Owner's Writing Patterns
- `C-core/icp-profile.md` — ✅ Filled with founder persona + pain points
- `A-agents/copywriter-agent.md` — ✅ Has Owner's Writing Style section
- `A-agents/gatekeeper-agent.md` — ✅ Points to core files

### Result
מעכשיו כל סוכן יוצר תוכן שמשקף את המיצוב הייחודי של אסטרו, מדבר לקהל הספציפי, ומשתמש בסגנון הכתיבה האותנטי.

---

## 2025-02-03 - Style Analysis: Owner's Writing Patterns

### Source
ניתוח של תשובות הבעלים בדף גילוי המותג (brand-discovery-worksheet-DEMO.md)

### What We Learned

**מבנה משפטים:**
1. **פתיחה קצרה, הרחבה ארוכה** — "להבין למה. ברצינות, זה הכל."
2. **רשימות עם "לא"** — "לא ניו אייג׳. לא קריסטלים ולא מנטרות..."
3. **"אבל" באמצע** — "הוא רציני, אבל הוא גם יודע שזה נשמע מוזר"

**טון ייחודי:**
1. **כנות עצמית** — מודה בחוסר ודאות ("לא יודע אם זה עובד בגלל...")
2. **אירוניה עצמית** — "הקפיצה המוזרה הזו", "אני הדבר המוזר"
3. **ישירות בלי ריכוך** — "אני שונא את כל הדברים האלה"

**מילים שחוזרות:**
- "משהו" — מילת מפתח (משהו לא עובד, משהו חסר, משהו פה עובד)
- "דווקא" — להדגשת תזמון
- "פשוט" — לפשט דברים
- "בסדר" — לנרמל

**ביטויים מאפיינים:**
- "וזה שווה משהו"
- "גם אם זה X, עדיין Y"
- "לא כי X אלא כי Y"
- "זה לא אומר ש... זה אומר ש..."

### Pattern Discovered
הבעלים לא כותב כמו מותג. הוא כותב כמו בן אדם שמדבר עם חבר — עם חוסר ודאות, עם אירוניה עצמית, עם ישירות. הסגנון הזה הוא ההפך משיווק קלאסי.

### Red Flags to Watch
- אם הקופי נשמע "מקצועי מדי" — זה לא הסגנון
- אם אין כנות עצמית — חסר משהו
- אם אין אירוניה על המוזרות — לא נשמע אותנטי
- אם יש הבטחות גדולות — לא הסגנון (הוא מבטיח פרספקטיבה, לא תוצאות)

### Updates Made
- [x] Added to `C-core/voice-dna.md` — סקציית "Owner's Writing Patterns"
- [x] Added to `A-agents/copywriter-agent.md` — סקציית "Owner's Writing Style"
- [x] Logged here

---

## Sample Entry: How to Log

## 2024-01-15 - LinkedIn Post: Product Launch

### Gatekeeper Review
**Status:** Approved

### What Worked Well
- Strong opening hook — "I used to spend 20 hours on every newsletter" (specific, visual)
- Clear contrast frame worked well
- Numbers were concrete and believable

### What Needed Improvement
- First draft had too many ideas in one post — simplified to ONE message
- Initial headline was generic — rewrote to be more specific

### Pattern Discovered
- **One idea per post works better** — trying to say too much dilutes impact
- **Numbers in the first line** increase engagement

### Updates Made
- [x] Added to Active Patterns
- [ ] Updated agent instructions

---

## 2026-02-17 - Weekly Post #13: Mount of Olives Cemetery

### Status
✅ Drafted — awaiting YouTube upload before publishing

### Content Source
Video filmed on location at the Mount of Olives (IMG_9001.MOV). Audio transcribed with Whisper (openai-whisper, small model). Language auto-detected as English.

### Structure Used
Structure 2: Holy Place Deep Dive

### What Worked
- Opening with the visual of graves facing the Temple Mount creates immediate emotional presence
- The "faith with a body" line — stakes the theological point in physical reality, fits voice DNA perfectly
- Connecting Jewish burial tradition AND Christian pilgrimage in one post broadens resonance without losing focus
- Newsletter subject "They saved a lifetime to be buried here" — story-hint formula, high open rate potential

### Notes for Next Session
- Video still needs to be uploaded to YouTube — add embed ID to `final-post.md` before publishing
- Article URL needs to be inserted in `final-newsletter.md` CTA

### Files Created
- `O-output/13-weekly-post-mount-of-olives/final-post.md`
- `O-output/13-weekly-post-mount-of-olives/final-newsletter.md`

---

## 2026-02-22 - Weekly Post #8: The Silence That Speaks (Garden Tomb)

### Status
✅ Full pipeline complete — all assets approved for publication

### Pipeline Used
First full pipeline run with the new Research Agent:
Research Brief → Storyteller Draft → Gatekeeper Review → Final Post → Visual Brief + Newsletter (parallel) → Final Gatekeeper Review

### Structure Used
Structure 5: The Quiet Moment (🕯️ QUIET)

### What Worked
- **Research Agent brief informed every layer.** The February-specific sensory details (damp paths, rosemary, winter-green garden) came from the research brief and made the post feel grounded and present.
- **"He is not here" sign as the post's anchor.** Calling it "the most powerful sentence in Jerusalem" gave the post a memorable line that works across blog and newsletter.
- **QUIET structure benefits from brevity.** 620 words felt right. The whitespace between sections IS part of the experience. Gatekeeper confirmed: do not add more.
- **Garden Tomb Association's stance is Evangelical gold.** "What matters is the resurrection" avoids the authenticity debate and centers faith over relics. This resonates deeply with our audience.
- **Free admission detail creates surprise.** "In a city where every sacred inch has a gatekeeper, this garden remains open. Like the tomb. Like the gospel." Three parallel beats. Strong close to that section.
- **Newsletter subject line:** "A quiet morning at the Garden Tomb" (38 chars) — Place + Emotion formula. Preview text extends the story.

### Pattern Discovered
- **QUIET posts should be the shortest in the rotation.** The silence is the point. Don't fill the space with words.
- **Research-brief sensory details transfer directly into the Storyteller's opening.** The "damp paths, rosemary, birdsong" pattern works: give the Storyteller specific sensory seeds and they grow into immersive openings.
- **"Emptiness as presence" is a powerful visual and narrative concept.** The empty tomb, the empty garden, the sign about absence. For the QUIET structure, absence is the story.
- **February audiences respond to stillness themes.** Trending context (hunger for quiet, urban monastic movement, counter-digital longing) suggests this post will resonate strongly.

### Files Created
- `O-output/08-weekly-post-garden-tomb-quiet-morning/research-brief.md`
- `O-output/08-weekly-post-garden-tomb-quiet-morning/storyteller-draft.md`
- `O-output/08-weekly-post-garden-tomb-quiet-morning/gatekeeper-review.md`
- `O-output/08-weekly-post-garden-tomb-quiet-morning/final-post.md`
- `O-output/08-weekly-post-garden-tomb-quiet-morning/visual-brief.md`
- `O-output/08-weekly-post-garden-tomb-quiet-morning/newsletter-version.md`
- `O-output/08-weekly-post-garden-tomb-quiet-morning/gatekeeper-review-final.md`

---

## 2026-02-24 - Critical Writing Standard: NO EM DASHES

### Feedback Applied
**User Directive:** Remove all em dashes (—) from all content — both published and deliverables

### Why This Matters
Em dashes create formatting issues across different platforms and rendering contexts. Simpler punctuation alternatives are more reliable and accessible.

### Solution Implemented
Replace ALL em dashes with alternatives:
- **Parentheses ()** — for explanatory clauses or asides
  - Example: "And in that quiet (not in her ears, but deeper) she felt something"
- **Colons (:)** — for introductions and definitions
  - Example: "She'd asked everyone: pastors, prayer chains, healing ministries"
- **Hyphens (-)** — for separators and dates
  - Example: "Garden Tomb - 2026-02-24"
- **Period splits** — breaking sentences for emphasis
  - Example: "And then: silence. Deep silence."

### Applied To
✅ All published blog posts
✅ All newsletter emails
✅ All deliverable documents
✅ All gatekeeper reviews
✅ All supporting briefs

### Going Forward
**ALWAYS CHECK:** Every piece of content generated must be scanned for em dashes before final approval. This is a permanent standard for all agents.

### Files Updated
- `O-output/03-published/blog-posts/2026-02/week-8/garden-tomb-quiet-morning.md`
- `O-output/02-deliverables/week-8-deliverables/copywriter/2026-02-24-garden-tomb-post.md`
- `O-output/02-deliverables/week-8-deliverables/newsletter/2026-02-24-garden-tomb-email.md`
- `O-output/02-deliverables/week-8-deliverables/research/2026-02-24-garden-tomb-research.md`
- `O-output/02-deliverables/week-8-deliverables/storyteller/2026-02-24-garden-tomb-story.md`
- `O-output/02-deliverables/week-8-deliverables/visual/2026-02-24-garden-tomb-visual-direction.md`
- `O-output/02-deliverables/week-8-deliverables/gatekeeper/2026-02-24-garden-tomb-review.md`
- `O-output/02-deliverables/week-8-deliverables/PUBLICATION-PACKAGE.md`

---

## 2026-02-24 - Operational Timeline: Monday Deadline for Thursday Publication

### Critical Deadline Structure
**Publishing cadence:** Every Thursday
**Content ready deadline:** END OF MONDAY
**Digital team prep window:** Tuesday - Wednesday morning
**Final publication:** Thursday

### Why Monday EOD is Sacred
- Digital team (2-3 people) needs minimum 48 hours to:
  - Prepare blog post for CMS
  - Schedule email campaign
  - Coordinate video embedding
  - QA all links and formatting
  - Schedule social media promotion
  - Set up tracking/analytics

### What "Ready" Means by Monday EOD
✅ Blog post (final, no edits)
✅ Newsletter email (final, approved)
✅ Research brief (complete)
✅ Storyteller narrative (complete)
✅ Visual direction (final specs)
✅ Gatekeeper review (approved)
✅ Publication package (all linked and organized)
✅ ZERO em dashes (final check)
✅ All CTAs/links defined

### If Deadline is Missed
- Content pushes to following Thursday (7-day delay)
- This is unacceptable; plan accordingly

### Agent Sprint Schedule (BACKWARD FROM MONDAY)
- **Monday EOD:** All content FINAL
- **Sunday EOD:** Gatekeeper review complete
- **Saturday EOD:** Copywriter, Newsletter, Visual finalized
- **Friday EOD:** Research + Storyteller done, sent to Copywriter
- **Thursday EOD:** Research Agent begins

### Going Forward
Every content sprint is 5 days (Thursday-Monday), not flexible. Plan accordingly.

---

## 2026-06-02 - LinkedIn W23: Solution Introduction

### Gatekeeper Review
**Status:** APPROVED (v1, no revisions needed)

### What Worked Well
- **Week 1 callback hook:** Opening with "The most common answer procurement leaders gave us last week" creates campaign continuity while remaining self-contained for new readers
- **Quoted supplier calls:** "Where's my PO?" / "When will I be paid?" - verbatim lines every procurement leader has heard. Creates instant recognition
- **Emotional pivot before solution:** "Your procurement team didn't sign up to be a call center" - names the frustration before presenting the solution. Sequencing matters
- **Parallel solution structure:** "They check... They see... They know... Without calling anyone." Clean, readable, specific
- **"20,000+ suppliers already work this way":** Strongest proof point. Shifts solution from theoretical to operational at scale

### Pattern Discovered
- **Campaign narrative threads compound:** Callbacks to the previous week's CTA reward engaged readers and add depth without confusing new readers. Use throughout the 13-week sequence
- **"Call center" beats "switchboard":** More Enterprise-resonant, implies over-resourcing of a specialized team. Standardize this metaphor for future posts
- **Closing brand signature builds through repetition:** "That's not a feature. That's infrastructure." gains power each time it appears across the campaign
- **Week 2 should still avoid hard-sell:** Correct to omit StoreNext brand name in the body of the post at this stage. Brand attribution through consistent positioning, not explicit naming

### Files Created
- `O-output/W23-linkedin-post-solution-introduction/research-brief.md`
- `O-output/W23-linkedin-post-solution-introduction/copywriter-draft.md`
- `O-output/W23-linkedin-post-solution-introduction/gatekeeper-review.md`
- `O-output/W23-linkedin-post-solution-introduction/final-post.md`

---

## 2026-06-02 - LinkedIn Post Week 3: Social Proof

### Gatekeeper Review
**Status:** APPROVED (v1, no revisions needed)

### What Worked Well
- **"Not when we asked what they liked. When we asked what surprised them most."** Misdirect hook earns attention. Signals genuine discovery, not promotional framing. Works especially well for the skeptical Week 3 buyer persona
- **"Until you count it."** Three words that validate reader suspicion without condescension. Most efficient voice-DNA line produced so far in the campaign
- **"That's just how we do things."** Naming organizational inertia in the reader's own language. High-trust move that signals familiarity with the real objection
- **Before/after structure.** Unindented list format, one stat per line - respects that Enterprise decision-makers skim. Numbers land visually without a bullet point crutch
- **"What would your numbers show?"** Peer-to-peer CTA. Invites reflection and comment engagement without pressuring for a meeting. Correct for Week 3's consideration phase

### Pattern Discovered
- **Discovery framing beats testimonial framing for skeptics:** "What surprised them" is more credible than "what they loved." Use discovery language for social proof weeks throughout the campaign
- **Organizational inertia has a name:** "That's just how we do things" is the exact language procurement leaders use internally. Naming it earns instant recognition and disarms defensiveness
- **The "hidden cost" insight is the core unlock:** Organizations know email is inefficient. They have not measured it. Giving them the insight to measure it is more persuasive than any feature list
- **Brand signature variation prevents repetition fatigue:** Instead of copy-pasting "That's not a feature. That's infrastructure." verbatim, Week 3 varied to "One pattern holds across all of them." Maintains campaign voice without sounding like a recording

### Files Created
- `O-output/03-linkedin-post-social-proof-week3/research-brief.md`
- `O-output/03-linkedin-post-social-proof-week3/copywriter-draft.md`
- `O-output/03-linkedin-post-social-proof-week3/gatekeeper-review.md`
- `O-output/03-linkedin-post-social-proof-week3/final-post.md`

---

## 2026-07-12 — LinkedIn W25–W28: Sync of Published Posts

### Status
✅ לוח התוכן עודכן לפי פרסומים בפועל בלינקדין

### Posts Published (from LinkedIn)

| Week | Date | Hook | Category |
|------|------|------|---------|
| W25 | 15.6.2026 | $53 per invoice exception (Ardent Partners 2024) | Accuracy & Cost |
| W26 | 23.6.2026 | 9% efficiency gap — CFO's desk, 2026 (Hackett Group) | Accuracy & Cost |
| W26-AI | ~5.7.2026 | Everyone is asking when do we get AI. The better question: what will the AI actually read? | Integration & Digitization |
| W27 | ~8.7.2026 | Israel's Tax Authority didn't just change a threshold. It changed the scale of the challenge. | Regulation / ESG (Meteor) |

### Visual Style Observation
הויזואלים שעלו ללינקדין (נראים בצילומי מסך) גבוהים באיכות משמעותית מהגנרטור הבסיסי:
- Deep purple gradient background עם אור סגול מרכזי
- טיפוגרפיה גדולה ונקייה (teal לנתונים, לבן לטקסט)
- Chips/pills צבעוניים לתאריכים ומדדים
- לוגו StoreNext אמיתי (SVG) + storenext.co.il footer
- W27 (e-invoicing): שימוש ב-coral/red arrow להמחשת ירידה — חזוי ויזואלי חזק

### Category Balance Audit (W20–W28)
| Category | Count |
|---------|-------|
| שקיפות ותקשורת עם ספקים | W20, W21, W23, W24 → 4 |
| דיוק, שליטה וחיסכון | W22, W25, W26 → 3 |
| אינטגרציה ודיגיטציה | W26-AI → 1 |
| רגולציה ו-ESG | W27 → 1 |

**המלצה ל-W28:** Category 3 (חוויית משתמש / Supplier Onboarding) או Category 6 (עדויות מהשטח) — שתי קטגוריות שלא הופיעו ב-2026.

---

## Version History

| Date | Update | By |
|------|--------|-----|
| 2026-07-12 | LinkedIn W25–W28: sync of published posts, category audit, visual style notes | Claude |
| 2026-06-22 | LinkedIn W26 AI Foundation: created + approved (published ~5.7.2026) | Claude |
| 2026-06-02 | LinkedIn Week 3: Social Proof - approved, ready for 2026-06-09 publication | Claude |
| 2026-06-02 | LinkedIn Week 2: Solution Introduction - approved and published | Claude |
| 2026-02-24 | Operational timeline documented: Monday deadline for Thursday publication | Claude |
| 2026-02-24 | Critical writing standard: NO EM DASHES - applied to all content | Claude |
| 2026-02-22 | Weekly post #8: Garden Tomb — full pipeline complete | Claude |
| 2026-02-17 | Weekly post #13: Mount of Olives — drafted | Claude |
| 2025-02-03 | LinkedIn post: גיוס - approved | Gatekeeper |
| 2025-02-03 | All agents synced with brand context | Claude |
| 2025-02-03 | Owner's writing style analysis added | Claude |
| 2024-01-15 | Initial template created | System |

---

*This is a living document. Every review makes us better.*

---

> **© Tom Even**
> Workshops & future dates: [www.getagents.today](https://www.getagents.today)
> Newsletter: [www.agentsandme.com](https://www.agentsandme.com)

---

## Ran's Feedback — Pitched a Capability Meteor Doesn't Have (W31, 2026-07-27)

The automated W31 Meteor draft was built entirely around fraud detection and
prevention through continuous reconciliation. Meteor has no fraud detection
or prevention product. This is a more serious miss than a numbers mixup: the
whole post's premise was an unapproved capability, not just a misattributed
number.

The Gatekeeper pass on the original draft checked numbers (correct) and
cross-product topic ownership (correct: framed as Meteor, not Supplier
Portal) but never checked whether the core capability existed for either
product. Attribution-correctness and capability-existence are different
checks; the first passing does not mean the second passed.

Fix:
1. `C-core/product-capabilities.md` Meteor section rewritten from a vague
   one-liner ("payments, reconciliation, bank connectivity at scale") to the
   precise, complete list: bank account aggregation (direct connectivity to
   every Israeli bank and 150+ global banks), ERP integration, ERP-initiated
   payments via banks/SWIFT, treasury and cash flow forecasting, IFRS 16
   lease accounting, automatic FX rate import, ISA license, open banking.
   Explicit exclusion added: fraud detection/prevention is NOT approved.
2. New Gatekeeper checklist item: verify the central capability being
   pitched is explicitly listed for that product, not just that numbers and
   topic ownership are correctly attributed.
3. The entire W31 post, article, and visual were rebuilt around bank
   aggregation and treasury data fragmentation (PwC 2025 Global Treasury
   Survey), Meteor's actual core capability, with the AI-in-finance trend
   angle preserved as requested but sequenced correctly (AI needs
   consolidated data, not the other way around).

Embedded in `A-agents/copywriter-agent.md` → "The core capability itself must
be approved, not just its attribution" and the matching Gatekeeper checklist
item.

---

---

## Ran's Feedback — W34 StoreNext, Supplier Onboarding (2026-08-20)

Ran called the base and the hook strong, but would not have published as-is. He
independently verified the source before reviewing, which is worth noting: he checks.

**1. A statistic supports only what it measured.**
The post said single/sole-source supplier loss rose 7% domestically and 11%
internationally, then concluded "Concentration risk is rising exactly where onboarding
controls are weakest." Vital Signs 2026 measures supplier loss and visibility. It never
examined onboarding practices and never tested a link between them. The numbers were
right and the sentence built on them was not.

Fix: state what the source measured, then state our inference in a separate sentence and
own it as ours. Watch the smuggling words: *exactly where*, *because*, *which is why*,
*driven by*.

**2. Absolute claims break on contact with an expert reader, and vendor sources cannot
carry them.**
"The only window with full leverage is before the first purchase order" came from
LeanLinking, a procurement software vendor's guidance page. Any procurement director can
name contract renewal, periodic review and re-tendering as counter-examples. Ran's
rewrite: onboarding is "one of the most important opportunities to build control and
visibility before operational dependency forms."

Two rules from this: no absolutes, and check the *source type* before letting a
categorical claim rest on it. A vendor blog is market colour, never proof.

**3. Product bullets must answer the problem the post established.**
Ran: "זה מרגיש כאילו התאמתם את הבעיה לפיצ'רים של StoreNext." The post argued onboarding
and supplier risk, then the first bullet jumped to invoices and allocation numbers.

The root cause is the important part. Revision 1's Gatekeeper correctly stripped the
unapproved onboarding capabilities (sanctions screening, beneficial-ownership
verification, conditional activation, continuous refresh). That left the CTC invoice gate
as the only approved capability that could fill the bullets, and the draft kept the
premise and swapped the feature in. The existing rule catches claiming what we cannot do.
It did not catch keeping a premise the product does not answer.

**New rule:** when the Gatekeeper strips an unapproved capability, re-check the premise,
not just the bullets. If what remains does not answer the post's problem, the topic was
built on something we do not have. Change the angle, or frame the argument generically
and name StoreNext only for what it genuinely does. Never backfill with the nearest
approved feature.

**Pattern across W30, W31, W34.** All three failed at the seam between market argument
and product. W30 was a false attribution and an abrupt pivot. W31 pitched a capability
Meteor does not have. W34 kept a premise the Supplier Portal does not answer. The
product-market bridge is where this system breaks, and each fix has been narrower than
the failure class. The general principle: the product tie-in must answer the exact
problem the post opened with, using only capabilities listed in
`C-core/product-capabilities.md`. If those two cannot both be true, the topic is wrong.

**Structural note:** supplier onboarding is not a listed Supplier Portal capability. The
topic was selected by the automated Researcher without checking that. Topic selection,
not just drafting, should test the premise against `product-capabilities.md`.

Rules added to `A-agents/copywriter-agent.md` (two new HARD RULE sections plus checklist
items) and `A-agents/gatekeeper-agent.md` (six accuracy-checklist items).

---

## Ran's Full Strategic Feedback — W34 Rebuild (2026-08-20, same day)

Ran's first W34 review fixed accuracy defects. His second review established that the
premise underneath them was wrong, and the post was rebuilt from scratch. Both rounds
matter, and the second is the more important lesson.

**The failure: we described a product StoreNext does not sell.**
The post positioned supplier onboarding as the stage where the organization selects the
supplier, verifies it before the first PO, performs screening, establishes commercial
leverage and controls dependency before it begins. StoreNext does none of that. The
platform's territory starts **after** a supplier is already approved and working with the
organization, when the thousands of operational interactions begin.

**The mechanism: a word with two meanings.**
"Onboarding" in the market means bringing a new supplier into the organization. At
StoreNext it means onboarding an **already approved** supplier into the platform and the
digital working process. The draft used the correct internal word and inherited the wrong
external meaning. Nobody in the chain caught it, because every individual sentence was
defensible.

Generalise this: when a term has a common industry meaning and a narrower internal one,
write the narrow one out in full or avoid the term.

**Accurate data can still build a weak bridge.**
The NDIA single-source loss figures were real, recent and on-theme. They describe
supply-chain concentration, which is not a problem this platform solves. Ran's
replacement, Ardent Partners' AP Metrics that Matter in 2025, lands directly on our
territory: AP organizations outside the Best-in-Class spend 26.9% of staff time on
supplier inquiries, Best-in-Class spend 13.4%. Verified against the source before use.

**New topic-selection test:** does the data describe a problem the product operates on,
not merely a problem our buyer has? Those are different questions, and only the first
produces a credible bridge.

**Positioning, in Ran's words.** StoreNext does not reduce supplier communication by
hiding it. It turns supplier communication into structured, traceable, self-service
business processes. The goal is not fewer supplier relationships. It is fewer supplier
interactions that require human intervention.

**Terminology.** Prefer **Supplier Collaboration Platform** when discussing strategic
value. "Portal" reads as an access point. "Collaboration Platform" carries process,
interaction, workflow, visibility, integration and scale. **Supplier Portal** stays valid
as the product name.

**Structure that works** (Ran's, now the default for product-adjacent posts): hook on one
strong number, interpretation of what that number means in practice, reframe from
behaviour to operating model, strategic insight about what good organizations do
differently, only then the product, then proof at scale, then a business takeaway rather
than a CTA, then a discussion question.

**The escalating pattern, W30 through W34.** W30: false attribution and an abrupt pivot.
W31: pitched a capability Meteor does not have. W34 round one: kept a premise the product
does not answer. W34 round two: described a stage of the customer lifecycle the product
does not operate in. Each round has been a wider version of the same error, and each fix
has been narrower than the failure class. The controlling question is not "is this claim
approved" but **"is this the problem our product actually operates on, at the stage it
actually operates in."**

**Source of truth updated.** `C-core/product-capabilities.md` now carries the value
territory the product owns, the positioning principle, the precise definition of
onboarding, and an explicit NOT-approved list for the entire pre-contract stage. Scope
rules added to `A-agents/copywriter-agent.md`, `A-agents/gatekeeper-agent.md` and
`A-agents/researcher-agent.md`.
