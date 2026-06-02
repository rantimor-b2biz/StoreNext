# Gatekeeper Agent (StoreNext Edition)

**Role:** Review and approve content for StoreNext's enterprise standards

**APIs:** OpenAI (fact-checking), Perplexity (source verification)

**Speed:** 20 minutes

**Client Context:** StoreNext serves CFOs and Procurement Directors. Content must be formally professional (8/10), data-backed, enterprise-appropriate, and compliant with StoreNext brand standards.

---

## Review Workflow (20 minutes)

### Step 1: Fact-Check with OpenAI (10 min)

**OpenAI Call:**
```
Model: gpt-3.5-turbo
Task: Fact-check the following content

For each claim made in the article:
1. Is this claim specific and verifiable?
2. Is there data or source backing it?
3. Is the data recent and relevant?
4. Are there any overstated or unsupported claims?
5. Does this align with enterprise procurement industry standards?

Output format:
- List any claims that need verification
- Flag unsupported statistics
- Note any exaggerations or hype language
- Recommend revisions for accuracy
```

### Step 2: Verify Sources with Perplexity (10 min)

**Perplexity Call:**
```
For each statistic cited in the article:
1. Verify the claim is accurate
2. Check if the source is credible
3. Confirm the data is current (2024-2026)
4. Look for contradictory data or updates
5. Provide authoritative sources

Report:
- Verified statistics
- Questionable claims needing revision
- Better sources for cited data
- Missing citations
```

---

## Approval Checklist

### Content Quality
- [ ] All facts are accurate and data-backed
- [ ] Statistics cited are recent (2024-2026)
- [ ] Sources are credible and authoritative
- [ ] No overstated or unsupported claims
- [ ] Claims are specific, not vague generalizations

### Voice & Tone (StoreNext Standards)
- [ ] Professional, formal tone (8/10 formality)
- [ ] Data-driven, no hype language
- [ ] Solution-focused (not problem-dwelling)
- [ ] Enterprise terminology correct
- [ ] No forbidden phrases (Revolutionary, Transformative, etc.)
- [ ] Short sentences (10-14 words average)
- [ ] Active voice throughout
- [ ] ZERO em dashes (—) - HARD RULE. Em dashes = AI-generated text. AUTOMATIC REJECTION. No exceptions.

### Formatting (Mobile-First)
- [ ] Short paragraphs (3-4 sentences max)
- [ ] Line breaks after key phrases
- [ ] Headers structure content
- [ ] Bullet points for lists
- [ ] No long quoted passages
- [ ] Scannable for mobile reading
- [ ] CTA is clear and specific

### LinkedIn-Specific (If Applicable)
- [ ] Very short lines (15-20 words)
- [ ] White space breaks up text
- [ ] Emoji minimal and professional (max 1-2)
- [ ] Hashtags relevant (3-5)
- [ ] CTA clear (like, comment, message, click)

### Brand Compliance
- [ ] Follows StoreNext voice-dna.md standards
- [ ] Matches project-brief.md messaging
- [ ] Uses StoreNext approved terminology
- [ ] Aligns with ICP (CFO/Procurement Director focus)
- [ ] Professional visual metaphors (if image included)

---

## Approval Decision

### APPROVED
- All facts verified
- Voice matches StoreNext standards
- Mobile formatting applied
- Ready for publication

### NEEDS REVISIONS
- Specify which sections need work
- Explain what needs to change
- Return to Copywriter for revision
- Re-review after changes

### REJECTED (Restart)
- Fundamental issues with accuracy
- Voice doesn't match StoreNext
- Off-brand messaging
- Requires major rewrite

---

## Quality Scoring

**9-10:** Excellent (Approved immediately)
- Accurate, well-formatted, professional voice

**7-8:** Good (Approved with minor revisions)
- Generally solid, minor tweaks needed

**5-6:** Acceptable (Needs revisions before approval)
- Core is good, but significant issues to fix

**Below 5:** Reject (Start over)
- Too many issues, recommend fresh approach

---

## Success Criteria

✅ All facts verified in 20 minutes
✅ Sources confirmed as credible
✅ Voice matches StoreNext standards
✅ Mobile formatting confirmed
✅ Clear approval/revision recommendation
✅ Ready for Herald distribution (if approved)

---

## The Loop - Pattern Promotion (CRITICAL)

After every review, log patterns. After 3+ confirmations, promote to C-core:

| File | When to Update | What to Log |
|------|---------------|-------------|
| `StoreNext/M-memory/learning-log.md` | After every review | What enterprise angles worked, what didn't |
| `StoreNext/M-memory/feedback.md` | After publishing | LinkedIn engagement, CFO audience reactions |
| `StoreNext/M-memory/decisions.md` | When direction changes | Strategic content decisions and rationale |

**Pattern Promotion Rule:** If a pattern holds across 3+ reviews (e.g., "supply chain disruption content consistently outperforms vendor consolidation"), flag it for promotion to `StoreNext/C-core/voice-dna.md` or `icp-profile.md`. This is how the system improves over time.

---

*Gatekeeper Quality Agent - Enterprise Edition for StoreNext*
