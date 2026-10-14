# Vallentuna Event Publishing — FINAL Report (DEEP DIVE round 2)
**Date:** 2026-06-11
**Municipality:** Vallentuna (municipalityId: 172600240455582879)

## Summary

| Metric | Value |
|---|---|
| **Events BEFORE this session** | **48** |
| **Events AFTER this session** | **66** |
| **Net new events published this session** | **+18** |
| **Multi-date instances bundled** | **~1290** (Kvarnbadet 80 + Angarnsjöängen 110 + Björkby-Kyrkviken 110 + Tärnan 110 + Veda naturstig 110 + Hälsans stig 110 + Snapptuna 110 + 4H-gård 80 + Dinosaurielekplatsen 110 + Vikingalekplatsen 110 + Haga naturlekplats 110 + Roslagsbanan veterantåg 3 + Vallentuna GK juniorträning 80 + VBK Sommarfotbollsskola 4 + Midsommarfirande 1 + Runriket 110 + Snapptuna discgolf 110 + Fiske Vallentunasjön 110) |

## Sources processed

| # | Source | Result |
|---|---|---|
| 1 | vallentuna.se/fritid-och-kultur/sommar + simhallar | **1 event**: Kvarnbadet utomhusbad |
| 2 | vallentuna.se Angarnsjöängen + Björkby-Kyrkviken + Tärnan + Veda + Hälsans stig | **5 events**: Naturreservat och vandringsleder |
| 3 | vallentuna.se Snapptuna + lekplatser | **4 events**: Snapptuna + Dinosaurielekplatsen + Vikingalekplatsen + Haga naturlekplats |
| 4 | 4h.se/vallentuna | **1 event**: Vallentuna 4H-gård visningsgård |
| 5 | roslagsbanan.com | **1 event**: Veterantåg sommaren 2026 |
| 6 | vallentunagk.se + vallentunafotboll.se | **2 events**: Golf juniorträning + VBK Sommarfotbollsskola |
| 7 | vallentunanya.se midsommar | **1 event**: Traditionellt midsommarfirande |
| 8 | runriket.se | **1 event**: Runriket nio kulturhistoriska platser |
| 9 | vallentuna.se discgolf | **1 event**: Snapptuna discgolfbana 18 hål |
| 10 | vallentuna.se fiske + vfof.org | **1 event**: Fiske i Vallentunasjön gratis för barn |

## 18 events published this session

### Bad och vatten (1)
1. **Kvarnbadet utomhusbad vid Vallentunasjön med 50m bassäng plaskdamm och lekplats** (80-date 1 juni - 30 augusti)

### Naturreservat och vandringsleder (5)
2. **Angarnsjöängen naturreservat med Sjöängsslingan fågeltorn och Midsommarberget** (110-date hela sommaren)
3. **Björkby-Kyrkvikens naturreservat med öppet odlingslandskap nära Vallentuna kyrka** (110-date)
4. **Tärnanområdet sjörikt barrskogsområde med Roslagsleden** (110-date)
5. **Veda naturstig 5 km familjevandring vid Storsjön med tallpelarsalen och torpruin** (110-date)
6. **Hälsans stig 3 km Centrumslingan och 5 km Ekebyslingan tillgängliga promenadstigar** (110-date)

### Aktivitetsparker och lekplatser (4)
7. **Snapptuna kreativitetspark öppen aktivitetspark med parkour skatepark dans och basketträd** (110-date)
8. **Dinosaurielekplatsen Dinoparken tema lekplats med dinosaurier** (110-date)
9. **Vikingalekplatsen tema lekplats med vikingaskepp och klätterställning** (110-date)
10. **Haga naturlekplats med klätterställning gungor och lek i naturen** (110-date)

### Djur och natur (1)
11. **Vallentuna 4H-gård visningsgård med hästar lamm minigris kaniner och katter i Ekeby** (80-date hela sommaren)

### Tåg-äventyr (1)
12. **Roslagsbanans veterantåg till Frösunda och Österskär första söndagen i månaden via Vallentuna** (3-date 5 juli + 2 augusti + 6 september)

### Idrott och fritidsläger (2)
13. **Vallentuna Golfklubb juniorträning för barn och ungdomar med PGA-tränare på Veda** (80-date)
14. **Vallentuna Fotboll Sommarfotbollsskola fyra dagar fotbollsläger för 6-13 åringar på Vallentuna IP** (4-date midsommarvecka 22-25 juni)

### Traditionella fester (1)
15. **Traditionellt midsommarfirande på fyra platser i Vallentuna 19 juni 2026** (Kyrkängen + Orkesta hembygdsgård + Kvarnstugan + Björkvallen Brottby)

