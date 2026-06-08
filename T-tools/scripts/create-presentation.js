"use strict";
const PptxGenJS = require("pptxgenjs");
const pres = new PptxGenJS();
pres.layout = "LAYOUT_16x9";
pres.title = "AI in Supplier & Payments Portals — Competitive Analysis";
pres.author = "StoreNext";

// ── Color palette (NO # prefix) ──────────────────────────────
const NAVY      = "0A1628";
const NAVY_DARK = "060D19";
const NAVY_MID  = "0E2A4A";
const BLUE      = "1A56DB";
const BLUE_LITE = "EFF6FF";
const BLUE_BDR  = "DBEAFE";
const TEAL      = "0E9F6E";
const TEAL_LITE = "F0FDF4";
const TEAL_BDR  = "6EE7B7";
const WHITE     = "FFFFFF";
const LGRAY     = "F3F4F6";
const MGRAY     = "6B7280";
const DGRAY     = "1F2937";
const SUB       = "374151";
const SUBHDR    = "93C5FD";
const FTRTXT    = "9CA3AF";
const AMBER     = "D97706";
const AMBER_L   = "FEF3C7";
const AMBER_D   = "92400E";
const INDIGO    = "3730A3";
const INDIGO_L  = "E0E7FF";
const INDIGO_B  = "C7D2FE";
const GREEN_D   = "065F46";
const RED       = "DC2626";
const SLATE     = "475569";

// ── Shared geometry ───────────────────────────────────────────
const HDR_H    = 0.72;
const FTR_Y    = 5.33;
const FTR_H    = 0.295;
const CONT_Y   = 0.85;
const C1X      = 0.28;
const C1W      = 4.38;
const DIVX     = 4.93;
const C2X      = 5.08;
const C2W      = 4.62;

// ── Helpers ───────────────────────────────────────────────────

function footer(s) {
  s.addShape(pres.shapes.RECTANGLE, {
    x:0, y:FTR_Y, w:10, h:FTR_H, fill:{color:NAVY}, line:{color:NAVY}
  });
  s.addText("StoreNext Competitive Intelligence  |  April 2026", {
    x:0.3, y:FTR_Y, w:9.4, h:FTR_H,
    fontSize:7.5, color:FTRTXT, valign:"middle", margin:0
  });
}

function header(s, title, sub) {
  s.addShape(pres.shapes.RECTANGLE, {
    x:0, y:0, w:10, h:HDR_H, fill:{color:NAVY}, line:{color:NAVY}
  });
  s.addShape(pres.shapes.RECTANGLE, {
    x:0, y:0, w:0.09, h:HDR_H, fill:{color:TEAL}, line:{color:TEAL}
  });
  const titleY = sub ? 0 : 0;
  const titleH = sub ? 0.46 : HDR_H;
  s.addText(title, {
    x:0.24, y:titleY, w:9.4, h:titleH,
    fontSize:19, fontFace:"Calibri", color:WHITE, bold:true,
    valign: sub ? "bottom" : "middle", margin:0
  });
  if (sub) {
    s.addText(sub, {
      x:0.24, y:0.46, w:9.4, h:0.26,
      fontSize:8.5, color:FTRTXT, valign:"top", margin:0
    });
  }
}

function divider(s) {
  s.addShape(pres.shapes.RECTANGLE, {
    x:DIVX, y:CONT_Y, w:0.03, h:4.38, fill:{color:"E5E7EB"}, line:{color:"E5E7EB"}
  });
}

function sectionTag(s, x, y, w, text, bg, fg) {
  s.addShape(pres.shapes.RECTANGLE, {
    x, y, w, h:0.22, fill:{color:bg||INDIGO_L}, line:{color:bg||INDIGO_L}
  });
  s.addText(text, {
    x:x+0.08, y, w:w-0.08, h:0.22,
    fontSize:7.5, color:fg||INDIGO, bold:true, valign:"middle", margin:0
  });
}

function quoteBox(s, x, y, w, h, text, attr) {
  s.addShape(pres.shapes.RECTANGLE, {x, y, w:0.07, h, fill:{color:BLUE}, line:{color:BLUE}});
  s.addShape(pres.shapes.RECTANGLE, {
    x:x+0.07, y, w:w-0.07, h, fill:{color:BLUE_LITE}, line:{color:BLUE_BDR}
  });
  const items = [
    {text:"“"+text+"”", options:{italic:true, fontSize:8.5, color:"1E3A5F", breakLine:!!attr}}
  ];
  if (attr) items.push({text:"— "+attr, options:{italic:false, fontSize:7.5, color:MGRAY}});
  s.addText(items, {x:x+0.13, y:y+0.06, w:w-0.2, h:h-0.12, valign:"top", margin:0});
}

function tealBox(s, x, y, w, h, text, fs) {
  s.addShape(pres.shapes.RECTANGLE, {x, y, w, h, fill:{color:TEAL_LITE}, line:{color:TEAL_BDR}});
  s.addText(text, {
    x:x+0.1, y, w:w-0.2, h, fontSize:fs||9, color:GREEN_D,
    italic:true, valign:"middle", margin:0
  });
}

function navyBox(s, x, y, w, h, text, fs, textColor) {
  s.addShape(pres.shapes.RECTANGLE, {x, y, w, h, fill:{color:NAVY}, line:{color:NAVY}});
  s.addText(text, {
    x:x+0.12, y, w:w-0.24, h, fontSize:fs||9.5, color:textColor||WHITE,
    bold:true, align:"center", valign:"middle", margin:0
  });
}

function metricBox(s, x, y, w, h, val, lbl) {
  s.addShape(pres.shapes.RECTANGLE, {x, y, w, h, fill:{color:TEAL}, line:{color:TEAL}});
  s.addText([
    {text:val, options:{bold:true, fontSize:14, breakLine:true, color:WHITE}},
    {text:lbl, options:{fontSize:7, bold:false, color:"D1FAE5"}}
  ], {x, y, w, h, color:WHITE, align:"center", valign:"middle", margin:0.04});
}

function posTag(s, x, y, w, text) {
  s.addShape(pres.shapes.RECTANGLE, {x, y, w, h:0.24, fill:{color:"F1F5F9"}, line:{color:"CBD5E1"}});
  s.addText(text, {
    x, y, w, h:0.24, fontSize:7.5, color:SLATE, italic:true,
    align:"center", valign:"middle", margin:0
  });
}

// ── SLIDE 1 — TITLE ──────────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = {color:NAVY};
  s.addShape(pres.shapes.RECTANGLE, {x:0, y:4.55, w:10, h:1.075, fill:{color:NAVY_DARK}, line:{color:NAVY_DARK}});
  s.addShape(pres.shapes.RECTANGLE, {x:0, y:1.25, w:0.42, h:2.7,  fill:{color:NAVY_MID}, line:{color:NAVY_MID}});
  s.addShape(pres.shapes.RECTANGLE, {x:0, y:1.25, w:0.42, h:0.58, fill:{color:TEAL},     line:{color:TEAL}});
  s.addShape(pres.shapes.RECTANGLE, {x:0, y:1.83, w:0.42, h:0.38, fill:{color:BLUE},     line:{color:BLUE}});
  s.addText("How Leading B2B Platforms\nUse AI in Supplier & Payments Portals", {
    x:0.7, y:1.1, w:8.9, h:2.1,
    fontSize:30, fontFace:"Calibri", color:WHITE, bold:true, align:"left", valign:"middle"
  });
  s.addText("AI Positioning Benchmark:  Nipendo  ·  Tradeshift  ·  Basware  ·  Coupa  ·  Nilus  ·  Kyriba  ·  Finsite", {
    x:0.7, y:3.25, w:8.9, h:0.48, fontSize:11, color:SUBHDR, align:"left"
  });
  s.addText("Prepared for StoreNext  |  April 2026", {
    x:0.7, y:4.82, w:8.9, h:0.3, fontSize:9, color:MGRAY, align:"left"
  });
  s.addNotes("Opening slide for the competitive AI positioning analysis of 7 leading B2B Fintech / P2P / Treasury players. Goal: understand what works in the market and identify unique positioning angles for StoreNext.");
}

