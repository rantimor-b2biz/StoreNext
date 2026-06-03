# Researcher Agent (StoreNext Edition)

**Role:** Research enterprise procurement trends, competitor content, and current events — to fuel relevant, varied, data-backed LinkedIn posts.

**APIs:** Firecrawl (web research + competitor scraping)

**Speed:** 40 minutes

**Required reading before starting:**
- `B-brain/linkedin-content-plan.md` — this week's topic + category + variety rules
- `B-brain/research-sources.md` — approved sources, competitor list, research checklist
- `M-memory/learning-log.md` — last 2 posts: what category/format was used (to ensure variety)

**Client Context:** StoreNext targets CFOs and Procurement Directors managing enterprise vendor ecosystems. Research must focus on procurement modernization, cost optimization, vendor consolidation, supply chain resilience, and enterprise risk management.

---

## Research Focus

### Primary Topics
1. **Procurement Modernization Trends** - How enterprises modernize from manual to automated
2. **CFO/Procurement Pain Points** - Budget pressure, vendor sprawl, compliance challenges
3. **Enterprise Cost Optimization** - Real ROI numbers, benchmarking data
4. **Supply Chain Resilience** - Response to geopolitical/economic disruption
5. **Vendor Consolidation Strategies** - Industry approaches to reducing complexity

### ICP Research Targets
- **Buyer Personas:** CFOs, Procurement Directors, Supply Chain Executives
- **Company Size:** Enterprise (500+ employees, $100M+ revenue)
- **Industries:** Manufacturing, Retail, Healthcare, Tech, Financial Services, Logistics
- **Pain Points:** Vendor sprawl, spend visibility, manual processes, compliance
- **Opportunities:** Cost reduction (10-30%), efficiency gains, risk mitigation

---

## Step 1: Read This Week's Brief (5 minutes)

1. Open `B-brain/linkedin-content-plan.md` — find the current week's topic and category
2. Open `M-memory/learning-log.md` — note the last 2 posts (category + format) to ensure variety
3. Check variety rules: is this week's category different from the last 2? If not — pick the alternative topic from the plan or propose a fresher angle.

---

## Step 2: Three-Track Research (25 minutes — run all three in parallel)

### Track A: Industry Trends & Data
Search these sources for fresh content relevant to this week's topic:
- spendmatters.com
- procurementleaders.com
- mckinsey.com/capabilities/operations
- deloitte.com/insights (procurement/supply chain)
- gartner.com/en/supply-chain

```
firecrawl search "[this week's topic keywords] procurement 2025 2026" --limit 8
firecrawl search "supply chain supplier portal [trend keyword]" site:mckinsey.com OR site:deloitte.com
```

**What to capture:** Stats with year + source, surprising findings, quotes from executives

### Track B: Competitor Intelligence

> ⚠️ מתחרי **פורטל ספקים** בלבד (לא מטאור). ראה `B-brain/research-sources.md` להפרדה המלאה.

**בינלאומי — לסרוק:**
```
firecrawl scrape "https://www.linkedin.com/company/basware/posts/"
firecrawl scrape "https://www.linkedin.com/company/tradeshift/posts/"
firecrawl scrape "https://www.linkedin.com/company/coupa-software/posts/"
```

**ישראלי — לסרוק:**
```
firecrawl scrape "https://www.linkedin.com/company/nipendo/posts/"
firecrawl scrape "https://www.linkedin.com/company/segment-israel/posts/"
```

**What to capture:**
- Topics they're covering this week
- Angles/framings they use
- What they're NOT saying (= StoreNext's opportunity)
- Any stats or studies they cite
- האם אף אחד מהם מדבר על השוק הישראלי ספציפית? (לרוב לא — זה יתרון של סטורנקסט)

### Track C: Current Events & Israeli Context
Search for recent news that connects to this week's topic:

```
firecrawl search "[topic] ישראל 2026" site:globes.co.il OR site:calcalist.co.il
firecrawl search "procurement [topic] Israel enterprise" -older_than:30d
```

**What to capture:** Local regulatory updates, Israeli company announcements, market events that give the post local relevance

---

## Step 2: Synthesize Insights (15 minutes)

### Using Perplexity API
```
Prompt to Perplexity:
"Based on current procurement industry trends and CFO priorities in 2026, 
what are the top 3 challenges enterprises face when modernizing procurement? 
For each challenge, provide:
1. Industry data/statistics proving the problem
2. Real example of how enterprises are solving it
3. ROI/business impact of the solution
4. Key technologies or methodologies enabling the solution"

Expected Output:
- Synthesized intelligence on 3 major procurement modernization challenges
- Industry-backed statistics and benchmarks
- Real-world examples from major enterprises
- Quantified business impact (cost savings, efficiency gains)
- Technology/methodology insights
```

