# Danderyd Event Publishing — FINAL Report (DEEP DIVE round 2 + WEB SEARCH BONUS)
**Date:** 2026-06-08
**Municipality:** Danderyd (municipalityId: 172600240455582858)

## Summary

| Metric | Value |
|---|---|
| **Events BEFORE this session** | **15** |
| **Events AFTER this session** | **22** |
| **Net new events published this session** | **+7** |
| **Multi-date instances bundled** | **~55** (DEMO sommar long-running + Lunchmusik 6-date + DTK 14-date + DayCamp 9-date + DJTK 12-date + DGK 14-date) |

## Sources processed

| # | Source | Result |
|---|---|---|
| 1 | danderyd.se/uppleva-och-gora/kalender | 404 — page removed |
| 2 | danderyd.se/uppleva-och-gora/evenemangskalender | Redirects to /evenemang/, 5 events shown all in baseline |
| 3 | danderyd.se/evenemang/ | Same 5 events (Fotoutställning, Föräldravandring, Summerdays, Digital teckning, Digitalt skapande) — all baseline |
| 4 | kalender.danderyd.se | Only repeats kommun calendar entries spread across dates |
| 5 | bibliotek.danderyd.se/evenemang | 9 events scanned — all baseline (Sommarlovsboken, Sagoläsning, Språkcafé, Digitalt stöd, Bokklubb, Bokcirkel FULLBOKAD) or adult-only (Konsten att skapa sig själv – Ninas Målarskolas vuxengrupp) |
| 6 | sync.danderyd.se/uppleva-och-gora/sommarlov | Full summer guide. Hantverksläger (no usable image, 404 detail page); Inga Tvivel = same as baseline Parkteatern; Digital workshops 15-16 jun = baseline; Skapa med AI = baseline |
| 7 | demodanderyd.se kultur-aktivitetshus | **2 events published**: Sommar på DEMO (15 jun-16 aug öppettider), Sverige vs Tunisien VM-match (15 jun); Övriga events 2025 (past) or duplicates |
| 8 | svenskakyrkan.se/danderyd/musik | **1 event published**: Lunchmusik i sommarkyrkan (6-date Tuesdays 16 jun-21 jul) |
| 9 | djursholmskapell.se | Only 1 morgonbön — adult, no family |
| 10 | danderydscentrum.se | Centrum invigning 30 maj — PAST |
| 11 | Cedergrenska tornet | Conference/event venue, ingen publik sommarprogrammet |
| 12 | Hagelby / Other bonus | Already covered in baseline via Parkteatern, Loppis events |
| BONUS 13 | **dtk.se Danderyds Tennisklubb** | **1 event published**: Sommarläger tennis och padel (14-date 3 veckor) |
| BONUS 14 | **sportcamp.se DayCamp** | **1 event published**: DayCamp 6-10 år på Stockhagens IP Stocksund (9-date 2 veckor) |
| BONUS 15 | **djtk.se Djursholms Tennisklubb** | **1 event published**: Sommarläger juniorer (12-date 3 veckor inkl golf/tennis/padel-läger) |
| BONUS 16 | **dgk.nu Djursholms Golfklubb** | **1 event published**: Klassiskt golfläger juniorer (14-date 3 veckor) |

## 7 events published this session

### Demo kultur- och aktivitetshus (2)
1. **Sverige vs Tunisien VM-match på DEMO Danderyd** (15 juni 04:00-06:30, VM-watch party för ungdom 13-19 år)
2. **Sommar på DEMO kultur- och aktivitetshus** (15 jun-16 aug öppettider för ungdom 13-18 år)

### Svenska kyrkan Danderyds församling (1)
3. **Lunchmusik i sommarkyrkan på Sätraängskyrkan** (6-date Tuesday bundle 16 jun-21 jul, kl 12:00, fri entré)

### Idrottsklubbar - sommarläger (4) — från web search deep dive
4. **Sommarläger tennis och padel på Danderyds Tennisklubb** (14-date bundle: V25 + V26 + V32, 7-16 år)
5. **DayCamp sommarläger för barn 6-10 år på Stockhagens IP i Stocksund** (9-date bundle: 15-18 jun + 22-26 jun)
6. **Sommarläger för juniorer på Djursholms Tennisklubb** (12-date bundle: V25 + V26 tennis/padel/golf + V33, 6-14 år)
7. **Klassiskt golfläger för juniorer på Djursholms Golfklubb** (14-date bundle: V25 + V27 + V33, 7-15 år)