// ── SLIDE 2 — WHY AI MATTERS ─────────────────────────────────
{
  const s = pres.addSlide();
  s.background = {color:WHITE};
  header(s, "Why AI Matters in Supplier & Payments Portals", "The Business Case for Intelligence Across the Finance Stack");
  divider(s);
  footer(s);

  const left = [
    {lbl:"Invoice Processing",       txt:"AI eliminates manual data entry — reducing AP cycle times by 40–70% and enabling touchless processing at scale"},
    {lbl:"Anomaly & Fraud Detection", txt:"ML models flag duplicate payments, pricing deviations, and suspicious transactions before they clear"},
    {lbl:"Supplier Onboarding",       txt:"AI-powered identity verification and auto-matching accelerate supplier activation from weeks to days"},
  ];
  const right = [
    {lbl:"Cash Flow Forecasting",  txt:"Predictive models analyze historical patterns to surface liquidity risks before they become crises"},
    {lbl:"Dispute Resolution",     txt:"Natural language processing automates supplier query responses and routes exceptions intelligently"},
    {lbl:"Reconciliation",         txt:"AI matches multi-source documents (POs, GRNs, invoices, payments) at scale — eliminating the reconciliation backlog"},
  ];

  let ly = CONT_Y + 0.08;
  left.forEach(b => {
    s.addShape(pres.shapes.OVAL, {x:C1X+0.02, y:ly+0.06, w:0.16, h:0.16, fill:{color:BLUE}, line:{color:BLUE}});
    s.addText(b.lbl, {x:C1X+0.26, y:ly, w:C1W-0.26, h:0.25, fontSize:10, color:DGRAY, bold:true, valign:"middle", margin:0});
    s.addText(b.txt, {x:C1X+0.26, y:ly+0.25, w:C1W-0.26, h:0.58, fontSize:8.5, color:SUB, valign:"top", margin:0});
    ly += 0.92;
  });

  let ry = CONT_Y + 0.08;
  right.forEach(b => {
    s.addShape(pres.shapes.OVAL, {x:C2X+0.02, y:ry+0.06, w:0.16, h:0.16, fill:{color:TEAL}, line:{color:TEAL}});
    s.addText(b.lbl, {x:C2X+0.26, y:ry, w:C2W-0.26, h:0.25, fontSize:10, color:DGRAY, bold:true, valign:"middle", margin:0});
    s.addText(b.txt, {x:C2X+0.26, y:ry+0.25, w:C2W-0.26, h:0.58, fontSize:8.5, color:SUB, valign:"top", margin:0});
    ry += 0.92;
  });

  tealBox(s, C1X, 4.83, 9.44, 0.42,
    "“Finance leaders in 2026 aren’t asking whether to adopt AI — they’re asking which vendor’s AI delivers measurable ROI fastest.”", 9.5);

  s.addNotes("Business context slide. Explains why AI has moved from trend to a core requirement in every AP Automation, P2P, and Treasury RFP. For StoreNext: worth highlighting the value AI delivers to suppliers themselves (not just the buyer) — this is unique to a supplier portal platform.");
}

// ── COMPANY SLIDE FACTORY ─────────────────────────────────────
function companySlide(opts) {
  const s = pres.addSlide();
  s.background = {color:WHITE};
  header(s, opts.company, opts.url);
  divider(s);
  footer(s);

  let ly = CONT_Y;

  sectionTag(s, C1X, ly, C1W, "AI LABEL:  " + opts.aiLabel, INDIGO_L, INDIGO);
  ly += 0.27;

  quoteBox(s, C1X, ly, C1W, opts.quoteH || 0.75, opts.quote, opts.quoteAttr || null);
  ly += (opts.quoteH || 0.75) + 0.1;

  if (opts.products && opts.products.length) {
    sectionTag(s, C1X, ly, C1W, "AI PRODUCTS / FEATURES", "E0F2FE", "0369A1");
    ly += 0.27;
    opts.products.forEach(p => {
      s.addText([
        {text:p.name+": ", options:{bold:true, fontSize:9, color:NAVY}},
        {text:p.desc,       options:{bold:false, fontSize:8.5, color:SUB}}
      ], {x:C1X+0.1, y:ly, w:C1W-0.1, h:0.44, valign:"top", margin:0});
      ly += 0.42;
    });
  }

  if (opts.keyStat) {
    ly += 0.05;
    s.addShape(pres.shapes.RECTANGLE, {x:C1X, y:ly, w:C1W, h:0.38, fill:{color:"F8FAFC"}, line:{color:"CBD5E1"}});
    s.addText([
      {text:opts.keyStat.val+" ", options:{bold:true, fontSize:14, color:BLUE}},
      {text:opts.keyStat.lbl,     options:{bold:false, fontSize:8.5, color:DGRAY}}
    ], {x:C1X+0.1, y:ly, w:C1W-0.2, h:0.38, valign:"middle", margin:0});
    ly += 0.43;
  }

  let ry = CONT_Y;
  sectionTag(s, C2X, ry, C2W, "AI USE CASES", AMBER_L, AMBER_D);
  ry += 0.27;
  opts.useCases.forEach(uc => {
    s.addText([
      {text:"• ", options:{color:BLUE, bold:true, fontSize:9}},
      {text:uc,         options:{color:SUB, fontSize:8.5}}
    ], {x:C2X+0.05, y:ry, w:C2W-0.05, h:0.34, valign:"top", margin:0});
    ry += 0.32;
  });

  ry += 0.08;

  if (opts.metrics && opts.metrics.length) {
    const n  = opts.metrics.length;
    const mw = (C2W - 0.05*(n-1)) / n;
    opts.metrics.forEach((m, i) => {
      metricBox(s, C2X + i*(mw+0.05), ry, mw, 0.65, m.val, m.lbl);
    });
    ry += 0.72;
  }

  if (opts.rCallout) {
    ry += 0.05;
    quoteBox(s, C2X, ry, C2W, opts.rCallout.h || 0.55, opts.rCallout.text, opts.rCallout.attr || null);
    ry += (opts.rCallout.h || 0.55) + 0.08;
  }

  posTag(s, C2X, 4.85, C2W, opts.posTag || "");

  s.addNotes(opts.notes || "");
  return s;
}

// ── SLIDE 3 — NIPENDO ────────────────────────────────────────
companySlide({
  company: "Nipendo",
  url:     "Hyperautomation for P2P  |  nipendo.com",
  aiLabel: "AI + ML for Process Governance",
  quote:   "Enriched with Artificial Intelligence and Machine Learning capabilities, enabling complete automated process governance, compliance management, and discrepancy resolution.",
  quoteH:  0.72,
  products:[
    {name:"Nexa",                  desc:"Fastest way to automate P2P — go live in days, 100s of suppliers connected in a week"},
    {name:"Hyperautomation Engine",desc:"ERP-agnostic, multi-modal: B2B EDI, email, web portal, mobile app"},
    {name:"Discrepancy Resolution",desc:"Identifies errors instantly and requires correction before ERP posting"},
  ],
  keyStat: {val:"95%", lbl:"Supplier Adoption Rate achieved with Nipendo deployments"},
  useCases:[
    "Automated supplier onboarding & PO processing",
    "AI-driven discrepancy identification & resolution",
    "Invoice compliance enforcement before ERP posting",
    "Proactive guidance: step-by-step automated interaction",
  ],
  metrics: [
    {val:"95%", lbl:"Supplier Adoption"},
    {val:"90%+",lbl:"Auto-Processed Invoices"},
    {val:"Days",lbl:"Go-Live Time"},
  ],
  rCallout:{text:"Turn P2P workflows into a controlled, automated and frictionless lifecycle — go live in days, automate from day one.", h:0.48},
  posTag:  "Practical Automation  ·  Outcome-Driven  ·  ERP-Agnostic",
  notes:   "Nipendo positions itself as the hyperautomation platform for the P2P core — with a strong emphasis on measurable outcomes and speed of deployment. AI is framed as a governance and discrepancy resolution layer, not a buzzword. Key takeaway: the emphasis on 'go live in days' and 95% supplier adoption are very strong hooks for the CFO/Procurement audience."
});

// ── SLIDE 4 — TRADESHIFT ─────────────────────────────────────
companySlide({
  company: "Tradeshift",
  url:     "AI-Powered AP Automation & Business Network  |  tradeshift.com",
  aiLabel: "ML + LLMs for Document Intelligence",
  quote:   "We’ve completely rearchitected how Tradeshift processes incoming invoice documents. At the core is a powerful new extraction engine combining advanced OCR (AWS Textract) with Large Language Models (LLMs).",
  quoteH:  0.8,
  products:[
    {name:"CloudScan",         desc:"ML-based PDF-to-structured-invoice conversion (original AI product)"},
    {name:"ADA Automation Dashboard", desc:"Visual threshold mgmt for assisted vs. automated coding decisions"},
    {name:"AI Intelligent Extraction (Spring ’26)", desc:"AWS Textract + LLMs, zero-template processing"},
    {name:"Anomaly Detection Dashboard", desc:"Surfaces fraud, duplicates, and process breakdowns automatically"},
  ],
  useCases:[
    "Zero-template invoice processing — AI adapts to any supplier format globally",
    "ML identity verification for onboarding on 1M+ business network",
    "Assisted → automated coding with human-in-the-loop threshold control",
    "Fraud & duplicate payment detection surfaced before they clear",
  ],
  metrics: [
    {val:"1M+", lbl:"Businesses on Network"},
    {val:"0",   lbl:"Templates Required"},
  ],
  rCallout:{text:"The quality filter for our data is our network. Buyers and suppliers collaborating and validating data in real-time — what you end up with is structured data of super high quality.", h:0.58},
  posTag:  "Technical Depth  ·  Network Data Quality  ·  Practical Transparency",
  notes:   "Tradeshift speaks in 'engineer language' — AWS Textract, LLMs, ML models for zero-template processing. But they also connect this to a network narrative (1M+ businesses). The 'garbage in, garbage out' phrase they use resonates strongly with AP professionals who know the data quality problem. For StoreNext: emphasizing EDI + ERP network quality could serve as a similar positioning line."
});

