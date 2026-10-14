# Stockholm Event Publishing — FINAL Report (DEEP DIVE round 2)
**Date:** 2026-06-10
**Municipality:** Stockholm (municipalityId: 172600240455582872)

## Summary

| Metric | Value |
|---|---|
| **Events BEFORE this session** | **90** |
| **Events AFTER this session** | **113** |
| **Net new events published this session** | **+23** |
| **Multi-date instances bundled** | **~400+** (most events bundled as "hela sommaren" säsongsbundles 60-80 dagar var) |

## Sources processed

| # | Source | Result |
|---|---|---|
| 1 | stadsmuseet.stockholm.se | **1 event**: Barnspår på Stadsmuseet med Stora tidsresan + Lilla djurspåret |
| 2 | gronalund.com | **1 event**: Gnutt-föreställning och Gnuttdisco för barnfamiljer |
| 3 | abbathemuseum.com | **1 event**: ABBA The Museum interaktiv musikupplevelse |
| 4 | bergianska.se | **1 event**: Bergianska trädgården med Victoriahuset + Edvard Andersons växthus |
| 5 | tekniskamuseet.se | **2 events**: Matematikträdgården utomhus, Teknoleket för yngre barn |
| 6 | sjohistoriska.se | **1 event**: Sjöhistoriska museet på Djurgården |
| 7 | historiska.se | **1 event**: Vikingasommar med vikingagård |
| 8 | modernamuseet.se | **1 event**: Familjevisningar och drop-in Verkstan |
| 9 | nordiskamuseet.se | **1 event**: Lekstugan interaktiv bondgårdslek |
| 10 | armemuseum.se | **1 event**: Rädd eller beredd utställning |
| 11 | skansen.se | **2 events**: Barnaktiviteter Oktorpsgården, Prova på drejning Krukmakeriet |
| 12 | nationalmuseum.se | **1 event**: Sergel fantasi och verklighet utställning |
| 13 | ekonomiskamuseet.se | **1 event**: Ekonomilabbet + barnspår |
| 14 | etnografiskamuseet.se | **1 event**: Sommar i Etnografiska museets park |
| 15 | hallwylskamuseet.se | **1 event**: Guidade palatsvisningar |
| 16 | waldemarsudde.se | **1 event**: Prins Eugens Waldemarsudde konstmuseum |
| 17 | liljevalchs.se | **1 event**: When We See Us samtidskonst utställning |

## 19 events published this session

### Stockholms egna museer (4)
1. **Barnspår på Stockholms Stadsmuseum med Stora tidsresan och Lilla djurspåret** (hela sommaren)
2. **Ekonomilabbet och barnspår på Ekonomiska museet med fri entré för barn** (hela sommaren)
3. **Guidade palatsvisningar på Hallwylska museet kulturhistoriskt palats** (hela sommaren)
4. **Armémuseum interaktiv utställning Rädd eller beredd för hela familjen** (hela sommaren)

### Djurgårdens museer (8)
5. **ABBA The Museum interaktiv musikupplevelse på Djurgården** (1 juni-16 augusti dagligen 9-20)
6. **Sjöhistoriska museet på Djurgården för hela familjen** (hela sommaren fri entré)
7. **Vikingasommar på Historiska museet med vikingagård** (hela sommaren)
8. **Lekstugan interaktiv bondgårdslek för barn på Nordiska museet** (hela sommaren från 5 år)
9. **Sommar i Etnografiska museets park med utställningar tehus och Matmekka** (hela sommaren)
10. **Prins Eugens Waldemarsudde konstmuseum på Djurgården** (hela sommaren)
11. **When We See Us samtidskonst utställning på Liljevalchs konsthall** (till 30 augusti)
12. **Bergianska trädgården med Victoriahuset och Edvard Andersons växthus** (hela sommaren)

### Tekniska + lärande (2)
13. **Matematikträdgården utomhuslekplats med matematik på Tekniska museet** (hela sommaren fri)
14. **Teknoleket lekfull värld för nyfikna barn på Tekniska museet** (hela sommaren)

### Skansen extra (2)
15. **Barnaktiviteter på Oktorpsgården halländsk gård 1870-tal** (hela sommaren)
16. **Prova på drejning på Krukmakeriets veranda på Skansen** (hela sommaren)

### Centrala Stockholm (3)
17. **Gnutt-föreställning och Gnuttdisco på Gröna Lund för barnfamiljer** (hela sommaren)
18. **Familjevisningar och drop-in Verkstan på Moderna Museet** (hela sommaren)
19. **Sergel fantasi och verklighet utställning på Nationalmuseum** (till 9 augusti)

### Round 3 deep web search bonus (4)
20. **Stockholms Kulturfestival fem dagar med fri entré i innerstaden** (12-16 augusti, Skeppsbron + Slottsbacken + Slussen + Sergels torg + UNG Kulturfestival)
21. **Postis interaktiv barnutställning på Postmuseum i Gamla stan** (hela sommaren, slottid bokning)
22. **Tantolunden park på Södermalm med badplats och 100 koloniträdgårdar** (hela sommaren, badsäsong 21 juni-15 augusti)
23. **Sommarlov på Polismuseet med Polisliv visningar och Här är polisen** (15 juni-16 augusti dagliga visningar)

## Rule compliance verification

