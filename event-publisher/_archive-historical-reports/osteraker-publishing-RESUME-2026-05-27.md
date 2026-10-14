# Österåker Publishing — RESUME HANDOFF
**Last session:** 2026-05-27
**Status:** Discovery complete, form started for first event, ready for full execution next session

## Quick context
User wants to publish events for Österåker (current count: 13, target: many more). 7 sources to process source-by-source. Each event must be unique (search first), have an image, have municipalityId, push notifications OFF, free/paid set correctly, multi-dates combined into ONE event.

## Critical Reference Data

### Municipality
- Name: Österåker  
- **municipalityId: 172600240455582882**

### Existing 13 Events (DO NOT DUPLICATE)
1. Bokcirkel för barn
2. Tisdagsklubben
3. Vi möts – dialog med näringslivet i Österåker
4. Horisonten – för dig med funktionsnedsättning
5. Möt studie- och yrkesvägledare från KCNO
6. Slöjdfröjdig mönsterskärning och karvsnitt
7. Sagan om den lilla farbrorn
8. Barnens Dag på Länsmansgården
9. Lyssna på en novell
10. Advokatjour
11. Bokcirkel på lätt svenska
12. Handarbetsverkstad
13. Talbokscirkel

### 7 Sources (process in order)
1. https://www.osteraker.se/arkivevenemangkrisochinfo/evenemang.4.592cfecd176fc0db87818e.html ← **CURRENT** (18 events scraped, see below)
2. https://bibliotek.osteraker.se/evenemang#/
3. https://evenemang.se/se/stockholms-l%C3%A4n/%C3%B6ster%C3%A5ker
4. https://publicakersberga.se/evenemang/
5. https://www.facebook.com/osterakerskommun/events/
6. https://www.svenskakyrkan.se/kalender?q=%C3%96ster%C3%A5ker
7. https://www.ticketmaster.se/search?q=%C3%96ster%C3%A5ker

## SOURCE #1 events scraped (18 unique, click "Se fler" for more)
See `osteraker-source1-events-2026-05-27.md` for full URLs & descriptions.

### TO PUBLISH (14 new + 1 multi-date)
1. Nätverksfrukost för företagare (27 maj, 07.30-09.30) — adult 18,18 — Restaurang Å Åkersberga Golfklubb
2. NY PLATS: Vi möts – dialog med näringslivet i Österåker (27 maj, 08.30-09.15) — adult 18,18 — Espresso House Åkersberga *(possibly publish as separate or skip — similar to existing)*
3. Anhöriggrupp för dig som har en partner med neurologisk sjukdom (27 maj, 10.30-12.00) — adult 18,18 — Åkersberga Fyren
4. Drop in för vägledning (27 maj, 13.00-15.00) — adult 18,18 — Åkersberga Centrum
5. Kom och prata framtidens Österåker med oss (28 maj, 11.00-14.00) — adult 18,18 — Åkersberga
6. Nya bygglovsregler – kom och ställ dina frågor på Ljusterö (28 maj, 15.00-) — adult 18,18 — Ljusterö
7. Linedance och öppen dans på Ekbacken (28 maj, 18.00-21.30) — adult 18,18 — Ekbacken
8. Campfire i Båthuset på Runö Möten & Events (29 maj, 17.00-23.00) — adult 18,18
9. Campfire med livemusik i Båthuset på Runö Möten & Events (29 maj, 17.00-23.00) — adult 18,18
10. **Morsdagsbrunch på Runö Möten & Events** (31 maj, 11.30-14.00) — **family 0,18** — STARTED in form, title+description filled
11. Slöjdalster och fika på Norrö (31 maj, 12.00-15.00) — family 0,18 — Tingshuset Norrö
12. Tävling i hundkapplöpning (30 maj, 13.00-15.00) — family 0,18 — Åkers Kanal Greyhound
13. Digital vägledning (30 maj, 11.00-14.30) — adult 18,18 — Österåkers bibliotek
14. Operasångerska lär oss ta höga C på Ljusterö (30 maj, 13.00-15.00) — adult 18,18 — Ljusterö
15. **Konsert: Klang i kristallen – nytt datum** (31 maj, TWO times 15.00-16.15 + 19.00-20.20) — adult/family — Åkersberga Bibliotek — **MULTI-DATE: combine to 1 event with 2 date ranges**

### Skip (already published)
- Slöjdfröjdig mönsterskärning och karvsnitt
- Horisonten – för dig med funktionsnedsättning
- (Check "NY PLATS: Vi möts" — basically the same as existing "Vi möts – dialog med näringslivet")