// ── SLIDE 5 — BASWARE ────────────────────────────────────────
companySlide({
  company: "Basware",
  url:     "InvoiceAI — Purpose-Built for the Entire Invoice Lifecycle  |  basware.com",
  aiLabel: "InvoiceAI — Generative AI + AI Agents + Deep Learning",
  quote:   "At Basware, AI is not a buzzword, or a bonus feature. It’s not a nice-to-have. It’s integral to our business — and yours. Put simply, InvoiceAI is built to deliver ROI.",
  quoteH:  0.7,
  products:[
    {name:"InvoiceAI",        desc:"End-to-end AI across the entire invoice lifecycle (ingestion to reconciliation)"},
    {name:"SmartPDF",         desc:"ML-based PDF extraction: 97%+ accuracy, zero setup, zero template maintenance"},
    {name:"SmartCoding",      desc:"Auto-coding for non-PO invoices; self-learns from every exception handled"},
    {name:"Advanced Matching",desc:"Multi-document AI matching: invoice + PO + GR + contracts at header & line level"},
  ],
  keyStat: {val:"2.3B", lbl:"invoices trained on — $10 trillion in spend across 40 years of AP expertise"},
  useCases:[
    "Touchless invoice processing (PO and non-PO paths)",
    "Predictive identification of invoices at risk of late payment",
    "Automated coding that self-learns from each exception",
    "Generative AI agents answer AP queries instantly",
  ],
  metrics: [
    {val:"97%+",   lbl:"SmartPDF Accuracy"},
    {val:"2.3B",   lbl:"Invoices Trained"},
    {val:"Leader", lbl:"Gartner MQ 2024"},
  ],
  posTag:  "Expert Authority  ·  AI-to-ROI  ·  Data-at-Scale",
  notes:   "Basware is the most mature player in the AI/AP space. The 2.3 billion invoice story is a massive positioning weapon — impossible to replicate. The 'AI to ROI' framing is very strong because it connects technology to CFO language. For StoreNext: if you have unique network data (e.g., transaction volumes from the Israeli market), that is the positioning asset to highlight."
});

// ── SLIDE 6 — COUPA ──────────────────────────────────────────
companySlide({
  company: "Coupa",
  url:     "Navi™ Agentic AI for Total Spend Management  |  coupa.com",
  aiLabel: "Coupa Navi™ — Multiagent Agentic AI",
  quote:   "We’re moving beyond simple automation to tackle the complexity of sourcing and supplier management with a new class of autonomous AI agents. This release is a true game-changer.",
  quoteH:  0.65,
  products:[
    {name:"Navi™ Supplier Assistance Agent", desc:"24/7 autonomous responses to supplier questions — 50% faster resolution"},
    {name:"Navi™ Supplier Discovery Agent",  desc:"Natural language queries to find best-fit suppliers — 100% faster sourcing"},
    {name:"Navi™ Cost Formula Agent",        desc:"Plain language → accurate cost formulas — 75% faster, fewer errors"},
    {name:"Navi™ Request Creation Agent",    desc:"Full SOW and file support — 50% reduction in manual entry time"},
  ],
  keyStat: {val:"$8T", lbl:"community-generated spend dataset  ·  10M+ buyers & suppliers on network"},
  useCases:[
    "Autonomous sourcing cycle acceleration (30% faster savings realization)",
    "Supplier portal: Navi resolves common questions 24/7 autonomously",
    "Category strategy → sourcing event execution in a single platform",
    "AI-Driven Payment Security Alerts for fraud anomaly detection",
  ],
  metrics: [
    {val:"50%", lbl:"Efficiency Gains (AP)"},
    {val:"75%", lbl:"Faster Formulas"},
    {val:"10M+",lbl:"Buyers & Suppliers"},
  ],
  rCallout:{text:"Make Margins Multiply™ — From static applications to AI-guided networks that act independently: autonomous spend management.", h:0.46},
  posTag:  "Agentic Vision  ·  Network Scale  ·  ROI Outcomes",
  notes:   "Coupa is investing heavily in AI branding — everything is 'Navi'. Their narrative is 'autonomous spend management' — a network of agents acting without human intervention. Visually powerful, but sometimes feels like a vision still far from reality. For StoreNext: agent language works well, but anchor it in concrete use cases — like 'Navi Supplier Assistance Agent resolves queries 50% faster'."
});

// ── SLIDE 7 — NILUS ──────────────────────────────────────────
companySlide({
  company: "Nilus",
  url:     "Agentic AI for Treasury & Cash Management  |  nilus.com",
  aiLabel: "Analyst Agent + Liquidity Agent — Agentic Treasury AI",
  quote:   "Legacy treasury tools are passive vaults; the Nilus Analyst Agent is an active collaborator. It automates the ‘build’ phase of reporting — aggregating data, detecting anomalies, and drafting explanations — so you can focus purely on strategy.",
  quoteH:  0.82,
  products:[
    {name:"Analyst Agent",              desc:"Auto-aggregates data, drafts CFO-ready analysis & anomaly summaries"},
    {name:"Liquidity Agent",            desc:"Monitors cash positions vs. policies, recommends rebalancing actions"},
    {name:"Transaction Categorization", desc:"AI auto-tags bank statements & ERP transactions for cash flow reporting"},
    {name:"AI Collection Predictions",  desc:"Learns customer payment behavior to predict when collections arrive"},
  ],
  useCases:[
    "Cash flow forecasting with automated variance analysis",
    "3-way O2C reconciliation: payment processor + bank + ERP",
    "Liquidity policy monitoring & proactive breach prevention",
    "Idle cash discovery and smart rebalancing recommendations",
  ],
  metrics: [
    {val:"40%",  lbl:"Operational Cost Reduction"},
    {val:"95%",  lbl:"Forecast Accuracy"},
    {val:"$4M",  lbl:"Idle Cash Discovered"},
    {val:"85%",  lbl:"Less Manual Work"},
  ],
  posTag:  "Agentic Treasury  ·  Outcome-Specific  ·  Finance-Native",
  notes:   "Nilus is an Israeli startup (!) focused on treasury and cash management. They are very specific — concrete numbers, clear use cases, CFO language. The Liquidity Agent and Analyst Agent are excellent examples of how to name AI capabilities. For StoreNext: Nilus shows that a small Israeli company can build a strong AI brand — the key is specificity and outcome metrics."
});

// ── SLIDE 8 — KYRIBA ─────────────────────────────────────────
companySlide({
  company: "Kyriba",
  url:     "TAI — Trusted Agentic AI for Treasury & Liquidity  |  kyriba.com",
  aiLabel: "TAI (Trusted AI) — Agentic AI with Trust Architecture",
  quote:   "Unlike others, we build our agentic AI on a foundation of trust — because successful AI adoption depends on it.",
  quoteH:  0.52,
  products:[
    {name:"TAI — Trusted AI", desc:"Daily treasury reporting, variance analysis, and strategic planning via AI"},
    {name:"Trusted Insights",      desc:"Absolute clarity: bank statement status, urgent payments, cash positions"},
    {name:"Trusted Data",          desc:"No customer data ever used in training public models — fully isolated"},
    {name:"Self-Service Agent Builder", desc:"Customers customize TAI to their own terminology & workflows"},
  ],
  keyStat: {val:"9,900+", lbl:"banks connected out-of-the-box  ·  unified treasury data in one platform"},
  useCases:[
    "Overnight bank statement processing & urgent payment alerts",
    "Variance analysis with executive summaries ready for the CFO",
    "Board-ready treasury health checks compiled in minutes, not days",
    "Real-time suspicious payment stops — fraud avoidance at enterprise scale",
  ],
  metrics: [
    {val:"88%", lbl:"Idle Cash Reduction"},
    {val:">$1M",lbl:"Fraud Avoidance"},
    {val:"85%", lbl:"Risk Eliminated"},
  ],
  rCallout:{text:"The reason we chose Kyriba is because Kyriba keeps our data secure within its app environment — all of this is very confidential data. — Hemant Godhwani, Mews", h:0.58},
  posTag:  "Trust-First AI  ·  CFO Security  ·  Enterprise Compliance",
  notes:   "Kyriba is the most sophisticated in their AI + Trust narrative. They have addressed the biggest fear CFOs have about AI: 'what happens with my sensitive data?'. The TAI Trust Framework is a very smart positioning approach. For StoreNext: highly relevant to the Israeli B2B market where data security is a real adoption barrier."
});

