# T-tools: Prompts, Templates & Workflows

**Directory:** Reusable tools for consistent, efficient agent execution

---

## Overview

This directory contains everything agents need to execute their work consistently and efficiently:

- **Prompts** — AI-powered instructions for each agent role
- **Templates** — Output templates for standardized formats
- **Workflows** — Step-by-step processes for complex tasks
- **Checklists** — Quality assurance guidelines
- **Scripts** — Automation and data processing

---

## Directory Structure

```
T-tools/
├── README.md (this file)
├── prompts/
│   ├── research-prompt.md
│   ├── copywriter-prompt.md
│   ├── paid-search-prompt.md
│   ├── newsletter-prompt.md
│   ├── visual-prompt.md
│   ├── abm-prompt.md
│   ├── sales-enablement-prompt.md
│   └── analytics-prompt.md
├── templates/
│   ├── blog-post-template.md
│   ├── case-study-template.md
│   ├── email-template.md
│   ├── pitch-deck-outline.md
│   └── research-brief-template.md
├── workflows/
│   ├── blog-post-workflow.md
│   ├── campaign-launch-workflow.md
│   ├── monthly-review-workflow.md
│   └── content-repurposing-workflow.md
├── checklists/
│   ├── content-quality-checklist.md
│   ├── brand-alignment-checklist.md
│   ├── campaign-launch-checklist.md
│   └── deliverable-review-checklist.md
└── scripts/
    ├── weekly-report-generator.py
    ├── content-scheduler.py
    └── lead-quality-scorer.py
```

---

## 📋 Prompts (For Each Agent)

Each agent has a detailed prompt guiding their work:

### research-prompt.md
Guide for **Research Agent**
- What to research and why
- How to structure findings
- Output template: Weekly research brief
- Quality standards and validation

### copywriter-prompt.md
Guide for **Copywriter Agent**
- Blog post structure and requirements
- Case study framework
- Email copy guidelines
- Sales copy templates
- SEO optimization checklist

### paid-search-prompt.md
Guide for **Paid Search Agent**
- LinkedIn Ads best practices
- Google Ads strategy
- Audience targeting guidelines
- Ad copy frameworks
- Campaign setup and naming conventions
- Performance targets

### newsletter-prompt.md
Guide for **Newsletter Agent**
- Email templates (welcome, nurture, promotional)
- Subject line frameworks
- Email structure and length
- CTA optimization
- Segmentation strategies
- List management

### visual-prompt.md
Guide for **Visual Agent**
- Brand guidelines reference
- Design templates
- Color palette and typography
- Image sourcing standards
- Accessibility requirements
- Design approval checklist

### abm-prompt.md
Guide for **ABM Agent**
- Account targeting criteria
- LinkedIn campaign setup
- Personalization strategies
- Engagement metrics
- Campaign structure and optimization

### sales-enablement-prompt.md
Guide for **Sales Enablement Agent**
- Pitch deck outline
- ROI calculator framework
- Battle card structure
- One-pager template
- Proposal outline
- Sales collateral checklist

### analytics-prompt.md
Guide for **Analytics Agent**
- KPI definitions
- Monthly report structure
- Dashboard setup
- Lead quality scoring
- Pipeline attribution methods
- Performance analysis framework

---

## 📋 Templates

Standardized output formats for consistency:

### Blog Post Template
```
# [Title]
## Intro (Hook + Problem)
## Deep Dive (3 sections)
## Solution: How StoreNext Addresses This
## Proof/Example
## Roadmap
## Conclusion & CTA
## Meta (Tags, Keywords, CTA)
```

### Case Study Template
```
# Case Study: [Company]
## Challenge
## Solution
## Results (Quantified)
## Customer Quote
## Key Takeaways
## Visuals
```

### Email Template
```
Subject: [Under 50 chars]
Preview: [40-60 chars]

[Greeting]
[Opening]
[Body - Value First]
[CTA Button]
[Signature]

Metadata: Segment, Send Time, Goals
```

### Research Brief Template
```
# Research Brief – [Topic]
## Executive Summary
## Key Findings (3-5)
## Data & Proof Points
## Competitive Landscape
## Recommended Actions
## Sources
```

---

## 🔄 Workflows (Step-by-Step Processes)

### blog-post-workflow.md
**End-to-End:** Research → Draft → Review → Publish
1. Research Agent: Create research brief
2. Copywriter: Draft blog post
3. Director: Review & approve
4. Visual: Create social graphics
5. Copywriter: Finalize & optimize for SEO
6. Director: Final approval
7. Copywriter: Publish & promote

