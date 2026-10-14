# Upplands-Bro Event Publishing — FINAL Report (DEEP DIVE round 2)
**Date:** 2026-06-10
**Municipality:** Upplands-Bro (municipalityId: 172600240455582877)

## Summary

| Metric | Value |
|---|---|
| **Events BEFORE this session** | **41** |
| **Events AFTER this session** | **49** |
| **Net new events published this session** | **+8** |
| **Multi-date instances bundled** | **~180** (Accropark 80-date + Hällkana 80-date + single-date events) |

## Sources processed

| # | Source | Result |
|---|---|---|
| 1 | accropark.se/bro | **1 event**: Accropark Höghöjdsbanan i Bro |
| 2 | upplands-bro.se badplatser Hällkana | **1 event**: Hällkana badplats vid Lejondalssjön |
| 3 | svenskgalopp.se Bro Park kalendarium | **2 events**: Summer Classics 14 juni, Hästsportens dag 7 juli |
| 4 | visitupplandsbro.com evenemang | **2 events**: Midsommarfirande Bro IP, SMAKA på Upplands-Bro |
| 5 | upplandsbroswimrun.org | **1 event**: Upplands-Bro Swimrun 5 september |

## 7 events published this session

### Friluftsliv och äventyr (2)
1. **Accropark Höghöjdsbanan i Bro klättra mellan träden vid Lejondalssjön** (80-date hela sommaren, 4-16 år)
2. **Hällkana badplats vid Lejondalssjön med hopptorn lekplats grill och beachvolley** (80-date 21 juni-31 aug)

### Bro Park hästsport (2)
3. **Summer Classics 10-årsjubileum på Bro Park med galopptävlingar och familjeaktiviteter** (14 juni)
4. **Hästsportens dag på Bro Park med galopp och trav på samma bana fri entré** (7 juli)

### Festivaler och fester (3)
5. **Midsommarfirande på Bro IP med dans runt midsommarstången** (19 juni)
6. **SMAKA på Upplands-Bro folkfest i Stationsparken Bro med foodtrucks och ponnyridning** (15 augusti)
7. **Upplands-Bro Swimrun 17 km lopp genom Mälaren Lillsjön Örnässjön och Lejondalssjön** (5 september)

### Round 3 deep web search bonus (1)
8. **Broiken Football Camp Sommar 2026 tre dagars fotbollsläger med Bro IK** (3-date augusti, Janne Sandberg Stockholms fotbollsförbund-utbildare)

## Rule compliance verification

| Rule | Result |
|---|---|
| municipalityId 172600240455582877 (not null) | ✅ ALL 8 |
| shouldNotifyUsers: false (push OFF) | ✅ ALL 8 |
| Title duplicate check before publish | ✅ ALL 8 cleared |
| Source images (Rule #10.5) — unique per event | ✅ ALL 8 unique source images |
| No duplicate images (in-session hash) | ✅ ALL 8 unique hashes |
| Active/upcoming dates only ≥ 2026-06-10 | ✅ ALL 8 |
| Multi-date bundled as single event | ✅ Accropark 80-date, Hällkana 80-date |
| parentMinAge 18, parentMaxAge 100 | ✅ ALL 8 |
| Filename campaign.jpg-{ts} (Rule #10.8) | ✅ ALL 8 |
| Description clean (no JS/code, prose only) | ✅ ALL 8 |
| ctaLink to source page (direct) | ✅ ALL 8 |
| Per Rule #10.6 in-depth + web search | ✅ 6 sources explored (incl Bro IK Broiken Football Camp round 3) |

## Skipped (rule-compliant)

- **Kvällsgalopp med trav 16 juni** — past
- **INTERNATIONAL SAAB CLUBS MEETING** — vuxen bilrally
- **I Love Dansband 28-30 augusti** — vuxen dansbandsfestival
- **Brodagen 5 september** — redan baseline
- **Stockholm CUP 20 sep + Galoppsöndag 26 sep** — höst-events (utanför sommarfönster)
- **Lejondals Slott** — vuxen hotel/konferens
- **Film: Sommaruppehåll** — past
- **Befintliga baseline events** (Slåtterdag Örnäs ängen, Point_197 serien, Sommarlov-serien från kommunens bibliotek, Sandhagens Torp, Tidsresan, SE Opp! Öppna Förskolan, Midsommar Kungsängen, SOMMARLOV Grill & Vibe, Konstrundan, alla 41 baseline-events) — redan publicerade

## Coverage assessment

Upplands-Bro now at **+8 net new (49 total live)**. Upplands-Bro hade redan rik baseline coverage (41 events) genom kommunens omfattande sommarlovsprogram. Round 2 lagt till signaturmål från regionens unika besöksverksamheter:

Höjdpunkter:
- **Accropark Bro Höghöjdsbanan** — klättra mellan träden med 12 m höjder för barn från 4 år
- **Hällkana badplats** — fullt friluftsbad vid Lejondalssjön med lekplats grill bastu beachvolley
- **Summer Classics Bro Park 10-årsjubileum** — Stockholms Stora Pris och klassiska galopplopp
- **Hästsportens dag Bro Park** — galopp + trav på samma bana fri entré
- **SMAKA på Upplands-Bro** — folkfest med foodtrucks ponnyridning Fritidsbanken
- **Upplands-Bro Swimrun** — 17 km lopp genom fyra sjöar
- **Midsommarfirande Bro IP** — traditionellt midsommar med kransbindning

Coverage now considered **FULL** per Rule #10.6 för accessible image-rich Upplands-Bro family-event ecosystem as of 2026-06-10.

Sources:
- [Upplands-Bro evenemangskalender](https://www.upplands-bro.se/evenemangskalender.html)
- [Visit Upplands-Bro evenemang](https://visitupplandsbro.com/evenemang/)
- [Accropark Bro](https://www.accropark.se/bro)
- [Hällkana badplats](https://www.upplands-bro.se/uppleva-och-gora/badplatser/hallkana.html)
- [Svensk Galopp Bro Park](https://www.svenskgalopp.se/banor-evenemang/bro-park/)
- [Summer Classics Bro Park](https://www.svenskgalopp.se/kalendarium/2026-06-14-summer-classics/)
- [Floristhörnan SMAKA event](https://www.floristhornan.se/event/smaka-pa-upplands-bro/)
- [Upplands-Bro Swimrun](https://www.upplandsbroswimrun.org/)
- [Bro IK Broiken Football Camp](https://www.broik.se/broik-fotboll-broikenfootballcamp)
