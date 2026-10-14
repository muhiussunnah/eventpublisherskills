# Event Publisher Skill for Claude

Automatically scrape events from Swedish municipality calendars and publish them to the [Famies](https://famies.app) dashboard — all powered by Claude.

This skill teaches Claude how to browse event websites, extract event details, generate family-friendly images, and publish everything to your Famies dashboard with one simple command.

---

## What Does This Skill Do?

When you give Claude a Swedish event calendar URL, it will:

1. **Scrape** every event (title, date, description, venue, organizer, image)
2. **Check for duplicates** on your Famies dashboard so nothing gets posted twice
3. **Filter out irrelevant events** (senior-only meetups, legal consultations, etc.)
4. **Generate beautiful images** via ChatGPT when the source image is not family-friendly
5. **Create the event** on your Famies dashboard with all details filled in
6. **Set the CTA** ("Läs mer") linking back to the original event page

No coding required. Just talk to Claude.

---

## Folder Structure

```
eventpublisherskills/
  event-publisher/
    CLAUDE.md                         # Session bootstrap: what to read first + end-of-session protocol
    SKILL.md                          # Main skill instructions (calendar events + permanent places)
    LEARNING-LOG.md                   # Dated training log — every new lesson is added here
    agent-memory-v4.9.md              # Operational memory (rules, code patterns, city status)
    *-FINAL-REPORT-*.md               # Reports from each run
    references/
      image-rules.md                  # Image selection decision tree
      technical-patterns.md           # Browser/API patterns (incl. Permanent Places Publishing)
      event-rules.md                  # Event filtering and exception rules
    _archive-historical-reports/      # Older per-city reports
  eventscounter/                      # Companion skill: count live events per city
```

## Quick setup on a new computer

```bash
git clone https://github.com/muhiussunnah/eventpublisherskills.git
mkdir -p my-project/.claude/skills
cp -r eventpublisherskills/event-publisher my-project/.claude/skills/
cd my-project && claude
```

Then ask Claude to read `event-publisher/CLAUDE.md` first. After each session Claude adds what it learned to
`LEARNING-LOG.md` and the skill files, and pushes the changes back to this repo — `git pull` to get the latest.

---

## How to Install (Step by Step)

### Option A: Using Claude Code (Terminal)

If you use [Claude Code](https://docs.anthropic.com/en/docs/claude-code) from your terminal, follow these steps:

**Step 1 — Clone this repo**

Open your terminal and run:

```bash
git clone https://github.com/muhiussunnah/eventpublisherskills.git
```

This downloads the skill files to your computer.

**Step 2 — Copy the skill folder to your Claude project**

Claude Code looks for skills in a `.claude/skills/` folder inside your project. Copy the `event-publisher` folder there:

```bash
# Go to your project folder (or create one)
mkdir -p my-project/.claude/skills

# Copy the skill
cp -r eventpublisherskills/event-publisher my-project/.claude/skills/
```

Your project should now look like this:

```
my-project/
  .claude/
    skills/
      event-publisher/
        SKILL.md
        references/
          image-rules.md
          technical-patterns.md
          event-rules.md
```

**Step 3 — Start Claude Code**

```bash
cd my-project
claude
```

That's it! Claude will now automatically detect and use the event-publisher skill when you ask it to publish events.

---

### Option B: Using Claude Desktop (Cowork Mode)

If you use [Claude Desktop](https://claude.ai/download) with Cowork mode:

**Step 1 — Download the skill files**

Download this repository as a ZIP file:
- Click the green **"Code"** button on this GitHub page
- Click **"Download ZIP"**
- Unzip the downloaded file

**Step 2 — Open a folder in Cowork**

In Claude Desktop (Cowork mode), click the folder icon to select a working folder on your computer. Place the `event-publisher` folder inside:

```
your-selected-folder/
  .claude/
    skills/
      event-publisher/
        SKILL.md
        references/
          image-rules.md
          technical-patterns.md
          event-rules.md
```

**Step 3 — Start chatting**

Claude will automatically pick up the skill. Just ask it to publish events!

---

## Before You Start: 3 Things You Need

Before asking Claude to publish events, make sure these 3 things are ready in your Chrome browser:

| # | What | Why |
|---|------|-----|
| 1 | **Event source URL** open in a tab | The website Claude will scrape events from |
| 2 | **Famies Dashboard** logged in at `dashboard.famies.app` | Where events get published |
| 3 | **ChatGPT** logged in at `chatgpt.com` | For generating family-friendly images |

All three must be open in separate Chrome tabs.

---

## How to Use: Example Commands

Once the skill is installed and your 3 tabs are ready, just tell Claude what you want in plain language:

**Scrape and publish all events:**
```
Publish all events from https://www.vallentuna.se/evenemang-och-upplevelser/evenemangskalender/ to the Famies dashboard
```

**Publish a single event:**
```
Publish this event to Famies: https://www.vallentuna.se/evenemang/sommarlovsfest/
```

**Fix an image on an existing event:**
```
Replace the image on "Fira nationaldagen" with a family-friendly one showing kids celebrating
```

**Check for duplicates:**
```
Check if "Kreativt skrivande" already exists on the Famies dashboard
```

**Batch process a whole calendar:**
```
Scrape all upcoming events from Vallentuna kommun and publish each one to Famies. Skip duplicates.
```

Claude handles everything automatically — scraping, duplicate checking, image generation, and publishing.

---

## Key Rules Claude Follows

The skill has built-in rules to keep the Famies app high quality:

- **No duplicates** — Claude always searches the dashboard before creating
- **Family-first images** — Images must show kids/families, not just objects or scenery
- **Smart filtering** — Senior-targeted or irrelevant events are skipped
- **Specific organizers** — Uses real organizer names (not just "Vallentuna kommun")
- **No push spam** — Push notifications are turned OFF for every event
- **Source linking** — Every event links back to the original page via "Läs mer"

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Claude says "I don't have the skill" | Make sure the `event-publisher` folder is inside `.claude/skills/` in your project |
| Dashboard page goes blank | Claude knows to scroll back to top — just ask it to retry |
| Image upload fails | Claude uses a proxy (wsrv.nl) to handle this — it will retry automatically |
| Organizer creation fails | Claude will try without email field — this is a known dashboard quirk |
| Claude navigates to wrong page | Dashboard is a SPA — Claude uses sidebar clicks instead of direct URLs |

---

## Want to Customize?

You can edit any of the reference files to change Claude's behavior:

- **`event-rules.md`** — Change which events get filtered out
- **`image-rules.md`** — Change image selection criteria
- **`technical-patterns.md`** — Update automation patterns if the dashboard UI changes
- **`SKILL.md`** — Modify the core workflow

---

## Credits

Built by the [Famies](https://famies.app) team for automating Swedish family event discovery.

Made with Claude.
