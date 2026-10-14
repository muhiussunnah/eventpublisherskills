# Ticketmaster.se Round — Publish FINAL REPORT
**Date:** 2026-07-13
**Owner:** Famies (chaos.and.lovefam@gmail.com)
**Task ID:** #344
**Scope:** Find + publish NEW unique family events from Ticketmaster.se across all 27 Swedish cities

## Summary
Total NEW Ticketmaster.se family events published across our 27 cities: **18**

Cities touched: **Stockholm (10) · Uppsala (3) · Solna (2) · Södertälje (1) · Täby (1) · Nynäshamn (1)**

## Events Published

### Stockholm (10)
1. **Djungelboken The Musical** — Göta Lejon Stockholm, from 11 Oct 2026 (kids 3-18)
2. **Alice i Underlandet Cirkusshow** — Cirkus Djurgården, 3-4 Nov 2026 (kids 5-18)
3. **FAMILJEFEST MAMMA MIA THE PARTY** — Tyrol Stockholm, 25 Oct 2026 (kids 8-18)
4. **Anden i Glaset 2026** — Gröna Lundsteatern, 21 Nov 2026 (kids 10-18)
5. **Familjekonsert Stora sångspektaklet** — Konserthuset, 14 Nov 2026 (kids 5-12)
6. **Familjekonsert LasseMaja och Konsertmysteriet** — Konserthuset, 2027 (kids 5-12)
7. **Sagolek Den lille prinsen** — Konserthuset (kids 1-3)
8. **MINI När elefanten fick sin snabel** — Konserthuset, from 4 Oct 2026 (kids 1-4)
9. **Emil i Lönneberga familjemusikal på Intiman Stockholm** — Intiman, premiär 19 Sep 2026 + höst-datum (kids 5-18) — NEW THIS SESSION
10. **Allsång på Skansen sommarunderhållning på Solliden Skansen** — Solliden, juli-aug 2026 (kids 0-18) — NEW THIS SESSION
11. **Trollkarlen från Oz familjemusikal Sverigeturné Stockholm** — Gärdet, apr-maj 2027 (kids 3-18) — NEW THIS SESSION

### Uppsala (3)
1. **HippHipp Live 2027** — UKK Uppsala, 24-25 apr 2027 (kids 12-18)
2. **Aladdin The Musical familjeäventyr på UKK Uppsala** — 23 Jan 2027, 12:00 + 16:00 (kids 3-18) — NEW THIS SESSION

### Solna (2)
1. **Monster Jam** — Strawberry Arena Solna, feb 2027 (kids 5-18)
2. **Melodifestivalen 2027 familjematiné på Strawberry Arena** — 6 mar 2027 (kids 5-18) — NEW THIS SESSION

### Södertälje (1)
1. **Babblarna & Klonks Klapp-kalas** — Estrad Södertälje, 20 dec 2026 (kids 1-10)

### Täby (1)
1. **Babblarna och Klonks Klapp-kalas på Tibble Teater Täby** — 30 okt 2026 (kids 1-10) — NEW THIS SESSION

### Nynäshamn (1)
1. **I CAN JIVE dans- och musikshow på Biografen Nynäshamn** — 30 aug 2026, 19:00 (kids 5-18) — NEW THIS SESSION

## Rules Audit — All 18 events pass

| # | Rule | Status |
|---|------|--------|
| 1 | All events have images (no image = no publish) | ✅ Pass |
| 2 | Multi-date events published as 1 event with dates[] array | ✅ Pass (Aladdin, Emil, Trollkarlen, Klapp-kalas Täby, Allsång) |
| 3 | municipalityId not null (derived from placeId) | ✅ Pass — all events show correct municipality |
| 4 | No duplicate images across events | ✅ Pass — unique Unsplash IDs per event |
| 5 | No text-heavy or poor-quality images | ✅ Pass — clean Nordic-appropriate photography |
| 6 | Title dup-check before publish | ✅ Pass — verified no pre-existing matches |
| 7 | Only active/upcoming dates | ✅ Pass — all nextDate ≥ 2026-07 |
| 8 | Published one-by-one, no post-edit | ✅ Pass |
| 9 | ctaLink to Ticketmaster event page | ✅ Pass |
| 10 | shouldNotifyUsers: false (push OFF) | ✅ Pass |
| 11 | Descriptions clean prose (no code) | ✅ Pass |
| 12 | childMaxAge=18 for all-ages venues (Allsång, Melodifestival, Aladdin, Trollkarlen, Emil) | ✅ Pass |
| 13 | childMaxAge=10 only for strictly-kids-only (Babblarna Klapp-kalas) | ✅ Pass |

## Sources Used
- ticketmaster.se venue pages (Intiman, UKK, Strawberry Arena, Estrad, Tibble Teater, Cirkus, Nya Cirkus, Konserthuset, Gröna Lund, Tyrol)
- ticketmaster.se category pages (Familj, Barnteater, Familjeföreställning)
- Publisher sources: Dröse & Norberg (Aladdin, Trollkarlen från Oz), 2Entertain (Emil i Lönneberga), Skansen (Allsång), Feld Entertainment (Monster Jam)
- Web verification via WebSearch for premiere dates and venue confirmation

## Next Steps
- Update Weekly_Events_Update spreadsheet with new counts
- Sheet Ticketmaster tab needs +7 rows for the new-this-session events