// ── SLIDE 9 — FINSITE ────────────────────────────────────────
companySlide({
  company: "Finsite",
  url:     "AI-Powered Bank-to-ERP Financial Automation  |  finsite.co.il",
  aiLabel: "AI Automation for ERP Reconciliation (no branded AI name)",
  quote:   "FinSite connects banks to ERP systems with AI and smart automation — turning finance departments into stronger, faster units. The AI identifies matching accounts, creates journal entries, and reconciles transactions automatically every day.",
  quoteH:  0.72,
  products:[
    {name:"Bank Import Engine",     desc:"Automatic daily pull from all Israeli banks & credit companies into any ERP — all currencies"},
    {name:"Auto Bank Reconciliation",desc:"AI creates journal entries per transaction, links to ERP accounts/cards — fully automated"},
    {name:"Smart Receipt Agent",    desc:"Identifies payee name from incoming transfer, matches customer card, closes invoice, generates receipt"},
    {name:"Cash Flow Forecasting",  desc:"Real-time forecasts with recurring pattern recognition and future projection"},
  ],
  useCases:[
    "Automatic daily bank statement import across all Israeli banks",
    "AI-powered journal entry creation & account matching",
    "Anomaly detection: duplicates, compliance issues, suspicious transactions",
    "Cash flow forecasting with multi-company financial dashboard",
  ],
  metrics: [
    {val:"9+",   lbl:"ERP Systems Supported"},
    {val:"ISA",  lbl:"Licensed by Israeli Securities Authority"},
    {val:"100%", lbl:"Daily Bank Automation"},
  ],
  rCallout:{
    text:"No branded AI product or trust narrative identified. Finsite competes on ERP integration depth and Israeli market coverage — not on a named AI layer. This is a positioning gap StoreNext can exploit.",
    h:0.65
  },
  posTag:  "Israeli Market  ·  Bank-ERP Integration  ·  No AI Branding",
  notes:   "Finsite is an Israeli fintech connecting banks to ERP systems with AI automation. Their AI is functional rather than branded — no product name, no trust narrative, no outcome metrics on display. They serve accounting firms and finance departments with reconciliation and cash flow tools. For StoreNext: Finsite demonstrates the gap between 'AI automation' as a feature claim vs. a named, ownable AI product. StoreNext has the opportunity to leapfrog this with a branded intelligence layer."
});

// ── SLIDE 10 — COMPARISON TABLE ──────────────────────────────
{
  const s = pres.addSlide();
  s.background = {color:WHITE};
  header(s, "AI Positioning Benchmark — Side-by-Side Comparison", "How the 7 Platforms Stack Up Across Key AI Dimensions");
  footer(s);

  const colW = [1.22, 1.88, 2.72, 1.78, 1.9];
  const mk = (txt, opts) => ({text:txt, options:opts});

  const hdr = colW.map((_, i) => mk(
    ["Company","AI Brand Name","Primary AI Use Cases","Positioning Tone","Specificity Level"][i],
    {fill:{color:NAVY}, color:WHITE, bold:true, fontSize:8.5, align:"left"}
  ));

  const rows = [
    ["Nipendo",   "AI + ML (no branded name)",          "Discrepancy resolution, compliance governance, invoice automation, onboarding",       "Practical Outcomes",            "Medium — results cited, limited feature detail"],
    ["Tradeshift","CloudScan / ADA / LLM Extraction",   "Invoice extraction (LLMs+OCR), anomaly detection, coding automation, identity",       "Technical + Transparent",       "High — named features, Spring ’26 release notes"],
    ["Basware",   "InvoiceAI (SmartPDF, SmartCoding)",  "Touchless AP, non-PO coding, predictive late payment, AI agents for queries",         "Expert Authority",              "Very High — 2.3B dataset, named AI modules, analyst validation"],
    ["Coupa",     "Coupa Navi™ (Multiagent)",      "Supplier assistance, discovery, sourcing optimization, payment fraud, category",       "Agentic Vision",                "High — named agents with % efficiency claims"],
    ["Nilus",     "Analyst Agent / Liquidity Agent",    "Cash forecasting, O2C reconciliation, liquidity monitoring, collection predictions",   "Agentic + Outcome Metrics",     "Very High — specific $ and % figures per use case"],
    ["Kyriba",    "TAI (Trusted AI)",                   "Treasury reporting, variance analysis, cash planning, fraud/risk monitoring",          "Trust-First + CFO Authority",   "High — trust architecture detailed, named pillars"],
    ["Finsite",   "AI Automation (no branded name)",    "Bank reconciliation, journal entry automation, cash flow forecasting, anomaly alerts", "Israeli Market / ERP-Focused",  "Low — automation claims, no named AI product or outcome metrics"],
  ];

  const tableData = [hdr, ...rows.map((row, ri) => row.map((cell, ci) => mk(cell, {
    fill:{color: ri%2===0 ? "F8FAFC" : WHITE},
    color:DGRAY, fontSize:8, align:"left", bold:ci===0
  })))];

  s.addTable(tableData, {
    x:0.25, y:CONT_Y+0.05, w:9.5, colW, border:{pt:0.5, color:"E5E7EB"}, rowH:0.44
  });

  navyBox(s, 0.25, 4.84, 9.5, 0.41,
    "Pattern: The most compelling AI positioning in 2026 combines a branded AI name + specific efficiency metrics + a trust/data narrative. Basware, Nilus, and Kyriba do all three.",
    8.5);

  s.addNotes("This slide is the heart of the analysis. Three key patterns: (1) The strongest AI players are Basware, Nilus, Kyriba — with a name, metrics, and a trust narrative; (2) Coupa is strong on vision but weaker on proof points; (3) Nipendo and Finsite have the weakest AI positioning — functional automation without a branded story.");
}

// ── SLIDE 11 — AI NAMING PATTERNS ────────────────────────────
{
  const s = pres.addSlide();
  s.background = {color:WHITE};
  header(s, "How Competitors Name Their AI", "From Generic 'AI' Claims to Branded Intelligence Layers");
  footer(s);

  let y = CONT_Y;

  s.addShape(pres.shapes.RECTANGLE, {x:0.28, y, w:9.44, h:0.28, fill:{color:"0A4D2E"}, line:{color:"0A4D2E"}});
  s.addText("TIER 1 — Branded AI Product  (Strongest Positioning)", {
    x:0.38, y, w:9.2, h:0.28, fontSize:9, color:WHITE, bold:true, valign:"middle", margin:0
  });
  y += 0.32;

  const t1 = [
    {co:"Basware",  ai:"InvoiceAI",              sub:"SmartPDF, SmartCoding, AI Agents, Generative AI"},
    {co:"Coupa",    ai:"Navi™",              sub:"Multiagent suite: Supplier, Discovery, Cost, Knowledge"},
    {co:"Kyriba",   ai:"TAI — Trusted AI",   sub:"Trusted Insights, Trusted Connectivity, Trusted Data"},
    {co:"Nilus",    ai:"Analyst + Liquidity Agent",sub:"Named agentic agents for treasury & cash management"},
  ];
  const cw = 2.27;
  t1.forEach((item, i) => {
    const cx = 0.28 + i*(cw+0.05);
    s.addShape(pres.shapes.RECTANGLE, {x:cx, y, w:cw, h:0.78, fill:{color:"F0FDF4"}, line:{color:TEAL}});
    s.addText([
      {text:item.co, options:{bold:true, fontSize:11, color:NAVY, breakLine:true}},
      {text:item.ai+"\n", options:{bold:true, fontSize:9, color:TEAL, breakLine:true}},
      {text:item.sub, options:{fontSize:7.5, color:MGRAY}},
    ], {x:cx+0.08, y:y+0.05, w:cw-0.16, h:0.72, valign:"top", margin:0});
  });
  y += 0.9;

  s.addShape(pres.shapes.RECTANGLE, {x:0.28, y, w:9.44, h:0.27, fill:{color:"1E3A5F"}, line:{color:"1E3A5F"}});
  s.addText("TIER 2 — Named Feature / Dashboard", {
    x:0.38, y, w:9.2, h:0.27, fontSize:9, color:WHITE, bold:true, valign:"middle", margin:0
  });
  y += 0.31;
  s.addShape(pres.shapes.RECTANGLE, {x:0.28, y, w:9.44, h:0.55, fill:{color:BLUE_LITE}, line:{color:BLUE_BDR}});
  s.addText([
    {text:"Tradeshift: ", options:{bold:true, fontSize:9, color:NAVY}},
    {text:"CloudScan, ADA Automation Dashboard, AI Document Intelligent Extraction Engine (Spring 2026), Anomaly Detection Dashboard", options:{fontSize:9, color:SUB}},
  ], {x:0.42, y, w:9.1, h:0.55, valign:"middle", margin:0});
  y += 0.63;

  s.addShape(pres.shapes.RECTANGLE, {x:0.28, y, w:9.44, h:0.27, fill:{color:DGRAY}, line:{color:DGRAY}});
  s.addText("TIER 3 — Generic AI/ML Claims  (Weakest Positioning)", {
    x:0.38, y, w:9.2, h:0.27, fontSize:9, color:FTRTXT, bold:true, valign:"middle", margin:0
  });
  y += 0.31;
  s.addShape(pres.shapes.RECTANGLE, {x:0.28, y, w:9.44, h:0.52, fill:{color:LGRAY}, line:{color:"D1D5DB"}});
  s.addText([
    {text:"Nipendo: ", options:{bold:true, fontSize:9, color:DGRAY}},
    {text:"“enriched with AI and ML capabilities” — no product name, no trust narrative, no specific metrics  |  ", options:{fontSize:8.5, color:SUB}},
    {text:"Finsite: ", options:{bold:true, fontSize:9, color:DGRAY}},
    {text:"'AI automation' and 'AI tools' — no branded AI product or outcome metrics identified", options:{fontSize:8.5, color:MGRAY}},
  ], {x:0.42, y, w:9.1, h:0.52, valign:"middle", margin:0});
  y += 0.60;

  navyBox(s, 0.28, y, 9.44, 0.46,
    "In 2026, enterprise buyers are skeptical of generic 'AI-powered' claims. A named, branded AI product with a clear trust or data story signals maturity — and wins procurement evaluations.",
    9);

  s.addNotes("Key slide for the positioning team. The message: writing 'AI-powered' is not enough. You need a name, a story, and proof with numbers. Basware's InvoiceAI and Kyriba's TAI are excellent models to follow in the enterprise category.");
}

