# FamMap Event Publisher — Complete Training Memory (v4 FINAL)
## Last updated: 2026-05-27 (Rule #10.5 + #10.6 added)

This file contains ALL accumulated knowledge for the FamMap event publishing agent. Read this BEFORE any age classification or event publishing work.

**v4 update (2026-05-22):** Major session of 175+ corrections. Updated rules based on client feedback. childMinAge=1 now FORBIDDEN. Pricing trap, författarsamtal-is-adult, "hela familjen → 0,18", active event judgment all added.

**v4 update (2026-05-27):** Three CRITICAL new rules added.
- **Rule #10.5 (CORRECTED) — Image source priority: SOURCE FIRST, ChatGPT only as Fallback.** Use the real source-page image by default (clean photo, no text, reasonable quality, activity-relevant). Fall back to ChatGPT generation ONLY when source image fails quality gate (text-heavy poster, blurry, generic placeholder, missing). Unsplash/Pexels/Pixabay/opensource stock photos remain ABSOLUTELY FORBIDDEN — never use even as fallback.
- **Rule #10.6 — IN-DEPTH coverage per city.** Every city gets ALL official sources processed + tourism sites + church + venues + ticketmaster + WEB SEARCH for hidden events. Never stop at "a few events" — target 30-60 per active city or however many genuinely exist. Mandatory 10-step coverage checklist (see event-rules.md Rule #10.6).
- **Rule #10.7 — Complete city BEFORE reporting.** Do NOT pause mid-city to ask user questions. Complete all 10 sources end-to-end then deliver ONE consolidated final report. Final report MUST include: before/after counts, net new, total live events for the city, audit results, sources processed, remaining work.

---

## 1. API Reference

### Base URL & Headers
- Base: `https://api.fammap.app`
- Headers (always required):
  - `Platform: web`
  - `Version: 0.0.0`
  - `Authorization: Bearer <JWT>`
- Token retrieval: `window.__token = localStorage.getItem('auth_token')` on dashboard.fammap.app
- **Token expiry:** JWT expires after ~1 hour. Refresh page on dashboard to get new token.

### Endpoints
- List events: `GET /admin/events?page=X&limit=Y` → `data.events[]` (does NOT include childMinAge/childMaxAge — must fetch detail)
- Event detail: `GET /admin/events/{id}` → `data` (includes all fields)
- Patch event: `PATCH /admin/events/{id}` with full body
- Upload image: `POST /admin/image` with multipart/form-data

### Event statuses
- `upcoming` — scheduled future event
- `ongoing` — currently happening (multi-date)
- `past` — already finished
- `live` = upcoming + ongoing (what to audit for fixes)

### PATCH Body (ALL fields required):
```json
{
  "title": "...", "description": "...", "images": ["url1"],
  "dates": [{"eventDateId": "...", "startDate": "...", "endDate": "..."}],
  "placeId": "...", "lat": 0.0, "lng": 0.0,
  "childMinAge": 0, "childMaxAge": 18,
  "parentMinAge": 18, "parentMaxAge": 100,
  "isFree": true, "ctaLink": "..."
}
```

### Patch Function (tested & working):
```javascript
window.__doPatchFresh = function(id, newCm, newCM) {
  var x = new XMLHttpRequest();
  x.open('GET', 'https://api.fammap.app/admin/events/' + id, false);
  x.setRequestHeader('Authorization', 'Bearer ' + window.__token);
  x.setRequestHeader('Platform', 'web');
  x.setRequestHeader('Version', '0.0.0');
  x.send();
  if (x.status !== 200) return {ok:false, status: x.status};
  var d = JSON.parse(x.responseText).data;
  var body = {
    title: d.title, description: d.description, images: d.images,
    dates: d.dates.map(function(dt) { return {eventDateId: dt.eventDateId, startDate: dt.startDate, endDate: dt.endDate}; }),
    placeId: d.placeId, lat: d.lat, lng: d.lng,
    childMinAge: newCm, childMaxAge: newCM,
    parentMinAge: 18, parentMaxAge: 100,
    isFree: d.isFree, ctaLink: d.ctaLink
  };
  var px = new XMLHttpRequest();
  px.open('PATCH', 'https://api.fammap.app/admin/events/' + id, false);
  px.setRequestHeader('Authorization', 'Bearer ' + window.__token);
  px.setRequestHeader('Platform', 'web');
  px.setRequestHeader('Version', '0.0.0');
  px.setRequestHeader('Content-Type', 'application/json');
  px.send(JSON.stringify(body));
  return {ok: px.status === 200, status: px.status};
};
```

