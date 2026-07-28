# Content Process Log — W31 — Meteor

- Date: 2026-07-27
- Brand: Meteor
- Topic: Why Most Treasury Forecasts Are Wrong Before AI Ever Touches Them
- Pillar: Financial operations & treasury (Pillar 2) | Product focus: Meteor
- Pipeline: automated (Researcher -> Copywriter -> Gatekeeper -> Artist -> Email), then manually rebuilt end to end
- Gatekeeper verdict: REPLACED
- Delivery: email to Ran for manual upload (article + post + visual)

## Full rebuild (2026-07-27, per Ran)

Ran flagged that the automated draft ("AI-Powered Payment Fraud Is Outrunning
Treasury's Detection Speed") pitched a capability Meteor does not have.
Meteor has no fraud detection or prevention product. The entire post,
article, and visual were rebuilt from scratch around Meteor's actual
capabilities, per Ran's direction:

- Bank account aggregation: direct connectivity to every Israeli bank and
  150+ of the largest banks worldwide
- ERP integration (1K+ integrations)
- Payments initiated directly from ERP, routed to banks or via SWIFT
- Treasury and cash flow forecasting system
- IFRS 16 lease accounting management
- Automatic FX rate import
- Operates under an Israel Securities Authority (ISA) license, open banking
- AI increasingly integrated across these capabilities (forecasting,
  reconciliation) — framed as a direction, not a fraud product

New angle: multi-bank fragmentation forces manual treasury data collection
(PwC 2025 Global Treasury Survey: 38-52% still manual, only 57% use a TMS),
which undermines forecast accuracy regardless of how good the AI forecasting
model is. Meteor's bank aggregation is the prerequisite. AI-in-finance trend
covered as requested, without repeating the "AI adoption gap" framing already
used in W28-W30.

## Root-cause fix

`C-core/product-capabilities.md` Meteor section rewritten with the accurate,
detailed capability list above (previously vague: "payments, reconciliation,
bank connectivity at scale"), plus an explicit exclusion: fraud
detection/prevention is NOT an approved Meteor capability, with an example of
the exact framing to avoid ("continuous reconciliation catches fraud").

## Process gap identified

The original Gatekeeper pass verified numbers and cross-product topic
ownership (invoice/CTC belongs to Supplier Portal, not Meteor) but never
checked whether the core capability being pitched (fraud detection) was
approved for either product. Attribution checks and capability-existence
checks are different checks; both are now required. See
`gatekeeper-review-meteor.md` and the Gatekeeper checklist update in
`A-agents/copywriter-agent.md`.

## Bug also found

`process/visual-data.json` for W31 was unsuffixed (predates the collision fix
merged for W30). Renamed to `visual-data-meteor.json` to match the now-fixed
convention before this week's StoreNext run could overwrite it.
