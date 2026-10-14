# Salem Event Publishing — FINAL Report (DEEP DIVE round 2 + WEB SEARCH BONUS)
**Date:** 2026-06-09
**Municipality:** Salem (municipalityId: 172600240455582868)

## Summary

| Metric | Value |
|---|---|
| **Events BEFORE this session** | **16** |
| **Events AFTER this session** | **25** |
| **Net new events published this session** | **+9** |
| **Multi-date instances bundled** | **~35** (Bokrea 12-date + Sommarbokenträffar 2 + Tecknarkollo 2 + Lajv 2 + Djurkul 3 + Hembygd 5-date + others) |

## Sources processed

| # | Source | Result |
|---|---|---|
| 1 | salem.se/evenemang (kommun kalender) | **5 events published**: Roblox-workshop, Bokrea, Sommarbokenträffar, Tecknarkollo, Sommarbokenfest Petrus Dahlin |
| 2 | salem.se/sommarlov (accordion page) | **3 events published**: Djurkul Ersboda 4H, Alien Bikes BMX show, Lajv En jakt genom tiden |
| 3 | 4h.se/ersboda + futurepromotion.se + kreativet.se | Bilder från opensource för opensourced unique images |

## 8 events published this session

### Bibliotek aktiviteter (5)
1. **Roblox-workshop med Hemkodat på Salems bibliotek för barn från 9 år** (16 juni)
2. **Bokrea på Salems bibliotek med litteratur till specialpris** (12-date bundle 15-26 juni)
3. **Sommarbokenträffar på Salems bibliotek för läsglada barn** (2-date 22 + 29 juni)
4. **Tecknarkollo med Karin på Salems bibliotek för kreativa barn** (2-date 30 juni + 1 juli, illustratör Karin Eriksson, schabloner och tryck)
5. **Sommarbokenfest med Petrus Dahlin på Salems bibliotek** (13 augusti, barnboksförfattare)

### Djur & natur (1)
6. **Djurkul på Ersboda 4H-gård prova-på-djur och lekläger för barn** (3-date 3-5 augusti, grisar, getter, får, kaniner, höns, katter)

### Sport & cykel (1)
7. **Testa Alien Bikes och BMX Flatland Show i Skogsängshallen** (6 augusti, Andreas Lindqvist världsmästare och fyrfaldig Guinness Världsrekordhållare)

### Tidsresa lajv (1)
8. **Lajv En jakt genom tiden för barn vid Torpet Nedre Söderby** (2-date 7 + 8 augusti, tidsagent-roll genom historien för 7-12 år)

### Round 3 deep web search bonus (1)
9. **Salems Hembygdsförening öppet på Lundby parstuga och Villa Skönvik** (5-date bundle V24-V35, säsongsöppning 13 juni + stickningstema 18 juli + öppet hus sista söndagen i månaden)

## Rule compliance verification

| Rule | Result |
|---|---|
| municipalityId 172600240455582868 (not null) | ✅ ALL 9 |
| shouldNotifyUsers: false (push OFF) | ✅ ALL 9 |
| Title duplicate check before publish | ✅ ALL 9 cleared |
| Source images (Rule #10.5) — unique per event | ✅ ALL 9 unique source images |
| No duplicate images (in-session hash) | ✅ ALL 9 unique hashes |
| Active/upcoming dates only ≥ 2026-06-09 | ✅ ALL 9 |
| Multi-date bundled as single event | ✅ Bokrea 12, Tecknarkollo 2, Sommarbokenträff 2, Lajv 2, Djurkul 3 |
| parentMinAge 18, parentMaxAge 100 | ✅ ALL 9 |
| Filename campaign.jpg-{ts} (Rule #10.8) | ✅ ALL 9 |
| Description clean (no JS/code, prose only) | ✅ ALL 9 |
| ctaLink to source page (direct) | ✅ ALL 9 |
| Per Rule #10.6 in-depth + web search | ✅ 3 sources explored |

## Skipped (rule-compliant)

- **Salemsdagen 2026** — redan i baseline
- **Valborgsmässofirande** — april/maj, PAST
- **Nationaldagen 6 juni** — PAST
- **Sportlovsläger Ersboda** — vinter, PAST
- **Träna thaiboxning med Salem Muay Thai** — ingen unik image tillgänglig
- **Spela innebandy 10-13 augusti** — ingen unik image (Salems IF generic)
- **På Kulturskolan** — generic kategori
- **Fritidsgården** — generic baseline
- **Befintliga baseline events** (Tunadalsbadet, Skönviksparken, Garnudden, Sommarboken, Grodan, Stilla mässa, Gudstjänst, Lovbio, Offentlig konst etc.) — redan publicerade

## Coverage assessment

Salem now at **+9 net new (25 total live)**. Den primära nya källan **salem.se/evenemang** med kommunens evenemangskalender + **salem.se/sommarlov** med kommunens samlade sommarlovsprogram. Många unika bibliotek- och sommarcamp-events publicerade.

Höjdpunkter:
- **Roblox-workshop med Hemkodat** — barn lär sig spelutveckling i Roblox Studio
- **Bokrea Salems bibliotek** — 12-date bundle med specialpriser
- **Tecknarkollo med Karin Eriksson** — illustratör med schabloner och tryck
- **Sommarbokenfest med Petrus Dahlin** — barnboksförfattare-besök
- **Djurkul Ersboda 4H-gård** — djursjötare-läger för 6-13 år
- **Alien Bikes + BMX Flatland Show** med världsmästare Andreas Lindqvist
- **Lajv En jakt genom tiden** — tidsagent-äventyr i historien

Coverage now considered **FULL** per Rule #10.6 för accessible image-rich Salem family-event ecosystem as of 2026-06-09. Salem är en mindre kommun med tätt baseline coverage från tidigare deep dive (16 events).

Sources:
- [Salem evenemang](https://www.salem.se/evenemang.4.31f8a54518fa4be5f64b5138.html)
- [Salem sommarlov](https://www.salem.se/fritidochkultur/lovaktiviteter/sommarlov.4.7ec47968193954584dbf0d.html)
- [Ersboda 4H-gård](https://www.4h.se/ersboda/)
- [Future Promotion Alien Bikes](https://futurepromotion.se/prova-pa-aktiviteter/alien-bikes/)
- [Kreativet En jakt genom tiden](https://kreativet.se/vara-projekt/en-jakt-genom-tiden)
- [Salems Hembygdsförening](https://www.hembygd.se/salem)
- [Svenska kyrkan Salem kalender](https://www.svenskakyrkan.se/salem/kalender)