## Workflow per event (use Dashboard UI)
1. Open event detail page on osteraker.se tab
2. Extract: title, full description, dates, times, place, image URL, price
3. Switch to dashboard `/events` tab, search title (no duplicate found → proceed)
4. Click + Add Event button
5. Fill Event Title
6. Fill Description (paste/type from source)
7. Upload Event Image:
   - Click + in Images
   - Either upload from disk (download image first) OR use ChatGPT-generated UGC if source image has text/poor quality
8. Select/create Event Venue (typically autocomplete on the venue dropdown)
9. Search Location (city/area) on map
10. Click + Add Date Range — set start/end date+time (multi-date → click + again for additional ranges)
11. Toggle Free Event OFF if paid (default ON)
12. **Toggle Send Push Notification OFF** (default ON — MUST OFF)
13. Set CTA Link: source event URL
14. Set age range (find field, default 0-18 or set per v4 rules)
15. Click "Create Event"
16. Verify redirect back to /events

## Standing rules (v4 FINAL)
- shouldNotifyUsers: false (Send Push Notification toggle OFF)
- parentMinAge: 18, parentMaxAge: 100 (default)
- municipalityId: 172600240455582882 (set in venue)
- No duplicate images across events
- No images with prominent text (Rule #3)
- Search title before publishing
- Only active/upcoming dates  
- Multi-date → single event with date array
- Age tags per v4 (0,18 family / 18,18 adult / specific ranges)

## API discovery progress
- POST /admin/events: requires placeId (BigInt string), full body. Discovered required fields but exact schema not fully reverse-engineered.
- DOES NOT accept: shouldNotifyUsers, municipalityId at root level (got "additional properties" error). These come from venue/place.
- For bulk batches: PATCH after UI creation may be better
- POST /admin/image: works with magic filename `event.jpg-{Date.now()}` (proven during ethnic-mismatch fix work)

## ✅ EVENT 1/15 PUBLISHED
**Morsdagsbrunch på Runö Möten & Events** — ID 370471327129175405
- Published: YES, Upcoming, 31 May 2026 11:30-14:00
- Venue: Österåkers kommun (placeholder — actual venue Runö Möten & Events doesn't exist yet, would need creation flow)
- Image: Source image from osteraker.se, uploaded via wsrv.nl proxy
- Ages: 0-18 (family Mother's Day brunch)
- Free Event: OFF (paid 365 kr/adult, 195 kr/kid)
- Push Notification: OFF ✓
- CTA: Läs mer → source URL

## 🔑 Proven Workflow (per event, ~15 tool calls)
1. **Scrape source detail page** (osteraker.se tab): title, description, dates, times, image URL
2. **Image transfer**: Use `wsrv.nl/?url=<src>` proxy in dashboard tab to fetch image without CORS, then inject via DataTransfer to file input
3. **Open create form**: Navigate /events → click + Add Event
4. **Fill text fields**: Title, Description (via clicks + type)
5. **Inject image**: Run JS to fetch via wsrv.nl + DataTransfer trick
6. **Pick venue from dropdown**: Click venue field, search "Österåkers", pick best match. Note: many specific venues don't exist; using `Österåkers kommun` as fallback
7. **Set lat/lng**: After venue picked, lat/lng auto-set
8. **Add Date Range**: Click + Add Date Range → click date in calendar → set times via JS (native setter on `input[type="time"]`) → click Add Date Range
9. **Toggle Free Event** OFF if paid (default ON)
10. **Toggle Send Push Notification** OFF (critical, default ON)
11. **CTA Link** + CTA Text "Läs mer"
12. **Set Children Max Age**: Click slider handle → press End key (extends to 18 for family events)
13. **Click Create Event** → wait → redirect to /events

## Key technical tricks discovered
- **wsrv.nl proxy**: `https://wsrv.nl/?url=<encoded source URL>` bypasses CORS for image fetch
- **DataTransfer**: `var dt=new DataTransfer(); dt.items.add(file); input.files=dt.files; input.dispatchEvent(new Event('change',{bubbles:true}))`
- **Native setter for time inputs**: `Object.getOwnPropertyDescriptor(HTMLInputElement.prototype,'value').set.call(input, '11:30')`
- **Slider keyboard**: Click handle → press End/Home/Arrow keys (custom sliders use ARIA role="slider" with valuenow/valuemin/valuemax)

## Limitations / Notes
- New venues require organizer creation (separate API flow), so for now using closest existing venue
- For exact venue match per source, could create venues batch via Venues admin page later
- Date picker requires clicking date AFTER setting times (clicking time inputs deselects date)

## Recommended next session opening prompt
"Bondhu, Österåker publishing continue koro. Read `osteraker-publishing-RESUME-2026-05-27.md` for full state. Source #1 e 15 events publish korte hobe (1 already partially started in form). Each event 100% perfect, all rules follow, push notifications OFF."
