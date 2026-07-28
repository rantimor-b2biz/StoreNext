# Gatekeeper Review — W31 — Meteor

**Verdict:** REPLACED (full rebuild, 2026-07-27)

## Original auto-generated draft: rejected

The auto-generated draft ("AI-Powered Payment Fraud Is Outrunning Treasury's
Detection Speed") built its entire premise on Meteor detecting or preventing
payment fraud through continuous reconciliation. **Meteor does not have a
fraud detection or prevention capability.** It was never an approved claim in
`C-core/product-capabilities.md`.

The original Gatekeeper pass checked numbers (correct) and cross-product topic
ownership (correct: fraud/reconciliation framed as Meteor, not Supplier
Portal) but never checked whether the underlying capability being pitched was
approved at all. That is the gap: verifying attribution between two products
is not the same as verifying the capability exists for either of them.

## Replacement: approved

New topic: "Why Most Treasury Forecasts Are Wrong Before AI Ever Touches
Them." Grounded entirely in approved Meteor capabilities: bank aggregation
(direct connectivity to every Israeli bank and 150+ global banks), ERP
integration, treasury and cash flow forecasting, IFRS 16 lease accounting,
automatic FX rate import. No fraud framing anywhere in post, article, or
visual.

- All facts sourced and verified: PwC 2025 Global Treasury Survey (manual
  data collection, TMS adoption, manual FX hedging figures).
- All Meteor numbers checked against `C-core/product-capabilities.md`: only
  "150+ global banks" is used, correctly attributed.
- No em dashes, exclamation marks, or banned hype words.
- Lead-with-pain, bridge-before-product, and business-value-thesis rules
  applied (multi-bank manual consolidation pain -> PwC data -> AI-needs-data
  bridge -> Meteor's bank aggregation, not a jump to the product).
- Closing question names a concrete, answerable gap (how many banks logged
  into by hand).
