# Gatekeeper Review — W34 — StoreNext

**Verdict:** REVISED

- Product claim overreach: article attributed sanctions screening, beneficial-ownership verification, financial-stability checks, conditional activation, and continuous refresh to StoreNext's Supplier Portal. None are approved capabilities. Rewrote the StoreNext tie-in to only approved capabilities (centralized supplier communication, structured document/invoice flow into the ERP, CTC/e-invoicing compliance gate, audit trail, operational continuity). The generic 'structured onboarding gate' section is fine as market best-practice, but the StoreNext-specific paragraph now claims only what the product actually does.
- Voice/formatting: no em dashes, no exclamation marks, no banned hype words found. Left intact.
- Numbers scoped correctly: no Meteor numbers borrowed for Supplier Portal; external stats retain named sources. Clean.
- No fraud-detection tie-in. No 'unified platform' or '40 years'. Clean.
- Tightened a few sentences toward 10-14 word cadence for CFO skim.

---

## Revision 2 — 2026-08-20, per Ran's review

**Verdict:** REVISED (post rewritten by Ran, article and visual realigned)

Ran validated the source independently and confirmed the 7% / 11% figures are accurate.
Three defects survived Revision 1 and were fixed:

1. **Causal leap beyond the source.** The post claimed "Concentration risk is rising
   exactly where onboarding controls are weakest." Vital Signs 2026 measures
   single/sole-source supplier loss. It does not examine onboarding and does not link
   the two. Removed. The article now states what the report measured, then labels our
   inference as ours.
2. **Absolute claim.** "The only window with full leverage is before the first purchase
   order" traced back to LeanLinking, a procurement software vendor's guidance page.
   Vendor content cannot carry a categorical claim, and contract renewal and
   re-tendering are obvious counter-examples. Reframed as one of the most important
   opportunities to build control before dependency forms.
3. **Product bullets answered a different problem.** The first bullet moved to invoices
   and allocation numbers while the post's problem was onboarding and supplier risk.
   Root cause: Revision 1 correctly stripped the unapproved onboarding capabilities
   (screening, conditional activation, continuous refresh), which left only the CTC
   invoice gate as an approved capability, and the draft kept the premise and swapped
   the feature in. Bullets are now generic to structured supplier platforms, with
   StoreNext named for scale rather than for onboarding features it does not have.

**Additions from Ran's source check:** 37% name single or sole-source suppliers as a
pressing vulnerability, 21% cite insufficient visibility into supplier challenges.
Attribution corrected to NDIA (publisher) rather than National Defense Magazine.

**Also updated:** article title and body, `visual-data.json` hook, regenerated
`W34-visual.png` and `article.docx`, new hard rules in `A-agents/copywriter-agent.md`
and `A-agents/gatekeeper-agent.md`.

**Open item for Ran:** the approved post names the product "StoreNext Supplier
Collaboration Platform"; `C-core/product-capabilities.md` calls it "Supplier Portal".
Confirm which name is canonical. Separately, supplier onboarding is not currently a
listed Supplier Portal capability, which is why this topic strained. Confirm whether
it should be added.

---

## Revision 3 — 2026-08-20, per Ran's full strategic feedback

**Verdict:** REBUILT. Premise replaced, not edited.

Revision 2 fixed accuracy defects inside a premise that was itself wrong. Ran's full
review established that the entire onboarding framing overstated the product.

**The scope error.** The post positioned StoreNext in the pre-contract stage: selecting
suppliers, verifying them before the first PO, screening, building commercial leverage,
controlling dependency before it forms. StoreNext does none of this. The platform's
territory begins after a supplier is already approved and working with the organization.

**The terminology trap.** "Onboarding" carries a market meaning (bringing a new supplier
into the organization) and a narrower StoreNext meaning (onboarding an already approved
supplier into the platform and the digital working process). The draft used the word and
inherited the market meaning.

**The data error.** NDIA's single-source supplier loss data is accurate, but it describes
supply-chain concentration, a problem the platform does not solve. Replaced with Ardent
Partners' Accounts Payable Metrics that Matter in 2025: AP organizations outside the
Best-in-Class spend 26.9% of staff time on supplier inquiries, Best-in-Class spend 13.4%.
Verified independently against the source before use.

**New thesis:** supplier inquiries are a process-design problem, not a communication
problem. The argument runs hook, interpretation, reframe, strategic insight, product,
proof, closing insight, question, per Ran's recommended structure.

**Terminology:** Supplier Collaboration Platform for strategic value, Supplier Portal as
the product name. Applied across post, article and `C-core/product-capabilities.md`.

**Rebuilt:** `final-post.md`, `article.md`, `visual-data.json`, `W34-visual.png`,
`article.docx`, `B-brain/topic-history.json` entry.

**Source-of-truth updated:** `C-core/product-capabilities.md` now carries the value
territory, the positioning principle, the precise definition of onboarding, and an
explicit NOT-approved list for the pre-contract stage. New scope rules added to
copywriter, gatekeeper and researcher agents.

**Note on precision:** the hook says "AP teams outside the Best-in-Class spend 26.9%"
rather than "26.9% of AP staff time", because 26.9% is the non-Best-in-Class figure, not
an all-respondent average. Ran's own section 4 used the precise form.
