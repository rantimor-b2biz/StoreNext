# Israel's Accelerated E-Invoicing Rollout Turns Compliance Into an AP Infrastructure Test

Israel's Tax Authority just compressed a multi-year rollout into six months. For CFOs, this is not a routine compliance update. It is a stress test of accounts payable infrastructure, arriving inside the current planning quarter.

Every invoice above NIS 10,000 now requires a pre-approved allocation number, starting January 1, 2026. By June 1, 2026, that threshold drops to NIS 5,000. Finance teams still validating allocation numbers manually will face payment delays and VAT exposure, at volumes far higher than originally planned.

## The Deadline Just Moved Up: What Israel's Accelerated CTC Timeline Actually Changes

According to Sovos, the Israeli Tax Authority issued VAT Implementation Order 01/2025, confirming an accelerated rollout of the invoice allocation number system under Israel's Continuous Transaction Controls (CTC) invoice model. The order skips the planned NIS 15,000 threshold step entirely.

The new schedule is compressed and specific. From January 1, 2026, businesses must obtain a 9-digit allocation number for invoices of NIS 10,000 or more, VAT excluded, according to Sovos and VATupdate. From June 1, 2026, that threshold falls to NIS 5,000.

The original schedule reached this final threshold in 2028. The accelerated timeline reaches it roughly two years earlier. For CFOs who planned integration work around a 2028 deadline, the planning window has effectively closed.

## From NIS 15,000 to NIS 5,000: Why the Tax Authority Skipped a Step

This is not a vendor pushing urgency. It is a regulatory decision with a clear mechanism behind it.

Since January 1, 2025, according to Sovos, every allocation number request has been subject to Tax Authority review before approval. The allocation number is mandatory for the recipient to claim input VAT deduction. That review layer already exists. Skipping the NIS 15,000 step simply extends an operating system the Tax Authority has already built and tested.

For finance teams, the structural implication matters more than the political one. This is not a one-time filing change. It is a permanent shift in how input VAT deduction is validated, invoice by invoice, at rapidly declining thresholds.

## The Hidden AP Bottleneck: Allocation Numbers, Review Delays, and VAT Deduction Risk

The mechanics are straightforward. The risk is in the volume.

At NIS 25,000 (the original starting threshold), a mid-size enterprise might process a few hundred qualifying invoices per month. At NIS 10,000, that number multiplies. At NIS 5,000, it multiplies again. Every one of those invoices now requires:

- A valid, Tax Authority-reviewed allocation number
- Matching between the allocation number and the invoice data
- Verification before input VAT can be claimed
- An audit trail defensible under review

Manual validation does not scale linearly with invoice count. It scales worse. Each additional invoice adds review time, error risk, and exposure to VAT deduction disputes. A missed or mismatched allocation number does not just delay payment. It can disqualify the input VAT claim entirely.

## Why Manual AP Processes Won't Survive the June 2026 Threshold

This timeline is landing at a moment when finance functions are already stretched.

According to Deloitte's Q4 2025 CFO Signals survey, 87% of CFOs say AI will be extremely or very important to finance operations in 2026. Yet only 21% of active AI users report clear, measurable value, and just 14% have fully integrated AI agents into finance workflows. The gap between ambition and execution is wide, and Israel's compressed CTC timeline does not leave room to close it gradually.

Digital transformation is already the top stated priority. Deloitte reports that 50% of CFOs cite digital transformation of finance as their top 2026 priority, and 49% cite automating processes to free employees for higher-value work as their top talent priority. The mandate does not create this priority. It accelerates the deadline for acting on it.

Infrastructure is shifting to support this. According to Gartner's 2026 Finance Technology Bullseye Report, cited by CFO Dive, cloud ERP adoption rose 7% year over year and remains the highest-performing finance technology category, increasingly valued as the foundation for embedded automation across finance operations. Israel's allocation number requirement is a direct test of whether that ERP foundation extends to AP validation, or stops short of it.

## What a Compliance-Ready Invoice Gate Looks Like

Compliance-ready AP infrastructure treats allocation number validation as a systematic gate in front of the ERP, not a manual checkpoint after it.

That means:

- **OCR validation at invoice intake.** The system reads the allocation number on every incoming invoice automatically.
- **Rule-based matching.** The allocation number is checked against the invoice amount and the thresholds defined by law.
- **A hard stop for non-compliant invoices.** An invoice that fails validation is held at the gate. It never enters the ERP.
- **Self-service allocation where permitted.** When an invoice arrives without an allocation number, the system obtains one and stamps it on the invoice itself.
- **A clean ERP.** Only invoices that meet the Tax Authority's conditions are pushed through, so the ERP remains the trusted system of record.

This is the control layer StoreNext's Supplier Portal implements between suppliers and the ERP. The portal validates every incoming invoice with OCR, checks the allocation number against the invoice amount and the legal thresholds, and stops non-compliant invoices inside the portal. Where the regulation permits, it assigns and stamps an allocation number on the invoice itself. Allocation number validation is not a feature to bolt on. It is a gate that has to work at every invoice, every time, without exception.

Your ERP is your source of truth. Compliance infrastructure integrates with it. It does not replace it, and it does not sit beside it as a second, unreconciled system.

## A CFO Checklist: Six Months to Get Ahead of the NIS 5,000 Threshold

Six months is a tight window for infrastructure change, but it is enough time to act deliberately. Consider this sequence:

1. **Audit current invoice volume** at the NIS 10,000 and NIS 5,000 thresholds to size the real scope of exposure.
2. **Map your allocation number workflow** end to end, from vendor invoice receipt to VAT claim.
3. **Identify manual checkpoints** where allocation numbers are validated by hand today.
4. **Confirm ERP integration readiness** for automated allocation number matching.
5. **Build the audit trail** your finance team will need to defend VAT claims under Tax Authority review.
6. **Test before January 1, 2026**, using actual invoice volumes at the NIS 10,000 threshold, not projected ones.

The January threshold is a rehearsal. The June threshold is the real test. Organizations that treat the first deadline as a pilot will be better positioned when volume triples in June.

Israel's accelerated CTC timeline is not asking finance teams to do something new. It is asking them to do something they already do, at a volume manual processes were never designed to handle. The organizations that get ahead of this will treat it as infrastructure work, not a filing deadline. The ones that wait will find out the difference in June.