#!/usr/bin/env python3
"""
SAOC (Survivable Airborne Operations Center) — Boston Harbor Islands
Program Kickoff Deck

Sources:
  - SNC press releases (Apr 2025, Aug 2025)
  - The War Zone, The Aviationist, Defense Daily
  - HigherGov SAOC budget line item
  - DIU Thunderforge announcement (Mar 2025)
  - Air Force FY2025/2026 budget justifications
  - Wikipedia: SNC E-4C SAOC
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from generate_deck import main

DECK = {
    "filename": "Boston_Harbor_Islands_SAOC_Kickoff",
    "slides": [
        # ── Title ─────────────────────────────────────────────────────
        {
            "layout": "title",
            "title": "Boston Harbor Islands — Program Kickoff",
            "subtitle": "SAOC · Survivable Airborne Operations Center\nScale AI · February 2026",
            "notes": "Welcome to the Boston Harbor Islands program kickoff. SAOC — the Survivable Airborne Operations Center — is the Air Force's next-generation airborne command post replacing the E-4B Nightwatch. This briefing covers program context, Scale AI's opportunity space, and proposed engagement approach. All content sourced from OSINT.",
        },

        # ── Section: Program Overview ─────────────────────────────────
        {
            "layout": "section",
            "title": "Program Overview",
            "notes": "Transition: Let's start with what SAOC is and where the program stands today.",
        },

        {
            "layout": "two_column",
            "title": "SAOC replaces the nation's 50-year-old airborne command post",
            "left_title": "E-4B Nightwatch (Current)",
            "left_bullets": [
                "Built in the 1970s on Boeing 747-200 airframes",
                "Approaching 115,000-hour airframe life limit (2039)",
                "Escalating maintenance costs, growing parts obsolescence",
                "Legacy comms architecture with limited modernization path",
                "Four aircraft in fleet, all operational from Offutt AFB",
            ],
            "right_title": "E-4C SAOC (Replacement)",
            "right_bullets": [
                "Boeing 747-8I airframes (ex-Korean Air)",
                "Five aircraft under $13B SNC contract (Apr 2024)",
                "USAF considering expansion to 6–8 aircraft",
                "Open architecture with model-based systems engineering",
                "Flight testing began Aug 7, 2025 at Dayton, OH",
            ],
            "notes": "The E-4B is the 'Doomsday Plane' — it provides POTUS, SECDEF, and CJCS an airborne command post during national emergencies or nuclear conflict. The E-4C SAOC is its replacement, built by Sierra Nevada Corporation on used Boeing 747-8I airframes purchased from Korean Air. Major update: USAF may expand the order from 5 to 6–8 aircraft at Offutt AFB, Nebraska.",
        },

        {
            "layout": "metrics",
            "title": "SAOC by the Numbers",
            "metrics": [
                {"label": "Contract Value", "value": "$13B", "detail": "Through 2036"},
                {"label": "Aircraft", "value": "5–8", "detail": "Expansion under review"},
                {"label": "FY26 Budget", "value": "$1.84B", "detail": "Up 9% from FY25 $1.69B"},
                {"label": "IOC Target", "value": "2032", "detail": "FOC early-mid 2030s"},
                {"label": "Prime", "value": "SNC", "detail": "Sierra Nevada Corp"},
                {"label": "Flight Test", "value": "Active", "detail": "Since Aug 2025"},
            ],
            "notes": "Key numbers: $13 billion total contract, 5 aircraft with potential expansion to 6–8. FY2026 budget request is $1.84B, up 9% from FY2025's $1.69B — indicating strong Congressional support. SNC won the contract in April 2024 after Boeing was eliminated in December 2023 for refusing to give up 747-8 data rights. Flight testing began August 7, 2025.",
        },

        {
            "layout": "chart",
            "title": "SAOC funding is accelerating year-over-year",
            "chart_type": "bar",
            "categories": ["FY23", "FY24", "FY25", "FY26"],
            "series": [
                {"name": "SAOC Budget ($M)", "values": [327, 744, 1688, 1842]},
            ],
            "notes": "Budget has grown 5.6x from FY23 to FY26. The FY24 jump reflects the contract award to SNC in April 2024. FY26 request of $1.84B signals the program is now in its peak development spending phase. This is one of the fastest-growing USAF line items. Source: HigherGov / Air Force budget justification documents.",
        },

        # ── Section: Strategic Context ────────────────────────────────
        {
            "layout": "section",
            "title": "Strategic Context",
            "notes": "Transition: Why does SAOC matter beyond the platform itself?",
        },

        {
            "layout": "process",
            "title": "SAOC absorbs missions from multiple legacy platforms",
            "steps": [
                {"label": "E-4B Nightwatch", "detail": "Airborne command post for POTUS, SECDEF, CJCS"},
                {"label": "E-6B Mercury", "detail": "ICBM launch command ('Looking Glass') transfers to SAOC"},
                {"label": "SAOC E-4C", "detail": "Unified NC3 node with open architecture for rapid tech insertion"},
            ],
            "notes": "SAOC isn't just replacing the E-4B — it's absorbing the 'Looking Glass' ICBM launch command mission from the Navy's E-6B Mercury. The Navy's replacement (E-130J) will handle TACAMO but NOT ICBM command. That mission transfers to SAOC, making it the single critical node for nuclear C2. This mission consolidation creates significant AI/ML integration opportunity.",
        },

        {
            "layout": "fact",
            "title": "The nuclear command consolidation creates a single point of AI integration",
            "value": "1 Platform",
            "label": "Unified NC3 Command Node",
            "detail": "SAOC consolidates E-4B airborne command + E-6B ICBM launch authority into one open-architecture platform, creating a single integration point for AI-driven C2.",
            "notes": "This is the key strategic insight. Instead of trying to integrate AI into two separate aging platforms (E-4B and E-6B), SAOC creates a single modernized platform with open architecture designed to accept new software capabilities. This dramatically simplifies Scale's integration pathway.",
        },

        # ── Section: Stakeholders ─────────────────────────────────────
        {
            "layout": "section",
            "title": "Key Stakeholders",
            "notes": "Transition: Who's involved and where does Scale fit in this ecosystem?",
        },

        {
            "layout": "table",
            "title": "Program ecosystem spans defense primes and innovation brokers",
            "headers": ["Entity", "Role", "Scale Relevance"],
            "rows": [
                ["Sierra Nevada Corp (SNC)", "Prime contractor — aircraft mod, mission systems", "Integration partner for AI/ML capabilities"],
                ["Collins Aerospace", "Mission systems & avionics", "Potential AI model deployment target"],
                ["Lockheed Martin", "Systems integration partner", "Existing Scale relationship vector"],
                ["GE Aerospace / Rolls-Royce", "Propulsion (GEnx-2B67)", "Low — hardware-focused"],
                ["USAF AFLCMC", "Program office oversight", "Customer — AI for T&E, digital twin"],
                ["US Strategic Command", "End user — NC3 operations", "High — AI-driven C2 decision support"],
                ["Wichita State NIAR", "Engineering & development facility", "Data curation for digital twin"],
                ["Defense Innovation Unit", "Innovation broker", "Direct pathway via Thunderforge"],
            ],
            "notes": "Key finding: Scale already has a DIU relationship through Thunderforge. DIU is the innovation broker for exactly this kind of AI insertion. The addition of Collins Aerospace and Lockheed Martin as SNC partners provides additional relationship vectors. NIAR at Wichita State is where the first aircraft was sent for engineering work in November 2024.",
        },

        # ── Section: Scale Opportunity ────────────────────────────────
        {
            "layout": "section",
            "title": "Scale AI Opportunity",
            "notes": "Transition: Here's where Scale can add value to SAOC.",
        },

        {
            "layout": "two_column",
            "title": "Three vectors for Scale engagement with SAOC",
            "left_title": "AI/ML Integration",
            "left_bullets": [
                "AI-assisted C2 decision support for NMCS operations",
                "Natural language interfaces for multi-domain coordination",
                "Automated threat assessment and COA generation",
                "Sensor fusion from heterogeneous intel feeds",
                "Extend Thunderforge planning agents to airborne C2",
            ],
            "right_title": "Data Infrastructure",
            "right_bullets": [
                "Training data curation for SAOC-specific models",
                "Digital twin data pipeline at NIAR facility",
                "T&E data labeling for flight test campaign",
                "Synthetic data generation for NC3 scenario modeling",
                "Data quality assurance for mission-critical systems",
            ],
            "notes": "Two primary vectors: AI/ML integration into SAOC mission systems via open architecture, and data infrastructure supporting the digital twin and test programs. The Thunderforge extension is the most compelling near-term opportunity — repurposing existing AI planning agents for the airborne C2 environment.",
        },

        {
            "layout": "quote",
            "quote": "Thunderforge will accelerate military decision-making by rapidly synthesizing vast information, generating multiple courses of action, and conducting AI-powered wargaming.",
            "attribution": "Defense Innovation Unit, March 2025",
            "notes": "This is from DIU's official Thunderforge announcement. The language maps directly to SAOC's mission: synthesizing information and generating courses of action is exactly what an airborne command post does. Scale, Anduril, and Microsoft are the Thunderforge prime team.",
        },

        {
            "layout": "content",
            "title": "Thunderforge creates a direct pathway from existing contract to SAOC",
            "bullets": [
                "Scale AI leads Thunderforge with Anduril and Microsoft (awarded Mar 2025)",
                "Scope: AI agents for operational/theater-level planning and wargaming",
                "Initial deployment: INDOPACOM + EUCOM — same commands SAOC serves",
                "SAOC's open architecture accepts modular AI insertions without monolithic redesign",
                "Thesis: Thunderforge AI planning agents → SAOC airborne C2 integration",
            ],
            "notes": "This is the strategic argument. Thunderforge is building AI for military planning at the combatant command level. SAOC is an airborne command post for those same commands. The open architecture on SAOC is designed for exactly the kind of modular AI integration that Thunderforge delivers. Scale's existing DIU relationship plus Anduril's defense credibility create a strong pathway.",
        },

        # ── Section: Engagement Approach ──────────────────────────────
        {
            "layout": "section",
            "title": "Engagement Approach",
            "notes": "Transition: How we get from here to a contract.",
        },

        {
            "layout": "gantt",
            "title": "Proposed Engagement Timeline",
            "subtitle": "Boston Harbor Islands · SAOC Engagement",
            "quarters": ["Q1 2026", "Q2 2026", "Q3 2026"],
            "months": ["Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"],
            "phases": [
                "Discovery",
                "Relationship",
                "Technical",
                "Proposal",
            ],
            "tasks": [
                ("Discovery", "OSINT deep-dive & landscape analysis", 0, 1, False, "15 Mar 2026"),
                ("Discovery", "Kickoff briefing (this deck)", 0, 0, True, "28 Feb 2026"),
                ("Relationship", "DIU introductions to AFLCMC PO", 1, 2, False, None),
                ("Relationship", "SNC / Collins partnership exploration", 2, 4, False, None),
                ("Relationship", "Lockheed Martin relationship leverage", 2, 3, False, None),
                ("Technical", "Thunderforge → SAOC demo mapping", 3, 4, False, "1 Jun 2026"),
                ("Technical", "Open architecture integration concept", 4, 5, False, None),
                ("Proposal", "White paper to program office", 5, 6, False, "1 Aug 2026"),
                ("Proposal", "Formal proposal submission", 6, 6, True, "31 Aug 2026"),
            ],
            "notes": "Seven-month engagement timeline. Phase 1: Discovery (we're here now). Phase 2: Use DIU relationships to open doors at AFLCMC and with SNC/Collins. Phase 3: Develop the technical case with Thunderforge demo mapping. Phase 4: Deliver formal proposals. Key milestone: demo mapping Thunderforge capabilities to SAOC use cases by June 2026.",
        },

        # ── Risks & Dependencies ──────────────────────────────────────
        {
            "layout": "table",
            "title": "Key risks are manageable with existing Scale relationships",
            "headers": ["Risk", "Impact", "Likelihood", "Mitigation"],
            "rows": [
                ["SNC controls integration scope", "High", "High", "Enter via DIU/Thunderforge, not direct to SNC"],
                ["Classified program limits access", "Medium", "High", "Start with unclassified T&E data, build toward clearance"],
                ["Budget sequestration or CR", "Medium", "Medium", "Leverage existing Thunderforge funding vehicle"],
                ["NC3 security requirements", "High", "Medium", "Scale's existing DoD security posture + cleared personnel"],
                ["Fleet expansion uncertainty", "Low", "Medium", "Core 5-aircraft program is funded regardless"],
            ],
            "notes": "Biggest risk: SNC as prime decides what goes on the plane. Mitigation: come through DIU/Thunderforge rather than selling to SNC directly. The classified nature of NC3 is a barrier, but starting with unclassified flight test data builds trust before seeking cleared access.",
        },

        # ── Next Steps ────────────────────────────────────────────────
        {
            "layout": "metrics",
            "title": "Five actions to advance the engagement in Q1 2026",
            "metrics": [
                {"label": "DIU Follow-Up", "value": "1", "detail": "Discuss SAOC as Thunderforge target"},
                {"label": "Personnel ID", "value": "2", "detail": "Find TS/SCI-cleared Scale staff"},
                {"label": "Concept Paper", "value": "3", "detail": "Draft Thunderforge → SAOC mapping"},
                {"label": "Strategy Decision", "value": "4", "detail": "SNC sub-tier vs. direct-to-PO"},
                {"label": "Go/No-Go", "value": "5", "detail": "Internal review by end of Q1"},
            ],
            "notes": "Five prioritized actions. Most critical is the DIU follow-up — if Thunderforge can be formally extended to target SAOC, that's the cleanest path. The go/no-go review at end of Q1 should assess whether relationship-building is yielding traction.",
        },

        # ── Closing ───────────────────────────────────────────────────
        {
            "layout": "title",
            "title": "Boston Harbor Islands",
            "subtitle": "SAOC Program Engagement · Scale AI\nAll content sourced from open-source intelligence",
            "notes": "Closing slide. This entire deck was built from OSINT — no classified or proprietary data was used. Data sources: SNC press releases, defense publications (The War Zone, The Aviationist, Defense Daily), HigherGov budget data, DIU Thunderforge announcement, and Air Force budget justification documents.",
        },
    ],
}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--theme", choices=["dark", "light"], default="dark")
    args = parser.parse_args()
    main(theme_name=args.theme, deck=DECK)