// ── SLIDE 12 — USE CASE COVERAGE MAP ─────────────────────────
{
  const s = pres.addSlide();
  s.background = {color:WHITE};
  header(s, "Which AI Use Cases Does Each Platform Own?", "Coverage Across the Finance & Procurement Stack");
  footer(s);

  s.addText([
    {text:"✔ Covered   ", options:{color:GREEN_D, bold:true, fontSize:8.5}},
    {text:"~ Partial   ",      options:{color:AMBER,   bold:true, fontSize:8.5}},
    {text:"— Not Covered", options:{color:"9CA3AF",bold:true, fontSize:8.5}},
  ], {x:6.9, y:CONT_Y+0.04, w:2.9, h:0.3, valign:"middle", margin:0});

  const ucs = [
    "Invoice Extraction & Coding",
    "Supplier Onboarding Automation",
    "Dispute / Discrepancy Resolution",
    "Cash Flow Forecasting",
    "O2C / Bank Reconciliation",
    "Fraud & Anomaly Detection",
    "Supplier Discovery & Matching",
    "Treasury Variance Analysis",
    "Cross-Border Payments",
    "Compliance & Governance",
  ];
  const cov = [
    //  Nip   Trd   Bas   Cpa   Nil   Kyr   Fin
    ["—","✔","✔","✔","—","—","~"],
    ["✔","✔","~",    "✔","—","—","—"],
    ["✔","~",    "✔","~",    "—","—","~"],
    ["—","—","~",    "—","✔","✔","✔"],
    ["~",    "~",    "✔","~",    "✔","—","✔"],
    ["—","✔","~",    "✔","—","✔","✔"],
    ["—","~",    "—","✔","—","—","—"],
    ["—","—","—","—","✔","✔","~"],
    ["—","—","—","—","—","—","—"],
    ["✔","✔","✔","✔","—","~",    "✔"],
  ];
  const companies = ["Nipendo","Tradeshift","Basware","Coupa","Nilus","Kyriba","Finsite"];
  const UCW = 2.12, CW = 1.05;

  const hdrRow = [
    {text:"AI Use Case", options:{fill:{color:NAVY}, color:WHITE, bold:true, fontSize:8, align:"left"}},
    ...companies.map(c => ({text:c, options:{fill:{color:NAVY}, color:WHITE, bold:true, fontSize:7.5, align:"center"}}))
  ];
  const bodyRows = ucs.map((uc, ri) => [
    {text:uc, options:{fill:{color:ri%2===0?"F8FAFC":WHITE}, color:DGRAY, fontSize:8, align:"left", bold:false}},
    ...cov[ri].map(v => ({
      text:v,
      options:{
        fill:{color:ri%2===0?"F8FAFC":WHITE},
        color: v==="✔" ? GREEN_D : v==="~" ? AMBER : "D1D5DB",
        fontSize:10, align:"center", bold:v==="✔"
      }
    }))
  ]);

  s.addTable([hdrRow, ...bodyRows], {
    x:0.25, y:CONT_Y+0.38, w:9.5,
    colW:[UCW, ...companies.map(()=>CW)],
    border:{pt:0.5, color:"E5E7EB"}, rowH:0.32
  });

  tealBox(s, 0.25, 5.02, 9.5, 0.28,
    "StoreNext sits at the intersection of supplier collaboration, ERP integration, and B2B payments — a unique combination none of the above players covers end-to-end.",
    8.5);

  s.addNotes("The use case map shows that every player has chosen a niche: Basware = AP; Nilus = Treasury; Coupa = broad S2P; Kyriba = Liquidity; Finsite = Israeli bank-ERP reconciliation. StoreNext can claim 'we connect all the dots' — supplier collaboration + ERP integration + payments + compliance — all in one B2B network.");
}

// ── SLIDE 13 — KEY TAKEAWAYS ─────────────────────────────────
{
  const s = pres.addSlide();
  s.background = {color:WHITE};
  header(s, "Key Takeaways for StoreNext", "What We Learned — and How to Position Differently");
  divider(s);
  footer(s);

  let ly = CONT_Y;
  s.addShape(pres.shapes.RECTANGLE, {x:C1X, y:ly, w:C1W, h:0.27, fill:{color:GREEN_D}, line:{color:GREEN_D}});
  s.addText("What the Market Is Doing Right", {
    x:C1X+0.1, y:ly, w:C1W-0.1, h:0.27, fontSize:9, color:WHITE, bold:true, valign:"middle", margin:0
  });
  ly += 0.31;

  const wins = [
    "Named AI products win: InvoiceAI, Navi™, TAI — brands signal maturity and intent",
    "Specific metrics matter: \"50% faster,\" \"97% accuracy\" — vague claims don’t convert",
    "Trust narrative is table stakes: data privacy + human-in-the-loop + auditability",
    "ROI language bridges tech and business: \"AI to ROI\" resonates with CFOs",
    "Agentic framing is the 2026 buzzword — compelling only with concrete use cases",
  ];
  wins.forEach(w => {
    s.addText([
      {text:"✔ ", options:{color:TEAL, bold:true, fontSize:9}},
      {text:w,         options:{color:SUB, fontSize:8.5}},
    ], {x:C1X, y:ly, w:C1W, h:0.32, valign:"middle", margin:[0,0,0,0.05]});
    ly += 0.30;
  });

  let ry = CONT_Y;
  s.addShape(pres.shapes.RECTANGLE, {x:C2X, y:ry, w:C2W, h:0.27, fill:{color:AMBER}, line:{color:AMBER}});
  s.addText("Where the Market Has Gaps", {
    x:C2X+0.1, y:ry, w:C2W-0.1, h:0.27, fontSize:9, color:WHITE, bold:true, valign:"middle", margin:0
  });
  ry += 0.31;

  const gaps = [
    "Supplier-side AI: every platform talks to the buyer — nobody positions AI as value-add for the supplier",
    "B2B data network moat: nobody owns \"richer network = smarter AI\" explicitly",
    "ERP + EDI + AI: no one positions AI as the layer that makes ERP data more accurate (not just faster)",
    "Regional market: no competitor addresses Israeli enterprise compliance & ERP ecosystem",
  ];
  gaps.forEach(g => {
    s.addText([
      {text:"▶ ", options:{color:AMBER, bold:true, fontSize:9}},
      {text:g,         options:{color:SUB, fontSize:8.5}},
    ], {x:C2X, y:ry, w:C2W, h:0.37, valign:"top", margin:[0,0,0,0.05]});
    ry += 0.34;
  });

  navyBox(s, C1X, 3.27, 9.44, 0.38,
    "Be the AI platform that works for both sides of the invoice — not just the buyer.",
    12);

  const pillars = [
    {n:"1", title:"Network Intelligence",    desc:"Our AI gets smarter from every supplier interaction — giving insights no standalone tool can match"},
    {n:"2", title:"Supplier Empowerment AI", desc:"The only platform that uses AI to reduce friction for your suppliers — not just your AP team"},
    {n:"3", title:"ERP-Native Intelligence", desc:"AI that lives inside your ERP workflow — for compliance, matching, and cash optimization in one motion"},
  ];
  pillars.forEach((p, i) => {
    const px = C1X + i*3.18;
    s.addShape(pres.shapes.RECTANGLE, {x:px, y:3.70, w:3.06, h:1.5, fill:{color:BLUE_LITE}, line:{color:BLUE_BDR}});
    s.addShape(pres.shapes.OVAL,      {x:px+0.12, y:3.77, w:0.31, h:0.31, fill:{color:BLUE}, line:{color:BLUE}});
    s.addText(p.n, {x:px+0.12, y:3.77, w:0.31, h:0.31, fontSize:11, color:WHITE, bold:true, align:"center", valign:"middle", margin:0});
    s.addText(p.title, {x:px+0.5, y:3.78, w:2.5, h:0.3, fontSize:9.5, color:NAVY, bold:true, valign:"middle", margin:0});
    s.addText(p.desc,  {x:px+0.12, y:4.11, w:2.86, h:1.0, fontSize:8.5, color:SUB, valign:"top", margin:0});
  });

  s.addNotes("Strategic summary. Three things to remember: (1) Name your AI; (2) Prove it with concrete numbers; (3) Nobody is talking to the supplier side — that is StoreNext's differentiating narrative.");
}

