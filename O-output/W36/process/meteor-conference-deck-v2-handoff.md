# Meteor Treasury Conference deck — v2 handoff

Date: 2026-09-03
Deliverable: `O-output/W36/final/meteor-treasury-conference-deck-v2.pdf` (10 slides, 16:9)
Source: `O-output/W36/process/build_meteor_conference_deck.py` (rebuild with `python <script>`)

---

## What changed from the sketch, and why

| # | Review finding | What v2 does |
|---|---|---|
| 1 | A third of the type was under 2% of slide height — unreadable at 3–5 m | Hard floor of 24 pt on a 1600×900 canvas = **2.67%**. Nothing on any slide is smaller. Verified by rendering at 1 px = 1 pt and scanning ink bounds |
| 2 | Content sat in the bottom 8–12%, where heads and podiums block it | Nothing below y = 800 of 900 (**bottom 11% kept clear**). Automated check passes on all 10 slides |
| 3 | Cover and body were two different design systems | One system throughout, palette sampled from the W34 booth proofs: navy `#0F2032`, teal `#32A89D`, blue `#4375C3`, red `#E63B47` |
| 4 | Colour meaning changed between slides | One rule everywhere: **blue = ERP / decision side, teal = visibility and bank side, red = Meteor's own layer and the point of action** |
| 5 | The deck invented SEE / ANTICIPATE / OPTIMIZE / ACT, which contradicts the booth | Adopts the booth's **SEE · DECIDE · EXECUTE** and the ERP–METEOR–BANKS rail. Deck and booth now say the same thing |
| 6 | Slide 3 stacked two four-part models in the same columns | Split into two slides: the connectivity chain (5) and the capability model (6) |
| 7 | Zero evidence anywhere | New slide 3 carries three sourced statistics; new slide 2 carries Meteor's approved numbers |
| 8 | No "who is Meteor" beat | New slide 2 |
| 9 | BANKONNECT was 0.89% of slide height, invisible and unexplained | Its own slide (7), at full size |
| 10 | Demo transition buried at the bottom of a busy slide | Its own dark slide (9), with what the audience is about to see |
| 11 | No closing slide, so no route to the booth | New slide 10 with QR placeholder, the booth's Apple Watch mechanic, booth number and speakers |
| 12 | Unqualified AI claim | Slide 8 ends on "Meteor recommends. Your approvals still govern every action." |

Also fixed a real rendering bug in the build: PDF character spacing is graphics state and
survives BT/ET, so one letterspaced line was silently widening every text run after it and
pushing copy past the margins. Tracking is now emitted explicitly on every run.

---

## Running order

| # | Slide | Ground | One idea |
|---|---|---|---|
| 1 | Connected Treasury. From Insight to Action. | dark | Who is speaking, and the through-line |
| 2 | Financial infrastructure for enterprise finance. | dark | Who Meteor is, with proof |
| 3 | Why this matters in 2026. | light | Urgency, with sources |
| 4 | The Treasury Challenge | light | The pain, drawn as broken links |
| 5 | Connected Treasury. End to end. | dark | ERP → METEOR → BANKS, with the seams named |
| 6 | See. Decide. Execute. | light | The capability model, matching the booth |
| 7 | Execution runs on BANKONNECT. | light | Where BANKONNECT sits |
| 8 | Intelligence where decisions happen. | light | AI as a decision pipeline, with governance |
| 9 | Now let's see it in action. | dark | Demo handoff, with expectations set |
| 10 | Connected Treasury. From Insight to Action. | dark | Booth, prize draw, names |

Dark / light alternates deliberately: 1–2 dark, 3–4 light, 5 dark, 6–8 light, 9–10 dark.
If the slot is short, the minimum viable run is **1, 3, 4, 5, 8, 9, 10**.

---

## Claims used, and where they come from

**Product numbers — from `C-core/product-capabilities.md` (approved list), slide 2**
- 400+ enterprise clients
- 150+ global banks, plus direct connectivity to every Israeli bank
- 1K+ ERP integrations
- Operates under an Israel Securities Authority (ISA) licence

Note: `C-core/icp-profile-meteor.md` says "400+ integrations" for payments, which conflicts
with product-capabilities' "1K+ ERP integrations". I used product-capabilities as the source
of truth. **Worth reconciling the two files.**

Deliberately NOT used: StoreNext Group's 20,000+ businesses and 20B ₪ procurement volume.
Those belong to the Supplier Collaboration Platform, and product-capabilities forbids
borrowing one product's numbers for another.

Deliberately NOT claimed: fraud or anomaly detection — not an approved Meteor capability.
Slide 8 says AI is "being built across forecasting, reconciliation and payments", which
matches the approved framing.

**Market statistics — slide 3, sources printed on the slide**
- 63% of senior finance leaders expect FX volatility to rise in 2026 — Alpha Group / Corpay,
  *Countdown to 2026* (via `O-output/W36/process/research-brief-meteor.md`)
- 89% of those surveyed do not systematically stress-test their FX forecasts — same source
- 61% of finance leaders report finance and accounting talent shortages — Corporate Finance
  & Accounting Talent Study 2026, via Controllers Council (via `W35` research brief)

These are global surveys, not Israeli. If anyone in the room asks, say so plainly rather
than implying a local sample.

---

## Needs your decision before this is stage-ready

1. **BANKONNECT copy (slide 7).** BANKONNECT appears nowhere in `C-core/`, so I had no
   approved wording. Slide 7 makes a structural claim only — Meteor decides, BANKONNECT
   executes, banks settle — plus "bank connectivity, payment initiation from the ERP, and
   the approval trail behind both." **Confirm this is accurate before it goes on stage.**
2. **Booth number** — slide 10 says `BOOTH [ 00 ]`.
3. **QR code** — slide 10 has a placeholder box; drop in the same code as the rollup.
4. **Demo bullets (slide 9)** — three promises. They should match what Limor and Shiran
   actually show, in that order.
5. **Speaker order** — "Limor Carmeli · Shiran Shapira" on slides 1 and 10.
6. **The two conflicting integration numbers** noted above.

---

## Typography and readability, measured

Smallest type on each slide, as % of 900 pt slide height (stage floor: 2.5%):

- Headlines: 8.2% (H1) and 10.7% (hero)
- Statistics: 12.9%
- Lead / subhead: 4.0%
- Body and labels: 3.1%
- Sources and footers: 2.67% — the floor

Text colour contrast: `#4E5866` on cream ≈ 8.4:1, `#B4C0CC` on navy ≈ 9.6:1. Both well
above the 7:1 that survives a washed-out projector.

Font is Arial / Arial Bold, matching the W34 booth print files, so nothing substitutes on
a strange laptop. If the brand moves to Inter, `C-core/fonts/Inter-var.ttf` is available and
the build script takes one line to switch.

---

## Not done

- No editable PPTX. The deck ships as PDF plus the build script. If a designer needs to
  hand-tune it in PowerPoint or Figma, say so and I will produce a PPTX.
- Files are written locally only. Nothing pushed to `routine-drafts` or `main`.
