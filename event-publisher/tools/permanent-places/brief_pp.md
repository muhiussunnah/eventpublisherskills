# Research brief — permanent family places (Norrbotten, Västerbotten, Västernorrland, Jämtland, Gotland) for the Famies app

Famies is a Swedish family app (parents with kids 0–12). Each **permanent family place** (museum, swim hall, park,
farm, lekland, ski hill …) is published as **organizer → venue → one recurring event**. You do the research only;
publishing is done later by someone else from your JSON. **100 % accuracy: official facts only, never guess.**

Input: `group_<G>.json` = list of places from a client file: `{i, id, name, municipality, region, category, ageMin,
ageMax, description, contact{address,phone,website}, coordinates{lat,lng}, source, priceLevel, tags}`.
The client file is only a hint: its names, coordinates, domains and details are often outdated or wrong.

Today is **2026-11-18**. It is winter: most summer places are closed for the season now, ski places are about to open.

## For every place, find out (official website first, then the kommun / visit-site, then official socials)
1. **Status** — open to the public? Permanently closed, renamed, merged, under renovation, private only? Is it
   really a place a family can just visit (fixed opening hours or always open)?
2. **Organizer** = the operator/owner:
   - official or legal name; `isGovernment` true for kommun / region / state;
   - generic email only (info@, kontakt@, kommun@ …) — **never a named person's email**;
   - business/switchboard phone only — **never a private person's mobile**; leave null if only private numbers exist;
   - website, Instagram, Facebook, YouTube (official accounts only);
   - logo: a direct URL to the official logo image (png/jpg/svg/webp, the biggest you can find), or null.
   Naming rules:
   - kommun-run → `"<official kommun name>"` exactly as the kommun writes it (e.g. "Luleå kommun", "Umeå kommun",
     "Skellefteå kommun", "Sundsvalls kommun", "Östersunds kommun", "Kiruna kommun", "Härjedalens kommun" …;
     on Gotland the kommun is called **"Region Gotland"**), with the kommun's main email + switchboard.
     Use exactly the same organizer name, email and phone for every place of the same kommun;
   - chains → one organizer per location: "Leos Lekland Umeå", "O'Learys Luleå", "JumpYard Sundsvall", "Boda Borg Skellefteå" — with that location's own phone/email/website (never the chain's shared email);
   - swim halls run by Medley → organizer "Medley" (it exists already; just say `reuse: "Medley"`);
   - naturum / nature reserves run by a länsstyrelse → the länsstyrelse's name as it writes it, e.g.
     "Länsstyrelsen Norrbotten", "Länsstyrelsen Västerbotten", "Länsstyrelsen Västernorrland",
     "Länsstyrelsen Jämtlands län", "Länsstyrelsen i Gotlands län" (gov), same name + contact for all its places;
   - ski resorts run by SkiStar → one organizer per destination ("SkiStar Åre", "SkiStar Vemdalen");
   - museums owned by a region/foundation → the museum's own name or the foundation's legal name
     ("Stiftelsen …", "Föreningen …", "… hembygdsförening").
3. **Venue** — official title, street address with postcode and town, exact coordinates (official / OpenStreetMap),
   website, generic email, phone, socials, **opening hours per weekday** for the current or next season
   (`[{day:0-6 (0 = Sunday), open:"HH:MM", close:"HH:MM"}]`, several rows per day allowed, never across midnight;
   `null` if the place is always open, like a park or a viewpoint).
4. **Event** (what families see in the app):
   - `title`: `"<Place name> – <short family-friendly description>"`, Swedish, ≤ 100 characters
     (example: "Munktellmuseet Eskilstuna – traktorer och grävmaskiner att klättra i, simulatorer och lekhörna");
   - `description`: Swedish, **300–650 characters**, plain sentences (no lists, no markdown, no emoji, no prices
     that may change, no opening hours), only facts from official sources: what the place is and what kids and
     parents can do there;
   - `isFree`: true only when the official site says entry is free; unknown → false;
   - `childMinAge`: the real minimum age if the place sets one (e.g. 8+ escape room), else 0; `childMaxAge` 18;
   - `recurrence` `{days, startTime "HH:MM:SS", durationMinutes, startDate, endDate}`:
     * ONE time window that is genuinely open on **every** listed day (if weekends close earlier, use the shorter
       window); the venue keeps the full per-day hours;
     * always-open outdoor place → days [0,1,2,3,4,5,6], "00:00:00", 1439 minutes;
     * open year-round → startDate "2026-11-18", endDate "2027-12-31";
     * in season right now → startDate "2026-11-18", endDate = official season end;
     * hours published only for a limited period (e.g. "höstens öppettider t.o.m. 20 december") → endDate = that date;
     * if the window shared by ALL open days is shorter than ~3 hours, list only the days that share a real window
       (e.g. Mon–Fri 14–18) instead of a useless 60-minute window;
     * season over: next season officially announced → those dates; not announced → copy the 2026 season span into
       2027 and flag `seasonCopied: true`;
     * winter places (ski, ice rinks, sled hills with lifts) → the 2026/27 season with the official lift/opening
       hours per weekday. Season dates announced → use them; only last season's dates on the official site → copy
       them to 2026/27 and flag `seasonCopied`. A hill that only says "öppet när det finns snö / se Facebook" with no
       weekday hours on any official page → skip ("no published hours");
     * boats with a public timetable and tickets on board are fine (window = first departure → last return);
       boat trips that must be booked → skip;
   - `interestIds`: exactly 2 from: 9 Bebis & Du, 7 Familjeliv & Pepp, 1 Fira & Njuta, 11 Lär & Utforska,
     8 Lek & Fart, 2 Mat & Mums, 4 Mys & Hitta på, 6 Ses & Hitta på, 5 Tillgängligt för alla, 10 Utflykter & Kul,
     3 Ut & Upptäck. Conventions: museums [10,11], swim/action/ski [8,10], nature/parks/viewpoints [3,10],
     farms/animals [3,10] or [10,11];
   - `ctaLink`: the official page for visitors (not a search page), `ctaText` "Läs mer".
   - `venueInterestId`: one of the ids above (the main one).