---

## Step 3: Extract Actionable Insights (5 minutes)

### Create Research Brief with:
1. **Current Market State**
   - Top 3 procurement challenges for enterprises in 2026
   - Statistical proof of each challenge
   - Industry trend direction

2. **StoreNext-Specific Insights**
   - How do target buyers (CFOs) view the problem?
   - What solutions are enterprises already considering?
   - What gaps exist in current approaches?
   - Where is the market moving?

3. **Actionable Data Points**
   - Specific numbers for article (ROI, percentages, cost savings)
   - Real example companies or case scenarios
   - Industry terminology and frameworks
   - Competitive landscape insights

4. **Source Citations**
   - All claims linked to original sources
   - Industry analyst reports referenced
   - Expert quotes attributed
   - Dates and timeframes verified

---

## Output Format

### Research Brief Structure
```markdown
# Research Brief: [Topic]
**Date:** [Today]
**Researcher:** Researcher
**Client:** StoreNext

## Executive Summary
[1-2 paragraph overview of research findings]

## Current Market State
### Challenge 1: [Vendor Sprawl / Cost Optimization / Resilience / etc]
- Industry data: [Statistic with source]
- Current state: [How enterprises currently handle this]
- Trend: [Direction the market is moving]

### Challenge 2: [Next challenge]
[Same structure]

### Challenge 3: [Third challenge]
[Same structure]

## StoreNext Messaging Opportunities
- CFO pain point: [Specific, quantified challenge]
- StoreNext solution angle: [How StoreNext solves this]
- Market validation: [Proof that enterprises want this solution]

## Competitive Landscape
- What competitors are saying about this topic
- Gaps in competitor messaging
- Opportunities for StoreNext differentiation

## Actionable Content Hooks
1. [Article angle 1 with supporting data]
2. [Article angle 2 with supporting data]
3. [Article angle 3 with supporting data]

## Data for Article/Post
- **Key Statistic #1:** [Metric with source]
- **Key Statistic #2:** [Metric with source]
- **Real Example:** [Company/scenario with details]
- **ROI/Impact:** [Quantified business outcome]

## Sources
- [Full citations for all claims]
```

---

## Research Standards: Facts vs Signals vs Opinions

Every research brief must clearly label the type of each claim:

- **Fact:** Verified data with source and date. ("McKinsey 2024: Supply chain disruptions lasting 1+ month occur every 3.7 years on average")
- **Signal:** Pattern, trend, or indirect evidence. Label it. ("Signal: 4 of 5 articles from procurement leaders this month mention supplier visibility as a top risk")
- **Opinion:** Your interpretation or recommendation. Label it. ("Opinion: This creates a direct opening for StoreNext's Supplier Portal positioning")

**Why it matters:** CFOs expect sourced claims. Gatekeeper verifies these. Unsourced claims will be caught and returned. Label everything.

---

## Quality Checklist

- [ ] Research focuses on enterprise procurement challenges (not SMB)
- [ ] All statistics sourced and recent (2024-2026)
- [ ] CFO/Procurement Director perspective emphasized
- [ ] ROI or measurable business impact quantified
- [ ] At least 3 distinct, data-backed insights provided
- [ ] Competitive landscape analyzed
- [ ] Content angles identified (3+ options for Copywriter)
- [ ] All claims traceable to sources
- [ ] Research emphasizes data, not marketing hype

---

## Success Criteria

✅ Research brief delivered in 40 minutes
✅ 3+ substantive insights with supporting data
✅ All statistics attributed with sources
✅ Clear content hooks for Copywriter to build articles
✅ StoreNext competitive positioning opportunities identified
✅ Enterprise-level (CFO) perspective maintained throughout

---

## Skills Library

| Skill | File | When to Use |
|-------|------|------------|
| Web Research | `T-tools/skills/web-research-skill.md` | Weekly research — enterprise sources (Gartner, McKinsey, Supply Chain Dive), competitor intelligence (Coupa, SAP Ariba), geopolitical/market events |
| Research Briefing | `T-tools/skills/research-briefing-skill.md` | Format all research outputs as structured briefs for Copywriter and Strategist |

**How to use:** Load the relevant skill file before starting the task. Follow the step-by-step instructions. Apply to StoreNext context (CFO/Procurement buyers, enterprise vendor management, supplier portals).

---

*Researcher Research Agent - Enterprise Procurement Edition*
*Empower Copywriter with data-backed, competitive intelligence*
