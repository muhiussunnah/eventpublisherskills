# Huddinge Event Publishing — FINAL Report (DEEP DIVE + WEB SEARCH)
**Date:** 2026-05-30
**Municipality:** Huddinge (municipalityId: 172600240455582861, fallback placeId: 340726476989039971 "Huddinge Kulturhus")

## Summary

| Metric | Value |
|---|---|
| **Events BEFORE this session** | **13** |
| **Events AFTER this session** | **25** |
| **Net new events published this session** | **+12** |

## Sources processed

| # | Source | Status |
|---|---|---|
| 1 | huddinge.se/fritid-natur-och-kultur/.../arliga-evenemang | ✅ 5 årliga events scanned. Parksommar published (others used kommun logo, skipped) |
| 2 | bibliotek.huddinge.se (Arena) | ✅ 22 unique events scanned (paginated all). 1 published — Sommarboken-kickoff. Rest used shared placeholder image (per "no dup images") |
| 3 | huddingekulturhus.se | ✅ Huddinge Jazz & Blues 2026 published |
| 4 | tickster.com Huddinge | ✅ 10 events scanned. 7 published with unique og:images |
| 5 | facebook.com/Huddingekommun/events | ⏸ Facebook login required |
| 6 | svenskakyrkan.se/huddinge/kalender | ✅ Samling för barn (söndagsskola) published with multi-date bundle |
| BONUS Web Search | Parkteatern Sjödalsparken | ✅ +1 (image PATCH'd unique after Danderyd collision) |

## 12 events published

### Source 1 — huddinge.se (1)
1. **Parksommar i Huddinges parker 2026** — 8-date bundle (juni-aug), musik & föreställningar i parker

### Source 2 — bibliotek.huddinge.se (1)
2. **Sommarboken-kickoff på Huddinge bibliotek** — 4 juni 18-20:30

### Source 3 — huddingekulturhus.se (1)
3. **Huddinge Jazz & Blues 2026 i Sjödalsparken** — 30 maj 12-21, 34:e upplagan

### Source 4 — Tickster Huddinge Kulturhus hos Folkes (7)
4. **Stockholm Jazztrio - Clarinet night med Staffan M** — 24 sep
5. **Violetta tar bussen – familjeföreställning** — 12 okt 16:00 (Tonsalen Teater Sláva, ages 3-10)
6. **Hyllning till Palle Danielsson – jazzkonsert** — 15 okt
7. **Nils Ferlin och KlaraBohemerna på Huddinge Kulturhus** — 8 nov
8. **Karl Olandersson kvartett på Huddinge Kulturhus** — 19 nov
9. **Christina Gustafsson och Leo Lindbergs Trio på Huddinge Kulturhus** — 5 dec
10. **Forsberg O. Westin – Långformsimpro med jultwist** — 6 dec

### Source 6 — svenskakyrkan Huddinge (1)
11. **Samling för barn i Mariakyrkan – söndagsskola** — 9-date Sunday bundle, ages 3-10, fri entré

### Web Search bonus (1)
12. **Parkteatern på Sjödalsparken – familjeföreställning i Huddinge** — 27 juni 14:00, ages 3-12, fri entré (image PATCH'd to unique Sjödalsparken nackrosdammen after duplicate detection)

## Image-duplicate audit + fixes during session

| Issue | Resolution |
|---|---|
| Parkteatern Sjödalsparken image initially used same parkteatern_press.jpg as Danderyd Kvarnparken Parkteatern (177,511 bytes hash match) | **PATCH'd** to unique Sjödalsparken nackrosdammen image (105KB) |

Session hash check (`window.__sessionHashes`) prevented in-session duplicates across all 12 publishes.

## Multi-date events bundled

- Parksommar: 8 dates (juni-aug 2026)
- Marklyft-style multi-date for Samling för barn: 9 dates (söndagar)
- Total: 17 date-instances bundled into 2 events

## Rule compliance verification

| Rule | Result |
|---|---|
| municipalityId 172600240455582861 (not null) | ✅ ALL 12 |
| shouldNotifyUsers: false (push OFF) | ✅ ALL 12 |
| Title duplicate check before publish | ✅ ALL 12 cleared |
| Source images (Rule #10.5) | ✅ ALL 12 |
| No duplicate images | ✅ ALL 12 (cross-municipality Parkteatern collision caught + PATCH'd) |
| Active/upcoming dates only ≥ 2026-05-30 | ✅ ALL 12 |
| Multi-date bundled | ✅ 2 bundles (8+9 dates) |
| parentMinAge 18, parentMaxAge 100 | ✅ ALL 12 |
| Filename campaign.jpg-{ts} (Rule #10.8) | ✅ ALL 12 |
| Description clean (no JS/code) | ✅ ALL 12 |
| ctaLink to source page | ✅ ALL 12 |
| Per Rule #10.6 in-depth + web search | ✅ 6 sources + 1 web search bonus |

## Skipped (rule-compliant)

- Huddingedagen, Demokratidagarna, Huddinge konst (Source 1) — only kommun logo as og:image
- Animationsverkstad, Bokcirkel för unga, Måleri för unga, Suomenkielinen lukupiiri, Rollspelsklubben, Skapa odla upptäck, Stick och virka, Konstverkstad x2, Soft dans seniorer, Öppen konstverkstad, Språkcafé, Studiestöd vuxna, Skrivworkshop, IT-handledning, Digitala fixaren, Högläsning turkiska, Biblioteket på Huddingedagen, Sommarfest!, Utställning/Vernissage Gott och blandat (Source 2) — all share same axiell placeholder image
- Jävla idioter (Tickster) — adult drama
- Tanter på rymmen (Tickster) — title duplicate with Botkyrka
- Siri Karlsson Fullerstaparken — Fullersta Gård og:image returned 404
- Sommarkonsert Mariakyrkan — would duplicate Samling för barn image
- Mässa Huddinge kyrka — gudstjänst (religious service, not family event)

## Web search sources used

- [Sjödalsparken Huddinge kommun](https://www.huddinge.se/sjodalsparken)
- [Parkteatern – Kulturhuset Stadsteatern](https://kulturhusetstadsteatern.se/parkteatern)
- [Fullersta Gård utställningsprogram](https://webb.huddinge.se/fullerstagard/utstallningar/program/)
- [Mariakyrkan Huddinge](https://www.svenskakyrkan.se/huddinge/om-mariakyrkan)

## Coverage assessment

Huddinge now at **+12 net new (25 total live)**. 5 of 6 spreadsheet sources thoroughly processed (Source 5 Facebook requires login). Library Arena system serves shared placeholder image to most events — limited library publish to 1 event with unique image. Cross-municipality image duplicate caught and fixed.

Coverage now considered FULL per Rule #10.6 for accessible Huddinge family events.

Sources:
- [Huddinge årliga evenemang](https://www.huddinge.se/fritid-natur-och-kultur/kultur-och-sevardheter/arliga-evenemang/)
- [Huddinge bibliotek](https://bibliotek.huddinge.se/evenemang)
- [Huddinge Kulturhus](https://huddingekulturhus.se/index.php/ct-menu-item-7)
- [Tickster Huddinge](https://www.tickster.com/se/sv/events/in/huddinge)
- [Svenska kyrkan Huddinge kalender](https://www.svenskakyrkan.se/huddinge/kalender)
- [Sjödalsparken Huddinge](https://www.huddinge.se/sjodalsparken)
- [Fullersta Gård program](https://webb.huddinge.se/fullerstagard/utstallningar/program/)
- [Parkteatern](https://kulturhusetstadsteatern.se/parkteatern)