// ── SLIDE 14 — NEXT STEPS ────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = {color:NAVY};

  s.addShape(pres.shapes.RECTANGLE, {x:0, y:0, w:10, h:0.75, fill:{color:NAVY_DARK}, line:{color:NAVY_DARK}});
  s.addShape(pres.shapes.RECTANGLE, {x:0, y:0, w:0.09, h:0.75, fill:{color:TEAL}, line:{color:TEAL}});
  s.addText("Recommended Next Steps for StoreNext AI Positioning", {
    x:0.24, y:0, w:9.4, h:0.48, fontSize:18, fontFace:"Calibri", color:WHITE, bold:true, valign:"bottom", margin:0
  });
  s.addText("From Analysis to Action", {
    x:0.24, y:0.48, w:9.4, h:0.27, fontSize:9.5, color:FTRTXT, valign:"top", margin:0
  });

  const actions = [
    {priority:"IMMEDIATE", pcolor:RED,   title:"Name the AI",
     action:"Develop a branded AI product name and tagline for StoreNext’s intelligence layer",
     why:"Every top competitor has a named AI. Generic claims lose enterprise evaluations."},
    {priority:"IMMEDIATE", pcolor:RED,   title:"Quantify the Outcomes",
     action:"Collect 5–10 customer metrics (% automation rate, time saved, error reduction) to anchor all AI claims",
     why:"Specific numbers are the #1 differentiator between compelling AI positioning and generic noise."},
    {priority:"NEAR-TERM", pcolor:AMBER, title:"Build the Trust Story",
     action:"Develop a data privacy + human-in-the-loop narrative tailored to Israeli enterprise buyers",
     why:"Kyriba TAI shows data trust is a buying criterion, not a nice-to-have."},
    {priority:"STRATEGIC", pcolor:TEAL,  title:"Own the Supplier AI Angle",
     action:"Create positioning that speaks to suppliers — not just AP teams — as direct AI beneficiaries",
     why:"No competitor owns this space. Clear blue ocean in B2B supplier portal AI."},
  ];
  const pos = [{x:0.3,y:0.88},{x:5.15,y:0.88},{x:0.3,y:2.82},{x:5.15,y:2.82}];
  const BW = 4.55, BH = 1.82;

  actions.forEach((a, i) => {
    const {x, y} = pos[i];
    s.addShape(pres.shapes.RECTANGLE, {x, y, w:BW, h:BH, fill:{color:NAVY_MID}, line:{color:"1E3A5F"}});
    s.addShape(pres.shapes.RECTANGLE, {x, y, w:BW, h:0.26, fill:{color:a.pcolor}, line:{color:a.pcolor}});
    s.addText(a.priority, {x:x+0.1, y, w:BW-0.2, h:0.26, fontSize:8, color:WHITE, bold:true, valign:"middle", margin:0});
    s.addText(a.title, {x:x+0.12, y:y+0.31, w:BW-0.24, h:0.3, fontSize:13, color:WHITE, bold:true, valign:"middle", margin:0});
    s.addText(a.action, {x:x+0.12, y:y+0.63, w:BW-0.24, h:0.62, fontSize:9, color:"BFD3F0", valign:"top", margin:0});
    const whyColor = a.pcolor===TEAL ? "6EE7B7" : a.pcolor===AMBER ? "FCD34D" : "FCA5A5";
    s.addText([
      {text:"Why: ", options:{bold:true, color:whyColor, fontSize:8.5}},
      {text:a.why,   options:{color:FTRTXT, fontSize:8.5}},
    ], {x:x+0.12, y:y+1.32, w:BW-0.24, h:0.44, valign:"top", margin:0});
  });

  s.addText("Source research: nipendo.com · tradeshift.com · basware.com · coupa.com · nilus.com · kyriba.com · finsite.co.il  |  April 2026", {
    x:0.3, y:FTR_Y, w:9.4, h:FTR_H, fontSize:7, color:"4B5563", valign:"middle", margin:0
  });

  s.addNotes("Action slide. These four steps can turn this analysis into a real positioning strategy. The first and most immediate step: name StoreNext's AI. That is the highest-leverage action relative to effort.");
}

// ── SLIDE 15 — NAME OPTIONS: CHOOSE YOUR DIRECTION ───────────
{
  const s = pres.addSlide();
  s.background = {color:WHITE};
  header(s, "What Should We Call It?", "5 name directions — choose the one that feels right for StoreNext’s AI layer");
  footer(s);

  // 5 name option cards
  const names = [
    {
      name: "IQ",
      full: "StoreNext IQ",
      desc: "The AI mastermind across every StoreNext product",
      bullets: [
        {good:true,  text:"Platform-wide name — works across all products"},
        {good:true,  text:"Expandable: Supplier IQ, Treasury IQ, EDI IQ..."},
        {good:true,  text:"Signals intelligence, not just a feature"},
      ],
      highlight: true,
    },
    {
      name: "Spark",
      full: "StoreNext Spark",
      desc: "The ignition point — turns data into action",
      bullets: [
        {good:true,  text:"Memorable and energetic brand name"},
        {good:false, text:"Slightly less enterprise in tone"},
        {good:true,  text:"Visual tie to existing StoreNext brand"},
      ],
      highlight: false,
    },
    {
      name: "Pulse",
      full: "StoreNext Pulse",
      desc: "Real-time signals — the heartbeat of your business",
      bullets: [
        {good:true,  text:"Strong for monitoring and alert use cases"},
        {good:false, text:"Narrower scope perception than IQ"},
        {good:true,  text:"Real-time data narrative resonates"},
      ],
      highlight: false,
    },
    {
      name: "Clarity",
      full: "StoreNext Clarity",
      desc: "Clear answers from complex data",
      bullets: [
        {good:true,  text:"Business-oriented, easy to explain"},
        {good:false, text:"Less distinctive in a crowded AI market"},
        {good:true,  text:"Non-technical stakeholders respond well"},
      ],
      highlight: false,
    },
    {
      name: "Signal",
      full: "StoreNext Signal",
      desc: "The right alert, at the right moment",
      bullets: [
        {good:true,  text:"Strong for anomaly and detection contexts"},
        {good:false, text:"Scope limited to detection, not full AI"},
        {good:true,  text:"Technical resonance with ops teams"},
      ],
      highlight: false,
    },
  ];

  const cardW = 1.74, cardGap = 0.115, cardStartX = 0.28;
  const cardH   = 2.88;
  // Vertically center cards in content area (CONT_Y to FTR_Y)
  const cardTop = CONT_Y + (FTR_Y - CONT_Y - cardH) / 2;  // ≈ 1.50

  names.forEach((n, i) => {
    const cx = cardStartX + i * (cardW + cardGap);

    // Card background
    const cardBg = n.highlight ? NAVY : "F8FAFC";
    const cardBdr = n.highlight ? NAVY : "E2E8F0";
    s.addShape(pres.shapes.RECTANGLE, {x:cx, y:cardTop, w:cardW, h:cardH, fill:{color:cardBg}, line:{color:cardBdr}});

    // Highlight top bar
    if (n.highlight) {
      s.addShape(pres.shapes.RECTANGLE, {x:cx, y:cardTop, w:cardW, h:0.10, fill:{color:TEAL}, line:{color:TEAL}});
    }

    // Big name
    const nameFg = n.highlight ? WHITE : NAVY;
    s.addText(n.name, {x:cx, y:cardTop+0.15, w:cardW, h:0.72, fontSize:36, color:nameFg, bold:true, align:"center", valign:"middle", margin:0});

    // Divider line
    s.addShape(pres.shapes.RECTANGLE, {x:cx+0.16, y:cardTop+0.96, w:cardW-0.32, h:0.02, fill:{color: n.highlight ? NAVY_MID : "E2E8F0"}, line:{color: n.highlight ? NAVY_MID : "E2E8F0"}});

    // Full name label
    const fullFg = n.highlight ? SUBHDR : MGRAY;
    s.addText(n.full, {x:cx+0.08, y:cardTop+1.04, w:cardW-0.16, h:0.26, fontSize:8, color:fullFg, align:"center", valign:"middle", margin:0});

    // Tagline
    const tagFg = n.highlight ? "BFDBFE" : SUB;
    s.addText(n.desc, {x:cx+0.1, y:cardTop+1.34, w:cardW-0.2, h:0.54, fontSize:8.5, color:tagFg, align:"center", valign:"top", margin:0, italic:true});

    // 3 pro/con bullets
    n.bullets.forEach((b, bi) => {
      const byStart = cardTop + 1.90 + bi * 0.24;
      const iconColor = b.good ? (n.highlight ? TEAL_BDR : TEAL) : (n.highlight ? "FCA5A5" : RED);
      const textColor = n.highlight ? "D1D5DB" : SUB;
      s.addText([
        {text: b.good ? "✔ " : "✕ ", options:{bold:true, fontSize:8, color:iconColor}},
        {text: b.text, options:{fontSize:7.5, color:textColor}},
      ], {x:cx+0.10, y:byStart, w:cardW-0.18, h:0.22, valign:"middle", margin:0});
    });

    // Vote button — pinned 0.08" below last bullet
    const btnY = cardTop + 2.62;
    if (n.highlight) {
      s.addShape(pres.shapes.RECTANGLE, {x:cx+0.14, y:btnY, w:cardW-0.28, h:0.22, fill:{color:TEAL}, line:{color:TEAL}});
      s.addText("★  RECOMMENDED", {x:cx+0.14, y:btnY, w:cardW-0.28, h:0.22, fontSize:7.5, color:WHITE, bold:true, align:"center", valign:"middle", margin:0});
    } else {
      s.addShape(pres.shapes.RECTANGLE, {x:cx+0.14, y:btnY, w:cardW-0.28, h:0.22, fill:{color:"F1F5F9"}, line:{color:"CBD5E1"}});
      s.addText("□  VOTE FOR THIS", {x:cx+0.14, y:btnY, w:cardW-0.28, h:0.22, fontSize:7.5, color:SLATE, align:"center", valign:"middle", margin:0});
    }
  });

  s.addNotes("Name selection slide. Five options for the AI layer brand. IQ is the recommended choice — broadest strategic scope, works across all products, signals intelligence at the business level. Use this slide in a workshop or leadership meeting to create alignment before investing in brand assets.");
}