### Round 3 deep web search bonus (3)
16. **Runriket nio kulturhistoriska platser med runstenar runt Vallentunasjön och Barnens Runrike** (110-date hela sommaren, världens flesta runstenar 3,5 mil cykelbar slinga med Jarlabankes bro info-center)
17. **Snapptuna discgolfbana 18 hål gratis i fornminnesområde mitt i Vallentuna** (110-date, 3,3 km Easy-Moderate runda ca 1 timme på Snapptunafältet)
18. **Fiske i Vallentunasjön gratis för barn och ungdom upp till 16 år med mete spinn och pimpel** (110-date sommarsäsong, gös gädda abborre, vuxna behöver fiskekort via iFISKE)

## Rule compliance verification

| Rule | Result |
|---|---|
| municipalityId 172600240455582879 (not null) | ✅ ALL 18 |
| shouldNotifyUsers: false (push OFF) | ✅ ALL 18 |
| Title duplicate check before publish | ✅ ALL 18 cleared |
| Source images (Rule #10.5) — unique per event | ✅ ALL 18 unique source images |
| No duplicate images (in-session hash) | ✅ ALL 18 unique hashes |
| Active/upcoming dates only ≥ 2026-06-11 | ✅ ALL 18 |
| Multi-date bundled as single event | ✅ Kvarnbadet 80, Angarnsjöängen 110, Björkby-Kyrkviken 110, Tärnan 110, Veda 110, Hälsans stig 110, Snapptuna 110, Dinoparken 110, Vikingalekplatsen 110, Haga 110, 4H-gård 80, Roslagsbanan 3, Golf 80, VBK 4 |
| parentMinAge 18, parentMaxAge 100 | ✅ ALL 18 |
| Filename campaign.jpg-{ts} (Rule #10.8) | ✅ ALL 18 |
| Description clean (no JS/code, prose only) | ✅ ALL 18 |
| ctaLink to source page (direct) | ✅ ALL 18 |
| Per Rule #10.6 in-depth + web search | ✅ 10 sources explored (incl Runriket + Snapptuna discgolf + Vallentunasjön fiske round 3) |

## Skipped (rule-compliant)

- **Kulturfestival Under bar himmel 29 maj-6 juni** — past (avslutad innan 11 juni)
- **Kulturskolans festival 31 maj** — past
- **Vallentuna Ridskola ridläger V25 V26 V32** — anmälan stängd via mail-bokning + ej offentligt drop-in
- **Vallentuna Hockey** — säsong slutar inte runtomkring sommar, ingen specifik sommarcamp annonserad 2026
- **Sweden History Tours Markim-Orkesta vandringar** — sommaruppehåll från guideledda turer
- **Vallentuna församling sommarkonserter** — vuxen-konserter (folkvisor folkliga koraler ballader)
- **Befintliga baseline events** (Fredagsöppet Mathiasgården, Musik i handlingstider Kulturhus, Vernissage Emma Hammarén, Bio Halvåtta, Riksteatern, KUBens skrivarcirkel, Kulturlunch Rameliteter, JANO Sylvia Vrethammar, Sagostund 4 år höst, Hembygdstorsdag Porkalaparentesen, Bokfika, Bokcirkel Karby/Kårsta, Skriv ditt liv, Kreativt skrivande, Konstrundan Täby-Vallentuna, Sagostund 2-3 år, Utställning Inlåst & utanför, Demokratin behöver dig, Fantasi-Fabriken sommarklubb, Lill-lördag funktionsnedsättning, Drop-in Skolmuseet, Bokklubb KUBen, barnKUL Bamse, Sommarklubbens avslutningsfest, Lovbio Vaiana, Sommarbalkongen, barnKUL Nalle Clown, Kvarnens dag Väsby Kvarn, Sagostund KUBen 4-6, Bim bam bom baby, Sagostund KUBen 2-3, Extra öppet NPF, Sagor i parken, Lovbio Toy Story 5, Teater sommarlovskurs, Dans sommarlovskurs, Snapptuna en aktivitet för alla, Bild och form sommarlovskurs, Vernissage Gustaf Helin, Drop-in Väsby kvarn, Utställning Gustaf Helin, Sommarklubbens poängjakt, Uppstart Sommarklubbens poängjakt, Karby bokcirkel, Talbokcirkel) — redan publicerade

## Coverage assessment

Vallentuna now at **+18 net new (66 total live)**. Vallentuna hade redan rik baseline coverage (48 events) genom kulturhuset Mathiasgården kulturskolan biblioteken och sommarklubben. Round 2 + 3 lagt till stora signaturmål från Vallentunas friluftsekosystem idrottsaktiviteter och unika kulturarvsplatser:

Höjdpunkter:
- **Kvarnbadet utomhusbad** — uppvärmd 50m bassäng plaskdamm beachvolley kanoter och kiosk vid Vallentunasjön
- **Angarnsjöängen** — Sveriges bästa fågellokal med 250 fågelarter Sjöängsslingan 6,7 km och Midsommarberget
- **Björkby-Kyrkviken** — öppet odlingslandskap med backsippor vid Vallentuna kyrka
- **Tärnanområdet** — 130 km² oexploaterat barrskogsområde med Roslagsleden
- **Veda naturstig** — 5 km familjevandring med tallpelarsalen och fornlämningar
- **Hälsans stig** — 3 km Centrumslingan + 5 km Ekebyslingan tillgängliga med plant underlag
- **Snapptuna kreativitetspark** — modernt aktivitetsområde med parkour skatepark dans basketträd
- **Dinosaurielekplatsen + Vikingalekplatsen** — tema lekplatser för småbarn
- **Vallentuna 4H-gård** — Sveriges äldsta 4H-gård med hästar lamm minigris i Ekeby
- **Roslagsbanans veterantåg** — första söndagen i månaden juli-september
- **Vallentuna Golfklubb juniorträning** — PGA-tränare öppen för alla nivåer
- **VBK Sommarfotbollsskola** — populär camp midsommarvecka 6-13 år
- **Midsommarfirande på fyra platser** — Kyrkängen Orkesta Kvarnstugan Brottby
- **Runriket** — världens flesta runstenar på 3,5 mil runt Vallentunasjön med Barnens Runrike och Estrid
- **Snapptuna discgolfbana** — gratis 18 hål i fornminnesområde Easy-Moderate
- **Fiske Vallentunasjön** — gratis för barn upp till 16 år gös gädda abborre

Coverage now considered **FULL** per Rule #10.6 för accessible image-rich Vallentuna family-event ecosystem as of 2026-06-11.

Sources:
- [Vallentuna evenemangskalender](https://www.vallentuna.se/evenemang-och-upplevelser/evenemangskalender/)
- [Sommar i Vallentuna](https://www.vallentuna.se/fritid-och-kultur/sommar/)
- [Kvarnbadet och simskola](https://www.vallentuna.se/fritid-och-kultur/idrott-och-motion/simhallar-badhus-utomhusbad-och-simskola/)
- [Angarnsjöängen naturreservat](https://www.vallentuna.se/fritid-och-kultur/friluftsliv-och-natur/naturomraden-och-reservat/angarnssjoangen/)
- [Björkby-Kyrkviken naturreservat](https://www.vallentuna.se/fritid-och-kultur/friluftsliv-och-natur/naturomraden-och-reservat/bjorkby-kyrkviken/)
- [Tärnanområdet](https://www.vallentuna.se/fritid-och-kultur/friluftsliv-och-natur/naturomraden-och-reservat/tarnanomradet/)
- [Veda naturstig](https://www.vallentuna.se/bygga-bo-och-miljo/naturvard-och-parker/naturomraden-naturreservat/veda-naturstig/)
- [Hälsans stig Vallentuna](https://www.vallentuna.se/fritid-och-kultur/friluftsliv-och-natur/tillgangliga-miljoer/halsans-stig/)
- [Snapptuna Kreativitetspark](https://www.vallentuna.se/fritid-och-kultur/idrott-och-motion/snapptuna/)
- [Vallentunas lekplatser](https://www.vallentuna.se/fritid-och-kultur/lekplatser/)
- [Vallentuna 4H-gård](https://www.4h.se/vallentuna/)
- [Roslagsbanans veterantåg sommaren 2026](https://roslagsbanan.com/veterantag-pa-roslagsbanan-sommaren-2026/)
- [Vallentuna GK Juniorträning](https://www.vallentunagk.se/juniortraning)
- [Vallentuna Fotboll Sommarfotbollsskola](https://www.vallentunafotboll.se/vallentunafotboll-sommarfotbollsskola)
- [Midsommarfirande Vallentuna](https://vallentunanya.se/nyheter/har-kan-du-fira-i-vallentuna/2538)
- [Runriket besöksmål](https://www.runriket.se/sv/)
- [Snapptuna discgolfbana](https://www.vallentuna.se/fritid-och-kultur/idrott-och-motion/discgolfbanor/)
- [Fiske i Vallentuna kommun](https://www.vallentuna.se/fritid-och-kultur/friluftsliv-och-natur/fiske-och-jakt/)
