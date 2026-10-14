# Event Publisher Agent — Memory v4.8
**Last consolidated:** 2026-06-05
**For:** New session continuity. Read this BEFORE any Famies publish/edit work.

> **You are the same agent who built this file.** Continue exactly as before. No fresh assumptions, no re-learning. The user is **Famies** (chaos.and.lovefam@gmail.com), FamMap workspace admin. He speaks Banglish (Bengali in Latin script) and prefers warm, addressed-as-"bondhu" replies.

---

## 0. ABSOLUTE NON-NEGOTIABLES (READ FIRST EVERY SESSION)

| # | Rule | Failure mode if broken |
|---|---|---|
| A | **No image = no publish.** Skip event entirely if no real unique image available. | App looks unprofessional; user complaint |
| B | **No duplicate images** across events or sessions. Maintain `window.__sessionHashes` for in-session dedup. | "Bondhu duplicate dilo" — must re-PATCH |
| C | **No duplicate titles.** Search dashboard before publish. Catch semantic duplicates too (e.g., "Midsommar på X" vs "Midsommarfirande på X"). | Have to DELETE post-publish |
| D | **municipalityId must NOT be null.** Always pull placeId tied to correct municipality. | Event invisible / wrong city |
| E | **Multi-date → 1 event** with `dates[]` array. Never separate events for same activity. | Feed feels spammy |
| F | **Only active/upcoming dates** (≥ today). Skip past events. | Junk in feed |
| G | **shouldNotifyUsers: false** on every POST. Push notifications OFF. | Users get spam push |
| H | **Image upload filename** must match `campaign.{ext}-{Date.now()}` pattern. Backend rejects others. | Upload returns non-200 |
| I | **Uploaded image must be > 5000 bytes.** Anything smaller = placeholder/error. Skip. | Broken image card |
| J | **Clean prose descriptions.** No JS, no inline code, no markdown bullets. Plain sentences. | Pollutes UI |
| K | **ctaLink → direct event page**, NEVER a search URL. If only artist-page available with multiple shows, use artist page (user can pick). | User clicks "Läs mer" → useless search results |
| L | **Source image first** (Rule #10.5). ChatGPT/opensource is FALLBACK only when source bad/blurry/text-heavy/missing. | Lazy ChatGPT use everywhere |
| M | **In-depth coverage** per city (Rule #10.6). Click "Visa fler", paginate all pages, web search related sources for bonus venues. Don't quit at 3 events. | User pushes back: "only 3ta?" |
| N | **Complete city before reporting** (Rule #10.7). Write `{city}-FINAL-report-{date}.md` only after all sources processed + rule audit run. | Premature claim of "done" |
| O | **Confirm 100% rules before publish** — not edit-after. One-by-one, not batch-then-fix. User explicitly said: "perfectly 1ta 1ta kore koro setai valo 500 eksathe kore pore abar sob edit korar chaite". | Endless cleanup PATCHes |
| P | **parentMinAge: 18, parentMaxAge: 100** on every event. childMinAge/Max per actual target. | Wrong demographic |

These rules sit on top of `references/event-rules.md` (the full 52-rule manual). Read this section every session start, then full rules file if needed.

---

## 1. SESSION STARTUP CHECKLIST

```
[ ] 1. Read this file (agent-memory-v4.8.md)
[ ] 2. Read references/event-rules.md (count = 52 rules; fail-fast if mismatch)
[ ] 3. Identify the user's actual ask (city deep-dive? fix bug? sheet update? client urgent?)
[ ] 4. Open dashboard.fammap.app/dashboard in a Chrome tab
[ ] 5. Verify auth: localStorage.getItem('auth_token') exists
[ ] 6. If token expired → ask user to re-login, wait
[ ] 7. Cache: window.__token, window.__cityMunId, window.__cityPlaces, window.__sessionHashes = {}
[ ] 8. Install city-specific publish helper window.__publishCity(opts)
[ ] 9. Use TaskCreate for the user's request as task #N
[ ] 10. Begin work — and use TaskUpdate liberally as work progresses
```

If the user opens with a continuation ("ekta city DEEP DIVE shuru koro"), assume the same ruleset they keep repeating. Don't ask them to re-state it.

---

## 2. CRITICAL CODE PATTERNS

### 2.1 Token retrieval

```javascript
window.__token = localStorage.getItem('auth_token');
// If null → user must log in. Don't try to fake it.
```

Token expires periodically. If you get `430 Token has expired` mid-publish:
1. Ask user to reload dashboard + log back in
2. Wait for "login done" confirmation
3. Re-cache token, then resume publish

### 2.2 City setup boilerplate

```javascript
// Run once per city. Cache everything.
(async () => {
  var hdrs = {'Authorization':'Bearer '+window.__token,'Platform':'web','Version':'0.0.0'};
  // Find municipality
  var mr = await fetch('https://api.fammap.app/admin/municipalities?page=1&limit=200', {headers: hdrs});
  var md = await mr.json();
  var mun = (md.data && md.data.municipalities || []).find(function(x){return x.name === 'CITY_NAME';});
  window.__cityMunId = mun.municipalityId;
  // Load places
  var pr = await fetch('https://api.fammap.app/admin/places?page=1&limit=100&municipalityId='+window.__cityMunId, {headers: hdrs});
  var pd = await pr.json();
  window.__cityPlaces = pd.data.places;
  window.__sessionHashes = window.__sessionHashes || {};
  return {munId: window.__cityMunId, placeCount: window.__cityPlaces.length};
})();
```

### 2.3 Publish helper (THE workhorse — adapt city name)

```javascript
window.__publishCity = async function(opts){
  var hdrs = {'Authorization':'Bearer '+window.__token,'Platform':'web','Version':'0.0.0'};
  var titleLc = opts.title.toLowerCase().trim();

  // 1. Title dedup check (across 3 pages of 100)
  for (var p=1; p<=3; p++) {
    var sr = await fetch('https://api.fammap.app/admin/events?page='+p+'&limit=100&isEnd=false&municipalityId='+window.__cityMunId, {headers: hdrs});
    var sd = await sr.json();
    var evs = (sd.data && sd.data.events) || [];
    if (evs.find(function(e){return e.title.toLowerCase().trim() === titleLc;})) return {skipped:'duplicate'};
    if (evs.length < 100) break;
  }

  // 2. Fetch image via wsrv.nl (cross-origin proxy, also normalizes format)
  var wsrv = 'https://wsrv.nl/?url=' + encodeURIComponent(opts.imgUrl) + '&w=800&h=800&fit=cover&output=jpg';
  var imgResp = await fetch(wsrv);
  var imgBlob = await imgResp.blob();
  if (imgBlob.size < 5000) return {err: 'image too small', size: imgBlob.size};

  // 3. SHA-256 hash → in-session dedup
  var hashBuf = await crypto.subtle.digest('SHA-256', await imgBlob.arrayBuffer());
  var hashHex = Array.from(new Uint8Array(hashBuf)).slice(0,8).map(function(b){return b.toString(16).padStart(2,'0');}).join('');
  if (window.__sessionHashes[hashHex]) return {err: 'session-duplicate-image', dupOfTitle: window.__sessionHashes[hashHex]};
  window.__sessionHashes[hashHex] = opts.title;

  // 4. Upload (filename MUST follow campaign.{ext}-{ts})
  var file = new File([imgBlob], 'campaign.jpg-'+Date.now(), {type:'image/jpeg'});
  var fd = new FormData(); fd.append('file', file);
  var upResp = await fetch('https://api.fammap.app/admin/image', {method:'POST', headers: hdrs, body: fd});
  if (upResp.status !== 200) return {err:'upload failed', status: upResp.status};
  var newS3 = (await upResp.json()).data.image;

  // 5. Build body
  var body = {
    title: opts.title, description: opts.description, images: [newS3],
    dates: opts.dates,           // [{startDate:'YYYY-MM-DD HH:mm:ss', endDate:'...'}]
    placeId: opts.placeId, lat: opts.lat, lng: opts.lng,
    childMinAge: opts.childMinAge, childMaxAge: opts.childMaxAge,
    parentMinAge: 18, parentMaxAge: 100,
    isFree: opts.isFree !== undefined ? opts.isFree : true,
    ctaLink: opts.sourceUrl, ctaText: 'Läs mer',
    shouldNotifyUsers: false
  };
  var postResp = await fetch('https://api.fammap.app/admin/events', {method:'POST', headers: Object.assign({'Content-Type':'application/json'}, hdrs), body: JSON.stringify(body)});
  return postResp.status === 200 ? {DONE: true, title: opts.title, imgBytes: imgBlob.size, hash: hashHex} : {fail: postResp.status};
};
```

### 2.4 PATCH event (for fixes — ctaLink, dates, image, etc.)

```javascript
// CRITICAL: when patching dates, reuse existing eventDateId from the GET response
// otherwise API returns 400 "must have required property 'eventDateId'"
var body = {
  ctaLink: '...',
  dates: [
    {eventDateId: 6755, startDate: '2026-10-18 11:00:00', endDate: '2026-10-18 12:00:00'},
    {eventDateId: 6756, startDate: '2026-10-18 14:00:00', endDate: '2026-10-18 15:00:00'}
  ]
};
await fetch('https://api.fammap.app/admin/events/' + eventId, {method:'PATCH', headers: {...hdrs, 'Content-Type':'application/json'}, body: JSON.stringify(body)});
```

### 2.5 DELETE event (for semantic-duplicate cleanup)

```javascript
await fetch('https://api.fammap.app/admin/events/' + eventId, {method:'DELETE', headers: hdrs});
// Returns 200 on success.
```

### 2.6 Soleil CMS body image extraction (lidingo.se, botkyrka.se, huddinge.se etc.)

These sites' fetch-via-DOMParser returns only icon SVGs because images are JS-rendered. You MUST navigate to the full URL in browser tab, wait ~5s, then query rendered `img` tags:

```javascript
(async () => {
  await new Promise(r => setTimeout(r, 5000));
  var imgs = Array.from(document.querySelectorAll('img'))
    .filter(i => i.naturalWidth >= 300 && !/lyssna|lattlast|skrivut|logo|icon/i.test(i.src))
    .map(i => ({src: i.src, w: i.naturalWidth}));
  return imgs;
})();
```

### 2.7 fetch() + DOMParser pattern (for non-JS sites)

```javascript
var r = await fetch('https://example.com/event-page');
var html = await r.text();
var doc = new DOMParser().parseFromString(html, 'text/html');
var ogImg = (doc.querySelector('meta[property="og:image"]')||{}).content;
```

Cross-origin fetch works because Famies dashboard is the running origin and most municipal sites allow it. wsrv.nl is the safe fallback for image fetches that need proxying.

### 2.8 Spreadsheet write technique (Google Sheets via computer tool)

TAB key types literal tab character (does NOT move column). Use one of:
- **Column-by-column** typing: navigate to A2, paste column A via newlines; then B2 for column B; then C2 for column C
- **Name Box** (cell ref input at top-left, coordinate ~37,103): click → type cell ref → Enter → type values with \n
- **Clipboard paste**: write TSV to clipboard via JS, then Ctrl+V into A2 (TSV splits into cells correctly)

---

## 3. RECENT LEARNINGS & ERROR FIXES

### 3.1 Semantic duplicate detection (Lidingö session, 2026-05-30)

Title check by exact-lowercase-trim misses semantic duplicates. After publishing 16 Lidingö events, audit revealed 5 were duplicates of pre-existing events with slightly different wording:

| New (mine) | Existing baseline |
|---|---|
| "Midsommar på Hustegaholm – traditionellt firande på Lidingö" | "Midsommarfirande på Hustegaholm" |
| "Sveriges nationaldag på Millesgården i Lidingö" | "Nationaldagsfirande på Millesgården" |
| "Alla vänners dag i Lidingö stadshus" | "Alla vänners dag på Lidingö stadshus" (only "i" vs "på") |
| "Rörelsebucklan: Motorikbanan i Högsätra för alla" | "Rörelsebucklan: Motorikbanan" |
| "Sommarutställning – Vägen till Centrum på Lidingö stadshus" | "Sommarutställning – Vägen till Centrum" |

**Lesson:** Before publishing, also check whether your candidate title starts with / is similar to any existing title (Levenshtein distance, or substring match in either direction). If 80%+ overlap → it's a duplicate, find the existing one and update IT instead of creating new.

### 3.2 ctaLink must NOT be a search URL (Babblarna fix, 2026-06-05)

User complaint: "ei 2tar source link e gele to oi specific event open hoy na". Babblarna Täby + Nacka events had ctaLink = `https://www.ticketmaster.se/search?q=Täby` instead of direct event URL.

**Fix:**
- If artist has only 1 show in city → ctaLink to direct event page `/event/.../1234567`
- If artist has multiple shows → ctaLink to artist page `/artist/.../982832` (user can pick)
- Never search URL

Also discovered Nacka event had wrong date (2026-11-07) when actual show is 2026-10-18 11:00 + 14:00. PATCHed dates using existing eventDateId values.

### 3.3 Image-hash collision for shared placeholders (Lorien Trio, Lidingö)

Millesgården entryevent.se serves the SAME 200,275-byte default event image for multiple concerts when they lack individual posters (Vårkonsert Orkesterakademi + Lorien Trio = identical hash). Session hash dedup correctly skipped Lorien Trio. Same pattern seen with Arena library systems (axiell placeholder), Botkyrka kommun logo on text-only events, etc.

### 3.4 Cross-municipality image collision (Parkteatern Huddinge/Danderyd, 2026-05-30)

Parkteatern Sjödalsparken (Huddinge) used same `parkteatern_press.jpg` (177,511 bytes) as Parkteatern Kvarnparken (Danderyd). Hash check caught it. PATCHed Huddinge to use unique Sjödalsparken nackrosdammen og:image (105KB).

**Lesson:** Hash dedup should span ALL cities in the session, not just current city.

### 3.5 Soleil CMS empty og:image (Lidingö Source 1)

fetch() against `lidingo.se/.../evenemang/{slug}.html` returns HTML with empty `<meta property="og:image">` and only icon SVGs. Images are JS-injected after page load. **Must navigate browser tab to the URL, wait 5s, then querySelector('img')**.

### 3.6 visitlidingo.se / Arena bibliotek lack per-event images

Pattern: aggregator sites + library Arena systems don't have unique images per event. Detail pages return generic site og:image or no image. **Per Rule A: no image = no publish from this source.** Move on to other sources for that city.

### 3.7 Token expired mid-publish (Centrumfestivalen, 2026-05-30 client urgent)

API returned `430 Token has expired` during upload. User reloaded dashboard, logged back in, then I successfully published with refreshed token. **Pattern:** if any non-200 status with "expired" in body, halt + ask user.

### 3.8 Wrong placeId for off-list venue (Centrumfestivalen)

Published Centrumfestivalen at Åkersberga Centrum but used "Åkersberga kyrkliga centrum" placeId because the actual mall wasn't in `__cityPlaces`. **Lesson:** When venue isn't in cache, search `places?searchKey=...` first or create new place via `/admin/places` POST before publishing event.

### 3.9 Soleil sites use lidingo.se/images/200.{id}/{ts}/{slug}.{ext} pattern

Image URLs from Soleil CMS look like `https://lidingo.se/images/200.62b03fb619e241caec7104/1779197125979/Midsommar%20p%C3%A5%20Hustegaholm.png`. They're stable, CDN-served, and cross-origin-friendly via wsrv.nl.

### 3.10 Cirkus Brazil Jack tour pattern

Multi-city tour with unique event-detail URLs per stop. Always prefer direct stop URL (e.g., `cirkus-brazil-jack-lidingo-gronsta-garde-biljetter/147565637`) over artist page when only 1 show per city.

---

## 4. CITY STATUS TABLE (as of 2026-06-05)

| City | Live count | Status | Net new this run | Notes |
|------|---|---|---|---|
| Stockholm | 158 | ✅ FULL | — | Kulturhuset, Junibacken, Skansen, Tekniska, Vasamuseet processed |
| Uppsala | 121 | ✅ FULL | — | Upplandsmuseet, UKK, destinationuppsala bonus |
| Vallentuna | 73 | ✅ FULL | — | Rule #10.6 in-depth applied |
| Österåker | 65 | ✅ FULL + Centrumfestivalen | +1 | Client urgent published 2026-05-30 |
| Botkyrka | 55 | ✅ FULL DEEP DIVE | +12 | Hågelbyparken bonus |
| Upplands-Bro | 51 | ✅ FULL | — | |
| Nacka | 49 | ✅ FULL | — | (Babblarna ctaLink + dates fixed 2026-06-05) |
| Upplands Väsby | 46 | ✅ FULL | — | Sigma + Wij + Hembygd bonus |
| Järfälla | 45 | ✅ FULL DEEP DIVE | +17 | upplevjarfalla.se citybreak images |
| Solna | 42 | ✅ FULL | — | |
| Sigtuna | 40 | ✅ FULL DEEP DIVE | — | 13 events after rewrite |
| Vaxholm | 37 | ✅ FULL | — | |
| Nynäshamn | 35 | ✅ FULL | — | |
| Lidingö | 31 | ✅ FULL DEEP DIVE | +16 | TAL R, Cirkus Brazil Jack, Lidingö 100 år events |
| Täby | 31 | ✅ FULL | — | (Babblarna ctaLink fixed 2026-06-05) |
| Södertälje | 30 | ✅ FULL | — | Tom Tits, Torekällberget |
| Norrtälje | 27 | ✅ FULL | — | |
| Haninge | 27 | ✅ FULL | — | |
| Sollentuna | 26 | ✅ FULL | — | |
| Nykvarn | 26 | ✅ FULL DEEP DIVE | — | Taxinge slott, Vidbynäs |
| Salem | 25 | ✅ FULL DEEP DIVE | — | |
| Huddinge | 25 | ✅ FULL DEEP DIVE | +12 | Parksommar, Tickster jazz |
| Värmdö | 24 | ✅ FULL | — | ChatGPT image fallback used |
| Danderyd | 21 | ✅ FULL DEEP DIVE | +9 | Parkteatern Kvarnparken bonus |
| Sundbyberg | 18 | ✅ FULL | — | Marabouparken |
| Ekerö | 12 | partial | — | Not yet deep-dived |
| Tyresö | 13 | partial | — | Not yet deep-dived |

**Sheet:** `https://docs.google.com/spreadsheets/d/10LqkGw7IbEupkSeFvTjoPI8nY-4Go8Rf3YkjwP9m4bY/edit?gid=0`
- Sheet "Events_Update" = per-city totals
- Sheet "Ticketmaster" = filtered list of all live ticketmaster.se events (13 as of 2026-06-05)

**Total live events:** ~1,121 (last full count 2026-05-30)

---

## 5. SOURCE-TYPE PLAYBOOK

| Source kind | Approach | Image source | Gotchas |
|---|---|---|---|
| Kommun website (Soleil CMS) | Navigate browser, wait 5s, querySelector img | Body image (lidingo.se/images/200...) | og:image often empty, must use rendered DOM |
| Arena library (bibliotek.*.se) | Visit event detail | None — shared placeholder | Per Rule A: skip unless event has unique image |
| Tickster (theater) | og:image on detail page | citybreak.com CDN | Usually unique per show |
| Ticketmaster | og:image + artist page tour listing | s1.ticketm.net | Use direct event URL not search URL (Rule K) |
| Facebook | Login required | — | Skip unless user logs in |
| evenemang.se | Cloudflare blocks bot | — | Skip |
| svenskakyrkan.se | Per-parish kalendarium | Usually no images | Often empty, only 1-2 events visible |
| Hembygdsförening | hembygd.se/{city} | og:image on news posts | Good for ongoing exhibitions |
| Web search bonus | WebSearch then web_fetch | Venue's own site og:image | Always do — Rule #10.6 |

---

## 6. SHEET UPDATE PROTOCOL

Per-city count update: column-by-column typing, click Name Box → type cell ref → Enter → type values with \n.

Date formatting: per user preference (2026-06-05) → English ordinal style "27th June", "20th June, 21st June" (NOT ISO dates). Use this function:

```javascript
function ord(n){ if (n%100>=11 && n%100<=13) return n+'th'; var s=n%10; return n+(s===1?'st':s===2?'nd':s===3?'rd':'th'); }
var months = ['January','February','March','April','May','June','July','August','September','October','November','December'];
function fmt(iso){ var p=iso.split('-'); return ord(+p[2])+' '+months[+p[1]-1]; }
```

---

## 7. COMMUNICATION STYLE WITH FAMIES

- Address as **"bondhu"** throughout
- Mix Banglish + English naturally — he writes Banglish, replies are warmer that way
- Be concise after finishing work. Bullet-summary of what was done + link to file/sheet
- Don't over-explain — he's an admin, knows the system
- When something fails, own it: "vul kora hoise, fix korci"
- Use ✅ ⚠️ ⏸ markers in city status tables and final reports

---

## 8. RULES OF THUMB FOR EDGE CASES

| Situation | Decision |
|---|---|
| Event ends today | Still publish if user could attend today |
| Title in English vs Swedish? | Match the source language (usually Swedish) |
| Description is poster image with no text | Skip per Rule A (no image alternative) |
| Multi-date with one cancelled date | Bundle only non-cancelled dates |
| Two events same title same day diff venue | Two events (different placeId) — not dups |
| Venue not in __cityPlaces | Create via POST /admin/places before publishing |
| Source says "fri entré" | isFree: true |
| Source says price | isFree: false, but no price field in API — note in description |
| User asks "x city DEEP DIVE shuru koro" | Default to in-depth (Rule #10.6): Sources 1-8 + web search bonus + final report |
| User says "publish hoise?" mid-session | Quick API count check before answering |
| Cross-session image collision risk | Always run hash check across ALL cities, not just current |

---

## 9. WHAT NEW SESSION SHOULD DO FIRST

When session starts:
1. Read `agent-memory-v4.8.md` (this file) — operational baseline
2. Read `references/event-rules.md` — full 52 rules (verify count)
3. Read `references/Agent_System_Prompt_v4_FINAL.md` — original v4 prompt for context
4. Read `references/TRAINING_MEMORY_v4_FINAL.md` — older training memory
5. Ask user what specifically they need (city deep-dive? bug fix? sheet? urgent client?)
6. Create TaskCreate for it
7. Use the city setup boilerplate (§2.2) for the target city
8. Begin work — and TaskUpdate liberally

**Don't re-derive any of these patterns. Don't re-discover Soleil CMS image extraction. Don't re-test the Babblarna ctaLink mistake. Read this file, follow the patterns, deliver.**

---

## 10. KNOWN PENDING WORK (carry over)

| ID | Status | What |
|---|---|---|
| #144 | pending | Fix duplicate-image cluster: keep 1 original, regenerate unique ChatGPT/source images for rest (21 of 27 remaining) |
| #145 | in_progress | Generate fresh ChatGPT images for 27-event placeholder cluster (6 of 27 done) |
| Ekerö | pending | Hasn't been DEEP DIVE'd — at 12 events |
| Tyresö | pending | Hasn't been DEEP DIVE'd — at 13 events |

---

## 11. APPENDIX — Spreadsheet IDs & API constants

```
Weekly_Events_Update sheet ID: 10LqkGw7IbEupkSeFvTjoPI8nY-4Go8Rf3YkjwP9m4bY
  - Events_Update gid: 0
  - Ticketmaster gid: 857559120

FamMap API base: https://api.fammap.app
  - GET /admin/events?page=N&limit=100&isEnd=false&municipalityId=X
  - GET /admin/events/{eventId}  (returns full detail incl. ctaLink, dates, etc.)
  - POST /admin/events (create)
  - PATCH /admin/events/{eventId} (update — reuse eventDateId for dates!)
  - DELETE /admin/events/{eventId}
  - POST /admin/image (multipart, file field name 'file')
  - GET /admin/places?municipalityId=X
  - GET /admin/municipalities?page=1&limit=200

Required headers: Authorization, Platform: web, Version: 0.0.0
  - JSON requests add: Content-Type: application/json
  - Multipart uploads: do NOT set Content-Type (browser auto-sets boundary)
```

---

## 22. v4.9 RECENT LEARNINGS (2026-06-29 / 2026-06-30)

### 22.1 POST /admin/events — dates field uses startDate/endDate (NOT startTime/endTime)
**CRITICAL.** Earlier sessions used `startTime`/`endTime`. As of 2026-06-30 the API only accepts:
```javascript
dates: [{ startDate: '2026-07-01 10:00:00', endDate: '2026-08-31 17:00:00' }]
```
Wrong format returns `400 / "Query error, code 42703"` (Postgres column not found).
- Format: `YYYY-MM-DD HH:MM:SS` (space, not T separator)
- One entry per recurring date if event repeats
- Past dates → skip event entirely (active/upcoming only)

### 22.2 No `municipalityId` in POST body
The body must NOT include `municipalityId` field — backend derives it from `placeId`. Including it returns:
`400 / "/body must NOT have additional properties"`

Minimum body shape:
```javascript
{ placeId, lat, lng, address, title, description, images: [url],
  dates: [{startDate, endDate}], childMinAge, childMaxAge,
  parentMinAge: 18, parentMaxAge: 100, isFree, ctaLink, ctaText,
  shouldNotifyUsers: false }
```

### 22.3 childMaxAge = 18 for ALL-AGES venues (NEVER 17)
**Already documented in `RULE-LEARNING-all-ages-cMax18-2026-06-29.md`** but reinforced here:
- The app renders cMax=17 as "**Max 17 år**" which makes badplats/parker/naturreservat look kid-only.
- Apply 18 for: badplats, simhall, naturreservat, park, festival, café, kyrka, slott, museum, utställning, opera, teater, konsert, gårdsbutik, vandring, bibliotek, kulturhus, lekplats (general), Skogsmulle spår.
- Use 17 ONLY for explicit kids-only: sport-camp, art-camp, cirkus-camp, simskola, småbarn sagostund, fritidsgård, tjejläger.

Audit pattern used 2026-06-30:
```javascript
// Fetch all 1259 live → fetch detail → filter cMax===17 → keyword-classify
// keepKeys = /tonår|ungdom|för\s+\d+-1[567]|9-13|10-15|13-19|fritidsgård|...
// rest → PATCH childMaxAge=18 via Promise.all batching of 20
```
Result: **237 events** fixed in one pass across all 27 cities + Uppsala.

### 22.4 PATCH /admin/events/{eventId} for partial updates
Single field update:
```javascript
await fetch(`https://api.fammap.app/admin/events/${id}`, {
  method: 'PATCH', headers: hdrs,
  body: JSON.stringify({ childMaxAge: 18 })
});
```
Works for any single field. Returns `{success:true, traceId}`.

### 22.5 Weekly_Events_Update sheet — current row mapping
Sheet ID: `10LqkGw7IbEupkSeFvTjoPI8nY-4Go8Rf3YkjwP9m4bY`, gid 0, tab `Events_Update`.

Column layout:
- A: City Name (one entry per city, alphabetical)
- B: Total Amount (live event count)
- C: Last Updated (YYYY-MM-DD)
- D: No of Sources
- E: Source URL (one URL per row — cities span multiple rows in E/F)
- F: City tag for that URL

Row order is fixed alphabetical:
2=Botkyrka, 3=Danderyd, 4=Ekerö, 5=Haninge, 6=Huddinge, 7=Järfälla, 8=Lidingö,
9=Nacka, 10=Norrtälje, 11=Nykvarn, 12=Nynäshamn, 13=Österåker, 14=Salem,
15=Sigtuna, 16=Södertälje, 17=Sollentuna, 18=Solna, 19=Stockholm, 20=Sundbyberg,
21=Täby, 22=Tyresö, 23=Upplands-Bro, 24=Upplands Väsby, 25=Vallentuna,
26=Värmdö, 27=Vaxholm, 28=Uppsala, 29=Events (SUM row, manual value)

Update via URL `?gid=0&range=B2` to navigate, then computer-use `type` with newline-separated values (Enter auto-advances to next row in Sheets).

### 22.6 Token rotation mid-session
Long sessions: token expires → POST returns `430` not `401`. Refresh by `navigate` to `https://dashboard.fammap.app/dashboard`, re-grab `localStorage.getItem('auth_token')`, retry failed batch.

### 22.7 Image rule reinforcement (2026-06-29 client feedback)
Storvretsbadet incident: bathing event image was Mediterranean villa pool → client said "looks weird when images are not relevant" → Nordic-looking images required. For Swedish municipality events use:
- Unsplash queries: `swedish summer pool nordic`, `swedish badplats lake`, `swedish forest hike`, `swedish midsummer`, `nordic playground`
- For ChatGPT-generated: prompt explicitly with "Nordic light, Swedish countryside, Scandinavian aesthetic"
- Avoid: Mediterranean/Tropical/tropical-villa/US-suburban look on Swedish nature/bathing events

### 22.8 Current city status snapshot 2026-06-30
All 27 cities + Uppsala completed Round 5 deep-dive. Total live = **1259 events**. Per-city counts in spreadsheet. Round 5 added **+403 events** vs Round 4 baseline. Folder cleaned (`_archive-historical-reports/` holds the historical FINAL reports per city per round).

---

*End of memory v4.9. If reading this for the first time in a new session: ack the user briefly that memory is loaded, then ask what they need. Don't recap this file unprompted.*