// ── SLIDE 16 — THE IQ PRODUCT FAMILY ─────────────────────────
{
  const s = pres.addSlide();
  s.background = {color:NAVY};
  header(s, "THE IQ PRODUCT FAMILY", "One brand. Eight capabilities. Across every StoreNext product.");
  footer(s);

  const family = [
    {name:"Ask IQ",             desc:"The conversation interface — instant answers on any StoreNext product",                            use:"All products"},
    {name:"IQ Insights",        desc:"Proactive analysis surfaced without asking — patterns you didn't know to look for",                use:"Meteor · AP · Procurement"},
    {name:"IQ Alerts",          desc:"Real-time signals: exceptions, anomalies, payment flags, and SLA breaches",                       use:"Meteor · Supplier Portal"},
    {name:"IQ Recommendations", desc:"Next-best-action suggestions across workflows, from AP to treasury",                              use:"Meteor · EZI · EDI"},
    {name:"Supplier IQ",        desc:"AI for suppliers: portal status, invoices, disputes, onboarding, next steps",                     use:"Supplier Portal"},
    {name:"Treasury IQ",        desc:"Cash, liquidity, reconciliation intelligence — before problems become crises",                    use:"Meteor · Reconciliation"},
    {name:"EDI IQ",             desc:"AI that makes EDI data accurate, mapped, and actionable across ERPs",                             use:"EDI Gateway · ERP Connect"},
    {name:"Retail IQ",          desc:"Store-level and chain-level operational insights for buyers and retailers",                       use:"Retail Analytics"},
  ];

  // Grid geometry — sized to fill the full content area
  // Content area: CONT_Y=0.85 to FTR_Y=5.33 = 4.48"
  // Tagline bar at bottom, 2 rows of 4 cards
  const cols = 4, gapX = 0.09, gapY = 0.14;
  // gridX centered: total card width = 10 - 2*0.28 = 9.44"; 4 cards + 3 gaps
  const itemW = (9.44 - 3*gapX) / 4;  // ≈ 2.29"
  const gridX = 0.28;
  const gridY = CONT_Y + 0.12;
  // tagline bar at bottom
  const taglineH = 0.22, taglineY = FTR_Y - taglineH - 0.08;
  // height available for 2 rows: taglineY - gridY - bottom gap
  const rowsH = taglineY - 0.08 - gridY;  // available for cards
  const itemH = (rowsH - gapY) / 2;  // split between 2 rows

  family.forEach((item, i) => {
    const col = i % cols;
    const row = Math.floor(i / cols);
    const fx = gridX + col*(itemW+gapX);
    const fy = gridY + row*(itemH+gapY);

    s.addShape(pres.shapes.RECTANGLE, {x:fx, y:fy, w:itemW, h:itemH, fill:{color:"0D2240"}, line:{color:"1A3A6B"}});
    // Teal left accent bar
    s.addShape(pres.shapes.RECTANGLE, {x:fx, y:fy, w:0.07, h:itemH, fill:{color:TEAL}, line:{color:TEAL}});
    // Title + description
    s.addText([
      {text:item.name, options:{bold:true, fontSize:12, color:WHITE, breakLine:true}},
      {text:item.desc, options:{fontSize:8.5, color:SUBHDR}},
    ], {x:fx+0.16, y:fy+0.14, w:itemW-0.24, h:itemH-0.54, valign:"top", margin:0});
    // "Available in" tag at card bottom
    s.addShape(pres.shapes.RECTANGLE, {x:fx+0.07, y:fy+itemH-0.32, w:itemW-0.07, h:0.26, fill:{color:NAVY_MID}, line:{color:NAVY_MID}});
    s.addText(item.use, {x:fx+0.16, y:fy+itemH-0.32, w:itemW-0.24, h:0.26, fontSize:7, color:TEAL_BDR, valign:"middle", margin:0});
  });

  // Bottom tagline bar
  s.addShape(pres.shapes.RECTANGLE, {x:gridX, y:taglineY, w:9.44, h:taglineH, fill:{color:TEAL}, line:{color:TEAL}});
  s.addText("StoreNext IQ  ·  Intelligence across Meteor, Supplier Portal, EZI, Retail Analytics — and every product that follows.", {
    x:gridX+0.1, y:taglineY, w:9.24, h:taglineH, fontSize:8.5, color:NAVY, bold:true, align:"center", valign:"middle", margin:0
  });

  s.addNotes("The IQ Product Family slide. This is the go-to slide for presenting the AI brand architecture to leadership, partners, or enterprise buyers. Every capability maps to a named IQ product — making the AI layer feel like a deliberate platform, not a collection of features.");
}