5. **Images** — 2 to 4 direct URLs to **real photos of this place** from its official website, the kommun or the
   visit-site (no stock photos, no Unsplash/Pexels, no AI images, no Instagram/Facebook CDN links that expire).
   Best: kids/families using the place, bright, no text or logo painted on the image, at least ~800 px wide.
   Open each URL to check it really loads as an image (HTTP 200, image content-type). Put the best first.
6. **Skip** (set `skip` with the reason) when: permanently closed / renovation with no reopening date, not open to the
   public, no fixed hours and no real drop-in visit, not family relevant (adult-only, a church with no family offer,
   a hotel/spa), no official source at all, or no real photo of the place exists anywhere official.


## STRICT accuracy rules (CEO, 2026-11-05) — these override anything above
A museum complained that the app showed it as open while it had been closed for years. Every published fact must
come from an **official, current** source (the place's own site or the kommun/länsstyrelse page), not from Google
Maps, TripAdvisor, Airbnb, blogs or the client file. Add to every place:
`"evidence": [{"fact": "status|hours|season|price|address", "url": "...", "quote": "short quote from the page"}]`.
- **Status:** confirm the place is open now or in its normal season (look for "stängt", "renovering", "tillfälligt
  stängt", "öppnar igen", "säsongen är slut", news about closure/bankruptcy). Closed for renovation with a reopening
  date → publish only from the reopening date; no date → skip.
- **Hours:** read the official opening hours for EACH weekday. For swimming pools use public/family swim hours
  (allmänhetens bad, familjebad, äventyrsbad), not lap swim or school time. Never use template hours. If the official
  page has no hours at all → skip ("no published hours").
- **Season:** seasonal places publish only their season. A short closure (< 6 weeks) inside the span → publish the
  longer open period. Next season not announced → copy the 2026 season into 2027 and flag `seasonCopied`.
- **Not drop-in → skip:** theatres, concert halls, cinemas (performance/screening only), escape rooms, booking-only
  tours, farms or rides, conference hotels, "by appointment" museums.
- **isFree:** true only if entry is free for everyone (free museum, library, park, nature reserve, beach, playground,
  monument, town walk). False if adults pay (even when children are free), and false for restaurants, cafés-as-the-
  activity, bowling, play centres, swimming, go-kart.
- **Links:** open the website and ctaLink; a dead domain or a page that now shows casino/spam content is not
  official → find the real one or skip.
- **Address:** the real visiting address and coordinates of THIS place (not the kommun office, not another branch).

## Output — write as you go
File: `<scratchpad>\pp3\res_<G>.json`
Re-write the whole file with Python `json.dump(data, f, ensure_ascii=False, indent=1)` after **each** place. A list of:
```
{"i": 12, "name": "<client name>", "skip": null | "reason",
 "org": {"name", "reuse": null | "<existing org name>", "isGovernment", "email", "phone", "website", "instagram",
         "facebook", "youtube", "logo"},
 "venue": {"title", "address", "lat", "lng", "municipality", "website", "email", "phone", "instagram", "facebook",
           "youtube", "openingHours": [...] | null, "venueInterestId"},
 "event": {"title", "description", "isFree", "childMinAge", "childMaxAge": 18, "recurrence": {...},
           "interestIds": [a, b], "ctaLink", "ctaText": "Läs mer"},
 "images": ["https://…", "…"],
 "sources": ["https://…"], "flags": ["seasonCopied", "hours unclear", …], "note": "short free text",
 "verified": "2026-11-18"}
```
Coordinates must be inside Sweden (lat 55–69.1, lng 11–24.2) and at the place itself. `venue.municipality` must be the
kommun name exactly as in the input (Gotland → "Gotland").

Working rules:
- At most **12 WebSearch calls** in total; use WebFetch / curl on the official sites for everything else.
- Keep your own scratch files in `<scratchpad>\pp3\w<G>\` (create it); write nothing else outside it except `res_<G>.json`.
- Places that are booked by nature (husky/sled-dog tours, rafting, riding tours, guided mine or cave tours, via
  ferrata, theatres, opera) need only a quick look at the official page: if there is no drop-in visit with published
  hours → skip with a one-line reason, don't spend more time on them.
- If the official site blocks scripts and you had to read a web.archive.org copy, add the flag `"wayback"` and the
  live URL in `note`, so the publisher can check the live page. If the official site is offline and no other official
  page (kommun, länsstyrelse, region) confirms current hours → skip.
- Two input items that are the same place → research once, skip the other with "duplicate of #<i>".
- Never state hours, dates or prices in `description` (they change); do say when something must be booked.

Use WebSearch / WebFetch / curl / Python only. Do not use any browser tools and do not touch the Famies dashboard,
the API or the Google Sheet. Never put a private person's name, email or mobile number in any field.

## Reply when done — SHORT (max 12 lines)
Per place: `i name → ok | skip (reason)`, then anything the publisher must know (shared organizers, flags).