| Rule | Result |
|---|---|
| municipalityId 172600240455582872 (not null) | ✅ ALL 23 |
| shouldNotifyUsers: false (push OFF) | ✅ ALL 23 |
| Title duplicate check before publish | ✅ ALL 23 cleared |
| Source images (Rule #10.5) — unique per event | ✅ ALL 23 unique source images |
| No duplicate images (in-session hash) | ✅ ALL 23 unique hashes |
| Active/upcoming dates only ≥ 2026-06-10 | ✅ ALL 23 |
| Multi-date bundled as single event | ✅ Alla bundlade som hela sommaren-evenemang |
| parentMinAge 18, parentMaxAge 100 | ✅ ALL 23 |
| Filename campaign.jpg-{ts} (Rule #10.8) | ✅ ALL 23 |
| Description clean (no JS/code, prose only) | ✅ ALL 23 |
| ctaLink to source page (direct) | ✅ ALL 23 |
| Per Rule #10.6 in-depth + web search | ✅ 21 sources explored (incl Kulturfestival + Postmuseum + Tantolunden + Polismuseet round 3) |

## Skipped (rule-compliant)

- **Medeltidsmuseet** — stängt för flytt
- **Spårvägsmuseet** — webbplats timed out, ej tillgänglig
- **Fotografiska** — mestadels vuxen konstfoto utan barnsfokus
- **Brunch med Gnuttarna** — 404 sida
- **Vårsalongen 2026 på Liljevalchs** — pågår till 3 maj, redan slut
- **Curatorvisning Brassaï på Moderna** — vuxen-curator
- **Vernissage Blir du lönsam, lille vän** — vuxen-vernissage
- **Operagala Jussi Björling, Lena Willemark Confidencen** — vuxen-konsert
- **Befintliga baseline events** (Vasamuseet, Cosmonova, Kulturhuset, Junibacken, Marionetteatern, Skansens marknader, Strawberry Arena-konserter, alla 90 baseline-events) — redan publicerade

## Coverage assessment

Stockholm now at **+23 net new (113 total live)**. Stockholm är Sveriges huvudstad med ett enormt utbud av museer och kulturella destinationer. Round 2 lagt till tunga signaturmål från Stockholms museilandskap:

Höjdpunkter:
- **ABBA The Museum** — dagligen 9-20 hela sommaren, interaktiv musikupplevelse
- **Vikingasommar Historiska museet** — vikingagård utomhus + Guldrummet
- **Bergianska trädgården** — Victoriahuset med jättenäckrosor + Edvard Andersons växthus
- **Stadsmuseet Barnspår** — Stora tidsresan + Lilla djurspåret
- **Lekstugan Nordiska museet** — interaktiv 1870-tals bondgård
- **Hallwylska museet** — palatsvisningar från sekelskiftet 1900
- **Etnografiska parken** — Tehuset + Matmekka + utomhusterass
- **Waldemarsudde** — prinsens hem med Galleriterassen
- **Liljevalchs When We See Us** — afrikansk diaspora samtidskonst
- **Matematikträdgården Tekniska** — fri utomhuslekplats
- **Teknoleket** — för yngre barn på Tekniska
- **Drejning på Skansen** + **Oktorpsgården** — extra Skansenaktiviteter
- **Sjöhistoriska** + **Armémuseum** + **Ekonomiska museet** — fri entré
- **Moderna Verkstan** + **Sergel Nationalmuseum** — konsthus
- **Gnutt-disco Gröna Lund** — barnfamiljshow

Coverage now considered **FULL** per Rule #10.6 för accessible image-rich Stockholm family-museum ecosystem som komplement till baseline-events.

Sources:
- [Stockholms Stadsmuseum Barnspår](https://stadsmuseet.stockholm/visningar-och-stadsvandringar/pa-egen-hand/for-barn/)
- [Gröna Lund familjeföreställningar](https://www.gronalund.com/familjeforestallningar)
- [ABBA The Museum](https://abbathemuseum.com/)
- [Bergianska trädgården](https://www.bergianska.se/)
- [Tekniska museet Matematikträdgården](https://www.tekniskamuseet.se/upplev/utstallningar/matematiktradgarden/)
- [Tekniska Teknoleket](https://www.tekniskamuseet.se/upplev/utstallningar/teknoleket/)
- [Sjöhistoriska museet](https://www.sjohistoriska.se/)
- [Historiska museet Vikingasommar](https://historiska.se/)
- [Moderna Museet familjeprogram](https://www.modernamuseet.se/sv/stockholm/program/familjesondagar-pa-moderna-museet/)
- [Nordiska museet Lekstugan](https://www.nordiskamuseet.se/utstallningar/lekstugan/)
- [Armémuseum](https://www.armemuseum.se/)
- [Skansen Oktorpsgården](https://www.skansen.se/se-och-gora/friluftsmuseum/barnaktiviteter-pa-oktorpsgarden/)
- [Skansen drejning](https://www.skansen.se/kalender/)
- [Nationalmuseum](https://www.nationalmuseum.se/)
- [Ekonomiska museet](https://ekonomiskamuseet.se/for-barn-och-familj/)
- [Etnografiska museet](https://www.etnografiskamuseet.se/)
- [Hallwylska museet](https://www.hallwylskamuseet.se/)
- [Prins Eugens Waldemarsudde](https://www.waldemarsudde.se/)
- [Liljevalchs konsthall](https://liljevalchs.se/kalender/)
- [Stockholms Kulturfestival](https://kulturfestivalen.stockholm.se/)
- [Postmuseum Postis](https://postmuseum.se/)
- [Tantolunden park](https://parker.stockholm/parker/tantolunden/)
- [Polismuseet sommarlov](https://polismuseet.se/besok-polismuseet/sommar-pa-polismuseet/)
