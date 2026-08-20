# Research Brief — W33 (2026-08-10) — Meteor

```json
{
  "topic": "Why November 2026 Is a Payments Deadline for CFOs, Not Just Banks (SWIFT ISO 20022 Structured-Address Mandate)",
  "pillar": "2. Financial operations & treasury (Meteor)",
  "product_focus": "Meteor",
  "angle": "SWIFT's move to ISO 20022 is usually framed as a bank IT project, but the November 2026 deadline to retire unstructured postal addresses puts the compliance burden on the corporate side: payment data must originate from the payer's own ERP. CFOs who assume their bank will handle this risk delayed or rejected cross-border payments starting in 2026. Meteor's direct ERP-to-bank/SWIFT payment initiation closes this gap by feeding structured, validated payment data straight from the ERP, with no manual re-entry, so enterprises are compliant by design rather than by year-end scramble.",
  "why_now": "SWIFT ended the MT/MX 'coexistence' period for cross-border payments in November 2025, and from January 1, 2026 is charging extra fees for firms still relying on legacy MT contingency processing. The next hard deadline, November 2026, forbids fully unstructured addresses in cross-border payment messages — a live, dated compliance milestone CFOs and treasury teams are actively planning for right now, not a hypothetical future trend.",
  "key_facts": [
    {
      "fact": "Legacy MT SWIFT messages have not been allowed in the SWIFT FIN network for cross-border payments since the November 2025 deadline, ending the MT/MX coexistence period.",
      "source": "Bank of America — business.bofa.com/en-us/content/iso-20022-migration.html"
    },
    {
      "fact": "Starting November 2026, fully unstructured postal addresses will no longer be accepted for RTGS and cross-border transfers; structured Country and Town Name fields become mandatory.",
      "source": "Kyriba — kyriba.com/resources/faqs/iso-20022-migration-frequently-asked-questions"
    },
    {
      "fact": "From January 1, 2026, SWIFT is applying additional charges for contingency processing and in-flow translation for institutions still sending legacy MT payment instruction messages.",
      "source": "SWIFT — swift.com/standards/iso-20022/iso-20022-faqs/implementation"
    },
    {
      "fact": "The enriched, structured payment data required under ISO 20022 (beneficiary addresses, payment purpose codes) must originate from corporate payment systems — banks will not add it on a customer's behalf.",
      "source": "Kyriba — kyriba.com/blog/iso-20022-corporate-treasury-2026"
    },
    {
      "fact": "Corporates are formally out of scope of SWIFT's mandatory migration timeline, but their banks are not — creating a compliance gap that falls back on the corporate ERP whenever address or purpose data is incomplete.",
      "source": "State Street — statestreet.com/us/en/insights/client-guide-to-iso-20022"
    },
    {
      "fact": "The Bank of Israel has already migrated its Zahav RTGS system to the ISO 20022 standard, aligning Israel's own payment infrastructure with SWIFT's cross-border messaging standard.",
      "source": "Bank of Israel — boi.org.il/en/economic-roles/payment-systems/payment-systems-in-israel/zahav"
    }
  ],
  "article_outline": [
    "A payments deadline hiding in a data field, not a bank system upgrade",
    "The ISO 20022 timeline so far: November 2025 coexistence ends, January 2026 legacy fees begin, November 2026 unstructured addresses are forbidden",
    "Why 'my bank will handle it' is the wrong assumption: payment data originates in the ERP, not the bank",
    "What's at risk for Israeli enterprises trading internationally: delayed settlement, rejected payments, manual remediation costs",
    "Zahav's own ISO 20022 alignment shows the direction is structural, not optional, even domestically",
    "Closing the gap: how ERP-to-bank/SWIFT payment initiation with structured data removes the manual re-entry step and the compliance risk"
  ],
  "candidates_considered": [
    "SWIFT ISO 20022 structured-address deadline (Nov 2026) and its ERP-side compliance burden — SELECTED",
    "Rising FX volatility (PwC: 83% of treasurers rank FX as top risk; Alpha Group: 63% expect more volatility in 2026) tied to Meteor's automatic FX rate import",
    "Open banking / API-first bank connectivity replacing manual multi-bank reporting (McKinsey: 88% of banking execs say APIs are more important) — set aside as too close to W32's fragmented bank/ERP data framing"
  ]
}
```
