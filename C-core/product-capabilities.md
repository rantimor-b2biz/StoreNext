# Product Capabilities — Approved Claims Only

> Source of truth for what each product actually does. The content automation
> (Researcher + Gatekeeper) may attribute to a product ONLY capabilities listed
> here. Anything not listed = describe generically ("leading organizations...")
> without naming a product. Update this file when capabilities ship.
> Last updated: 2026-07-03 (per Ran).

## Supplier Portal ("Supply Chain Automations")
Buyer: CFO (primary), Procurement Director (secondary).
The portal sits between suppliers and the ERP — a communication, document and
compliance gate.
Approved numbers: 300+ Enterprise clients / 20,000+ suppliers / 20B+ ₪ annual
procurement volume / 3 million transactions per day. NEVER use Meteor's numbers
(1K+ ERP integrations / 400+ clients / 150+ global banks) for Supplier Portal —
they are a different product with a different client base.

- Centralized supplier communication and structured updates (one place, not scattered emails)
- Digital document and invoice flow from suppliers into the organization
- **Israeli e-invoicing / CTC compliance gate:** only invoices that meet the Tax
  Authority's conditions are pushed to the ERP. The portal:
  - runs OCR validation on every incoming invoice and reads the allocation number
  - validates the allocation number against the invoice amount and the thresholds defined by law
  - stops non-compliant invoices inside the portal (they never reach the ERP)
  - or, where permitted, obtains an allocation number and stamps it on the invoice itself
- Operational continuity during supply disruptions (structured supplier status, mass communication)
- Audit trail of supplier documents and invoice handling

## Meteor ("Financial Operations")
Buyer: CFO. AI-native financial operations. Direct competitor: NILUS.
Approved numbers: 20K+ transactions / 1K+ ERP integrations / 400+ clients / 150+ global banks.
Regulatory: operates under an Israel Securities Authority (ISA) license.

- **Bank account aggregation:** direct connectivity to all Israeli banks and to
  150+ of the largest banks worldwide. Open banking.
- **ERP integration:** connects to all leading ERP systems (1K+ integrations).
- **Payments:** initiates payments directly from the ERP, routed to banks or
  via SWIFT. No manual re-entry of payment data.
- **Treasury and cash flow forecasting** system.
- **IFRS lease accounting** (IFRS 16) management system.
- **Automatic FX rate import**, kept current across ERP and reporting.
- Real-time financial data across banks and ERP systems, built on the direct
  bank connectivity above.
- AI-native positioning ("Enterprise Financial Operations. AI-Native, Real-Time, Always in Control.") — AI is being integrated across these capabilities (forecasting, reconciliation, payments); frame as an ongoing direction, not a shipped fraud/anomaly-detection product (see exclusion below).

**NOT an approved Meteor capability — do not pitch this:** fraud detection,
fraud prevention, or anomaly/AI-based fraud monitoring. Meteor does not market
a fraud product. Do not build a post or article around "Meteor stops fraud" or
imply fraud detection as a feature, even indirectly via "continuous
reconciliation catches fraud." Reconciliation and cash visibility are real
capabilities; fraud-detection as a marketed capability is not.

## Hard rules
- NEVER present the two products as one "unified platform" — separate implementations.
- NEVER use "40 years" as positioning.
- Invoice/allocation-number/CTC compliance topics belong to **Supplier Portal**, not Meteor.
- Retail Analytics ("Market & Consumer Intelligence") = website presence only, no active marketing content.
- **Numbers belong to their own product only.** Each product's "Approved numbers"
  line above is scoped to that product. Never borrow another product's numbers
  because they are nearby in this file or because a post's product_focus is
  ambiguous. If unsure which number set applies, use neither and describe scale
  generically ("at Enterprise scale") instead of inventing or borrowing a figure.
- **Meteor does NOT have a fraud detection/prevention capability.** Never build
  content around Meteor stopping, detecting, or reducing fraud. A trending fraud
  statistic can be cited as market context, but the product tie-in must be one
  of Meteor's actual capabilities (bank aggregation, ERP integration, payments,
  treasury/cash flow forecasting, IFRS lease accounting, FX rate automation) —
  never implied fraud detection via "continuous reconciliation" or similar.
