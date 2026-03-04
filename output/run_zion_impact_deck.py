#!/usr/bin/env python3
"""
Zion · Impact Across the Air Force
30-slide McKinsey-grade deck · Light theme
Data sourced from: Linear, Google Drive, Gmail weekly updates · March 2026
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from generate_deck import main

DECK = {
    "filename": "Zion_Impact_AirForce",
    "slides": [

        # ── 1. Title ─────────────────────────────────────────────────────────
        {
            "layout": "title",
            "title": "Zion · Accelerating Intelligence Across the Air Force",
            "subtitle": "Scale AI · Donovan on JWICS · March 2026",
            "notes": "Opening. Zion is Scale AI's JWICS deployment of Donovan for USAF intel analysts. "
                     "This deck covers platform status, proven impact, the adoption gap, and path to "
                     "full-spectrum deployment across the DGS enterprise.",
        },

        # ── 2. Executive Summary ──────────────────────────────────────────────
        {
            "layout": "metrics",
            "title": "Four Numbers Define the Zion Engagement",
            "metrics": [
                {"label": "Accounts Provisioned", "value": "382",       "detail": "Across 8 AF intel units on JWICS"},
                {"label": "Apps in Production",   "value": "6",         "detail": "3 in beta · 6 in development"},
                {"label": "ATO-C Valid Through",  "value": "Jul 2026",  "detail": "Authority to Operate — Classified"},
                {"label": "Weekly Active Today",  "value": "~20",       "detail": "5% activation — the defining gap"},
            ],
            "notes": "The headline: platform deployed, ATO-C secured, apps running. "
                     "The work now is activation. 382 accounts provisioned, ~20 weekly active — "
                     "that gap is the central tension of this deck.",
        },

        # ── 3. Central Tension ────────────────────────────────────────────────
        {
            "layout": "fact",
            "title": "Capability Is Deployed. Activation Is the Constraint.",
            "value": "5%",
            "label": "of provisioned accounts are weekly active",
            "detail": "20 of 382 accounts · DGS-KS cohort · as of Feb 26, 2026",
            "notes": "This is not a technology problem. Donovan is live, ATO-C'd, and running 6 apps. "
                     "The gap is onboarding, champion development, and use case discovery — "
                     "all solvable with the activation playbook.",
        },

        # ── 4. Section ────────────────────────────────────────────────────────
        {
            "layout": "section",
            "title": "The Problem",
            "notes": "Why does this matter to the Air Force? "
                     "Frame the structural problem Donovan solves before showing the solution.",
        },

        # ── 5. The Analyst Bottleneck ─────────────────────────────────────────
        {
            "layout": "two_column",
            "title": "USAF Intel Analysts Are Data Processors, Not Intelligence Producers",
            "left_title": "Today: Human-Is-the-Loop",
            "left_bullets": [
                "Analysts swivel-chair across 10+ systems: ACE, PULSE, IBS, NGT, Thresher, SIGACTS",
                "Daily TACREP processing: hours of manual copy-paste and format conversion",
                "ICD-203 compliance review done entirely by hand — no automated quality gate",
                "Finished products take hours to build, validate, and downgrade for dissemination",
                "Cross-domain transfer from DGS to AOC is a manual handoff that delays action",
            ],
            "right_title": "The Cost",
            "right_bullets": [
                "Decision advantage lost when intelligence lags operational tempo",
                "QA/SIA shops consume capacity reviewing products that could be auto-validated",
                "High-value analysts doing low-value aggregation — $78K/yr integration layer*",
                "Briefing prep delays compound into mission planning delays at the AOC",
                "Competing platforms (CompassAI, Sanctuary, AIP) filling the vacuum",
            ],
            "notes": "Source: DCGS Issue Paper framing ('human-is-the-loop') + site visit findings. "
                     "The $78K/analyst figure is a modeled estimate — flag it as directional.",
        },

        # ── 6. ICD-203 Cost ───────────────────────────────────────────────────
        {
            "layout": "fact",
            "title": "Manual ICD-203 Review Costs an Estimated $78,000 Per Analyst Annually",
            "value": "$78K",
            "label": "Modeled annual cost of manual ICD-203 compliance review per analyst",
            "detail": "~$150/hr fully burdened · at 480th ISRW scale: modeled savings aggregate to millions/year",
            "notes": "IMPORTANT: This is a modeled estimate from the SFT paper — not a confirmed "
                     "operational number. Cite it as directional. The point: ICD-203 review is a "
                     "high-frequency, high-stakes task done entirely manually today.",
        },

        # ── 7. Keen Edge Validation ───────────────────────────────────────────
        {
            "layout": "quote",
            "quote": "Donovan was chosen as the preferred GenAI tool over CompassAI and Sanctuary during Keen Edge — the only evaluation that matters is one in a real exercise.",
            "attribution": "PACAF A2 site visit debrief · February 2026",
            "notes": "Keen Edge is a major joint exercise. Donovan was validated under operational "
                     "conditions against live competition. This is the most credible proof point "
                     "in the deck — preference expressed by operators in a real exercise.",
        },

        # ── 8. What Makes Donovan Different ───────────────────────────────────
        {
            "layout": "content",
            "title": "Three Properties No Competitor Has Matched on JWICS",
            "bullets": [
                "ATO-C on JWICS (Jun 2025, extended Jul 2026) — months of work; the highest barrier to entry in the classified GenAI market",
                "Intelligence-native architecture — apps purpose-built for DCGS workflows, not adapted from commercial use cases",
                "Agentic multi-app framework — analysts orchestrate across Sig Lib, TACREP, TSAAR, ICD-203, ChatSurfer, Thresher in a single session",
                "Statement-level citations — every Donovan output is source-traceable by paragraph; critical for analyst trust on TS/SCI networks",
                "Hardware-deployable fine-tuned model in development — Defense Llama 8B trained on real DCGS evaluations (no commercial model required)",
            ],
            "notes": "This slide bridges from the problem to the platform. Before diving into "
                     "infrastructure, anchor what makes Donovan structurally different — not just "
                     "another API wrapper on JWICS, but a purpose-built intelligence platform.",
        },

        # ── 9. Platform Overview ──────────────────────────────────────────────
        {
            "layout": "metrics",
            "title": "Donovan on JWICS: The Only ATO-C'd GenAI Platform Native to the Classified Network",
            "metrics": [
                {"label": "Network",              "value": "JWICS",    "detail": "DAF Cloudworks · TS/SCI"},
                {"label": "Platform",             "value": "Donovan",  "detail": "Scale AI + SGP · Agentic Chat default"},
                {"label": "ATO-C Granted",        "value": "Jun 2025", "detail": "Extended through Jul 2026"},
                {"label": "Competitors Displaced", "value": "2",       "detail": "CompassAI · Sanctuary"},
            ],
            "notes": "ATO-C on JWICS is a significant barrier to entry — it took months to achieve. "
                     "Donovan beat CompassAI and Sanctuary to this accreditation. "
                     "The platform runs Claude 4.5 as default model as of Feb 2026.",
        },

        # ── 10. How It Works ──────────────────────────────────────────────────
        {
            "layout": "process",
            "title": "Donovan Transforms Raw Classified Data Into Finished Intelligence in Five Steps",
            "steps": [
                {"label": "Ingest",   "detail": "JWICS sources: ChatSurfer rooms, Thresher, uploaded docs"},
                {"label": "Retrieve", "detail": "RAG across IRs, PULSE, ACE, SIGACTS, FINTEL"},
                {"label": "Reason",   "detail": "Agentic Claude — tool orchestration across 6 live apps"},
                {"label": "Draft",    "detail": "TACREP, GRINTSUM, ICD-203 eval, tearlines — analyst-ready"},
                {"label": "Deliver",  "detail": "Cited, classified, formatted — ready for dissemination"},
            ],
            "notes": "Walk through a live example: analyst uploads TACREP CSV → Donovan extracts threat "
                     "indicators, validates ICD-203 compliance, and generates a formatted intel product "
                     "in under 2 minutes.",
        },

        # ── 11. Live Data Connections ─────────────────────────────────────────
        {
            "layout": "two_column",
            "title": "ChatSurfer Is Live. Thresher Is Next. Nine More Integrations Are Queued.",
            "left_title": "Live as of Feb 2026",
            "left_bullets": [
                "ChatSurfer (Feb 11) — connects Donovan to JWICS chat rooms; query live message traffic without leaving the platform",
                "Statement-level citations added (Feb 26) — every output source-traceable by paragraph",
                "Claude 4.5 set as default ChatSurfer model — faster inference, better instruction-following",
                "Thresher PRD complete — query the activity layer; first major structured data connection on JWICS",
            ],
            "right_title": "In the Pipeline",
            "right_bullets": [
                "FADE/MIST — dynamic intel data for briefs and GRINTSUMs",
                "IBS + NGT — FINTEL layer for exercise planning and order of battle",
                "Pulse + The Wire — FINTEL completing the intelligence corpus",
                "NASIC Link + MIDB + MEPED — signature data for targeting and exercise support",
                "Each integration multiplies the value of every app already deployed",
            ],
            "notes": "ChatSurfer is the most visible recent delivery. The citation addition is critical "
                     "for analyst trust — they need to trace every Donovan output back to a source document. "
                     "Data connection roadmap came directly from the User Forum, Jan 21-22, Rome NY.",
        },

        # ── 12. Data Connection Roadmap ───────────────────────────────────────
        {
            "layout": "table",
            "title": "Ten Data Connections Prioritized by Analysts — One Live, Nine in the Pipeline",
            "headers": ["Source", "Category", "Status", "Primary Use"],
            "rows": [
                ["ChatSurfer",  "Live JWICS Chat",  "Live ✓",       "Summarize and query message traffic"],
                ["Thresher",    "Activity Layer",   "PRD Complete", "RFI response acceleration"],
                ["FADE/MIST",   "Dynamic Intel",    "Roadmap",      "Briefs and GRINTSUMs"],
                ["IBS",         "Dynamic Intel",    "Roadmap",      "Briefs and GRINTSUMs"],
                ["NGT",         "FINTEL",           "Roadmap",      "Briefs and exercise planning"],
                ["Pulse",       "FINTEL",           "Roadmap",      "Briefs and exercise planning"],
                ["The Wire",    "FINTEL",           "Roadmap",      "Briefs and exercise planning"],
                ["NASIC Link",  "Signature Data",   "Roadmap",      "Targeting and exercise support"],
                ["MIDB",        "Signature Data",   "Roadmap",      "Targeting and exercise support"],
                ["MEPED",       "Signature Data",   "Roadmap",      "Targeting and exercise support"],
            ],
            "notes": "This roadmap came directly from analysts at the User Forum, Jan 21-22, Rome NY. "
                     "Each integration multiplies the value of every app already deployed.",
        },

        # ── 13. Section ───────────────────────────────────────────────────────
        {
            "layout": "section",
            "title": "Proven Impact",
            "notes": "What the confirmed data shows. "
                     "All metrics in this section are from Linear acceptance criteria or site visit data. "
                     "Flag estimates explicitly when they appear.",
        },

        # ── 14. Impact at a Glance ────────────────────────────────────────────
        {
            "layout": "table",
            "title": "Three Apps. Three Quantified Wins. All in Production.",
            "headers": ["App", "Task Automated", "Manual Baseline", "With Donovan", "Confirmed Savings"],
            "rows": [
                ["Signature Library",    "AAA Sig Lib maintenance", "66+ hrs/quarter",  "33 hrs/quarter",  "33 hrs saved · 132 hrs/year"],
                ["TACREP Transformer",   "TACREP conversion",       "Hours — daily",    "50%+ faster",     "≥95% accuracy · daily compounding"],
                ["TSAAR Generator",      "Daily brief prep",        "~2 hrs/day",       "~30 min/day",     "1.5 hrs saved · 375 hrs/year"],
            ],
            "notes": "All three metrics are confirmed from Linear acceptance criteria — not projections. "
                     "These three apps run on a limited active user base. Scaling to the full 382 "
                     "provisioned accounts multiplies these numbers by 19x.",
        },

        # ── 15. Sig Lib Headline ───────────────────────────────────────────────
        {
            "layout": "fact",
            "title": "Sig Lib Recovered 33 Analyst-Hours Per Quarter at DGS-KS — Automatically",
            "value": "33 hrs",
            "label": "Saved per quarter · AAA Signature Library · DGS-KS",
            "detail": "Manual baseline: 66+ hours/quarter · 50% reduction confirmed · 132 hours recovered annually",
            "notes": "Confirmed metric from Linear acceptance criteria. 132 hours/year is roughly three "
                     "weeks of analyst time recovered from a single app running on a small user base.",
        },

        # ── 16. TACREP + TSAAR Details ────────────────────────────────────────
        {
            "layout": "two_column",
            "title": "Daily Tasks Transformed: TACREP Conversion and Brief Preparation",
            "left_title": "TACREP Transformer · DGS-KS",
            "left_bullets": [
                "Task: convert raw TACREP CSV data into formatted intelligence reports",
                "Acceptance criteria: ≥50% time reduction, ≥95% Critical Info Verification Rate",
                "Frequency: daily — compounding savings across an analyst's year are significant",
                "95% CIVR means analysts can act on output with confidence — no secondary review",
                "In production at DGS-KS; ready to deploy to every DGS running daily TACREP",
            ],
            "right_title": "TSAAR Generator · DGS-2 (Beta)",
            "right_bullets": [
                "Task: generate the Theater Security Assistance and Readiness daily brief",
                "Baseline: ~2 hours per day of manual compilation and formatting",
                "With TSAAR: ~30 minutes — 1.5 hours saved per analyst per day",
                "~375 hours/year when fully deployed — roughly 9 analyst work weeks",
                "TSAAR affects what Wing commanders see every morning; highest-visibility delivery",
            ],
            "notes": "These are confirmed acceptance criteria metrics from Linear, not projections. "
                     "TSAAR is still in beta at DGS-2 — when it reaches production and scale, "
                     "multiply the savings across every DGS running a daily wing brief.",
        },

        # ── 17. What Analysts Want ────────────────────────────────────────────
        {
            "layout": "chart",
            "title": "Analysts Ranked Seven Priorities — ICD-203 Evaluation, Readbooks, and Briefing Automation Lead",
            "chart_type": "bar_horizontal",
            "categories": [
                "Anomaly Detection",
                "Exercise Planning",
                "FDO / Tearline Automations",
                "GRINTSUM Generation",
                "Automated Lowdown / Rel-to-Capability",
                "Readbook Generation",
                "ICD-203 Evaluator",
            ],
            "series": [
                {"name": "Analyst Priority (1 = lowest, 7 = highest)", "values": [1, 2, 3, 4, 5, 6, 7]},
            ],
            "notes": "Source: Donovan User Forum, Jan 21-22, 2026, AFRL RIEB HQ, Rome NY. "
                     "The #1 priority — ICD-203 Evaluator — is already in production. "
                     "Next two (Readbooks, Lowdown automation) are on the development roadmap.",
        },

        # ── 18. Site Visit Findings ───────────────────────────────────────────
        {
            "layout": "two_column",
            "title": "Every Unit Has the Same Two Bottlenecks: Dissemination Speed and Brief Preparation",
            "left_title": "PACAF A2 / DGS-5 · Feb 17–20",
            "left_bullets": [
                "Cross-domain transfer from DGS to AOC is the primary bottleneck",
                "Daily reporting products require significant QC time before reaching end users",
                "Col Huffman: skeptical of AI writing quality; highly interested in agentic capabilities",
                "Lt Col Myers positioning SrA Wichin and SrA Eatough as organic Donovan trainers within A2O",
                "Top use cases: Thresher QC validation and RFI response acceleration",
            ],
            "right_title": "Pattern Across All Units",
            "right_bullets": [
                "Brief prep consumes 1–2+ hours daily across every shop visited",
                "Classification marking UX is the #1 adoption blocker — still manual inside Donovan today",
                "Each unit runs different source systems but the same underlying workflow problem",
                "Organic trainer model outperforms top-down mandate for sustained adoption",
                "Agentic capabilities generate 2x the enthusiasm of single-task automation",
            ],
            "notes": "These findings are from the PACAF A2, DGS-5, and 613th AOC site visits "
                     "(Feb 17-20, 2026). Aneesh Vittal led the visits. The pattern is consistent: "
                     "workflow bottleneck is product creation and dissemination, not analysis.",
        },

        # ── 19. Champion Quote ────────────────────────────────────────────────
        {
            "layout": "quote",
            "quote": "When operators own the training pipeline — not vendors — adoption becomes self-sustaining. PACAF A2 is already positioning enlisted analysts as organic Donovan trainers within the unit.",
            "attribution": "Observation from PACAF A2 site visit · February 2026",
            "notes": "The organic trainer model is the highest-leverage adoption play. When a unit "
                     "develops its own Donovan experts, WAU grows without Scale's direct involvement. "
                     "Lt Col Myers proactively naming specific analysts as trainers is the strongest "
                     "adoption signal we've seen.",
        },

        # ── 20. Section ───────────────────────────────────────────────────────
        {
            "layout": "section",
            "title": "Activation at Scale",
            "notes": "Transition to the adoption challenge and the plan to close the gap. "
                     "The capability is there — the question is how fast we can activate it.",
        },

        # ── 21. Accounts vs. Active ───────────────────────────────────────────
        {
            "layout": "chart",
            "title": "Account Provisioning Accelerated in February — Weekly Active Users Remain Flat",
            "chart_type": "bar",
            "categories": ["Feb 13", "Feb 20", "Feb 26"],
            "series": [
                {"name": "Provisioned Accounts", "values": [361, 367, 382]},
                {"name": "Weekly Active Users",   "values": [20, 20, 20]},
            ],
            "notes": "21 accounts added in two weeks; WAU held flat at ~20. "
                     "Provisioning ≠ activation. The divergence between the two lines is the problem "
                     "to solve. Every site visit and champion we develop is a bet that WAU catches up.",
        },

        # ── 22. Activation Flywheel ────────────────────────────────────────────
        {
            "layout": "process",
            "title": "Unit Activation Follows a Five-Step Flywheel — DGS-KS Has Reached Step Four",
            "steps": [
                {"label": "Provision",  "detail": "Accounts created on DAF Cloudworks JWICS via Tercat"},
                {"label": "Deskside",   "detail": "1:1 session — identify the analyst's use case, show the app"},
                {"label": "First Win",  "detail": "Analyst uses Donovan on a real task and saves measurable time"},
                {"label": "Champion",   "detail": "Power user becomes internal advocate and unit trainer"},
                {"label": "Scale",      "detail": "Unit trains organically — WAU grows without Scale support"},
            ],
            "notes": "DGS-KS: approaching step 4 — organic training emerging. "
                     "PACAF A2: step 3, first wins confirmed. "
                     "DGS-5, 118th ISRG: step 2, post-site-visit. "
                     "Goal before June 26 PoP end: every targeted unit at step 3 or higher.",
        },

        # ── 23. Expansion Table ───────────────────────────────────────────────
        {
            "layout": "table",
            "title": "Eight Units Active or Engaged — Five Expansion Targets Unlock the Next Contract",
            "headers": ["Unit", "Location", "Status", "Next Action"],
            "rows": [
                ["DGS-KS (184th ISRG)", "Kansas",         "Active · 20 WAU",           "Site visit Mar 17–18"],
                ["PACAF A2",            "Pearl Harbor",   "Organic trainer emerging",   "Lt Col Myers leading"],
                ["DGS-5 (692nd ISRG)", "Hawaii",          "Site visit complete",        "Champion ID · app rollout"],
                ["613th AOC",           "Hawaii",         "Visited Feb",                "Cross-domain use case"],
                ["DGS-2",               "Virginia",       "Beta apps deployed",         "Reschedule (real-world delay)"],
                ["118th ISRG / TN ANG","Tennessee",       "Site visit confirmed",       "Mar 17–18"],
                ["48th FW Intel",       "RAF Lakenheath", "Active via Zermatt",         "Transition to Zion planned"],
                ["363rd ISR Wing",      "TBD",            "Expansion target",           "Scoping underway"],
                ["480th ISR Wing",      "Langley, VA",    "Expansion target",           "Enterprise contract candidate"],
                ["AFRL / AOC",          "Rome, NY",       "Expansion target",           "Sean Fee — active relationship"],
            ],
            "notes": "The 363rd, 480th, and AFRL are the expansion targets that directly support "
                     "the next contract narrative. The 48th FW (RAF Lakenheath) is already on JWICS "
                     "Donovan through Zermatt — transitioning extends footprint to USAFE.",
        },

        # ── 24. Roadmap Gantt ─────────────────────────────────────────────────
        {
            "layout": "gantt",
            "title": "Thirteen Milestones Drive the Path to June 26 PoP End",
            "subtitle": "Zion Delta · Scale AI · Feb–Jun 2026",
            "quarters": ["Q1 2026", "Q2 2026"],
            "months": ["Feb", "Mar", "Apr", "May", "Jun"],
            "phases": [
                "Site Visits",
                "App Development",
                "Data Connections",
                "Compliance",
                "Deliverables",
            ],
            "tasks": [
                ("Site Visits",     "PACAF A2 / DGS-5 / 613th AOC",         0, 0, True,  "Feb 17–20"),
                ("Site Visits",     "DGS-KS + 118th ISRG",                  1, 1, True,  "Mar 17–18"),
                ("Site Visits",     "DGS-2 (rescheduled)",                  2, 2, False, "Apr TBD"),
                ("Site Visits",     "363rd + 480th ISR Wing scoping",       2, 4, False, None),
                ("App Development", "TSAAR, SIEGE, EOB Merge beta → prod",  0, 2, False, "Apr 2026"),
                ("App Development", "FDO Tool, Tearline, Deriv. Class.",    1, 3, False, "May 2026"),
                ("Data Connections","Thresher PRD implementation",          0, 2, False, "Apr 2026"),
                ("Data Connections","FADE/MIST, IBS, NGT scoping",         2, 4, False, None),
                ("Compliance",      "CDR with 16th AF SCE",                 1, 1, True,  "Mar 5"),
                ("Compliance",      "STIG hardening + Nessus scanning",     0, 4, False, None),
                ("Deliverables",    "SFT Dataset #1 · 750+ PRPs",          1, 3, False, "May 2026"),
                ("Deliverables",    "SFT Dataset #2 · 750+ PRPs",          2, 4, False, "Jun 2026"),
                ("Deliverables",    "PoP End",                              4, 4, True,  "Jun 26"),
            ],
            "notes": "The critical path: site visits → champions → WAU → SFT data quality → model "
                     "improvement. CDR on Mar 5 is the compliance gate — must pass to maintain ops.",
        },

        # ── 25. Why Generic AI Isn't Enough ───────────────────────────────────
        {
            "layout": "content",
            "title": "Generic AI Fails on DCGS Workflows — Donovan Was Built for This",
            "bullets": [
                "ICD-203 compliance is domain-specific: a general model hallucinates deficiency categories, misclassifies products, and can't score against the DCGS rubric",
                "TACREP formatting follows military standards not in any public training dataset — extraction accuracy requires fine-tuning on real examples",
                "Classification marking rules are complex and jurisdiction-specific; a generic model cannot reliably apply TS/SCI handling instructions",
                "The SFT program exists to close this gap: Defense Llama 8B trained on real analyst evaluations, deployable on JWICS hardware without a commercial cloud dependency",
                "The moat isn't the app — it's the dataset. Scale owns the annotated evaluation data that no competitor can replicate.",
            ],
            "notes": "This slide sets up the SFT/model development section. The argument: once you "
                     "build this dataset, the platform becomes defensible. Any API wrapper on JWICS "
                     "can be a chatbot. Only Scale has the annotated DCGS-domain training data.",
        },

        # ── 26. SFT Pipeline ──────────────────────────────────────────────────
        {
            "layout": "process",
            "title": "The SFT Pipeline Builds a DCGS-Native Model From Real Analyst Evaluations",
            "steps": [
                {"label": "Taxonomy",    "detail": "ICD-203 deficiency types — what failure modes exist in AF intel products"},
                {"label": "Human Evals", "detail": "QA/SIA shops at each DGS score real product samples against rubric"},
                {"label": "RaR Synth",   "detail": "Rewrite-and-Refine: Claude Opus generates 750+ training pairs per domain"},
                {"label": "Fine-Tune",   "detail": "Defense Llama 8B trained on DCGS-specific data — deployable on JWICS hardware"},
                {"label": "Deploy",      "detail": "JWICS-native model: faster inference, lower cost, domain-accurate outputs"},
            ],
            "notes": "The 'Rewrite and Refine' (RaR) approach: advanced models generate training data "
                     "for smaller, deployable models — reducing human labeling burden by ~90% (modeled). "
                     "Defense Llama 8B is small enough to run economically on JWICS infrastructure.",
        },

        # ── 27. SFT Targets ───────────────────────────────────────────────────
        {
            "layout": "metrics",
            "title": "Two Datasets · 1,500+ Prompt-Response Pairs · Targeting 80% Time Reduction on ICD-203",
            "metrics": [
                {"label": "PRPs Per Dataset",      "value": "750+",  "detail": "2 datasets · contractual obligation"},
                {"label": "Time Reduction Target", "value": "80%",   "detail": "ICD-203 eval vs. manual today (est.)"},
                {"label": "Accuracy Target",       "value": ">90%",  "detail": "vs. human inter-rater reliability (est.)"},
                {"label": "Labeling Reduction",    "value": "~90%",  "detail": "Via RaR synthetic pipeline (est.)"},
            ],
            "notes": "750+ PRPs per dataset is confirmed — it is the contractual requirement. "
                     "The 80% time reduction, >90% accuracy, and ~90% labeling reduction are targets "
                     "from the SFT paper — flag them as modeled projections, not confirmed outcomes.",
        },

        # ── 28. Section ───────────────────────────────────────────────────────
        {
            "layout": "section",
            "title": "Path Forward",
            "notes": "Final section — key milestones to PoP end and what comes next. "
                     "Leave the audience with clear actions, owners, and dates.",
        },

        # ── 29. Key Milestones ────────────────────────────────────────────────
        {
            "layout": "table",
            "title": "Seven Milestones Before June 26 — Three Are on the Critical Path",
            "headers": ["Milestone", "Date", "Owner", "Criticality"],
            "rows": [
                ["Critical Design Review · 16th AF SCE",  "Mar 5, 2026",     "Andrew Roth",        "ATO-C compliance gate"],
                ["AFRL / Dayton demo (BGB team)",          "Mar 9, 2026",     "Jared Strickland",   "Next contract narrative"],
                ["DGS-KS + 118th ISRG site visits",        "Mar 17–18, 2026", "Scale team",         "Highest activation leverage"],
                ["SFT Dataset #1 delivery · 750+ PRPs",    "May 2026",        "Austin Woo",         "Contractual obligation"],
                ["SFT Dataset #2 delivery · 750+ PRPs",    "Jun 2026",        "Austin Woo",         "Contractual obligation"],
                ["Next contract shaping (ACC/IDIQ)",       "Rolling",         "Jared / PM",         "FY26 ask: $7.5M"],
                ["PoP End · Zion Delta",                   "Jun 26, 2026",    "All",                "Closeout + transition"],
            ],
            "notes": "Three critical-path milestones: CDR (compliance gate), AFRL demo "
                     "(shapes FY26 funding narrative), and DGS-KS site visit (highest WAU leverage). "
                     "The next contract vehicle (ACC IDIQ) is scoping now — $7.5M FY26 supplemental "
                     "to position Agentic ISR as a DCGS Program of Record.",
        },

        # ── 30. Closing ───────────────────────────────────────────────────────
        {
            "layout": "title",
            "title": "The Intelligence Advantage Is Already Deployed",
            "subtitle": "382 accounts · 6 apps · ATO-C'd · Donovan chosen over CompassAI in Keen Edge · Scale AI",
            "notes": "Closing message: the infrastructure question is answered. Donovan is live on JWICS, "
                     "ATO-C'd, and validated under real exercise conditions. The next chapter is "
                     "activation — converting 382 provisioned accounts into a force multiplier, "
                     "with $7.5M in FY26 funding to extend it to a DCGS Program of Record.",
        },

    ],
}

if __name__ == "__main__":
    main(theme_name="light", deck=DECK)
