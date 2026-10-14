# Event Publisher Workflow Rules v5 — 2026-06-22

## CRITICAL META-RULE
**Never stop mid-city.** When user says "process [city]", complete ALL sources from the spreadsheet for that city + web search + final report in ONE session. Don't break into "next session" — that's a session-management mistake.

## Per-City Workflow (mandatory)

### 1. Setup
- Get JWT token from dashboard
- Get municipalityId, existing live events (status: ongoing+upcoming only — NOT past!)
- Build dup-check title set from live events only

### 2. Process EVERY source from spreadsheet
For each source URL listed for the city in Weekly_Events_Update sheet:
- Fetch source landing page
- Click "Visa fler"/"Show more"/pagination → 100% coverage, no missed events
- For each event:
  - Check title dup against live events (lowercase contains match on keyword)
  - Check date is active/upcoming only (today onwards)
  - Fetch event detail page → get image URL + clean description + dates + venue
  - Image quality check: text-heavy or low quality → ChatGPT-generated replacement
  - Hash check first 8KB of image for in-session dup prevention
  - Multi-date → bundle into single event with dates[] array
  - Publish via POST /admin/events with:
    - `municipalityId` (never null)
    - `placeId` + `lat` + `lng` + `address` (required for postgres earth_distance)
    - `title`, `description` (no JS/code, prose only, source-accurate, NO fabricated facts)
    - `images: [s3Url]` (single image)
    - `dates: [{startDate, endDate}, ...]` in "YYYY-MM-DD HH:MM:SS" format
    - `childMinAge: 0`, `childMaxAge: 17`
    - `parentMinAge: 18`, `parentMaxAge: 100`
    - `isFree`, `ctaLink`, `ctaText`
    - `shouldNotifyUsers: false` (push notifications OFF)

### 3. After all sources
- Web search for hidden/secret unique events not in standard sources
- Fetch + publish those too with same rules

### 4. Audit + Final report
- Verify all 52+ rules compliance for published events
- Fix any issues found before reporting (don't leave for later edit)
- Report: city, before count, after count, +N net, list of events published per source, rules verified

## API schema notes

### POST /admin/events body
```json
{
  "placeId": "string",
  "lat": 59.86,
  "lng": 17.63,
  "address": "string",
  "title": "string",
  "description": "string",
  "images": ["s3url"],
  "dates": [{"startDate":"YYYY-MM-DD HH:MM:SS","endDate":"YYYY-MM-DD HH:MM:SS"}],
  "childMinAge": 0,
  "childMaxAge": 17,
  "parentMinAge": 18,
  "parentMaxAge": 100,
  "isFree": true,
  "ctaLink": "https://...",
  "ctaText": "Mer info",
  "shouldNotifyUsers": false
}
```
**NO** `municipalityId` in body — it's derived from place
**NO** `eventId` — server generates

### POST /admin/image upload
- FormData with field name `image`
- Returns `data.image` (S3 URL, NOT `data.url`)

### Place lookup
- `/admin/places?limit=100&page=N` (no other params except limit/page)
- Paginate to find Uppsala municipality places
- For events without exact venue match, use closest central place (Stadsbiblioteket for Uppsala center, Upplandsmuseet for Gamla Uppsala/Disagården, etc.)

## Image rules
- Source image first (og:image from event detail page)
- If text-heavy / quality bad → ChatGPT generate (no external opensource sites)
- wsrv.nl proxy: `https://wsrv.nl/?url={src}&w=800&h=800&fit=cover&output=jpg`
- Hash first 8KB SHA-256 for dedup

## Description rules
- Source-accurate ONLY
- No fabricated dates, prices, opening hours, named features, activity counts
- No JS/code/HTML tags
- Clean prose, no bullet points
- 200-700 chars typical

## Title rules
- Match source page title where reasonable
- 60-90 chars typically
- No fabricated descriptors

## Date rules
- ONLY active/upcoming (today onwards)
- Multi-date → bundle dates[] array, not separate events
- Format: "YYYY-MM-DD HH:MM:SS" (no T, no Z)

## Dup check
- Against LIVE events only (ongoing + upcoming), NOT past
- Lowercase contains match on key word from title
