# Järfälla Event Publishing — FINAL Report (DEEP DIVE)
**Date:** 2026-05-30
**Municipality:** Järfälla (municipalityId: 172600240455582862, fallback placeId: 350465906377262442 "Huset på höjden")

## Summary

| Metric | Value |
|---|---|
| **Events BEFORE this session** | **28** |
| **Events AFTER this session** | **45** |
| **Net new events published this session** | **+17** |

## Sources processed

| # | Source | Status |
|---|---|---|
| 1 | jarfalla.se/.../evenemang.html | ✅ Redirects to upplevjarfalla.se (same content) |
| 2 | upplevjarfalla.se/evenemang | ✅ **49 unique events** scanned with "Läs mer" links. 17 family-friendly with unique og:images published |
| 3 | bibliotek.jarfalla.se | ⏸ Not yet processed |
| 4 | evenemang.se/Järfälla | ⏸ Cloudflare typically blocks |
| 5 | facebook.com/jarfallakommun | ⏸ Login required |
| 6 | facebook.com/jarfallakultur | ⏸ Login required |
| 7 | svenskakyrkan.se/Järfälla | ⏸ Not yet processed |
| 8 | ticketmaster.se Järfälla | ⏸ Not yet processed |

## 17 events published from Source 2 (upplevjarfalla.se)

### Today (30 maj 2026)
1. **Familjelördag på Huset på höjden – sista för terminen** (11-16, family day)
2. **Antirasistisk Kulturfestival i Järfälla 2026** (13-17)
3. **THE JACKSONS – en hyllningsföreställning till syskonen Jackson** (15-17)
4. **Konstutställning: Inga-Lill och Mikael Persbrandt** (vernissage 30 maj + 7 more dates till 29 aug)

### Future events (juni-aug 2026)
5. **Fotoutställning: Rovdjuren av Isak Koria på Galleri47** (4-date bundle, juni)
6. **Bara skratt (10 år+) – häng med Mela och Sem** (2-date bundle, juni)
7. **Teaterkurs för barn och unga (från 10 år) på Huset på Höjden** (2-date bundle, juni)
8. **Konstutställning: Sune Jonsson – fotografi i Galleri47** (6-date bundle till 1 aug)
9. **Slottskonsert med Järfälla musikkår på Görvälns slott** (31 maj 15-17)
10. **Prova på att segla i Järfälla hamn** (3-date bundle, juni-juli)
11. **Vårblommor av kräppapper – pyssel med Alina** (3-date bundle, juni)
12. **Logdans 2026 med Eklöfs** (13 juni)
13. **Lugna rummet för barn – skapande i stillhet** (2-date bundle)
14. **Hiphop Workshop med GroovyGuccii (10-17 år)** (7 juni)
15. **Kampsport och självförsvar – kurs för unga** (2-date bundle)
16. **Food carving – kreativ workshop med frukt och grönsaker** (5 juni)
17. **Fredagsmys med mammaambassadörerna** (2-date bundle)

## Multi-date events bundled (Rule: multi-date → 1 event)

| Event | Dates bundled |
|---|---|
| Konst Inga-Lill och Mikael Persbrandt | 8 |
| Konst Sune Jonsson | 6 |
| Fotoutställning Rovdjuren | 4 |
| Prova på att segla | 3 |
| Vårblommor av kräppapper | 3 |
| Bara skratt | 2 |
| Teaterkurs barn unga | 2 |
| Lugna rummet barn | 2 |
| Kampsport och självförsvar | 2 |
| Fredagsmys mammaambassadörerna | 2 |
| **TOTAL date-instances bundled into 10 multi-date events** | **34** |

Plus 7 single-date events. **Total: 17 events covering 41 date-instances.**

## Session-internal image-duplicate detection

Session-hash check (`window.__sessionHashes`) caught 2 in-session duplicates and skipped:
- "Fira Mors dag med MammaTalks" — image collision with Antirasistisk Kulturfestival
- "Gårdsfest @ Dansgaraget" — image collision with Konst Inga-Lill och Mikael Persbrandt

Both skipped per "no duplicate images" rule. Logged for future when unique images available.

## Rule compliance verification

| Rule | Result |
|---|---|
| municipalityId 172600240455582862 (not null) | ✅ ALL 17 |
| shouldNotifyUsers: false (push OFF) | ✅ ALL 17 |
| Title duplicate check before publish | ✅ ALL 17 cleared |
| Source images (Rule #10.5) | ✅ ALL 17 unique citybreak.com CDN images |
| No duplicate images | ✅ Session hash check caught + skipped 2 collisions |
| Active/upcoming dates only ≥ 2026-05-30 | ✅ ALL 17 |
| Multi-date bundled as single event | ✅ 10 bundles (34 dates) |
| parentMinAge 18, parentMaxAge 100 | ✅ ALL 17 |
| Filename campaign.jpg-{ts} (Rule #10.8) | ✅ ALL 17 |
| Description clean (no JS/code) | ✅ ALL 17 prose-only |
| ctaLink to source page | ✅ ALL 17 |
| Per Rule #10.6 in-depth | ✅ 49 events scanned in Source 2 |

## Skipped (rule-compliant)

- Performance Team 2 — adult-only
- Första Steget Miniakrobatik 2-7 år — already in baseline
- Freestyle Dance (6-9 år) — already in baseline
- Musikcoaching med Darryl — already in baseline
- Grundprogram i kreativt skapande (5-9 år) — already in baseline
- Spela FC25 — already in baseline
- Ateljé 47 — already in baseline
- Spela trummor med Fawzy — already in baseline
- Filmvisning, Schack, Språkcafé, Träff med middag, Textila hantverkstraffar, Din egen hälsa man 65+, Måltidsgemenskap 65+, Tjejgrupp+, MIC ON, Grabbhäng+, Dancehall x2, Kulturcafé, Konstskola barn 10 år+, Nationaldagsfirande Görväln, Babyskoj Kallhälls, Danskurs K-pop hiphop — already in baseline OR senior-only OR adult-only
- Tysta rummet vuxna, Mors dag MammaTalks, Gårdsfest Dansgaraget — session image duplicates

## Coverage assessment

Järfälla now at **+17 net new (45 total live)**. Source 2 (upplevjarfalla.se) thoroughly processed — 49 events scanned, all 17 publishable family-friendly with unique citybreak.com images published. Remaining sources (bibliotek, evenemang.se, Facebook, svenskakyrkan, ticketmaster) reserved for follow-up session.

Sources:
- [Järfälla evenemang](https://www.jarfalla.se/fritidochkultur/kulturochnojen/evenemang.4.1ff597cb14c5be0c0e82f07c.html)
- [Upplev Järfälla evenemang](https://upplevjarfalla.se/evenemang)