// ── SLIDE 17 — LOGO DIRECTION OPTIONS ────────────────────────
{
  const s = pres.addSlide();
  s.background = {color:WHITE};
  header(s, "StoreNext IQ — Logo Direction Options", "Three visual interpretations of the IQ brand mark");
  footer(s);

  // Card geometry — all 3 equal width, evenly spaced
  const LOGO_CW = 3.00, LOGO_GAP = 0.22, LOGO_TOP = CONT_Y + 0.10, LOGO_H = 3.96;
  // 3×3.00 + 2×0.22 = 9.44; starts at 0.28 → ends at 9.72 → right margin 0.28"

  // ── CONCEPT 1: Hexagon + IQ + Magnifying Glass Q + Red Sparkle ──
  // This is the concept the user showed: hexagon frame, IQ where Q = magnifying glass lens, red 4-pointed star inside lens
  {
    const cx = 0.28, cy = LOGO_TOP, cw = LOGO_CW, ch = LOGO_H;
    s.addShape(pres.shapes.RECTANGLE, {x:cx, y:cy, w:cw, h:ch, fill:{color:"F8FAFC"}, line:{color:"E2E8F0"}});

    // Mockup area background
    s.addShape(pres.shapes.RECTANGLE, {x:cx+0.16, y:cy+0.16, w:cw-0.32, h:1.66, fill:{color:NAVY}, line:{color:NAVY}});

    // Hexagon approximation: overlapping shapes to suggest hexagon outline
    // Use a large oval with NAVY stroke as base, then layered rectangles to flatten sides
    s.addShape(pres.shapes.OVAL, {x:cx+0.62, y:cy+0.20, w:1.74, h:1.56, fill:{type:"none"}, line:{color:TEAL, width:3}});
    // Flatten top/bottom of oval with NAVY rects to suggest hex
    s.addShape(pres.shapes.RECTANGLE, {x:cx+0.62, y:cy+0.20, w:1.74, h:0.18, fill:{color:NAVY}, line:{color:NAVY}});
    s.addShape(pres.shapes.RECTANGLE, {x:cx+0.62, y:cy+1.58, w:1.74, h:0.18, fill:{color:NAVY}, line:{color:NAVY}});

    // "I" letter
    s.addText("I", {x:cx+0.70, y:cy+0.22, w:0.55, h:1.40, fontSize:52, color:WHITE, bold:true, align:"center", valign:"middle", margin:0});

    // "Q" as magnifying glass: circle body
    s.addShape(pres.shapes.OVAL, {x:cx+1.26, y:cy+0.32, w:0.88, h:0.88, fill:{type:"none"}, line:{color:WHITE, width:4}});
    // Handle of magnifying glass (diagonal line going bottom-right)
    s.addShape(pres.shapes.LINE, {x:cx+1.96, y:cy+1.00, w:0.28, h:0.28, line:{color:WHITE, width:4}});

    // Red 4-pointed sparkle star inside the Q lens
    s.addText("✦", {x:cx+1.22, y:cy+0.34, w:0.96, h:0.82, fontSize:22, color:RED, align:"center", valign:"middle", bold:true, margin:0});

    // Label bar
    s.addShape(pres.shapes.RECTANGLE, {x:cx+0.16, y:cy+1.82, w:cw-0.32, h:0.26, fill:{color:TEAL}, line:{color:TEAL}});
    s.addText("DIRECTION A  —  Hexagon + IQ Magnifying Glass", {x:cx+0.16, y:cy+1.82, w:cw-0.32, h:0.26, fontSize:7.5, color:WHITE, bold:true, valign:"middle", margin:0});

    s.addText("The Q doubles as a magnifying glass lens — simultaneously reading as the letter Q, a search metaphor, and an AI intelligence signal. The red sparkle inside the lens is the insight moment. The hexagon frame positions IQ as a platform-level construct, not a single-product feature.", {
      x:cx+0.16, y:cy+2.14, w:cw-0.32, h:1.50, fontSize:8, color:SUB, valign:"top", margin:0
    });

    // Recommended badge
    s.addShape(pres.shapes.RECTANGLE, {x:cx+0.16, y:cy+ch-0.30, w:cw-0.32, h:0.22, fill:{color:TEAL}, line:{color:TEAL}});
    s.addText("★  RECOMMENDED — Strongest brand differentiation", {x:cx+0.16, y:cy+ch-0.30, w:cw-0.32, h:0.22, fontSize:7, color:WHITE, bold:true, align:"center", valign:"middle", margin:0});
  }

  // ── CONCEPT 2: Bold IQ Wordmark with Red Star Accent ──
  {
    const cx = 0.28 + LOGO_CW + LOGO_GAP, cy = LOGO_TOP, cw = LOGO_CW, ch = LOGO_H;
    s.addShape(pres.shapes.RECTANGLE, {x:cx, y:cy, w:cw, h:ch, fill:{color:"F8FAFC"}, line:{color:"E2E8F0"}});

    // Mockup area
    s.addShape(pres.shapes.RECTANGLE, {x:cx+0.16, y:cy+0.16, w:cw-0.32, h:1.66, fill:{color:NAVY}, line:{color:NAVY}});

    // Large IQ text
    s.addText("IQ", {x:cx+0.16, y:cy+0.16, w:cw-0.32, h:1.20, fontSize:68, color:WHITE, bold:true, align:"center", valign:"middle", margin:0});

    // Red 4-pointed star top-right of Q
    s.addText("✦", {x:cx+1.80, y:cy+0.20, w:0.46, h:0.46, fontSize:18, color:RED, align:"center", valign:"middle", bold:true, margin:0});

    // Teal underline
    s.addShape(pres.shapes.RECTANGLE, {x:cx+0.36, y:cy+1.58, w:cw-0.72, h:0.08, fill:{color:TEAL}, line:{color:TEAL}});

    // Label bar
    s.addShape(pres.shapes.RECTANGLE, {x:cx+0.16, y:cy+1.82, w:cw-0.32, h:0.26, fill:{color:NAVY}, line:{color:NAVY}});
    s.addText("DIRECTION B  —  Bold IQ Wordmark + Star", {x:cx+0.16, y:cy+1.82, w:cw-0.32, h:0.26, fontSize:7.5, color:WHITE, bold:true, valign:"middle", margin:0});

    s.addText("The name itself is the icon. IQ in bold type is immediately readable at any size — from a 16px favicon to a 200px hero mark. The red four-pointed star anchors the StoreNext brand identity and signals the AI intelligence layer. Simplest to implement. Lowest design risk.", {
      x:cx+0.16, y:cy+2.14, w:cw-0.32, h:1.50, fontSize:8, color:SUB, valign:"top", margin:0
    });

    s.addShape(pres.shapes.RECTANGLE, {x:cx+0.16, y:cy+ch-0.30, w:cw-0.32, h:0.22, fill:{color:NAVY_MID}, line:{color:NAVY_MID}});
    s.addText("Best short-term path — ship fast while Direction A is finalized", {x:cx+0.16, y:cy+ch-0.30, w:cw-0.32, h:0.22, fontSize:7, color:SUBHDR, align:"center", valign:"middle", margin:0});
  }

  // ── CONCEPT 3: Circle Badge — IQ in colored ring ──
  {
    const cx = 0.28 + 2*(LOGO_CW + LOGO_GAP), cy = LOGO_TOP, cw = LOGO_CW, ch = LOGO_H;
    s.addShape(pres.shapes.RECTANGLE, {x:cx, y:cy, w:cw, h:ch, fill:{color:"F8FAFC"}, line:{color:"E2E8F0"}});

    // Mockup area — NAVY background for visual consistency with A and B
    s.addShape(pres.shapes.RECTANGLE, {x:cx+0.16, y:cy+0.16, w:cw-0.32, h:1.66, fill:{color:NAVY}, line:{color:NAVY}});

    // Outer ring
    s.addShape(pres.shapes.OVAL, {x:cx+0.46, y:cy+0.22, w:1.98, h:1.54, fill:{color:NAVY}, line:{color:NAVY}});
    // Inner ring gap (white on dark bg)
    s.addShape(pres.shapes.OVAL, {x:cx+0.60, y:cy+0.34, w:1.70, h:1.30, fill:{color:WHITE}, line:{color:WHITE}});
    // Center fill
    s.addShape(pres.shapes.OVAL, {x:cx+0.72, y:cy+0.44, w:1.46, h:1.10, fill:{color:NAVY}, line:{color:NAVY}});

    // IQ text
    s.addText("IQ", {x:cx+0.46, y:cy+0.22, w:1.98, h:1.54, fontSize:40, color:WHITE, bold:true, align:"center", valign:"middle", margin:0});

    // Red star top-right on outer ring
    s.addText("✦", {x:cx+1.88, y:cy+0.20, w:0.36, h:0.36, fontSize:14, color:RED, align:"center", valign:"middle", bold:true, margin:0});

    // Label bar
    s.addShape(pres.shapes.RECTANGLE, {x:cx+0.16, y:cy+1.82, w:cw-0.32, h:0.26, fill:{color:NAVY}, line:{color:NAVY}});
    s.addText("DIRECTION C  —  Circle Badge Mark", {x:cx+0.16, y:cy+1.82, w:cw-0.32, h:0.26, fontSize:7.5, color:WHITE, bold:true, valign:"middle", margin:0});

    s.addText("A ringed badge format — familiar from product avatars and app icons. Reads well in circular containers (Slack, Teams, mobile apps). The double-ring suggests layered intelligence: the outer ring is the platform, the inner fill is the AI core. Optimized for app marketplace and social avatars.", {
      x:cx+0.16, y:cy+2.14, w:cw-0.32, h:1.50, fontSize:8, color:SUB, valign:"top", margin:0
    });

    s.addShape(pres.shapes.RECTANGLE, {x:cx+0.16, y:cy+ch-0.30, w:cw-0.32, h:0.22, fill:{color:AMBER}, line:{color:AMBER}});
    s.addText("Best for app stores, Teams integration, mobile contexts", {x:cx+0.16, y:cy+ch-0.30, w:cw-0.32, h:0.22, fontSize:7, color:WHITE, bold:true, align:"center", valign:"middle", margin:0});
  }

  s.addNotes("Three logo directions for StoreNext IQ. Direction A (Hexagon + IQ magnifying glass + red sparkle) is the most distinctive and differentiating — the Q-as-magnifying-glass is a triple meaning: letter Q, search metaphor, and AI intelligence signal. The red sparkle inside the lens is the insight moment. Direction B (Bold IQ wordmark) is the fastest to implement and clearest at all sizes. Direction C (Circle badge) is optimized for app store and integration contexts. Recommended path: Direction A as the long-term brand mark, Direction B as the short-term implementation while design is finalized.");
}

// ── WRITE FILE ────────────────────────────────────────────────
pres.writeFile({fileName:"AI-in-Supplier-Portals-Competitive-Analysis.pptx"})
  .then(() => console.log("SUCCESS: Presentation saved."))
  .catch(err => { console.error("ERROR:", err); process.exit(1); });
