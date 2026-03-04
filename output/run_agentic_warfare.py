#!/usr/bin/env python3
"""
Agentic Warfare — Scale AI Capabilities Pitch.
A vision deck for defense stakeholders: what happens when AI agents
operate at the speed of the fight.

Run from project root:
    python3 output/run_agentic_warfare.py
    python3 output/run_agentic_warfare.py --theme light
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from generate_deck import main

DECK = {
    "filename": "Agentic_Warfare_Capabilities",
    "slides": [
        # ── 1. Title ──────────────────────────────────────────────────
        {
            "layout": "title",
            "title": "Agentic Warfare",
            "subtitle": "When AI Operates at the Speed of the Fight · Scale AI",
        },

        # ── 2. The problem we solve ──────────────────────────────────
        {
            "layout": "content",
            "title": "Your Adversaries Don't Wait for Your Analysts to Finish Reading",
            "bullets": [
                "The OODA loop is a race — and manual intelligence fusion loses it",
                "Analysts drown in data while commanders starve for decisions",
                "Today's kill chain has human bottlenecks at every handoff",
                "Peer threats move at machine speed; we respond at meeting speed",
            ],
        },

        # ── 3. What agentic means ────────────────────────────────────
        {
            "layout": "two_column",
            "title": "Agentic Is Not a Buzzword — It's a Force Structure Change",
            "left_title": "Traditional AI",
            "left_bullets": [
                "Human asks a question, model answers",
                "One task, one prompt, one response",
                "Analyst stays in the loop at every step",
                "Speed limited by the slowest human handoff",
            ],
            "right_title": "Agentic AI",
            "right_bullets": [
                "Agent receives an objective, decomposes it, and executes",
                "Chains tools, queries sources, validates its own work",
                "Human sets intent and reviews outcomes",
                "Speed limited by compute, not coffee breaks",
            ],
        },

        # ── 4. Where we've proven it ─────────────────────────────────
        {
            "layout": "metrics",
            "title": "We're Not Pitching Theory — We're Fielding This Today",
            "metrics": [
                {"label": "Apps in Production", "value": "9", "detail": "SIPR, Donovan, cleared users"},
                {"label": "Analysts Served", "value": "200+", "detail": "Valley of Fire · Project ASCEND"},
                {"label": "RFI Response Time", "value": "Seconds", "detail": "Was hours — per analyst, per query"},
                {"label": "ATO Coverage", "value": "Active", "detail": "Continuous through Aug 2026"},
            ],
        },

        # ── 5. The capability stack ──────────────────────────────────
        {
            "layout": "content",
            "title": "Five Agents That Change How You Fight",
            "bullets": [
                "SIGINT Fusion Agent — Ingests multi-INT feeds, correlates across sources, surfaces patterns no analyst could find in time",
                "Threat Hunt Agent — Natural language RFI drafting with citations pulled from live knowledge bases",
                "CCIR Decision Agent — Evaluates incidents against commander's criteria and renders MET / NOT MET in real time",
                "Cyber IOC Agent — Extracts indicators of compromise and generates Splunk queries from raw threat reports",
                "Battlespace Risk Agent — Continuous site risk scoring with exportable heat maps and alert triggers",
            ],
        },

        # ── 6. How it actually works ─────────────────────────────────
        {
            "layout": "two_column",
            "title": "Human Intent, Machine Execution",
            "left_title": "What the Commander Says",
            "left_bullets": [
                '"Give me the threat picture for the eastern corridor"',
                '"What changed in the last 12 hours that I need to know?"',
                '"Draft the RFI response for the CCIR trigger"',
                '"Show me which sites are at elevated risk right now"',
            ],
            "right_title": "What the Agent Does",
            "right_bullets": [
                "Queries SIGINT, HUMINT, OSINT feeds; fuses; renders a brief",
                "Diffs overnight data across all sources; flags deltas",
                "Pulls citations, structures the response, cites sources",
                "Runs risk model, generates heat map, pushes to dashboard",
            ],
        },

        # ── 7. The Scale difference ──────────────────────────────────
        {
            "layout": "metrics",
            "title": "Why Scale — Not a Lab, Not a SETA, Not a Slideware Vendor",
            "metrics": [
                {"label": "Defense Data", "value": "30B+", "detail": "Labeled data points for DoD models"},
                {"label": "Cleared Staff", "value": "250+", "detail": "TS/SCI across 4 new offices"},
                {"label": "Production Agents", "value": "Fielded", "detail": "Not prototypes — mission systems"},
                {"label": "Model Expertise", "value": "Every LLM", "detail": "We trained the models you use"},
            ],
        },

        # ── 8. Architecture ──────────────────────────────────────────
        {
            "layout": "table",
            "title": "Deployed Architecture — Nothing Theoretical",
            "headers": ["Layer", "What It Does", "Where It Runs"],
            "rows": [
                ["Agent Orchestration", "Task decomposition, tool selection, self-validation", "SIPR / JWICS"],
                ["RAG Knowledge Base", "Real-time retrieval across IRs, PULSE, ACE, SIGACTS", "SIPR (Donovan)"],
                ["Model Layer", "Fine-tuned LLMs for defense-specific reasoning", "On-prem / IL-5+"],
                ["Data Connectors", "ServiceNow, Splunk, JWICS feeds, CSV/XML/JSON ingest", "Configurable"],
                ["Human Interface", "Natural language queries, dashboard, exportable products", "Web / Donovan"],
            ],
        },

        # ── 9. What this unlocks ─────────────────────────────────────
        {
            "layout": "two_column",
            "title": "The Difference Between Having AI and Having Agents",
            "left_title": "With AI (Today, Most Programs)",
            "left_bullets": [
                "Analyst queries a chatbot, gets a paragraph",
                "One question at a time, no memory between sessions",
                "Output needs human reformatting for every product",
                "Useful but not transformative — still analyst-limited",
            ],
            "right_title": "With Agents (What We Deliver)",
            "right_bullets": [
                "Commander states intent, agents execute across domains",
                "Persistent context — agents remember the mission",
                "Outputs formatted for Splunk, CCIR briefs, dashboards",
                "Transformative — analyst capacity multiplied 10x",
            ],
        },

        # ── 10. Engagement model ─────────────────────────────────────
        {
            "layout": "content",
            "title": "How We Get You From Here to Fielded in 90 Days",
            "bullets": [
                "Week 1–2: Mission mapping — we learn your data sources, workflows, and pain points on-site",
                "Week 3–6: Agent build — custom agents wired to your feeds, tested against your scenarios",
                "Week 7–8: Operator validation — your analysts stress-test, we iterate in real time",
                "Week 9–12: Authority to operate — security package, accreditation support, production cutover",
            ],
        },

        # ── 11. Closing ──────────────────────────────────────────────
        {
            "layout": "title",
            "title": "The Fight Won't Slow Down for You.\nYour Agents Won't Slow Down Either.",
            "subtitle": "Scale AI · Agentic Warfare",
        },
    ],
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Agentic Warfare capabilities pitch")
    parser.add_argument("--theme", choices=["dark", "light"], default="dark", help="Color theme")
    args = parser.parse_args()
    main(theme_name=args.theme, deck=DECK)
