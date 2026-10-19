---
name: event-publisher
skill_version: "1.42.0"
last_updated: "2026-10-19"
rule_count: 24
rules_file: references/event-rules.md
learning_log: LEARNING-LOG.md
github_repo: https://github.com/muhiussunnah/eventpublisherskills
description: >
  Automated event scraping and publishing to the Famies dashboard (dashboard.fammap.app).
  Use this skill whenever the user wants to scrape events from any Swedish municipality or event calendar website
  and publish them to the Famies dashboard. Triggers include: publishing events, scraping events, adding events
  to Famies, importing events from a website, event calendar automation, "publish events from [website]",
  "scrape [website] events", or any mention of the Famies dashboard combined with events. Also use when the user
  wants to update images, fix duplicates, bulk-add images to existing events, or manage events on the Famies dashboard
  (including via the admin API for large batches — see Rule #10). Also use when the user wants permanent family
  places (museums, swim halls, parks, farms, ski resorts) published as organizer → venue → recurring event.
---

# !! SESSION-START INTEGRITY CHECK (Rule #15) !!
# Before doing ANY Famies work, ALWAYS:
# 1. Read `references/event-rules.md` and count `## Rule #` headers.
# 2. Verify that count equals the `rule_count` field in this frontmatter above.
# 3. If mismatch, STOP. Tell the user: "Skill integrity check failed: expected N rules, found M. Don't proceed until we fix."
# 4. Only after integrity is confirmed, begin batch work.
# This prevents silent skill-file corruption from causing a session to run with stale or partial rules.
# NOTE (2026-10-14): event-rules.md has 24 `## Rule #` headers. Rule numbers are sparse
# (1–11, 10.5–10.7, 28, 51, 52, 59, 61–65), so the old "52" was the highest number, not the header count.

# Famies Event Publisher

Automate the process of scraping events from source websites (Swedish municipality calendars, event pages, etc.)
and publishing them to the Famies dashboard at https://dashboard.fammap.app/events.

Famies is a family app targeting parents with children aged 0–12 in Sweden. Every decision — which events to
publish, what images to use, how to describe things — should be made through the lens of "would a Swedish parent
scrolling for fun activities for their kids find this relevant and appealing?"

## Prerequisites (3 Things You Need)

To use this skill, you need exactly 3 things ready in your Chrome browser:

1. **Event Source URL** — The user provides the URL of the event calendar to scrape (e.g., `https://www.vallentuna.se/evenemang-och-upplevelser/evenemangskalender/`). Open this in a Chrome tab.

2. **Famies Dashboard (logged in)** — https://dashboard.fammap.app must be open in Chrome and you must be **already logged in**. Navigate to the Events section.

3. **ChatGPT (logged in)** — https://chatgpt.com must be open in Chrome and you must be **already logged in**. This is used for generating family-targeted images when needed.

All 3 must be open in separate browser tabs before starting. Use `tabs_context_mcp` to get tab IDs.

If any of these are not ready, ask the user to:
- Provide the event source URL
- Log in to dashboard.fammap.app
- Log in to chatgpt.com

## Core Workflow

For each event on the source website, follow this sequence:

### Step 1: Scrape the Event

Navigate to the source event page and extract:
- **Title** — Event name in Swedish
- **Description** — Full event description (rewrite concisely if very long)
- **Date(s)** — Start date, end date, time. Check for recurring dates
- **Venue** — Location name and address
- **Organizer** — Who is arranging the event
- **Image** — The event image (if any)
- **Price** — Free or paid (note the amount if paid)
- **Source URL** — The original event page URL (used for CTA link)

### Step 2: Check for Duplicates on Dashboard

Before creating any event, search the dashboard by title. Click the search input on the Events page and type part of the event title. Wait for results to filter (2 seconds).

- If the event already exists (published/active/upcoming) → **SKIP** — do not create a duplicate
- If not found → proceed to create

This is critical. Duplicates make the app look unprofessional and confuse users.

### Step 3: Evaluate Relevance (Rule #4)

Decide if this event belongs on Famies:

**PUBLISH** these:
- Events for children, teens, families, young adults (age 0–49)
- General community/culture events families could attend
- Events without a narrow senior-only audience

**SKIP** these:
- Events explicitly for seniors (50–60+ years): "senior träff", "pensionärsaktivitet"
- Irrelevant professional events: lawyer help, legal advice ("advokat"), advocacy
- Events where the target audience is clearly not families or children

When in doubt, publish — it's better to have a slightly broader selection than to miss good family events.

### Step 4: Prepare the Image (Rule #45 — Source First, ChatGPT Fallback)

The image is what parents see first when scrolling. It must feel family-relevant. **CRITICAL: ALWAYS try the source image FIRST before generating via ChatGPT.** Read `references/event-rules.md` Rule #45 for the full pipeline. The short version:

1. **FIRST: Fetch the source image** from the event detail page (og:image, article img, hero bg)
2. **Score it** with Rule #39 quality gate (blur + text + overall ≥ 0.80)
3. **If passes** → center-crop (Rule #35) → upload to CDN → DONE (no ChatGPT needed)
4. **If fails** (text-heavy, blurry, generic, no family connection) → generate via ChatGPT
5. **No image on source page** → Generate via ChatGPT
6. **Multiple events share the same image** → Keep original on one, generate unique images for others

ChatGPT is the FALLBACK, not the default. Most source images (~60-70%) pass the quality gate.

When generating images (fallback only), use this prompt format in ChatGPT:
```
authentic vertical 1:1 photo of Nordic children/families [engaging with the event activity in a way that feels warm and relevant to parents browsing a family events app]
```

The generated image must show kids and/or parents actively engaging with the topic — not just objects or scenery alone.

### Step 5: Prepare Organizer and Venue

Check if the organizer and venue already exist on the dashboard before creating new ones.

**Organizer:**
- Use the specific organizer from the source (e.g., "Bibliotek Vallentuna", "Kultur Vallentuna", "Vallentuna Kulturskola")
- Do NOT use generic names like "Vallentuna kommun" when a specific organizer is mentioned
- If no organizer is mentioned → use the source website name (e.g., "Vallentuna kommun")
- If organizer creation fails with email → try without email

**Venue:**
- Use the specific venue and address from the source
- Municipality selection is NOT needed on venue creation — skip it
- Interest category IS required on venue creation — select the most relevant one
- If no venue/address in source → use the source website name as venue

### Step 6: Create the Event on Dashboard

Click "+ Add Event" on the dashboard and fill in:

1. **Event Title** — From source
2. **Description** — From source (concise, informative)
3. **Image** — Upload the prepared image (see Step 4)
4. **Organizer** — Select existing or create new (see Step 5)
5. **Venue** — Select existing or create new (see Step 5)
6. **Date Range(s)** — Set start and end dates/times
   - For recurring events: create ONE event with multiple date ranges using "+ Add Date Range" button
   - Do NOT create separate events for each occurrence
7. **Pricing** — Set as free or enter the price
8. **CTA Text** — Set to "Läs mer"
9. **CTA Link** — Set to the source event URL
10. **Push Notification** — Turn OFF (default is ON, must be manually toggled off). **API route:** pass `shouldNotifyUsers: false` in the POST body and NEVER omit it — absence defaults push ON (this wrongly pushed a partner event on 2026-09-22). See `references/technical-patterns.md` → "Partner & Ongoing-Venue Events".

### Step 7: Publish

Click "Create Event" (or "Update Event" if editing). Verify the page redirects back to the events list, confirming success.

## Permanent Places → Events (Organizer → Venue → Recurring Event) — NEW 2026-10

Used when the user gives a list of **permanent family places** (e.g. the "Vad ska vi hitta på idag?" HTML with
embedded `places`, filtered by `region`) instead of a dated event calendar. Full API details:
`references/technical-patterns.md` → "Permanent Places Publishing". Runs: Gävleborg 2026-10-13
(`GAVLEBORG-PERMANENT-PLACES-FINAL-REPORT-2026-10-13.md`, 52 published), Södermanland 2026-10-18
(`SODERMANLAND-PERMANENT-PLACES-FINAL-REPORT-2026-10-18.md`, 40 published).

0. **New HTML version?** Find what is unpublished: compare places per region/kommun in the HTML with the app's place
   counts; only the regions (and stray places) that are missing get researched.
1. **Duplicate check first** — against ALL existing places, events and organizers (name tokens + places within
   ~1 km of the coordinates). Also catch duplicates inside the input list itself. Already-published → skip.
   Reuse existing operator orgs (Medley, Nordiska museet, kommun orgs) instead of creating look-alikes.
2. **Research each place** (parallel research subagents are fine): status (open/closed), real operator,
   legal/official organizer name, phone, generic email, website, Instagram/Facebook/YouTube, logo, exact address,
   OSM/official coordinates, opening hours + season, 2–3 real images from the official site / visit-site.
   The input list is a hint only — its coordinates, domains and names are often outdated.
3. **Organizer** — reuse if it exists (exact name match); otherwise create with as much verified info as
   possible + logo avatar. Kommun-run places → "X kommun" (isGovernment: true).
4. **Venue** — create with full address, coordinates, municipalityId (never null), per-day openingHours,
   interestId, website/phone/email/socials of the place.
5. **Event** — recurring: title "Platsnamn – kort beskrivning", Swedish description 300–650 chars from
   official facts only, `shouldNotifyUsers: false`, parent 18–100, child 0–18 (real minimum if the place sets one),
   2 interests, ctaText "Läs mer" + official ctaLink.
6. **Recurrence rule** — pick ONE time window that is genuinely open on every listed day (e.g. weekends close
   earlier → use the shorter window). Always-open outdoor places: 00:00 + 1439 min. Season over and next season
   not announced → copy the previous season's calendar span into next year and flag it in the report.
7. **Skip** when: closed to the public, no fixed hours AND no real visit option, no official source, or no real
   image of the place. Report every skip with the reason.
8. **Privacy** — only generic/business contacts. Never personal-name emails or private individuals' phones.
9. **Audit after publishing** — re-fetch all events of the region: no duplicate titles/images, municipality set,
   ages, recurrence, CTA, interests; visual contact-sheet check of every event image and avatar.

## Technical Patterns

Read `references/technical-patterns.md` for the detailed browser automation code patterns including:
- Image transfer between tabs (ChatGPT → tmpfiles.org → wsrv.nl proxy → dashboard) — for UI flow
- **Bulk publishing via Famies admin API** (GET / POST /admin/image / PATCH /admin/events) — for 10+ event batches, see Rule #10
- **Partner & ongoing-venue events (recurring restaurants/venues) via POST /admin/events** — push-safe CREATE (`shouldNotifyUsers:false`, omit `isPublished`), the recurring+past-start template, feed-visibility rules (per-city / age-chip / interests-don't-gate), and the `/admin/image` "Folder name not allowed" gotcha (reuse the place's S3 image). NEW 2026-09.
- **JWT extraction & cross-tab transfer** via char-code encoding (bypasses output content filter)
- **Three-call pattern per event** (send → wait 42s → finish) to stay inside the CDP 45s timeout
- ChatGPT rate-limit detection and 4-minute recovery pattern
- Programmatic file upload via JavaScript DataTransfer API
- Dashboard navigation quirks and fixes
- Search and edit workflows

## Image Prompt Formula

For any new image generation, use the **Rule #11 UGC 5-ingredient formula**:
Subject + Activity/Venue + Realism anchors + Light + Mood.
See `references/event-rules.md` Rule #11 for the full template and uniqueness rule (no two events in a batch share a prompt).
(Note: the existing Rule #9 in `event-rules.md` also covers Nordic UGC photo style — both rules are complementary.)

## Dashboard Navigation Tips

- **Direct URL navigation** to /events/edit redirects to /dashboard — always click "Events" in the sidebar instead
- **After saving an event**, the page redirects to /events but the search field gets cleared
- **Blank page bug**: Scrolling too far down on the edit page can cause a blank white page — fix with `window.scrollTo(0, 0)`
- **Search timing**: After typing in search, wait 2 seconds for results to filter before clicking any event's menu
- **Three-dot menu**: Click ⋮ → Edit to open an event for editing
- **Use `find` tool** to locate buttons like "Update Event" by ref, then `scroll_to` and click by ref — more reliable than coordinates

## Batch Processing

When scraping multiple events from a source calendar:
1. First, get a list of all events from the calendar page
2. For each event, open the detail page to get full information
3. Check for duplicates on dashboard before creating
4. Process events one by one, following the full workflow for each
5. Track which events were published, skipped (duplicate), or skipped (irrelevant)
6. Report a summary at the end
