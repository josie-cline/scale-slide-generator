# Demo Walkthrough: Cradle to Grave

This guide walks through the complete workflow — from installing Cursor to holding a finished slide deck. Follow each step in order. Total time: ~5 minutes.

---

## Prerequisites

- macOS, Windows, or Linux
- Python 3.9+
- A GitHub account
- Internet connection

---

## Step 1: Install Cursor

1. Go to [cursor.com](https://cursor.com) and download the installer for your OS
2. Install and launch Cursor
3. Sign in with your account (GitHub SSO works)

> Cursor is a fork of VS Code with built-in AI. If you've used VS Code, the interface will be familiar.

---

## Step 2: Clone the Repo

Open Cursor's integrated terminal (`` Ctrl+` `` or `` Cmd+` ``) and run:

```bash
git clone https://github.com/josie-cline/scale-slide-generator.git
```

Then open the folder:
- **File > Open Folder** and select `scale-slide-generator`

Cursor automatically detects the `.cursor/rules/` directory. This gives the AI full context about the generators, commands, and project structure — no setup required.

---

## Step 3: Install Dependencies

In the terminal:

```bash
pip install -r requirements.txt
```

This installs `python-pptx` (PowerPoint) and `python-docx` (Word). No APIs, no databases, no complex setup.

---

## Step 4: Explore with Ask Mode

Before generating anything, use **Ask mode** to understand what's available.

### Switch to Ask mode

In the Cursor chat panel, click the mode selector and choose **Ask**.

### Example prompts

**Discover what's available:**

```
What generators does this project have and how do I use them?
```

The AI will explain both generators, their flags, and how to configure them.

**Plan your task:**

```
I need to create a roadmap for a new program. What do I need to configure?
```

The AI will walk you through `PROGRAM`, `QUARTERS`, `MONTHS`, `PHASES`, and `TASKS` — the five things you edit to define any roadmap.

**Understand themes:**

```
What themes are available and how do I add a custom one?
```

> **Why Ask mode?** It's read-only — the AI explores and explains without changing files. Use it to plan before you execute.

---

## Step 5: Generate a Roadmap (Agent Mode)

Switch to **Agent mode** (click the mode selector and choose **Agent**).

### Set up your program

**Prompt:**

```
Update the roadmap for my program. Here's the info:

Program name: Thunderbolt
Contract: HC1084-26-0042
Title: Project Roadmap: Phase 1 & 2
Period: Phase 1: Mar-Jun 2026 · Phase 2: Jul-Oct 2026

Quarters: Q1 2026, Q2 2026, Q3 2026, Q4 2026
Months: Mar, Apr, May, Jun, Jul, Aug, Sep, Oct

Phases: Onboarding, Development, Testing, Delivery

Tasks:
- Onboarding: Stakeholder engagement, Mar-Apr
- Onboarding: Data source identification, Mar-May
- Development: Core application build, Apr-Jul
- Development: Integration testing, Jun-Aug
- Testing: User acceptance testing, Jul-Aug, due 31 Aug 2026
- Delivery: Production deployment, Sep-Oct, due 15 Oct 2026
- Delivery: Documentation & training, Sep-Oct

Generate in both dark and light mode.
```

**What happens:** The AI updates `generate_roadmap.py` with your program data, then runs it twice — once for each theme.

### Open the results

```bash
open output/Thunderbolt_Roadmap_dark.pptx
open output/Thunderbolt_Roadmap_light.pptx
```

---

## Step 6: Make Changes

Instead of editing PowerPoint shapes by hand, describe what you want.

### Add a task

```
Add a milestone called "Kickoff Review" under Onboarding in the first month, due 15 Mar 2026. Regenerate both themes.
```

### Change dates

```
Move "User acceptance testing" to Aug-Sep and update the due date to 30 Sep 2026. Regenerate dark mode.
```

### Add a phase

```
Add a new phase called "Optimization" with one task: "Performance tuning" from Sep to Oct. Regenerate both themes.
```

---

## Step 7: Generate a Status Report

If you have a `.docx` template for your program's monthly status report:

**Prompt:**

```
I need to generate a monthly status report. My template is at templates/my_template.docx.
First inspect it so I can see the paragraph structure, then I'll tell you what to update.
```

The AI runs `--inspect`, shows you the structure, and you provide the updates.

---

## Step 8: Review and Deliver

```bash
# Open generated files
open output/Thunderbolt_Roadmap_dark.pptx
open output/Monthly_Status_Report.docx
```

The files are ready for presentation — no manual formatting needed.

---

## Time Comparison

| Task | Manual (PowerPoint) | With Cursor |
|------|-------------------|-------------|
| Create a roadmap from scratch | 2-3 hours | ~30 seconds |
| Update task dates and regenerate | 20-30 minutes | ~15 seconds |
| Generate both dark and light versions | Double the above | One extra prompt |
| Add a new task row with Gantt bar | 15-20 minutes | ~10 seconds |
| Generate a monthly status report | 1-2 hours | ~10 seconds |

---

## Tips for Effective Prompting

1. **Give all your program data up front** — name, contract, phases, tasks, and dates in one prompt
2. **Specify the theme** — Include "dark mode", "light mode", or "both themes"
3. **Be precise about changes** — Exact task names, date ranges, and due dates
4. **Ask the AI to regenerate** — It won't auto-run the script unless you say so
5. **Use Ask mode first** if you're unsure — it explains without modifying anything

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `ModuleNotFoundError: No module named 'pptx'` | Run `pip install -r requirements.txt` |
| Output file won't open | Close any existing copy of the file first |
| AI doesn't know about the generators | Make sure you opened `scale-slide-generator` as the workspace folder |
| Want a custom color theme | *"Add a 'navy' theme with dark navy headers and gold accents"* |
| Too many/few months in the table | Update `MONTHS` and `QUARTERS` to match your timeline |
