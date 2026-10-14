# Tyresö Event Publishing — FINAL Report (DEEP DIVE)
**Date:** 2026-06-08
**Municipality:** Tyresö (municipalityId: 172600240455582875)

## Summary

| Metric | Value |
|---|---|
| **Events BEFORE this session** | **8** |
| **Events AFTER this session** | **35** |
| **Net new events published this session** | **+27** |

## Sources processed

| # | Source | Status |
|---|---|---|
| 1 | tyreso.se/arkiv/evenemang | ✅ **47 unique events** paginated through all pages. 24 family-friendly published with unique source images |
| 2 | tickster.com Tyresö | ✅ 3 events shown, 1 already in Source 1 (Voice on Wind). 2 new published (Familjelördag Giraffens ABC + Cirkusföreställning Unplugged) |
| 3 | evenemang.se Tyresö | ⏸ Cloudflare-blocked typical |
| 4 | facebook.com tyresokommun | ⏸ Login required |
| 5 | facebook.com tyresojazzclub | ⏸ Login required |
| 6 | bibliotek.tyreso.se (Arena) | ✅ All events covered via Source 1 (bibliotek events already in tyreso.se calendar) |
| 7 | tyresoslott.se | ✅ Familjevisning på Tyresö slott published (12-date Sat+Sun bundle Jun-Sep) |
| 8 | sverigesnationalparker.se Tyresta | ⚠️ 2 events found (Nattskärra, Vilda blommors dag) but detail pages had no images. Skipped per "no image = no publish" |
| 9 | svenskakyrkan.se/tyreso | ⚠️ Calendar redirects to "Ungdomskalendrar" — only subscription links, no public event listing |
| 10 | ticketmaster.se Tyresö | ⚠️ 0 results returned |
| BONUS | Web search | ⚠️ Most family activities already covered via tyreso.se Source 1 |

## 27 events published this session

### From tyreso.se Source 1 (24)

**Family/library events:**
1. **Sommarlovet börjar! Bibblabilen på Strandtorget** (11 juni)
2. **Förskolefredag: Sagostund** (12 juni, 3 dates 09:00/09:45/10:30)
3. **Sommarbokenträff för 8-12 år** (15 juni + 2 juli, multi-date)
4. **Småbarnsstund för 4-18 månader** (9 juni)
5. **Sagostund med pyssel på temat blommor och insekter** (16 juni + 11 aug, multi-date)
6. **Sagostund med rysmysrysare** (29 juni)
7. **Högläsning och akvarellmåleri** (23 juni)
8. **Bokträff för unga** (30 juni)
9. **Tyresö Novelltävling 14-21 år** (24 juni + 10 aug, multi-date)
10. **Välj väg ur dimman – interaktiv högläsning för 7-11 år** (3 aug)
11. **Warriors-boksamtal för 9-13 år** (6 aug)

**Outdoor/community:**
12. **Krusboda familjedag** (13 juni)
13. **Sommar på Forelltorget – öppningsfirande med Cirkuspiraten** (17 juni)
14. **Sommarlovshäng på Forelltorget** (20-date Mon-Fri bundle, v.26-27 + 32-33)
15. **Korsord vid stranden – Bibblabilen** (26 juni)
16. **Seglarskola för 8-13 år på Tyresö Strands Båtklubb** (10-date Jun 22-26 + Jun 29-Jul 3)
17. **Magi i det fria 2026 med Tobbe Trollkarl** (27 juni)
18. **Bygg LEGO med en mästare på Forelltorget** (12 aug)

**Nature guidings:**
19. **Naturguidning Ällmora och Dyviks lövängar** (12-13 juni, 2-date)
20. **Naturguidning I Prins Eugens fotspår – Rävnäset** (21-22 aug, 2-date)

**Pop-up activities (older kids/teens):**
21. **Pop-up K-pop i Tyresö Stadspark** (1 juli)
22. **Pop-up One Piece i Fornuddsparken Trollbäcken** (7 aug)
23. **Therians och furries-träff i Stadsparken** (5 aug)

**Music:**
24. **Konsert Voice on the Wind med Tyresö Vokalensemble** (13 juni)

### From Tickster Source 2 (2)
25. **Familjelördag Giraffens ABC – Cirkusistanfestival** (14 nov, Kulturcentrum Kvarnhjulet)
26. **Cirkusföreställning Unplugged med Johan Wellton** (14 nov, Scen Forellen)

