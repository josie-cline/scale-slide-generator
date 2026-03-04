#!/usr/bin/env python3
"""Project ASCEND strategic roadmap deck — built from Google Drive docs."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from generate_deck import main

DECK = {
    "filename": "ASCEND_Strategic_Roadmap_OP2",
    "slides": [
        {
            "layout": "title",
            "title": "Project ASCEND\nOption Period 2 Strategy",
            "subtitle": "Valley of Fire  ·  HC1084-25-0001\nFebruary 15 – May 14, 2026",
            "notes": "Strategic roadmap for the 3-month OP2 period. Audience is internal Scale leadership plus DISA stakeholders. The goal is to move from prototype to production-ready posture.",
        },
        {
            "layout": "fact",
            "value": "200",
            "label": "Provisioned Users on SIPR",
            "detail": "Target: >40% weekly active users across DISA Mission Groups",
            "title": "Adoption is the metric that unlocks the Production OTA",
            "notes": "The single number that matters. We have 200 accounts provisioned — the question is whether we can convert them to active weekly users. >40% WAU is the threshold that gives Raleigh the proof he needs for the Production OTA conversation.",
        },
        {
            "layout": "metrics",
            "title": "Nine workflow applications are live — two advancing to v1",
            "metrics": [
                {"label": "Apps Delivered", "value": "9", "detail": "All operational on SIPR"},
                {"label": "v0 → v1", "value": "2", "detail": "IR Review + Intel Agent"},
                {"label": "Platform Uptime", "value": "99.9%", "detail": "ATO-C valid thru Aug 2026"},
                {"label": "Data Connections", "value": "+1", "detail": "ServiceNow integration"},
            ],
            "notes": "Status snapshot. 9 apps live, 2 being refined, platform stable, one new data connection in progress. The v1 refinements for Apps 5 and 9 are due within 14 days of contract award.",
        },
        {
            "layout": "process",
            "title": "OP2 has three parallel workstreams driving toward Production",
            "steps": [
                {"label": "Sustain", "detail": "Maintain 9 apps, 200 users, bug fixes, ATO compliance"},
                {"label": "Refine", "detail": "Apps 5 & 9 from v0 to v1 within 14 days"},
                {"label": "Prove", "detail": "5 user vignettes, ROI metrics, demo event by May 14"},
            ],
            "notes": "Not sequential — these run in parallel. Sustain is the baseline. Refine delivers the v1 upgrades. Prove generates the evidence Raleigh needs for the Production OTA. All three must succeed for OP2 to be considered a win.",
        },
        {
            "layout": "table",
            "title": "Each workstream has a clear owner and timeline",
            "headers": ["Milestone", "Lead", "Target Date", "Status"],
            "rows": [
                ["OP2 Kickoff", "All", "Feb 20, 2026", "Complete"],
                ["Apps 5 & 9 v1 delivery", "Tom Walsh (ENG)", "NLT 14 days post award", "In Progress"],
                ["Production Strategy Kickoff", "Raleigh Sims (GTM)", "Mar 15, 2026", "Upcoming"],
                ["ROI Impact Report", "Josie (Delivery)", "Apr 1, 2026", "Upcoming"],
                ["Expansion Roadmap", "ENG / GTM", "May 1, 2026", "Upcoming"],
                ["Final Prototype Demo", "Josie (Delivery)", "May 14, 2026", "Upcoming"],
            ],
            "notes": "Six milestones, three months. The critical path runs through the March 15 Production Strategy Kickoff — that's when Raleigh initiates the Mutual Close Plan with DISA leadership.",
        },
        {
            "layout": "two_column",
            "title": "Three functional teams, one shared objective: Production OTA",
            "left_title": "Who Owns What",
            "left_bullets": [
                "GTM (Raleigh): Stakeholder management, Production close plan",
                "ENG (Tom): App refinement, platform stability, data connections",
                "Delivery (Josie): User adoption, ROI evidence, demo execution",
            ],
            "right_title": "How They Connect",
            "right_bullets": [
                "ENG → Delivery: Stable apps for users to adopt",
                "Delivery → GTM: Proof-of-value metrics for close plan",
                "GTM → All: Clear definition of the Production finish line",
            ],
            "notes": "The interdependency model is the key insight. No team succeeds alone. Engineering delivers the product, Delivery proves it works, GTM closes the deal. If any leg breaks, the Production OTA stalls.",
        },
        {
            "layout": "quote",
            "quote": "Our collective goal should be to tie VoF initiatives to a Scale roadmap creating a flywheel of feature capabilities that are mutually beneficial.",
            "attribution": "ASCEND Strategic Roadmap",
            "notes": "Direct quote from the strategic roadmap document. This frames the transition from 'one-off prototype' to 'sustained platform relationship.' The flywheel metaphor is important — each OP should make the next one easier to justify.",
        },
        {
            "layout": "table",
            "title": "Key risks center on integration dependencies and scope definition",
            "headers": ["Risk", "Impact", "Mitigation"],
            "rows": [
                ["ServiceNow POC approval delayed", "Data connection slips", "Architecture diagrams submitted; TEM on POC designation"],
                ["v1 feedback not provided in time", "14-day delivery misses", "Request written feedback week 1; verbal capture via TEM"],
                ["Optional CLINs exercised late", "Scope can't fit in OP2 window", "Initiate JAD sessions in month 1"],
                ["SIPR performance under load", "User experience degrades", "Stress testing + infra coordination with Gov"],
            ],
            "notes": "Four risks, all mitigatable. The ServiceNow dependency is the highest-impact because it's the only deliverable entirely dependent on Government action (POC designation).",
        },
        {
            "layout": "content",
            "title": "The path from OP2 to Production OTA requires three proof points",
            "bullets": [
                "1.  Active user adoption above 40% WAU — proves the platform has mission pull",
                "2.  Documented ROI through 5+ user vignettes — gives DISA leadership the business case",
                "3.  Successful final demo for CTO-level stakeholders — creates the decision moment",
            ],
            "notes": "End with the strategic thesis. Three things must be true for Production to happen. If we deliver all three by May 14, the Production OTA conversation is a formality. If we miss any one, it becomes an uphill negotiation.",
        },
    ],
}

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--theme", choices=["dark", "light"], default="dark")
    args = parser.parse_args()
    main(theme_name=args.theme, deck=DECK)