### API Quirks
- `shouldNotifyUsers: false` — ALWAYS include in POST requests
- `parentMinAge=18, parentMaxAge=100` — ALWAYS, no exceptions
- `municipalityId` — MUST NOT be null
- Rate limiting: Max ~50 synchronous XHR per JS execution block
- Sending null for childMinAge/childMaxAge → stores as 0,0 (broken). Use 18,18 for adult events.

---

## 2. Age Classification Rules — v4 FINAL (2026-05-22)

### Authoritative source
File: `Agent_System_Prompt_v4_FINAL.md` — THIS IS THE AUTHORITATIVE REFERENCE
File: `event-rules.md` — Rules #1-#11, #28, #51, #52, #59, #61-#65 (20 active rules)
**Removed in v4:** Rules #58 (deprecated) and #60 (revoked) — deleted from file 2026-05-22

### Core principle
**Read the FULL description carefully → decide.** No blanket rules. Every event = individual reading.

### FORBIDDEN values (v4)
- **childMaxAge=17** — NEVER. Use 18.
- **childMinAge=17** — NEVER.
- **childMinAge=1** — NEVER (NEW v4). Use 0 instead.

### Allowed values
- `childMinAge`: 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18
- `childMaxAge`: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18

### Four event types
| Type | childMin | childMax | When |
|---|---|---|---|
| A: Baby | 0 | 1 | Baby vocab (bebis, babybabbel, etc.) OR months pattern (0-12 mån) |
| B: Specific kid range | X (0+) | Y (1-18) | Description states explicit "X-Y år" (with 1→0, 17→18 substitution) |
| C: Family / hela familjen | 0 | 18 | "Hela familjen", "familjedag", community celebration |
| D: Adult-only | 18 | 18 | Vinprovning, författarsamtal, "Målgrupp: Vuxna", senior events |

### v4 Quick Reference Table