### campaign-launch-workflow.md
**End-to-End:** Strategy → Build → Launch → Monitor
1. Strategy: Define goals, audience, budget
2. Research: Competitive & audience analysis
3. Copywriter: Ad copy & landing page
4. Visual: Creative assets
5. Paid Search: Campaign setup & targeting
6. Director: Approval
7. Paid Search: Launch & daily monitoring
8. Analytics: Track performance & report

### monthly-review-workflow.md
**End-to-End:** Collect → Analyze → Report → Improve
1. Analytics: Pull all monthly metrics
2. All agents: Share learnings & feedback
3. Director: Aggregate insights
4. All agents: Review performance report
5. Director: Recommend optimizations
6. Record decisions in M-memory/decisions.md

### content-repurposing-workflow.md
**End-to-End:** One piece → Multiple formats
1. Copywriter: Create original blog post
2. Newsletter: Adapt for email sequence
3. Visual: Create social graphics
4. Copywriter: Pull key quotes for LinkedIn
5. Copywriter: Create 1-page summary
6. Visual: Create infographic
7. All: Publish across channels

---

## ✅ Checklists (Quality Assurance)

### content-quality-checklist.md
- [ ] Grammar & spelling perfect
- [ ] Brand voice aligned
- [ ] Claims verified with data
- [ ] Links functional & relevant
- [ ] CTA clear & specific
- [ ] SEO optimized (keywords, headers, meta)
- [ ] Mobile responsive
- [ ] Accessibility standards met
- [ ] Legal/compliance reviewed
- [ ] Ready for publishing

### brand-alignment-checklist.md
- [ ] Positions StoreNext as infrastructure (not tool)
- [ ] Addresses Enterprise complexity appropriately
- [ ] Speaks to correct personas
- [ ] Data-driven, not hype
- [ ] Professional tone (technical, confident, transparent)
- [ ] No buzzwords or vague language
- [ ] Consistent with established messaging
- [ ] All claims supported by proof

### campaign-launch-checklist.md
- [ ] Goals & success metrics defined
- [ ] Target audience clearly defined
- [ ] Ad copy & creatives approved
- [ ] Landing pages tested & functional
- [ ] Tracking & analytics configured
- [ ] Team notified of launch
- [ ] Monitoring plan established
- [ ] Budget allocated & approved
- [ ] Schedule confirmed

### deliverable-review-checklist.md
- [ ] Matches stated deliverable format
- [ ] On time (Monday EOD for weekly items)
- [ ] Meets quality standards
- [ ] Brand-aligned
- [ ] Complete (no sections missing)
- [ ] Links/references functional
- [ ] Data accurate
- [ ] Ready for next step

---

## 🔧 Scripts (Automation)

### weekly-report-generator.py
**Purpose:** Aggregate metrics and generate reports
- Pulls data from Google Analytics, LinkedIn, email platform
- Aggregates key metrics
- Generates markdown report
- Highlights trends and winners/losers

### content-scheduler.py
**Purpose:** Schedule content across channels
- Reads content calendar
- Schedules posts to LinkedIn, email, blog
- Manages timing and coordination
- Tracks scheduled vs. published

### lead-quality-scorer.py
**Purpose:** Score and rank leads by sales readiness
- Uses company data (size, industry, behavior)
- Assigns quality score
- Ranks by propensity to buy
- Provides intelligence to sales team

---

## 🚀 How to Use These Tools

### Using a Prompt
1. Find the agent's prompt file
2. Copy the prompt text
3. Paste into Claude or AI tool
4. Customize with specific details
5. Execute and review output
6. Use relevant template for structure

### Using a Template
1. Review the template structure
2. Copy and use as starting point
3. Fill in with your content
4. Verify it matches the template format
5. Submit for review

### Following a Workflow
1. Read the workflow file completely
2. Follow each step in sequence
3. Complete outputs before moving to next step
4. Reference prompts/templates as needed
5. Use checklists for quality gates

### Quality Assurance
1. Complete deliverable
2. Review relevant checklist
3. Fix any items that don't pass
4. Get approval before moving forward

---

## 🔄 Continuous Improvement

**Prompt Updates:**
- Monthly review of effectiveness
- Agent feedback on usefulness
- Update based on learnings
- Version control with dates

**Template Updates:**
- Track actual usage
- Simplify based on feedback
- Add new templates for new processes
- Remove obsolete templates

**Workflow Improvements:**
- Monthly retrospective
- Identify bottlenecks
- Streamline steps
- Document lessons learned

---

*Last updated: 2026-02-25*

---

> **StoreNext Group**
> T-tools: Templates, Prompts & Workflows
> Standardization for Consistency & Speed
