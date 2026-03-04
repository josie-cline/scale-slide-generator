#!/usr/bin/env python3
"""
Two decks that prove the generator is flexible, not templated.

Deck A: Executive strategy brief — tight, punchy, 6 slides.
Deck B: Customer onboarding walkthrough — narrative, visual, 8 slides.

Same Scale styling. Completely different structures.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from generate_deck import main


STRATEGY_BRIEF = {
    "filename": "Strategy_Brief_Physical_AI",
    "slides": [
        {
            "layout": "title",
            "title": "Physical AI Will Be\nScale's Largest Market",
            "subtitle": "Executive Strategy Brief  ·  February 2026",
            "notes": "This is a 5-minute read for the leadership team. No fluff, no filler. Every slide makes one argument.",
        },
        {
            "layout": "fact",
            "value": "$416B",
            "label": "Global Robotics Market by 2035",
            "detail": "4x growth from $108B today — faster than cloud, faster than SaaS, faster than mobile",
            "title": "The market is larger than anything we've pursued",
            "notes": "Lead with the number. The $416B figure comes from IDTechEx and multiple industry analyses. The comparison to cloud/SaaS/mobile growth rates makes it tangible.",
        },
        {
            "layout": "quote",
            "quote": "Data readiness, not model sophistication, is the bottleneck for physical AI.",
            "attribution": "Encord Series C announcement, February 2026",
            "notes": "This quote from our competitor's fundraise validates our thesis. They raised $60M specifically because the market agrees: data infrastructure is the constraint. If Encord sees it, the market sees it.",
        },
        {
            "layout": "two_column",
            "title": "We already own the hardest part of the stack",
            "left_title": "What physical AI needs",
            "left_bullets": [
                "Multimodal annotation (video + LiDAR + telemetry)",
                "RLHF for robot policy training",
                "Petabyte-scale data curation",
                "Sim-to-real validation pipelines",
            ],
            "right_title": "What Scale already has",
            "right_bullets": [
                "3D point cloud + video labeling (production)",
                "RLHF infrastructure (proven on LLMs)",
                "Data engine at petabyte scale",
                "AV sensor fusion pipelines",
            ],
            "notes": "The left column is the market requirement. The right column is our existing capability. The point: we don't need to build from scratch. The AV data engine IS a robotics data engine.",
        },
        {
            "layout": "process",
            "title": "Three bets, sequenced over 18 months",
            "steps": [
                {"label": "Extend", "detail": "Port AV pipeline to humanoid robots by Q3 2026"},
                {"label": "Differentiate", "detail": "Launch robot RLHF — no competitor has this"},
                {"label": "Scale", "detail": "Synthetic data layer on NVIDIA Cosmos by 2027"},
            ],
            "notes": "Three steps, not five. Not seven. Three. Each one builds on the previous. Extend is low-risk (reuse existing tech). Differentiate is the moat. Scale is the force multiplier.",
        },
        {
            "layout": "content",
            "title": "The ask: green-light the Physical AI Data Engine by end of Q1",
            "bullets": [
                "Staff a 5-person team to port the AV annotation pipeline to humanoid use cases",
                "Allocate $2M in engineering budget for H1 2026",
                "Designate a robotics design partner from the existing customer base",
                "Decision deadline: March 15, 2026",
            ],
            "notes": "End with a clear ask. Not 'let's explore this' — a specific team size, budget, timeline, and deadline. The leadership team should leave this meeting with a yes/no decision to make.",
        },
    ],
}


ONBOARDING_DECK = {
    "filename": "Customer_Onboarding_Guide",
    "slides": [
        {
            "layout": "title",
            "title": "Welcome to Scale",
            "subtitle": "Your onboarding guide  ·  Getting started in 30 minutes",
            "notes": "Warm, clear, no jargon. This deck is for a new customer who just signed. They need to feel confident, not overwhelmed.",
        },
        {
            "layout": "timeline",
            "title": "You'll be up and running in four steps over two weeks",
            "events": [
                {"date": "Day 1", "label": "Kickoff call", "detail": "Meet your team"},
                {"date": "Day 3", "label": "Environment setup", "detail": "Access + config"},
                {"date": "Week 1", "label": "First project", "detail": "Guided pilot"},
                {"date": "Week 2", "label": "Go live", "detail": "Production ready"},
            ],
            "notes": "Show the full journey upfront so they know what to expect. Four steps, two weeks. Simple and achievable.",
        },
        {
            "layout": "image_content",
            "title": "Your dedicated team is already assembled",
            "image": "assets/scale_logo_dark.png",
            "bullets": [
                "Customer Success Manager — your single point of contact",
                "Solutions Architect — designs your data pipeline",
                "Project Lead — manages delivery and quality",
                "Support channel — Slack or email, < 4hr response time",
            ],
            "image_position": "left",
            "notes": "Put faces to the relationship. The customer should know exactly who to call and how fast they'll respond.",
        },
        {
            "layout": "fact",
            "value": "< 4 hrs",
            "label": "Average Support Response Time",
            "detail": "Measured across all Scale customers in Q4 2025",
            "title": "We respond fast because your timeline matters",
            "notes": "Reinforce the support commitment with a real number. This builds trust early.",
        },
        {
            "layout": "content",
            "title": "Three things to do before your kickoff call",
            "bullets": [
                "1.  Confirm your project lead and technical point of contact",
                "2.  Share sample data (even a small set) so we can demo with YOUR content",
                "3.  Review the onboarding checklist we sent via email",
            ],
            "notes": "Give them homework. Three items, numbered, concrete. If they do these three things, the kickoff call will be productive.",
        },
        {
            "layout": "metrics",
            "title": "Here's what our customers typically achieve in the first 90 days",
            "metrics": [
                {"label": "Time to First Output", "value": "< 1 wk", "detail": "From kickoff to first delivery"},
                {"label": "Annotation Accuracy", "value": "98.5%", "detail": "Across all project types"},
                {"label": "Cost Reduction", "value": "40%", "detail": "vs. in-house labeling teams"},
            ],
            "notes": "Set expectations with real benchmarks. These aren't promises — they're what customers typically see. The 'typically' qualifier is important.",
        },
        {
            "layout": "quote",
            "quote": "We went from contract signing to production data in 9 days. I've never seen an enterprise vendor move that fast.",
            "attribution": "Director of ML, Fortune 500 customer",
            "notes": "Social proof. A real quote from a real customer. The specificity (9 days) makes it credible.",
        },
        {
            "layout": "content",
            "title": "Questions? Your Customer Success Manager is one message away",
            "bullets": [
                "Slack: #scale-support (we'll invite you on Day 1)",
                "Email: your-csm@scale.com",
                "Docs: docs.scale.com/onboarding",
                "Emergency: support@scale.com (24/7 monitored)",
            ],
            "notes": "End with contact info, not a generic 'thank you' slide. Give them every way to reach us.",
        },
    ],
}


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--theme", choices=["dark", "light"], default="dark")
    args = parser.parse_args()

    main(theme_name=args.theme, deck=STRATEGY_BRIEF)
    main(theme_name=args.theme, deck=ONBOARDING_DECK)
