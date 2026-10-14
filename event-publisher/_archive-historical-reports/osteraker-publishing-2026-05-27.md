# Österåker Event Publishing — Session Plan
**Date:** 2026-05-27
**Status:** Starting source #1

## Municipality
- Name: Österåker
- municipalityId: 172600240698852664 (verify - actually stored in window.__osterakerMunId)

## 7 Sources to Process (in order)
1. https://www.osteraker.se/arkivevenemangkrisochinfo/evenemang.4.592cfecd176fc0db87818e.html (municipality calendar) ← **CURRENT**
2. https://bibliotek.osteraker.se/evenemang#/ (library)
3. https://evenemang.se/se/stockholms-l%C3%A4n/%C3%B6ster%C3%A5ker (aggregator)
4. https://publicakersberga.se/evenemang/ (Åkersberga publica)
5. https://www.facebook.com/osterakerskommun/events/ (FB municipality)
6. https://www.svenskakyrkan.se/kalender?q=%C3%96ster%C3%A5ker (church)
7. https://www.ticketmaster.se/search?q=%C3%96ster%C3%A5ker (ticketmaster)

## Existing 13 Events (DO NOT DUPLICATE)
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

## Standing Rules (v4)
- shouldNotifyUsers: false (ALWAYS)
- parentMinAge: 18, parentMaxAge: 100 (ALWAYS)
- municipalityId: 172600240698852664 (NOT null)
- No duplicate images across events
- No images with prominent text
- Search title before publishing (avoid duplicate)
- Only active/upcoming dates
- Multi-date events → single event with date array
- Age rules: 0-18=family, 18,18=adult, etc per v4

## Source 1 Events Found (initial scan)
- "Nätverksfrukost för företagare" (27 maj 2026, 07.30-09.30) at Restaurang Å (Åkersberga Golfklubb) — business breakfast, adult
- "NY PLATS: Vi möts – dialog med näringslivet i Österåker" (27 maj 2026) — POSSIBLE DUPLICATE of existing #3
- "Anhöriggrupp för dig som har en partner med neurologisk sjukdom" (27 maj 2026, 10.30-12.00) at Åkersberga Fyren — caretaker support, adult

(More to find by scrolling/clicking show more)

## Workflow per event
1. Click event title → open detail page
2. Read full description, dates, location, image
3. Search existing events for duplicate title (window.__osterakerExisting + fresh API search)
4. Download image (or generate UGC if missing/bad/has text)
5. Upload image to FamMap S3
6. POST /admin/events with full body
7. Confirm 200 response

## Next session resume point
After confirming POST endpoint structure, loop through all source 1 events.