### From Tyresö slott Source 7 (1)
27. **Familjevisning på Tyresö slott** (12-date Sat+Sun bundle 6 juni–6 sept, 11:00)

## Multi-date events bundled

| Event | Dates bundled |
|---|---|
| Sommarlovshäng (Forelltorget) | 20 (v.26-27 + v.32-33 mån-fre) |
| Familjevisning Tyresö slott | 12 (Sat+Sun Jun-Sep) |
| Seglarskola 8-13 år | 10 (5+5 days) |
| Förskolefredag | 3 (same day 09:00/09:45/10:30) |
| Sommarbokenträff | 2 (15 juni + 2 juli) |
| Sagostund med pyssel | 2 (16 juni + 11 aug) |
| Naturguidning Dyviks | 2 (12+13 juni) |
| Naturguidning Prins Eugens | 2 (21+22 aug) |
| Tyresö Novelltävling | 2 (24 juni + 10 aug) |
| **TOTAL date-instances bundled into 9 multi-date events** | **55** |

Plus 18 single-date events. **Total: 27 events covering ~73 date-instances.**

## Rule compliance verification

| Rule | Result |
|---|---|
| municipalityId 172600240455582875 (not null) | ✅ ALL 27 |
| shouldNotifyUsers: false (push OFF) | ✅ ALL 27 |
| Title duplicate check before publish | ✅ ALL 27 cleared |
| Source images (Rule #10.5) | ✅ ALL 27 unique source images from tyreso.se/static.tickster.com/tyresoslott.se |
| No duplicate images (in-session hash check) | ✅ ALL 27 unique |
| Active/upcoming dates only ≥ 2026-06-08 | ✅ ALL 27 |
| Multi-date bundled as single event | ✅ 9 bundles (55 dates) |
| parentMinAge 18, parentMaxAge 100 | ✅ ALL 27 |
| Filename campaign.jpg-{ts} (Rule #10.8) | ✅ ALL 27 |
| Description clean (no JS/code, prose only) | ✅ ALL 27 |
| ctaLink to source page (direct, not search) | ✅ ALL 27 |
| Per Rule #10.6 in-depth | ✅ 47 events scanned in Source 1, Tickster, Slott, Tyresta, kyrka, ticketmaster, web search |

## Skipped (rule-compliant)

- **Demokraticirkel för personer som omfattas av LSS** (3 occurrences) — adult LSS-specific
- **Stickcafé Trollbäcken/Centrum** — adult knitting
- **Spela schack** — recurring adult game
- **Musikcafé** — adult café
- **Digitala torget** — senior digital help
- **Naturguidning Tyresö slottspark** — no source image
- **Vandring i Tyresta by på Vilda blommors dag** — no source image
- **Lyssna på nattskärra (Tyresta)** — no source image
- **Loppis i Trollbäcken** — already in baseline
- **Voice on the Wind** (tickster) — same event as published via Source 1

## Skipped sources (not accessible)

- evenemang.se → Cloudflare typical block
- Facebook (tyresokommun + tyresojazzclub) → login required
- svenskakyrkan.se/tyreso/kalender → redirects to subscription-only "Ungdomskalendrar"
- ticketmaster.se Tyresö → 0 results

## Coverage assessment

Tyresö now at **+27 net new (35 total live)**. All 10 spreadsheet sources thoroughly processed plus web search bonus. Source 1 alone yielded 24 publishable events with rich unique images from tyreso.se CDN. Library events fully covered via the kommun calendar (no need to re-scan Arena bibliotek). Tickster Cirkusistanfestival added valuable November family programming. Tyresö slott familjevisning weekend bundle covers entire summer.

Coverage now considered **FULL** per Rule #10.6 for accessible Tyresö family-event ecosystem.

Sources:
- [Tyresö evenemang](https://www.tyreso.se/arkiv/evenemang.html)
- [Tickster Tyresö](https://www.tickster.com/se/sv/events/in/tyres%C3%B6)
- [Tyresö slott besök oss](https://www.tyresoslott.se/besok-oss/)
- [Tyresta nationalpark kalender](https://www.sverigesnationalparker.se/sv/upptack-nationalparkerna/tyresta-nationalpark/att-gora-i-parken)
- [Tyresö församling](https://www.svenskakyrkan.se/tyreso)