| Description signal | Tag |
|---|---|
| "Målgrupp: Vuxna" | 18, 18 |
| "bebisar", "babybabbel", "9-12 månader" | 0, 1 |
| "hela familjen", "familjedag" | 0, 18 |
| "barn 0-5 år" stated | 0, 5 |
| "barn 1-X år" stated | 0, X (childMinAge=1 → 0) |
| "barn 3-7 år" stated | 3, 7 |
| "13-19 år" stated | 13, 18 (17 → 18) |
| "från X år" | X, 18 |
| "åk 3 & 4" (or årskurs 3-4) | 9, 10 |
| "åk 8 till år 2 i gymnasiet" | 14, 18 |
| "fritidsgård" / "ungdomens hus" | 10, 16 |
| Konfirmation | 14, 15 |
| Vinprovning / stickkafé / sopplunch | 18, 18 |
| "Föreläser författaren" (even about kids) | 18, 18 |
| City walks / long focused activities | 8 or 10, 18 |
| Senior events (65+, pensionärer) | 18, 18 (or skip per Rule #4) |

---

## 3. Critical traps (mistakes from session 14-15)

### Trap 1: Pricing tier ≠ target audience
"Pris: barn 0-2 år gratis, barn 3-12 år 95 kr, vuxna 295 kr" — this is PRICING, not target.
Family lunch with this pricing → tag `0, 18` (family event), not `0, 2`.

### Trap 2: Lectures are adult events
"Föreläser författaren om barns upplevelser" — author lecture about kids = adult audience.
Tag `18, 18`. Topic doesn't change audience.

### Trap 3: "Free entry 0-14" trap
"Fri entré 0-14 år" for a city walk = PRICING for kids who'd come. But the actual activity is for older kids who can walk.
Use parent judgment: `10, 18` not `0, 14`.

### Trap 4: childMinAge=1 sneaking in
v4 rule: never tag 1. Always 0 if babies could attend.

### Trap 5: childMaxAge=17 sneaking in
v3 rule: never tag 17. Always 18.

### Trap 6: Don't extrapolate one rule to other events
Each event = read its own description. A rule that fits one event doesn't mean other similar-looking events get the same tag.

### Trap 7: "Hela familjen välkommen" on adult event
Marketing fluff doesn't change adult content (vinprovning, konstutställning, författarsamtal). Apply 5-Second Test.

---

## 4. Session History Summary

- **Sessions 1-10:** Built publishing pipeline, published events for 27 municipalities
- **Session 11:** Major age reclassification (v2.0 Type A/B/C/D system)
- **Session 12:** Rule #28 v3.0 "Read Like a Swedish Parent" — complete rewrite
- **Session 13:** Rule #60 disaster — wrongly converted X,17 to 0,17, then reverted 61 events
- **Session 14 (2026-05-21):** v3 FINAL implementation — childMaxAge=17 FORBIDDEN, patched 158 events
- **Session 15 (2026-05-22) — CURRENT:**
  - Patched 1 leftover Max-17 event (PUNKT)
  - Description-vs-tag scan: 65 events corrected (baby keywords, months, range mismatches)
  - 19 reverts (Group 4 → strict 0,X)
  - Swedish parent pass: 49 events corrected (hela familjen → 0,18, från X år, fritidsgård, etc.)
  - 27 events: childMinAge=1 → 0 (NEW rule)
  - 9 ambiguous events: nuanced parent-judgment fixes
  - 7 events re-checked after 1→0 sweep (Lådbilslandet, Bokklubb åk 3&4, Jag är barn jag svär, Barnrytmik 3-5, Morsdagslunch, Grillkväll, Extraöppet NPF)
  - Total: ~175 events corrected
  - v4 rules locked in: pricing trap, författarsamtal=adult, hela familjen→0,18, childMinAge=1 forbidden, active event judgment

---

## 5. Standing instructions

1. `shouldNotifyUsers: false` — ALWAYS on POST
2. `parentMinAge=18, parentMaxAge=100` — ALWAYS, agent doesn't set parent ages
3. `municipalityId` — MUST NOT be null
4. No duplicate images across events (use Rule #1)
5. Work source by source from spreadsheet
6. Follow ALL rules in event-rules.md (#1-#65)
7. No images with prominent text (Rule #3)
8. All images must show Nordic kids/families engaged (Rule #5 + #9)
9. Use 5-ingredient UGC image prompt formula (Rule #11)
10. **NEW v4:** Read description before any age decision. No blanket rules.

---

## 6. File Locations

- `event-publisher/references/event-rules.md` — ALL operational rules (#1-#65, v4 FINAL)
- `event-publisher/references/Agent_System_Prompt_v4_FINAL.md` — v4 FINAL age classification (authoritative)
- `event-publisher/references/TRAINING_MEMORY_v4_FINAL.md` — THIS FILE
- `event-publisher/references/Agent_System_Prompt_v3_FINAL.md` — DEPRECATED (kept for history)
- `event-publisher/references/TRAINING_MEMORY_v3_FINAL.md` — DEPRECATED (kept for history)

---

## 7. Pixabay IDs already used (DO NOT reuse)

436913, 8343273, 451438, 951000, 7945201, 6143052, 5524961, 589325, 3437942, 2406078, 5070481, 2313462, 4879243, 6603120, 3524649, 6981771, 2441849, 1822474, 7467503, 1497942, 108539, 6775216, 4116363, 419589, 2060093, 3691623, 751576, 2600954, 3101151, 4803151, 3833280, 14669, 5176235, 1386236, 942970, 2343558, 4894710, 2557396, 4287291, 5002636, 5159266, 996635, 813666, 2566854, 6583825, 9159715, 5098862, 4283401, 6483796, 2178857, 1705249, 8724340, 6008512, 2576017, 2985782, 1093758, 5987406, 1851483, 3038974, 4524838, 6917351, 4096410, 4092600, 1126136, 818459, 84628, 4783685, 5133657, 6688951, 4823341, 4000290, 10184748, 4045414, 933165, 4355886, 4838037, 5663393, 7674189, 5781096, 2434138, 7842864, 7424190, 3087585, 3187617, 3129361, 4793110, 2821600, 3050615, 4879861, 1576790, 116690, 3898440, 5348929, 8539958, 1850184, 1850109, 2159913, 9054709, 820272, 3917994, 5187375, 2432417, 3092026, 4468247, 2724442, 436498, 3187708, 6348164, 7255362, 1869616, 4200286, 4664313, 3396713, 246222, 3301195, 995779, 79632, 3994042, 7358064, 2606317, 1639327