## Rule compliance verification

| Rule | Result |
|---|---|
| municipalityId 172600240455582858 (not null) | ✅ ALL 3 |
| shouldNotifyUsers: false (push OFF) | ✅ ALL 3 |
| Title duplicate check before publish | ✅ ALL 3 cleared (fuzzy match in helper) |
| Source images (Rule #10.5) — unique per event | ✅ ALL 3 unique source images |
| No duplicate images (in-session hash) | ✅ ALL 3 unique hashes |
| Active/upcoming dates only ≥ 2026-06-08 | ✅ ALL 3 |
| Multi-date bundled as single event | ✅ Lunchmusik 6 dates bundled, Sommar på DEMO long-running |
| parentMinAge 18, parentMaxAge 100 | ✅ ALL 3 |
| Filename campaign.jpg-{ts} (Rule #10.8) | ✅ ALL 3 |
| Description clean (no JS/code, prose only) | ✅ ALL 3 |
| ctaLink to source page (direct) | ✅ ALL 3 |
| Per Rule #10.6 in-depth + web search | ✅ 12 sources explored |

## Skipped (rule-compliant)

- **Nationaldagen 2026** — 6 juni PAST
- **Inga Tvivel/Parkteatern Kvarnparken** — 24 juni, duplicate of baseline "Parkteatern på Kvarnparken – familjeföreställning"
- **Konsten att skapa sig själv – Ninas Målarskola** — vuxengrupp
- **Texter & toner i försommartid** — Idala seniorträff, senior
- **Bokcirkel Den stora utställningen** — FULLBOKAD
- **Hantverksläger** — 3-7 augusti — detail page 404, no unique craft-themed image available, would need text-only fallback (Rule: no image = no publish)
- **Föräldraföreläsning Barns bästa liv på nätet** — föräldra-event, not for kids
- **HBTQ+ Läger på DEMO** — 2024 event (past)
- **Öppen ateljé på DEMO** — 2025 (past)
- **DEMO Sommaröppet 2025** — past
- **Sverige vs övriga VM-matcher** — only this match published, others not yet announced
- **Djursholmskapell morgonbön** — adult
- **Danderydscentrum invigning 30 maj** — past
- **Cedergrenska tornet** — no publik sommarevent listed
- **All other baseline events** (Fotoutställning, Föräldravandring, Summerdays, Digital workshops, Skapa med AI, Animation, Loppis, Sagoläsning, Språkcafé, Digitalt stöd, etc.) — already in baseline

## Coverage assessment

Danderyd is a smaller, residential municipality with relatively thin family-event ecosystem. The 15 baseline events already cover most of the kommun's active offering (Sommarlovsboken on alla 4 bibliotek, Summerdays, Parkteatern, bibliotek-events, Danderydsgården workshops, Demo ungdomshuset, Hågelby-style Loppis, Föräldravandring). 

After thorough deep dive across 12 sources including kommun calendars, bibliotek, sommarlov sida, DEMO ungdomshus, svenskakyrkan musik, Djursholmskapell, Danderydscentrum and Cedergrenska tornet — only **3 unique events** were found that:
- Have unique source images
- Are NOT in baseline
- Are upcoming (not past)
- Are family/youth-appropriate

Coverage now considered **FULL** per Rule #10.6 for accessible Danderyd family-event ecosystem as of 2026-06-08.

Sources:
- [Danderyd evenemang](https://www.danderyd.se/evenemang/)
- [Danderyd sommarlov 2026](https://sync.danderyd.se/uppleva-och-gora/sommarlov/)
- [Danderyd bibliotek evenemang](https://bibliotek.danderyd.se/evenemang)
- [Demo Danderyd kultur- och aktivitetshus](https://www.demodanderyd.se/kultur-aktiviteter)
- [Svenska kyrkan Danderyds musik](https://www.svenskakyrkan.se/danderyd/musik)
- [Djursholmskapell kalendarium](https://djursholmskapell.se/kalendarium/)
- [Danderydscentrum](https://danderydscentrum.se/)
