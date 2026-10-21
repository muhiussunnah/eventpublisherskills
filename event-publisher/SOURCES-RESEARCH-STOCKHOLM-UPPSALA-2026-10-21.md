# Source research — Stockholm län + Uppsala (2026-10-21)

**Why:** CEO said we are missing big sources and asked *"which are the biggest sources/URLs where we can find info about temporary events?"* (he pointed at Barnistan as the model — "we published almost everything from them").

**What was done:** 5 parallel research agents checked all 27 cities (city → existing URLs from the sheet as input), fetched every candidate on 2026-10-21 and kept only pages that list **current/upcoming** family events or are strong **permanent-place** lists. Then de-duplicated against the 176 existing URLs.

**Sheet:** `Weekly_Events_Update` → tab **Events_Update** (gid=0). A = Source URL, B = City (first row of each city bold), C = **Total Sources Amount** (`=COUNTIF(B$2:B;B<row>)` on each city's first row). **Light-green rows = new sources added 2026-10-21.** Old rows kept first, new rows below them per city. Stray yellow fill that sat on empty rows below the old list end was cleared.

## Totals

- Before: **176** sources · Removed dead: **2** · Added: **197** · After: **371**

| City | Total sources | New |
|---|---:|---:|
| Botkyrka | 17 | 10 |
| Danderyd | 6 | 3 |
| Ekerö | 11 | 7 |
| Haninge | 10 | 5 |
| Huddinge | 18 | 12 |
| Järfälla | 16 | 8 |
| Lidingö | 10 | 4 |
| Nacka | 16 | 9 |
| Norrtälje | 14 | 6 |
| Nykvarn | 7 | 5 |
| Nynäshamn | 7 | 4 |
| Österåker | 13 | 6 |
| Salem | 7 | 4 |
| Sigtuna | 19 | 11 |
| Sollentuna | 12 | 7 |
| Solna | 16 | 8 |
| Stockholm | 36 | 24 |
| Sundbyberg | 11 | 4 |
| Södertälje | 20 | 10 |
| Täby | 11 | 4 |
| Tyresö | 17 | 7 |
| Upplands-Bro | 13 | 6 |
| Upplands Väsby | 13 | 7 |
| Vallentuna | 9 | 4 |
| Vaxholm | 9 | 4 |
| Värmdö | 10 | 4 |
| Uppsala | 23 | 14 |
| **All** | **371** | **197** |

## Answer for the CEO — biggest sources for temporary family events

1. **Kommun "lov" pages** (höstlov/sportlov/jullov/påsklov/sommarlov) — the single biggest win: Södertälje Kulturlovet (61), Botkyrka Lov (59), Stockholm stad höstlov category (350+ in lov week), Järfälla lovaktiviteter (40), Sollentuna (30), Tyresö (24). Re-check them **before every school holiday** — the URL often carries the year.
2. **Stockholm stad city-wide calendar** `start.stockholm/aktuellt` filtered on Barn och familj + Parklek + Kulturskolan (109 now; every stadsdel, parklekar, Stadshuset, Stadsmuseet, Medeltidsmuseet).
3. **KUBIK Uppsala** (230 activities for children/youth) + Biotopia, UKK familj, Uppsala konstmuseum, Slottshistoriska, Uppsala universitet family filter.
4. **Kommun calendars we were missing or had broken:** Huddinge Kommunkalender (152), Vallentuna new calendar URL (139), Sigtuna full calendar `kalender.sigtuna.se` category Barn och familj (44; old URL only showed ~9 teasers).
5. **Visit Roslagen — Barn & familj category** (60, covers Österåker + Norrtälje).
6. **Barnistan area pages** (Nacka/Värmdö, Haninge/Nynäshamn, Uppsala) and Barnistan teater list.
7. **Museum/culture calendars with family filters:** Kungliga slotten (Familj/För barn), Skansen, Junibacken, Tekniska, Moderna, Nationalmuseum, Nordiska, Etnografiska, Polismuseet, Konserthuset 0–5 år, Berwaldhallen, Dockteatern Tittut, Teater Bristol (82 barnteater shows).
8. **Permanent places:** kommun lekplats/badplats/utflykt pages + Naturkartan city guides (Stockholm parker.stockholm lists 498 lekplatser/parklekar/plaskdammar).

## Top 25 new sources by number of upcoming items seen

| # | City | Source | Type | Family | Items |
|---:|---|---|---|---|---:|
| 1 | Stockholm | [Stockholms stad – Hitta lekplatser, parklekar och plaskdammar](https://parker.stockholm/hitta-lekplatser-parklekar-plaskdammar/) | kommun | high | 498 |
| 2 | Uppsala | [Tickster – evenemang i Uppsala](https://www.tickster.com/se/sv/events/in/uppsala) | ticketing | low | 308 |
| 3 | Uppsala | [KUBIK Uppsala – hitta aktiviteter för barn och unga](https://www.kubikuppsala.se/hitta-aktiviteter/) | aggregator | high | 230 |
| 4 | Huddinge | [Huddinge kommun – Kommunkalender (På gång i Huddinge)](https://www.huddinge.se/kommunkalender) | kommun | high | 152 |
| 5 | Vallentuna | [Vallentuna kommun – Evenemang (ny kalender-URL)](https://www.vallentuna.se/uppleva-och-gora/evenemang-och-motesplatser/evenemang) | kommun | high | 139 |
| 6 | Stockholm | [Stockholms stad – Kalendarium (Barn och familj + Parklek + Kulturskol…](https://start.stockholm/aktuellt/?t=event&c=279&c=885&c=760) | kommun | high | 109 |
| 7 | Sundbyberg | [Teater Bristol – barnteater i Sundbyberg](https://www.teaterbristol.se/) | teater | high | 82 |
| 8 | Södertälje | [Södertälje kommun – Kulturlovet (höstlovsprogram)](https://www.sodertalje.se/kultur-och-fritid/kulturlov/) | kommun | high | 61 |
| 9 | Österåker | [Visit Roslagen – evenemang kategori Barn & familj](https://roslagen.se/evenemang-2/kategori/barn-familj/) | visit | high | 60 |
| 10 | Botkyrka | [Botkyrka kommun – Lov i Botkyrka (höstlov 2026)](https://www.botkyrka.se/uppleva-och-gora/fritid-och-aktiviteter/lov-i-botkyrka) | kommun | high | 59 |
| 11 | Solna | [Lekplatser i Solna](https://www.solna.se/uppleva--gora/for-barn-och-unga/lekplatser-i-solna) | kommun | high | 46 |
| 12 | Lidingö | [Lidingö stad – Lekparker](https://lidingo.se/kultur-fritid/aktiviteter-for-barn-och-unga/lekparker/) | kommun | high | 44 |
| 13 | Sigtuna | [Sigtuna kommuns kalender – Barn och familj (full kalender)](https://kalender.sigtuna.se/events?by_categories=2780) | kommun | high | 44 |
| 14 | Järfälla | [Upplev Järfälla – Lovaktiviteter (läslov v44)](https://upplevjarfalla.se/lovaktiviteter) | kommun | high | 40 |
| 15 | Norrtälje | [Biblioteken i Norrtälje – evenemang](https://bibliotek.norrtalje.se/evenemang) | bibliotek | high | 40 |
| 16 | Sigtuna | [Gröna Ladan – biograf i Sigtuna stad](https://www.gronaladan.se/) | other | high | 40 |
| 17 | Stockholm | [Kungliga slotten – kalendarium (Familj/För barn, Kungliga slottet + K…](https://www.kungligaslotten.se/kalendarium.html?kategorier%5B%5D=Familj&kategorier%5B%5D=F%C3%B6r+barn&kategorier%5B%5D=H%C3%B6stlov&besoksmal%5B%5D=4.46ca39931600d1b7b981945&besoksmal%5B%5D=4.3ced9ede1817ff2e17c1cabb&besoksmal%5B%5D=4.46ca39931600d1b7b98198f) | museum | high | 31 |
| 18 | Danderyd | [Danderyds kommun – Lekplatser](https://www.danderyd.se/uppleva-och-gora/idrott-motion-och-friluftsliv/friluftsliv/lekplatser/) | kommun | medium | 30 |
| 19 | Järfälla | [Huset på höjden – veckoschema (kultur- och aktivitetshus, Jakobsberg)](https://www.jarfalla.se/fritidochkultur/kulturochnojen/husetpahojden.4.4b149fc016400a9f7871223b.html) | kulturhus | high | 30 |
| 20 | Sollentuna | [Höstlov i Sollentuna – lovaktiviteter (kommun)](https://www.sollentuna.se/uppleva--gora/aktiviteter-pa-loven/) | kommun | high | 30 |
| 21 | Stockholm | [Moderna Museet Stockholm – kalender](https://www.modernamuseet.se/sv/stockholm/kalender/) | museum | high | 30 |
| 22 | Uppsala | [Uppsala konstmuseum – kalendarium](https://konstmuseum.uppsala.se/kalendarium/) | museum | medium | 30 |
| 23 | Uppsala | [Biotopia – kalender (inkl. Upplandsstiftelsen/Hammarskog)](https://biotopia.nu/kalender/) | museum | high | 28 |
| 24 | Stockholm | [Etnografiska museet – kalendarium Barn & Familj](https://www.etnografiskamuseet.se/kalendarium/barn--familj/) | museum | high | 25 |
| 25 | Södertälje | [Futurum Järna – Aktiviteter (kulturhus: bibliotek, kulturskola, friti…](https://www.sodertalje.se/kultur-och-fritid/futurum/aktiviteter-pa-futurum/) | kulturhus | high | 25 |

## Fixed / replaced / flagged

- **Lidingö** old kommun calendar URL returned 404 → removed; replaced by `lidingo.se/kultur-fritid/evenemangskalendern/` with the *barn* keyword filter.
- **Vallentuna** old calendar URL redirected away → removed; new kommun calendar `vallentuna.se/uppleva-och-gora/evenemang-och-motesplatser/evenemang` (139 events).
- **Sigtuna** `sigtuna.se/evenemang.html` (kept) shows only ~9 teasers — the real list is `kalender.sigtuna.se` (category 2780 Barn och familj, 2779 Lovaktivitet).
- **Tom Tits Experiment** (Södertälje) — tomtit.se refused/timed out from our network every time, so it is listed but **not verified**; the place is open (Destination Södertälje + Barnistan reference it).

## Rejected (do not add)

- allevents.in — 403 / Cloudflare. · Kidsinfo — domain dead. · hembygd.se — Cloudflare block.
- Westfield Täby Centrum / Nacka Forum event pages — 0 events. · Reginateatern — closed autumn 2026.
- Barnistan has **no** area page for many suburbs (only the main Stockholm list + a few areas) — use the area pages where they exist.

## All new sources per city (best first)

### Botkyrka — 17 total (10 new)

- **Botkyrka kommun – Lov i Botkyrka (höstlov 2026)** — kommun, gives events, family high, ~59 items  
  https://www.botkyrka.se/uppleva-och-gora/fritid-och-aktiviteter/lov-i-botkyrka  
  e.g. Bokäventyr med Sofia Tångelin + klapphage, Hågelbyparken 28 okt; lovbio 'Aya och häxan' 26 okt; Skapa med lera i Botkyrka konsthall  
  _A seasonal page rewritten before every lov. It has about 59 dated activities from many organisers: Subtopia, Cirkus Cirkör, MKC, Tumba bruksmuseum, simhallar, Riksteatern, idrottsföreningar, bibliotek and Hågelby 4H. Each item has Info/Ålder/Tid/Plats fields…_
- **Upplev Botkyrka – Kalendarium (Hågelbyparken, Lida, Subtopia, Vårstavi)** — visit, gives events, family high, ~14 items  
  https://www.upplevbotkyrka.se/kalendarium/  
  e.g. Eldshow på höstlovet, Lida 28 okt; Ugglejakt i ficklampssken, Lida 29 okt; Julmarknad Hågelbyparken 28–29 nov  
  _The kommun-owned company's combined calendar for the big family destinations, with a filter per venue. Event pages live on hagelby.se/evenemang/, lida.se/evenemang/ and varstavi.se/evenemang/._
- **Mångkulturellt centrum (MKC), Fittja – Kalendarium** — museum, gives events, family medium, ~6 items  
  https://mkcentrum.se/kalendarium/  
  e.g. Storytelling och Stop Motion 27 okt; Kollektivt konstkaos i Verkstan 28 okt; Lovbio med Fittja bibliotek 29 okt  
  _Has category filters: Lovaktiviteter, Öppen verkstad, Lördagsöppet, Film. Around lov it runs free family workshops. It also lists adult talks and conferences._
- **Tumba bruksmuseum – Kalender** — museum, gives both, family medium, ~4 items  
  https://tumbabruksmuseum.se/pa-gang/kalender/  
  e.g. Höstlov 24 okt–1 nov (fri entré för barn); Bebishänder – avtryck i papper 23 okt & 27 nov; familjeutställning 'Från spargris till Swish'  
  _Has a category filter (Familjeaktivitet, Workshop, Visning) and a lov page at /pa-gang/lov/. It is a family-friendly museum (brandstation, gamla skolan). Request with Accept text/html, because the site returns raw JSON if application/json is accepted._
- **Subtopia (Alby) – Kalendarium** — kulturhus, gives events, family medium, ~5 items  
  https://subtopia.se/kalendarium/  
  e.g. Söndagsöppet 25 okt, 15 nov, 29 nov (gratis aktiviteter för alla åldrar med Cirkus Cirkör & Fanzingo); FEAR höstlovskurs 10–14 år; Kongo Groove Festival 31 okt  
  _A culture centre in Alby, home of Cirkus Cirkör. The calendar is short but 'Söndagsöppet' is a recurring free family day. Its events also appear in the Upplev Botkyrka calendar._
- **Hågelbyparken – Evenemang (folkpark med 4H-gård)** — park, gives both, family medium, ~4 items  
  https://hagelby.se/evenemang/  
  e.g. Film 'Aya och häxan' 26 okt; Klapphage på Hågelby 4H-gård 26 & 28 okt; Julmarknad 28–29 nov  
  _A big family park with a 4H-gård (www.4h.se/hagelby/, lovläger and klapphage), lekplats and Ekorrstigen. The same events show in the Upplev Botkyrka kalendarium, so this source is mainly for places and event detail._
- **Botkyrka kommun – Öppna förskolor (Fittja, Hallunda-Norsborg, Storvreten, Tullinge)** — kommun, gives both, family medium, ~5 items  
  https://www.botkyrka.se/forskola-och-skola/oppna-forskolor  
  e.g. Tullinge: sångstunder varje vardag, Pappaträff 21 okt, rytmik 9 okt; samma struktur på övriga tre  
  _There are 4 free open preschools (0–6 år) as places, and each subpage has a monthly 'Händer hos oss' list of dated activities._
- **Cirkus Cirkör – Kurser i Cirkörhuset, Alby** — förening, gives events, family medium, ~3 items  
  https://www.cirkor.se/kurser/  
  e.g. Familjecirkus (barn 5–18 + vuxen) terminskurs; FEAR höstlovskurs (10–14 år, with Subtopia); drop-in-träning i Cirkörhuset  
  _These are mostly bookable courses and lovkurser, not one-off events. Botkyrka residents under 20 get a 600 kr discount and Fritidskortet is accepted. Prova-på days run through Subtopia 'Söndagsöppet'._
- **Lida friluftsgård (Tullinge)** — natur, gives both, family low, ~3 items  
  https://lida.se/  
  e.g. Lida Night Trail 28 okt; Eldshow på höstlovet 28 okt; Ugglejakt 29 okt; Accropark, balanslekplats, friluftsbad, skidspår  
  _A major outdoor family destination. Use it mainly for places (activities at /aktiviteter/), since events are also in the Upplev Botkyrka kalendarium (and /kalender/ here)._
- **Naturkartan – Botkyrka kommun** — natur, gives places, family low, ~0 items  
  https://www.naturkartan.se/sv/botkyrka  
  e.g. Naturreservat, leder, badplatser, grillplatser  
  _The official kommun nature guide on Naturkartan. Use it for places._

### Danderyd — 6 total (3 new)

- **Danderyds kommun – Höstlov 2026** — kommun, gives events, family high, ~10 items  
  https://www.danderyd.se/uppleva-och-gora/hostlov-2026/  
  e.g. Sagostund med spöktema 26 okt (Danderyds bibliotek); Kreativ Halloween-workshop 29 okt (Djursholms bibliotek, 6+); Ungdomscentrum Enebyberg höstlovsprogram 26–…  
  _Collects all lov activities: libraries, Ungdomscentrum Enebyberg, and ungdomskoordinator outings (Gröna Lund, bio, dans). The URL is year-specific, so expect new pages such as jullov/sportlov-2027 under /uppleva-och-gora/. Library items overlap the existing b…_
- **Danderyds kommun – Lekplatser** — kommun, gives places, family medium, ~30 items  
  https://www.danderyd.se/uppleva-och-gora/idrott-motion-och-friluftsliv/friluftsliv/lekplatser/  
  e.g. 'Över 30 lekplatser' with map in Kartportalen  
  _PLACES: playgrounds are shown on the municipal map (Kartportalen) rather than as a text list._
- **Danderyds kommun – Badplatser** — kommun, gives places, family medium, ~9 items  
  https://www.danderyd.se/uppleva-och-gora/idrott-motion-och-friluftsliv/bad/badplatser/  
  e.g. Germaniaviken; Kevinge strand; Ösbysjön  
  _PLACES: 9+ beaches with water-quality info. Related pages: parker (/friluftsliv/parker/) and naturområden (/friluftsliv/naturomraden/)._

### Ekerö — 11 total (7 new)

- **Upplev Ekerö – Höstlovsaktiviteter** — visit, gives events, family high, ~15 items  
  https://www.upplevekero.se/tips--guider/hostlovsaktiviteter  
  e.g. Dockteater 'Treo, Enis och en till' 29 okt (2–6 år, Erskinesalen); Speldag på Ekebyhovs slott 26 okt; Kusliga majslabyrinter på Thorslunda 24 okt–1 nov  
  _The kommun's visit site with a curated lov guide: bibliotek, kulturhus, Thorslunda, Birka, Drottningholm, Ekerö centrum spökjakt 30 okt, and outdoor tips. It is redone each lov. We had no kommun or visit source for Ekerö before._
- **De Kungliga Slotten – Kalendarium filtrerat på Drottningholms slott + Kina slott** — museum, gives events, family high, ~20 items  
  https://www.kungligaslotten.se/kalendarium.html?besoksmal%5B%5D=4.46ca39931600d1b7b98194d&besoksmal%5B%5D=4.46ca39931600d1b7b981995  
  e.g. Höstlovstema 'Drottningar' 24–25 okt & 31 okt–1 nov (familjevisningar, bildjakt); Familjevisning på Drottningholm söndagar 25 okt, 1, 8, 15, 22 nov  
  _A filtered calendar URL (besoksmal[] = Drottningholm + Kina slott). Items are tagged 'Familj', 'För barn' and 'Höstlov'. Kina slott is closed for the season but appears in summer. The same calendar can be filtered for Tullgarn (Södertälje), but Tullgarn has n…_
- **Thorslunda gård – självplock, pumpor & majslabyrinter** — other, gives both, family medium, ~3 items  
  https://thorslunda.se/  
  e.g. Kusliga majslabyrinter med skådespelare 24 okt–1 nov; livemusik 24, 25 & 30 okt; pumpaland + barnområde (halm, traktorlekstugor)  
  _A seasonal family farm (summer självplock, autumn pumpkins and labyrinths) with bookable entry. Events are on the start page; /vadhanderpaomradet/ is outdated._
- **Birka Vikingastaden – aktiviteter & teman** — museum, gives both, family low, ~1 items  
  https://www.birkavikingastaden.se/hitta-pa-birka/  
  e.g. Álfablót – vikingarnas halloween 24–25 okt (/hitta-pa-birka/vikingarnas-halloween-alvablot-pa-birka/)  
  _A World Heritage viking island, reached by boat from Stockholm. Seasonal (May–Sept plus a höstlov theme weekend), so use it mainly as a family place. Theme weekends are posted as pages._
- **Upplev Ekerö (kommunens besöksguide)** — visit, gives places, family low, ~0 items  
  https://www.upplevekero.se/  
  e.g. Våra slott, världsarv (Birka, Hovgården), vandringsleder, Naturstigen vid Ekebyhov, gårdsbutiker/självplock  
  _The places side of the same visit site: Se & göra, natur & friluftsliv, sport & fritid, världsarv._
- **Ekerö kommun – Lekparker & lekplatser** — kommun, gives places, family low, ~0 items  
  https://www.ekero.se/uppleva-gora/for-barn/lekparker--lekplatser  
  e.g. Aktivitetsparken vid Ekebyhov (stor lekplats, skatepark), Borgenparken Stenhamra, ~20 kommunala lekplatser i Ekerökartan  
  _Highlights the big parks; the full list is in the Ekerökartan map layer 'Lekplatser'. Use it for places._
- **Naturkartan – Ekerö kommun** — natur, gives places, family low, ~0 items  
  https://www.naturkartan.se/sv/ekero  
  e.g. Vandringsleder, naturreservat, grillplatser, Barfotastigen på Kärsön  
  _The official kommun nature guide (Upplev Ekerö links to it). Use it for places._

### Haninge — 10 total (5 new)

- **Ormteatern (Haninge) – föreställningar** — teater, gives events, family medium, ~9 items  
  https://www.ormteatern.se/  
  e.g. Mojängen (Martin Widmark, familj, fri entré) 25 okt Muskö & 1 nov Ornö; Damen i svart (från 13 år) 30 okt–21 nov  
  _Haninge's professional theatre (Rudan, Handen). It has family productions touring the Haninge archipelago. Tickets are via Nortic organiser 1047 (https://www.nortic.se/dagny/organizer/1047, loads by JS). Some dates also appear in haninge.se's calendar. The sc…_
- **Barn i stan – aktiviteter för barn i Haninge & Nynäshamn** — aggregator, gives places, family medium, ~1 items  
  https://www.barnistan.se/stockholm/omrade/aktiviteter-barn-haninge-nynashamn/  
  e.g. Leos Lekland Länna; Tungelsta trädgårdsparks lekplats; Monsterstigen i Sorunda; Ösmo simhall  
  _Barnistan area filter, mostly permanent places with few dated events. It also covers Nynäshamn, so it is listed only here. Because it is radius-based, some cards are in Farsta/Huddinge/Tyresö._
- **Haninge kommun – Platser att besöka** — kommun, gives places, family low, ~0 items  
  https://www.haninge.se/uppleva-och-gora/lekplatser-natur-och-sevardheter/platser-att-besoka/  
  e.g. Gålö (sandstrand); Årsta havsbad; Utö; Dalarö; Tyresta  
  _Permanent places: 13 destinations. Also see /sevardheter/arsta-slott/ (Museilekstugan Margaretas stuga, Engelska parken; no public museum viewings in 2026)._
- **Haninge kommun – Lekplatser** — kommun, gives places, family low, ~0 items  
  https://www.haninge.se/uppleva-och-gora/lekplatser-natur-och-sevardheter/lekplatser/  
  e.g. Eskilsparken (temalekplats 'Den förtrollade ängen'); Tungelsta trädgårdspark; Nakterhusparken (lekskepp)  
  _Permanent places: about 40 municipal playgrounds grouped by area, with a lekplatsplan PDF._
- **Naturkartan – Haninge** — natur, gives places, family low, ~0 items  
  https://www.naturkartan.se/sv/haninge  
  e.g. Rudan, Gålö, Tyresta, Sörmlandsleden  
  _Naturkartan city guide (loads by JS or API), for outdoor places such as Rudan friluftsområde (lekplats, pulkabacke, aktivitetsbana) and Gålö._

### Huddinge — 18 total (12 new)

- **Huddinge kommun – Kommunkalender (På gång i Huddinge)** — kommun, gives events, family high, ~152 items  
  https://www.huddinge.se/kommunkalender  
  e.g. Spontan Sport för barn 8–13 år (veckovis, t.o.m. mars 2027); Nyboda museum öppet söndagar; utställning 'Att samla samtiden för framtiden' t.o.m. 8 nov  
  _The main kommun calendar - we only had the 'årliga evenemang' page. 152 hits, 10 per page. The JS filters are Målgrupp ('Barn och familj', 'Ungdom'), Kommundel (17 areas), Ämne and date. The kommun's lov page says all lovaktiviteter are published here. List d…_
- **Huddinge kommun – Barnkultur (höstens barnprogram)** — kommun, gives events, family high, ~4 items  
  https://www.huddinge.se/fritid-natur-och-kultur/for-barn-och-unga/barn--och-ungdomskultur/barnkultur  
  e.g. Dockteater 'Musen och äpplet' 24 okt (Lyktan, Skogås); 'Vilken soppa!' Cirkus Trattofon 15 nov (Segeltorp); 'Snögubben' med Lilla O 21 nov (Flemingsberg); Cirk…  
  _A free children's culture programme (dockteater, cirkus, berättelser), grouped by kommundel and run with local kulturföreningar. It is updated each term. The program is small but 100% family._
- **Rådsparken – parklek med djur (Huddinge kommun)** — park, gives both, family high, ~5 items  
  https://www.huddinge.se/radsparken/  
  e.g. Åsna med vagn 26, 28 & 30 okt; tipspromenad/bingo/bildjakt hela höstlovet 24 okt–1 nov; Mini djurträff för 2–5 år  
  _A parklek with animals (åsnor, getter, kaniner) open 365 days. It works as a permanent place, plus lov programmes on https://webb.huddinge.se/radsparken/hostlov-i-radsparken/. The site redirects to webb.huddinge.se/radsparken/._
- **Fullersta Gård – konsthall, utställningar & program** — museum, gives events, family medium, ~4 items  
  https://webb.huddinge.se/fullerstagard/  
  e.g. Höstlovsworkshop 'Väv i papper' 27 okt; 'Skapa en kreativ rya i ask' 28 okt; utställning t.o.m. 8 nov  
  _The municipal konsthall in a park, with free entry. It runs lov workshops via Konstverkstan (/fullerstagard/konstverkstan/lovprogram/). The program list is at /fullerstagard/utstallningar/._
- **Kulturskolan Huddinge – Öppen kulturskola (gratis drop-in)** — kommun, gives events, family medium, ~6 items  
  https://webb.huddinge.se/kulturskolanhuddinge/oppen-kulturskola/  
  e.g. Animationsverkstad Vårby bibliotek tisdagar 14.30–17 (8–12 år, drop-in); Animationsverkstad Skogås onsdagar; Streetdance Flemingsberg fredagar  
  _These are weekly recurring, free drop-in activities (1 Sep–8 Dec 2026), not one-off events. They suit recurring-event entries. Kulturskolan's lov courses are booked via StudyAlong (subject=Lovkurser)._
- **Teater Sláva – Tonsalen (egen scen i Huddinge)** — teater, gives events, family medium, ~4 items  
  https://www.teaterslava.org/  
  e.g. Kalevalaskåpet 8 nov (sagoteater från 4 år); Barnens jul 6 dec (från 2 år)  
  _A small independent theatre with its own stage in Huddinge. About half of the program is for children or families, the rest is adult concerts and theatre. Tickets via 'Köp biljett'._
- **Huddinge Centrum – Evenemang** — shopping, gives events, family medium, ~2 items  
  https://www.huddingecentrum.se/evenemang/  
  e.g. Höstlovsaktiviteter 28–30 okt (gaming, pingis, design studio, DJ school – gratis); Jokkmokksdagarna 22–25 okt  
  _A shopping centre events page with few but family-relevant lov events. Expect activity around lov and Christmas._
- **Heron City (Kungens Kurva) – Aktuellt** — shopping, gives events, family medium, ~2 items  
  https://www.heroncity.se/aktuellt/  
  e.g. Happy höstlov 26 okt–1 nov (pingis, halloweenpyssel, ansiktsmålning); Super-mega-loppis 7 nov  
  _An entertainment centre at Kungens Kurva. The 'Aktuellt' list mixes events with offers, and each item has a date. Lov programmes appear every sportlov, påsklov, sommarlov and höstlov._
- **Upplev Huddinge (kommunens besöksguide)** — visit, gives places, family low, ~0 items  
  https://upplev.huddinge.se/  
  e.g. Friluftsområden Flottsbro, Sundby gård, Ågesta; naturreservat & badplatser; lekland, trampolinpark, Lekplatsrally  
  _A places guide with no event calendar. Good for permanent family places (nature, parks and lekplatser, museums, activities) and has 'Upptäck naturen med barnen' tips._
- **Huddinge kommun – Lekplatser i kommunen** — kommun, gives places, family low, ~0 items  
  https://www.huddinge.se/fritid-natur-och-kultur/lekplatser-och-parker/lekplatser-i-kommunen  
  e.g. About 40 lekparker, each with its own page (e.g. Flemingsbergsparken, Fullerstaparken, Ängsnäsparken)  
  _A full list of municipal playgrounds with sub-pages plus a downloadable lekplatsguide. Use it for places._
- **Naturkartan – Huddinge kommun** — natur, gives places, family low, ~0 items  
  https://www.naturkartan.se/sv/huddinge  
  e.g. Naturreservat, leder, badplatser, grillplatser  
  _The official kommun nature guide on Naturkartan. Use it for places._
- **Flottsbro – skidbacke, bike park, camping & bad** — sport, gives places, family low, ~1 items  
  https://www.flottsbro.se/  
  e.g. Säsongskort vinter 2026/27; bike park events such as 'Jam i parken'; family ski slope and beach in summer  
  _A family activity place (ski slope, downhill bike, camping, badplats, klättring). It has few dated events and posts news at /nyheter/._

### Järfälla — 16 total (8 new)

- **Huset på höjden – veckoschema (kultur- och aktivitetshus, Jakobsberg)** — kulturhus, gives both, family high, ~30 items  
  https://www.jarfalla.se/fritidochkultur/kulturochnojen/husetpahojden.4.4b149fc016400a9f7871223b.html  
  e.g. Dancehall med ungdomscoach (6–12 år) tors 22 okt; Digitalt skapande (8–12 år) fre 23 okt; Järfälla schacksällskap juniorer mån 19 okt  
  _Static HTML weekly schedule (v.43 shown, updated weekly) with ~30 activities/week, many run by föreningar (Unga Mål, Jasminhuset, schacksällskap, Teatersällskapet) – likely not all of these reach upplevjarfalla.se. Also a permanent place: barnhörna, café, hem…_
- **Jakobsbergs Centrum – eventkalender** — shopping, gives events, family high, ~2 items  
  https://www.jakobsbergscentrum.se/eventkalender/  
  e.g. Halloween: spökrunda i centrum lör 24 okt; Julfirande för hela familjen 12–19 dec (Musse & Helium, lucia, tomtebesök)  
  _Shopping-centre family days (påsk-äggjakt, glitterfest, Mamma Mu meet & greet earlier in 2026). Few but very family-oriented; page also keeps past events, filter by date._
- **Friluftsfrämjandet Järfälla – äventyr** — förening, gives events, family medium, ~24 items  
  https://www.friluftsframjandet.se/regioner/malardalen/lokalavdelningar/jarfalla/  
  e.g. Bytesmarknad 24 okt (gratis, ingen anmälan); Skridskoskola nybörjare lördagar 7 nov–12 dec (från 7 år); Frilufsargruppen Vargarna (barn födda -14)  
  _List is JS-rendered (shows 8, 'visa ytterligare 16'). Mostly bookable courses (Skogsmulle, Frilufsare, skridskoskola) + open events; Rockstastugan söndagscafé. friluftsframjandet.se/jarfalla redirects here._
- **Upplev Järfälla – Lovaktiviteter (läslov v44)** — kommun, gives events, family high, ~40 items  
  https://upplevjarfalla.se/lovaktiviteter  
  e.g. Läslovsgymnastik med Maja 26–29 okt; Höstlovet på Rocksta gård 27–29 okt; Spåra spöken i mörkret (bibblan) 27 okt  
  _CAUTION: same CBIS database as the existing upplevjarfalla.se/evenemang, but pre-filtered to barn/unga lovaktiviteter with age filter – handy family filter during lov. Vue/JS-rendered (needs browser)._
- **Naturskyddsföreningen Järfälla – kalender** — natur, gives events, family medium, ~3 items  
  https://jarfalla.naturskyddsforeningen.se/  
  e.g. Konstnärlig fladdermus-workshop för barn 24 okt (Huset på höjden); Bildvisning 2 nov; Vi gör fågelmat 6 dec  
  _Small but active local chapter calendar on the start page; some events also appear on upplevjarfalla.se._
- **Lekplatser i Järfälla (ca 60, temalekplatser)** — kommun, gives places, family high, ~0 items  
  https://www.jarfalla.se/fritidochkultur/barnochunga/lekplatser.4.7649a918158917b879e24dc.html  
  e.g. Kyrkparken Barkarby (lek för alla); Ålstaparken (flygplatstema); Stäketfläcken Kallhäll (tågtema)  
  _PLACES: ~60 kommunala lekplatser, themed ones described per area (Barkarby, Kallhäll, Jakobsberg, Skälby, Viksjö) + map link._
- **Naturkartan – Järfälla kommun (Järfällas naturpärlor)** — natur, gives places, family low, ~0 items  
  https://www.naturkartan.se/sv/jarfalla  
  e.g. Görvälns naturreservat; Ängsjö; Hälsans stig Viksjö  
  _PLACES: kommunens 25 'naturpärlor' utflyktsmål + naturreservat, vandring, badplatser, utegym (JS site)._
- **Badplatser i Järfälla** — kommun, gives places, family low, ~0 items  
  https://www.jarfalla.se/fritidochkultur/idrottochmotion/badplatser.4.640dac6b1300db73e7c800015282.html  
  e.g. Bonäsbadet; Görvälnbadet; Ängsjö friluftsbad  
  _PLACES: 5 kommunala badplatser (season 15 maj–15 sep)._

### Lidingö — 10 total (4 new)

- **Lidingö stad – evenemangskalendern, tagg Barn (NY URL)** — kommun, gives events, family high, ~12 items  
  https://lidingo.se/kultur-fritid/evenemangskalendern/?archive_event_keywords_name%5B%5D=barn  
  e.g. Natursnoksträff med pinnbrödsgrillning 25 okt (Hustegaholm); Välkommen på lovhandboll 28 okt; Capoeira familj och barn 27 okt  
  _IMPORTANT: the existing Lidingö kommun URL (lidingo.se/toppmeny/kulturfritid/evenemangskalender.4.56084d171880bf3fa61629.html) now returns 404. This is the new calendar and should replace it. Server-rendered with tag filters via archive_event_keywords_name[]:…_
- **Millesgården – kalendarium och evenemang** — museum, gives both, family medium, ~2 items  
  https://www.millesgarden.se/besoka-museet/kalendarium-och-evenemang  
  e.g. Familjevisning: Myter på Millesgården 25 okt 13:00 & 15:00; Lidingö Kulturvecka-visningar 13–14 nov  
  _26 dated items through November, mostly adult tours, with occasional familjevisningar. Tickets: https://millesgarden.entryevent.se/ticketshop/all-events. The sculpture garden is a top permanent place._
- **Lidingö stad – Lekparker** — kommun, gives places, family high, ~44 items  
  https://lidingo.se/kultur-fritid/aktiviteter-for-barn-och-unga/lekparker/  
  e.g. Abborrparken (Sticklinge); Kyttingeparken; Bikepark i Högsätra  
  _PLACES: 44–47 playgrounds split by norra/södra ön, 2 pages. Map at karta.lidingo.se (layer 'lekplats')._
- **Naturkartan – Lidingö stad guide** — natur, gives places, family medium, ~0 items  
  https://www.naturkartan.se/sv/lidingo  
  e.g. Categories: Naturreservat, Friluftsområde, Grillplats/Eldplats, Badplats, Vandring; Kottlasjön, Ekholmsnäsbacken  
  _PLACES: official Lidingö stad guide on Naturkartan (JS map, items load client-side). Grillplatser and vindskydd are also at https://lidingo.se/kultur-fritid/idrott-och-friluftsliv/grillplatser-och-vindskydd/ and beaches at /idrott-och-friluftsliv/bad-och-simh…_

### Nacka — 16 total (9 new)

- **Barn i stan – aktiviteter för barn i Nacka & Värmdö** — aggregator, gives both, family high, ~10 items  
  https://www.barnistan.se/stockholm/omrade/aktiviteter-barn-nacka-varmdo/  
  e.g. Pimpa din pumpa (Siggesta) 30 okt; Familjelördag: Alea iacta est (Dieselverkstaden) 7 nov; Allt är matte 5–11 dec  
  _The Barnistan area filter that the CEO asked for. It shows 18 cards, then 'Ladda fler', mixing dated events with places (Skogshinderbanan, Klätterverket Sickla, simhallar). It also covers Värmdö (Siggesta), so it is listed only here. The filter is radius-base…_
- **Kulturhuset Dieselverkstaden – Familjelördagar (barnteater)** — kulturhus, gives events, family high, ~3 items  
  https://www.nacka.se/valfard-samhallsservice/kulturhusetdieselverkstaden/familjelordagar/  
  e.g. Alea iacta est (Teater Mo, från 2 år) 7 nov 13 & 15; Stjärnhimlar (från 3 år) 28 nov; En häxas dagbok (Pygméteatern, från 4 år) 12 dec  
  _Family theatre series with an age for every show and 2 showings per date, updated 5 Oct 2026. The full Dieselverkstaden calendar (/kulturhusetdieselverkstaden/kalender-diesel/) is paged and mostly repeats pa-gang-i-nacka?type=dieselverkstaden, which we alread…_
- **DV-biblioteken (Dieselverkstadens, Saltsjöbadens & Älta bibliotek) – evenemang** — bibliotek, gives events, family medium, ~8 items  
  https://dvbib.se/evenemang  
  e.g. Mangakurs 8–12 år: Saltsjöbaden 26 okt, Älta 27 okt, Dieselverkstaden 28 okt; Rollspel Drakar och demoner 29 okt; NPF-öppet för familjer (söndagar)  
  _A different library operator from Forumbiblioteken (Orminge/Nacka Forum/Fisksätra), which we already have, so these events are new. Axiell Arena site (Liferay calendar-event-list portlet) that loads by JS, so reuse the Forumbiblioteken scraper. Höstlov dates…_
- **Kulturhuset Älta – program** — kulturhus, gives events, family medium, ~12 items  
  https://www.nacka.se/valfard-samhallsservice/kulturhuset-alta/  
  e.g. Gör din egen halloweenkostym 27 okt; Halloween i Älta (pumpatävling, spökjakt, ansiktsmålning) 30 okt; Eldföreställning för stora och små 30 okt  
  _Kommun-run kulturhus with about 12 dated events 21 Oct–18 Nov (some for seniors). The listing is at /kulturhuset-alta/evenemang/. Some events probably also appear in pa-gang-i-nacka; workshops are booked via Billetto. Its 'Halloween i Älta' teaser says lördag…_
- **Nacka kommun – Höstlov i Nacka (lovaktiviteter)** — kommun, gives events, family medium, ~20 items  
  https://www.nacka.se/uppleva--gora/sasongsinformation/hostlov/  
  e.g. Mangakurs på biblioteken 26–28 okt; Halloween i Älta 30 okt; Karate halloweenläger; Nacka Dans & Teater lovläger 26 okt  
  _Lov hub with 9 subpages (simhallar, bibliotek, fritidsgårdar, Fisksätra, Dieselverkstaden, Nacka Dans & Teater kulturskola, karate, volleyboll, Älta), updated 16 Oct 2026. It is aimed mainly at ages 10–20, but the library and kulturskola items start at 8 year…_
- **Nyckelviken – friluftsgård med bondgård (Nacka kommun)** — park, gives both, family medium, ~1 items  
  https://www.nacka.se/uppleva--gora/friluftsliv-motion/friluftsgardar/nyckelviken/  
  e.g. Adventsdagen 29 nov 2026 11–15 (kransbindning, julmarknad, tomten, ponnyridning, eldshow)  
  _A strong permanent family place: farm animals, pony rides on weekends (children up to 25 kg), the 'Hebbe' lekstuga, café, grill spots, Nacka hembygdsmuseum. It has few dated events, mainly seasonal days like Adventsdagen. Sister pages: /friluftsgardar/velamsu…_
- **Nacka kommun – Lekplatser** — kommun, gives places, family low, ~0 items  
  https://www.nacka.se/uppleva--gora/friluftsliv-motion/lekplatser/  
  e.g. About 100 kommunala lekplatser on a map, with area pages for Boo, Fisksätra/Saltsjöbaden, Sicklaön and Älta  
  _Permanent places. The area subpages give a selection with photos and descriptions. Related places pages: /friluftsliv-motion/badplatser-och-badvatten/, /pulkabackar/, /parker/._
- **Nacka kommun – Utflykter i naturen** — kommun, gives places, family low, ~0 items  
  https://www.nacka.se/uppleva--gora/friluftsliv-motion/utflykter-i-naturen/  
  e.g. Nyckelviken, Velamsund, Hellasgården, Saltisbadet, Svindersvik  
  _Permanent places: 7 outing destinations with descriptions (bondgård, bad, grill, café). Good seed list for family places._
- **Naturkartan – Nacka** — natur, gives places, family low, ~0 items  
  https://www.naturkartan.se/sv/nacka  
  e.g. Category filters: naturreservat, friluftsområde, vandring, grillplats/eldplats, badplatser  
  _The official city guide on Naturkartan. The map and places load by JS (the Naturkartan API is a better way to pull them). It had no events._

### Norrtälje — 14 total (6 new)

- **Biblioteken i Norrtälje – evenemang** — bibliotek, gives events, family high, ~40 items  
  https://bibliotek.norrtalje.se/evenemang  
  e.g. Sagoklubben Norrtälje 23 okt; Minecraftpyssel, Hallstaviks bibliotek 27 okt; Höstlovsmys: Bokmagi, brädspel & varm choklad, Väddö bibliotek 29 okt  
  _Not in the existing list. It covers 6 libraries plus the bokbuss, with about 40 events in 2 weeks (about 15 for kids: sagoklubb, babysång, läshunden Åke, Minimonster). It is an Arena/JS page with filters Målgrupp=Barn and tags (höstlov, Mitt lov, sagostund).…_
- **Pythagoras industrimuseum – evenemang** — museum, gives events, family medium, ~6 items  
  https://pythagorasmuseum.se/evenemang/  
  e.g. Höstlovsöppet med pyssel & skuggteater 27–31 okt; I skuggorna på Pythagoras (6–12 år) 29–30 okt; Julmarknad + pepparkakshustävling 6 dec  
  _A museum calendar with lov, jul and föreläsningskafé items. The museum is open Saturdays Apr–Oct; ticketed items go via Tickster._
- **Norrtälje konsthall – aktuella utställningar och evenemang** — museum, gives events, family medium, ~5 items  
  https://www.norrtalje.se/info/kultur-och-fritid/kultur-och-konst/offentlig-konst/norrtalje-konsthall/utstallningar/aktuella-utstallningar/  
  e.g. Lördag i Studion 24 okt; Vi bygger ett monument till Moder Kosmos! (höstlovsworkshop) 27–29 okt; Workshop i bokbindning 30 okt  
  _Konsthall program with workshops, Barnens konsthall in the Studio on Saturdays, and exhibitions. Some items are also in the kommun calendar._
- **Roslagsmuseet – evenemang** — museum, gives events, family medium, ~4 items  
  https://www.norrtalje.se/roslagsmuseet  
  e.g. Filmworkshops på Roslagsmuseet (10–14 år, höstlov) 26–27 okt; Invigning 'Fångade ögonblick' 24 okt  
  _The museum's events are on this kommun page; roslagsmuseet.se/kalender is empty. It runs holiday workshops for kids._
- **Norrtälje kommun – Lekplatser** — kommun, gives places, family high, ~0 items  
  https://www.norrtalje.se/info/kultur-och-fritid/idrott-motion-friluftsliv/lekplatser-i-norrtalje-kommun/  
  e.g. Badvägens lekplats (Norrtälje); Ekvägens lekplats (Hallstavik); Pop-up-lekplatsen  
  _PLACES: 21 playgrounds across Norrtälje stad (9 + pop-up), Hallstavik (5) and Rimbo (6)._
- **Norrtälje kommun – Badhus** — kommun, gives places, family medium, ~0 items  
  https://www.norrtalje.se/info/kultur-och-fritid/bad/badhus/  
  e.g. Norrtälje badhus; Rimbo badhus; Hallstavik badhus (+ utomhusbad)  
  _PLACES: 3 indoor pools plus an outdoor pool. The linked news posts announce lov activities (Höstlov på Rimbo/Hallstavik badhus, v.44). Beaches are at /info/kultur-och-fritid/bad/badplatser/._

### Nykvarn — 7 total (5 new)

- **Nykvarns kommun – Höstlov 2026 (Ung i Nykvarn)** — kommun, gives events, family high, ~19 items  
  https://nykvarn.se/uppleva-och-gora/ung-i-nykvarn/hostlov-2026  
  e.g. Hemlig lovfilm för de yngsta 27 okt (Qulturum Sländan); Halloweenverkstad – gör din egen mask 27 okt; Monstermusik – bygg & spela instrument 27–28 okt  
  _A lov-filtered view of the kommun calendar (category 'höstlov', 19 results, 2 pages), so it overlaps the existing evenemangskalendern. It gives a clean kids/lov list, and the same category filter exists for sportlov, jullov and sommarlov._
- **Nykvarn – Konstverkstan (öppen konstverkstad med kulturskolan)** — kommun, gives events, family medium, ~1 items  
  https://nykvarn.se/uppleva-och-gora/kultur-och-konst/konstverkstan  
  e.g. Öppen konstverkstad varje måndag 15–16 på biblioteket (gratis, drop-in; under 7 år med vuxen)  
  _A weekly recurring free activity for children (pause during lov). Add it as a recurring event._
- **Östra Södermanlands Järnväg (ÖSlJ) – E-butik / På gång** — other, gives events, family medium, ~2 items  
  https://event.oslj.nu/  
  e.g. Spöktåget 23 & 24 okt 2026 (Mariefred–Läggesta)  
  _A heritage steam railway running Mariefred–Läggesta–Taxinge-Näsby. Its main base is Mariefred (Strängnäs), so list it under Strängnäs too. Nykvarn kommun promotes the Taxinge ångtåg + ångbåt trip. Seasonal: summer traffic, spöktåg, jultåg._
- **Taxinge slott (Kakslottet) – nyheter & evenemang** — other, gives events, family low, ~2 items  
  https://www.taxingeslott.se/  
  e.g. Jul på Taxinge Näsby (julmarknad) 13–15 & 19–22 nov; julbord helger nov–dec  
  _A castle café with seasonal events. Only the julmarknad is family-relevant. Posts are dated (/2026/11/13/)._
- **Upplev Nykvarn (kommunens besöksguide)** — visit, gives places, family low, ~0 items  
  https://nykvarn.se/uppleva-och-gora/upplev-nykvarn  
  e.g. Lådbilslandet (3–9 år), Träffa alpackor, Ånglok och ångbåt från Taxinge, Larssons lada, badplatser/naturreservat  
  _A places hub for Nykvarn (Se och göra, Friluftsliv och motion). Use it for permanent places; Naturkartan has no Nykvarn page._

### Nynäshamn — 7 total (4 new)

- **Nynäshamns bibliotek – evenemang** — bibliotek, gives events, family high, ~6 items  
  https://bibliotek.nynashamn.se/evenemang  
  e.g. Pomperipossa med Teater Tummeliten (Ösmo bibliotek) 24 okt; Läslovet på Sorunda bibliotek 26–29 okt; Rollspel på läslovet 9–12 år 30 okt  
  _Library calendar (Axiell Arena, loads by JS). 5 of 6 upcoming events are for children. The kommun calendar (nynashamn.se/uppleva/aktiviteter) lists Pomperipossa but not the läslov/rollspel events, so most of these are new. There is also https://bibliotek.nyna…_
- **Nynäshamns kommun – Familj (Se & göra)** — visit, gives places, family low, ~0 items  
  https://nynashamn.se/uppleva/se--gora/familj  
  e.g. Nickstabadet (vattenrutschkana, minigolf); lekskeppet Hoppetossan på Frejas holme; Nåttarö & Drottninggrottan  
  _A curated list of about 30 family places (bad, öar, grottor, naturområden, barnvänliga matställen, skatepark), updated 21 Sep 2026. A strong seed for permanent places._
- **Nynäshamns kommun – Lekparker** — kommun, gives places, family low, ~0 items  
  https://nynashamn.se/service/kultur--fritid/fritid/lekparker  
  e.g. Lekskeppet Hoppetossa (Frejas holme); Kamelparken (Idunvägen 3); Ängsparkens lekplats Källberga  
  _Permanent places: 19 municipal playgrounds with addresses, grouped Nynäshamn/Sorunda/Ösmo._
- **Folkets Hus Nynäshamn / Bio Vågen – evenemang** — kulturhus, gives events, family medium, ~4 items  
  https://folketshusnynashamn.se/evenemang/  
  e.g. Babblarna & Klonks Klapp-kalas 23 maj 2027; barnfilmer Fåret Shaun och monstret på bondgården, Nelly Rapp – Porten till underjorden (Bio Vågen); Daytrippers 31…  
  _The town's stage and cinema. Children's films are listed on /bio/ (screenings are weekly, with dates on the event pages). curl gets 403 (bot protection), but WebFetch and browsers work. There are few stage events, but family shows like Babblarna come on tour._

### Österåker — 13 total (6 new)

- **Visit Roslagen – evenemang kategori Barn & familj** — visit, gives events, family high, ~60 items  
  https://roslagen.se/evenemang-2/kategori/barn-familj/  
  e.g. Halloween för barn på Drivis Deli, Ljusterö 29–31 okt; Lorpan längtar, Berga teater 8 nov; Sagolik julmarknad på Wira bruk 27 nov  
  _Visit Roslagen covers Norrtälje, Österåker (Södra Roslagen) and Östhammar. Of about 60 upcoming family events, 14+ are Åkersberga/Ljusterö (venue city 'Åkersberga'). There is no kommun URL filter. It is new for Österåker; Norrtälje already has roslagen.se/eve…_
- **Åkersberga Centrum – eventkalender** — shopping, gives events, family medium, ~5 items  
  https://www.akersbergacentrum.se/eventkalender/  
  e.g. Halloween! Spökrunda i centrum 24 okt; Julfirande för hela familjen 12–19 dec; Fira påsk med Knatteberga (vår)  
  _A Citycon mall page with few but recurring family events for Halloween, jul and påsk. Event pages are at /event/<slug>/._
- **Österåkers kommun – Höstlovsveckan** — kommun, gives events, family medium, ~6 items  
  https://www.osteraker.se/specialsidor/kommunalaverksamheter/kulturochfritid/lovhogtiderevenemangsperioder/hostloviosteraker.4.40523b741958b6adf741be4e.html  
  e.g. Pokémon-tipspromenad 26 okt; Bygg ett instrument med Hemkodat 27 okt; Lilla deckarskolan med Karolina Schützer 29 okt  
  _A seasonal lov page. Its dated items are also in the kommun calendar, but it adds undated lov tips (ishallar, Hitta ut, skatepark, Bergagården, digital tipspromenad). Moderate uniqueness. Berga teater's page is only a subset of the kommun calendar, so it was…_
- **Naturkartan – Österåkers kommun** — natur, gives places, family medium, ~0 items  
  https://www.naturkartan.se/sv/osteraker  
  e.g. Naturreservat, vandringsleder, badplatser  
  _PLACES: the official nature guide (linked from the kommun höstlov page)._
- **Österåkers kommun – Badplatser** — kommun, gives places, family medium, ~0 items  
  https://www.osteraker.se/upplevagora/badplatser.106.44fe6fa019e40e754cd685a.html  
  e.g. Garnsviken (barnvänlig sandstrand); Domarudden; Linanäsbadet  
  _PLACES: 8 municipal beaches with facility details (child-friendly beach, jetty, toilets, play park)._
- **Österåkers sju underverk** — kommun, gives places, family medium, ~0 items  
  https://www.osteraker.se/specialsidor/kommunalaverksamheter/kulturochfritid/osterakerssjuunderverk.4.5f4ce35f18ecbde7180bf1e.html  
  e.g. Siaröfortet; Wira bruk; Biskopstuna borgruin  
  _PLACES: 7 utflyktsmål (fort, bruk, castle, ruins, Husarö by, Åkers kanal), good for family outings._

### Salem — 7 total (4 new)

- **Salems kommun – Höstlov (lovaktiviteter)** — kommun, gives events, family high, ~20 items  
  https://www.salem.se/fritidochkultur/lovaktiviteter/hostlov.4.39155d0219e634874bf13ccc.html  
  e.g. Clownföreställning 'Bygget' 27 okt (från 5 år, Stora Murgrönan, gratis); lovbio 'Paw Patrol' 28 okt; Prova på tennis Rönninge TK 26–28 okt  
  _A seasonal page with about 20 dated activities: bio, teater, 4H-läger, kulturskola-kollo, tennis, bibliotek and fritidsgård. The parent page /fritidochkultur/lovaktiviteter.4.69755fc319b2be124e43e7de.html links each lov and is updated a few weeks before it. N…_
- **Salem Kulturskola – Kalendarium läsåret 26/27** — kommun, gives events, family medium, ~4 items  
  https://www.salem.se/forskolaochskola/kulturskola/kulturskolanskalendarium2026.4.1780fcad196d896650a4e65.html  
  e.g. Avslutningskonserter 7–11 dec (Lilla & Stora Murgrönan); stor offentlig julkonsert 15 dec kl 17; Kulturdagen 16 jan  
  _A year plan of public concerts, kollon, festivals and the yearly musical. It is a static list, and detailed concert programmes are added later. Some items are school-only (marked 'åk 2/3/4')._
- **Ersboda 4H-gård (Salem)** — förening, gives both, family medium, ~3 items  
  https://www.4h.se/ersboda/  
  e.g. Höstlovsläger 26–30 okt (mini 5–7 år, 8–12 år); Halloween på gården 31 okt; Prova på Djurkul  
  _A farm with animals, lovläger every lov (/hostlovslager/, /jullovslager/ …), kalas and private visits. It is a good permanent place. The Halloween date comes from Salem's höstlov page; the farm announces details on FB/IG._
- **Salems kommun – Friluftsliv och motion** — kommun, gives places, family low, ~0 items  
  https://www.salem.se/fritidochkultur/friluftslivochmotion.4.1e0fa62b19047f61fccc4aa0.html  
  e.g. Möllebadet (kommunens badplats, kiosk, beachvolley), grillplatser vid Garnudden, motionsspår, skridsko  
  _A hub for permanent places (bad, grill, spår, skridsko). Salem is small, so this is the main places page._

### Sigtuna — 19 total (11 new)

- **Gröna Ladan – biograf i Sigtuna stad** — other, gives events, family high, ~40 items  
  https://www.gronaladan.se/  
  e.g. Lilla spöket Laban busar vidare 25 okt; Bus och mysterier med Alfons Åberg 29 okt; Bamse och havets hemlighet 30 okt  
  _100-year-old cinema; dense höstlov family-film schedule + opera/konsert. Static HTML (bio.se platform)._
- **Sigtuna kommuns kalender – Barn och familj (full kalender)** — kommun, gives events, family high, ~44 items  
  https://kalender.sigtuna.se/events?by_categories=2780  
  e.g. Sagostund Märsta bibliotek (3–6 år) ons; Titta boken! (0–2 år) Valsta 22 okt; Familjecentralens öppna förskola (0–6 år) 23 okt  
  _NOTE: the existing sigtuna.se/evenemang.html only shows ~9 teaser items – this is the full calendar app behind it (same kommun data). Use category filters: Barn och familj = by_categories=2780, Lovaktivitet = by_categories=2779. JS app._
- **Destination Sigtuna – Höstlov i Sigtuna** — visit, gives events, family high, ~9 items  
  https://www.destinationsigtuna.se/sv/nyhetsartiklar/hostlov-i-sigtuna/  
  e.g. Upptäckardag på Sigtuna museum 24 okt; Halloweenparad i Sigtuna stad 31 okt; Rävstas mardrömsstig (Märsta ridklubb) 31 okt  
  _Curated lov article (static HTML) incl. non-kommun organisers (företagarförening, ridklubb, Skokloster). Seasonal page – also see https://www.destinationsigtuna.se/sv/sigtuna-julmarknad/ (29 nov, 6, 13, 20 dec)._
- **Öppen kulturskola och prova på – Mötesplatsen i Valsta** — kommun, gives both, family high, ~12 items  
  https://www.sigtuna.se/uppleva-och-gora/kulturskolan/oppen-kulturskola-och-prova-pa.html  
  e.g. Barndans 2–6 år + vuxen måndagar 15.45; Musik och dans 6–11 år onsdagar 14.30; Prova på instrument tis & fre  
  _Free weekly drop-in groups (hösttermin 2026), recurring – good as recurring family activities._
- **Sigtuna kommun Kultur och Fritid – Nortic biljetter (Kulturum, Biokällan)** — ticketing, gives events, family medium, ~6 items  
  https://www.nortic.se/customer/organizereventlist/401  
  e.g. Höstlovsbio: Monsterfabriken 27 okt (Biokällan, gratisbiljett); Höstlovsbio: Space Cadet 28 okt; Riksteatern: Football Dramatics 26 okt (från 6 år)  
  _Ticket organiser page for kommunens scener (Kulturumteatern, Biokällan Märsta, Kulturlänken). kulturum.se is a parked domain – this is the real program source._
- **Friluftsfrämjandet Märsta-Sigtuna – äventyr** — förening, gives events, family medium, ~7 items  
  https://www.friluftsframjandet.se/marsta-sigtuna  
  e.g. Tipspromenad för barn och vuxna i Rävsta (t.o.m. 25 okt); Skogsknopp i Rävsta från 22 nov; Adventspaddling 29 nov  
  _Mostly family/kids activities (Skogsmulle, Strövare, skridskoskola). JS-rendered list._
- **ValstaKonst – konsthall & drop-in-ateljé (Valsta)** — kulturhus, gives both, family medium, ~4 items  
  https://valstakonst.com/  
  e.g. Halloweenpyssel i ateljén 24–25 okt; Drop-in-ateljé lör–sön 12–17 (gratis, alla åldrar); utställning Där Sverige börjar t.o.m. 11 jan 2027  
  _Kommunal konsthall (part of Sigtuna Museum & Art) with weekend drop-in ateljé for families; 'Utställningar + Program' page._
- **Steninge slottsby – nyheter/evenemang** — shopping, gives events, family medium, ~3 items  
  https://steningeslottsby.se/nyheter/  
  e.g. Spökhuset i Trälogen 30 okt; Julmarknad 28–29 nov & 5–6 dec  
  _Page is an embedded Facebook feed (no structured calendar) – höstmarknad, julmarknad, spökhus, Uppsala 4H djurhage. Lilla Steninge lekpark = permanent place._
- **Destination Sigtuna – För barnfamiljen** — visit, gives places, family high, ~0 items  
  https://www.destinationsigtuna.se/sv/se-gora/for-barnfamiljen/  
  e.g. Lilla Steninge lekpark; Äventyrsgolf Sigtuna; Midgårdsbadet  
  _PLACES: filterable family guide (barnaktiviteter, biografer, badplatser, museum, naturområden, slott)._
- **Lekplatser i Sigtuna kommun (28)** — kommun, gives places, family high, ~0 items  
  https://www.sigtuna.se/uppleva-och-gora/bada-simma-och-leka/lekplatser.html  
  e.g. Fågelparken (Märsta); Kanonkulleparken; Sätunaparken  
  _PLACES: 28 lekplatser with descriptions per ort (starting with Märsta)._
- **Sigtuna Museum & Art** — museum, gives both, family medium, ~3 items  
  https://www.sigtuna.se/uppleva-och-gora/uppleva-kultur/sigtuna-museum--art.html  
  e.g. Upptäckardag – vävning 24 okt; höstlov tema vävning (koja i Black Box, upptäckarspår); Bröllop som politik 5 nov  
  _Museum page (fri entré under 20, barnspår, Skapa leka lära). Its dated events are published in kalender.sigtuna.se; valuable mainly as PERMANENT place._

### Sollentuna — 12 total (7 new)

- **Höstlov i Sollentuna – lovaktiviteter (kommun)** — kommun, gives events, family high, ~30 items  
  https://www.sollentuna.se/uppleva--gora/aktiviteter-pa-loven/  
  e.g. Skapa ett dansspel med BUSSTER 26 okt (7–12 år, Skaparverkstan Stallbacken); Spindelworkshop med Emmalill Frank 27–30 okt (bibliotek); Skaparverkstan 31 okt–1…  
  _Static HTML lov page (re-used each lov) grouped by theme: skapa, bakning, idrott, kultur, utomhus; activities from BUSSTER (mobile fritid 7–12), bibliotek, Familjerummet, fritidsgårdar, föreningar. May partly overlap with the existing aktuell-kalender, but th…_
- **Sollentuna Centrum – evenemang** — shopping, gives events, family high, ~2 items  
  https://sollentunacentrum.se/evenemang/  
  e.g. Skattjakt med Spöket Laban (Barnklubben) 24 okt; Bluey kommer på besök 30 okt–1 nov  
  _Shopping-centre family events (barnklubb, character visits); small list, static HTML._
- **Edsvik / Stallbacken kultur – Skaparverkstan** — kulturhus, gives both, family high, ~20 items  
  https://www.sollentuna.se/uweb/edsvik/stallbacken-kultur/skaparverkstan/  
  e.g. Skaparverkstan lör–sön 11–16 (från 4 år med vuxen, boka 90 min); Textilworkshop familj 28 okt; Höstlovs-Skaparverkstan 31 okt–1 nov  
  _Recurring free family creative workshop every weekend (bookings open 2 weeks ahead) at Edsvik (Landsnoravägen 42). Edsvik's own event page https://www.sollentuna.se/uweb/edsvik/stallbacken-kultur/evenemang/ is mostly adult lunchkonserter; Edsbergsparken hosts…_
- **Bögs gård – visningsgård på Järvafältet** — park, gives places, family medium, ~0 items  
  https://bogsgard.se/visningsgard/  
  e.g. Öppen alla dagar 10–16, gratis; får, kalvar, grisar, getter, kaniner; ponnyridning  
  _PLACE: free open farm year-round with värmestugor and grillplatser; occasional events (e.g. Svenska kyrkan visit)._
- **Lekplatser i Sollentuna (ca 60)** — kommun, gives places, family high, ~0 items  
  https://www.sollentuna.se/uppleva--gora/idrott-motion-och-friluftsliv/lekplatser/  
  e.g. Skogsparken och Raketparken (Sjöberg); lekplatser i Edsberg/Väsjön; Rotebro (11 st)  
  _PLACES: ~60 lekplatser with sub-pages per kommundel (Edsberg/Vaxmora, Helenelund, Häggvik, Rotebro, Silverdal, Sjöberg, Tureberg, Viby/Norrviken)._
- **Badplatser i Sollentuna** — kommun, gives places, family low, ~0 items  
  https://www.sollentuna.se/uppleva--gora/idrott-motion-och-friluftsliv/badplatser/  
  e.g. Rösjöbadet (sandstrand, hopptorn, minigolf); Torparängsbadet Norrviken; Badberget Edsviken  
  _PLACES: 8 badplatser with facilities._
- **Naturkartan – Sollentuna kommun** — natur, gives places, family low, ~0 items  
  https://www.naturkartan.se/sv/sollentuna  
  e.g. Rösjön runt; Törnskogen runt; Skogsstigen Rösjöskogens naturreservat  
  _PLACES: 4 naturreservat + närnaturområden, leder (JS site)._

### Solna — 16 total (8 new)

- **Fjärilshuset Haga Ocean – höstlov & visningar** — other, gives both, family high, ~15 items  
  https://www.fjarilshuset.se/  
  e.g. Höstlov med zoolog Owe Sandström 24–29 okt, 31 okt–1 nov; Hajvisning & 'Dagens djur' visningsdagar 14, 15, 21, 28, 29 nov  
  _Events are listed on the homepage (no separate calendar): visning days with a fixed daily schedule (hajvisning 11:30/13:30, koi-matning 13:00, rovfiskmatning 15:00). Also a top permanent place in Hagaparken._
- **Överjärva gård – aktiviteter på gården** — kommun, gives both, family high, ~4 items  
  https://www.solna.se/overjarva-gard/uppleva-och-gora/aktiviteter-pa-garden  
  e.g. Slankvecka och höstlov 24–25 okt (klappa får, extraöppet 29–30 okt); Gårdshelg: Jul på Överjärva 5–6 dec; Luciafirande 12–13 dec  
  _Municipal farm with animals, café and Statarmuseet. Seasonal gårdshelger (Ljus och mörker 21–22 nov). Some items may also appear in the solna.se calendar. Barnens Överjärva pages cover the permanent place (animals, lekmiljöer)._
- **Westfield Mall of Scandinavia – kalendarium** — shopping, gives events, family medium, ~2 items  
  https://www.westfield.com/sv/sweden/mallofscandinavia/kalendarium  
  e.g. Halloween-jakt i butik 24–31 okt; LEGO Botanicals 27–28 nov; Joe Labero's Magic World (okt–nov)  
  _7 dated items, 2 clearly for families; also lists Strawberry Arena match days and Filmstaden events. Strawberry Arena (Solna) is already in the Stockholm list (strawberryarena.se/evenemang/), so it is not repeated here._
- **Solna Centrum – nyheter & händelser** — shopping, gives events, family medium, ~2 items  
  https://solnacentrum.se/nyheter/  
  e.g. Halloween i Solna Centrum 29 okt 14–17 (maskpyssel, ansiktsmålning, maskotarna Solis & Solrosa); Invigning av Fjärilskvarteret (ny lekyta) 2 okt  
  _Lov and holiday family events (also Sportlovskul). Halloween details: https://solnacentrum.se/events/halloween/. Fjärilskvarteret is a new permanent indoor play area._
- **Solna kulturskola – evenemang och aktiviteter** — kommun, gives events, family medium, ~3 items  
  https://www.solna.se/uppleva--gora/kultur-och-noje/solna-kulturskola/evenemang-och-aktiviteter-pa-kulturskolan  
  e.g. Kulturskolan på Bokmässan 14 nov (Biblioteket i Solna centrum); Pinocchio – familjeföreställning 17 dec (fri entré); Streetstar Dance School Challenge 29 okt  
  _Small but unique list of student concerts and shows. Event pages follow the pattern .../evenemang-kulturskolan/<date>-<slug>._
- **Kungliga slotten – kalendarium filtrerat på Ulriksdals slott + Gustav III:s paviljong (Ha…** — museum, gives events, family medium, ~3 items  
  https://www.kungligaslotten.se/kalendarium.html?besoksmal%5B%5D=4.46ca39931600d1b7b981965&besoksmal%5B%5D=4.46ca39931600d1b7b981989  
  e.g. Höstmarknad på Ulriksdal 23, 24, 25 okt (Familj/Höstlov)  
  _Server-side besoksmal[] filter for the two royal sites in Solna. Few items now, but Ulriksdal has seasonal markets (jul) and 'Barnens Ulriksdal'. The same calendar is listed under Stockholm with other filters._
- **Lekplatser i Solna** — kommun, gives places, family high, ~46 items  
  https://www.solna.se/uppleva--gora/for-barn-och-unga/lekplatser-i-solna  
  e.g. Skytteholmsparken; Järvastadens skogslekplats; Mulle Meck-parken  
  _PLACES: 46 numbered public playgrounds with locations._
- **Badplatser och friluftsbad i Solna** — kommun, gives places, family medium, ~7 items  
  https://www.solna.se/uppleva--gora/idrott-och-anlaggningar/badplatser-och-friluftsbad  
  e.g. Huvudstabadet; Frösundavik strandbad; Plaskdamm Hagalundsparken  
  _PLACES: 2 outdoor pools, 2 beaches and 3 plaskdammar._

### Stockholm — 36 total (24 new)

- **Stockholms stad – Kalendarium (Barn och familj + Parklek + Kulturskolan)** — kommun, gives events, family high, ~109 items  
  https://start.stockholm/aktuellt/?t=event&c=279&c=885&c=760  
  e.g. Höstlov i Stadshuset: familjevisning och pyssel 26 okt; Grilla popcorn i parkleken 26 okt; Lilla spöket Laban busar vidare 23 okt  
  _Biggest new source: the city-wide calendar for all stadsdelar (parklekar, fritidsgårdar, Kulturskolan, Stadshuset, Stadsmuseet, Medeltidsmuseet, Skarpnäcks kulturhus). Server-rendered HTML, 9 per page, paging &sida=N (12 pages for this filter). Category ids:…_
- **Kungliga slotten – kalendarium (Familj/För barn, Kungliga slottet + Kungliga Djurgården +…** — museum, gives events, family high, ~31 items  
  https://www.kungligaslotten.se/kalendarium.html?kategorier%5B%5D=Familj&kategorier%5B%5D=F%C3%B6r+barn&kategorier%5B%5D=H%C3%B6stlov&besoksmal%5B%5D=4.46ca39931600d1b7b981945&besoksmal%5B%5D=4.3ced9ede1817ff2e17c1cabb&besoksmal%5B%5D=4.46ca39931600d1b7b98198f  
  e.g. Höstlovsjakt på Kungliga slottet 24 okt–1 nov; Familjevisning på Kungliga slottet lördagar 24 okt–26 dec; Juljakt på Kungliga slottet 26 dec–6 jan  
  _Server-side filter via kategorier[] and besoksmal[] params. Without filters the calendar has ~70 dates, also covering Drottningholm (Ekerö), Gripsholm (Strängnäs) and Ulriksdal/Haga (Solna). Each date has its own ?occasion= link._
- **Moderna Museet Stockholm – kalender** — museum, gives events, family high, ~30 items  
  https://www.modernamuseet.se/sv/stockholm/kalender/  
  e.g. Familjevisning för 3–6 år 24 okt; Drop-in i Verkstan 24–31 okt (daily); Babyvisning & måleri 22 okt  
  _About 61 events in the next 10 days, 30 of them tagged Familj (family tours for 3–6 and 7+, Verkstan drop-in, babyvisning). Shows about 10 days ahead, then loads more._
- **Nationalmuseum – kalender** — museum, gives events, family medium, ~4 items  
  https://www.nationalmuseum.se/kalendarium  
  e.g. Babyvisning: I det blå 23 okt; Teckningsfest vid havet! 24 okt; Familjedag i ateljéerna 25 okt (every Sunday, 4+)  
  _Dense calendar (~20 events per 5 days), mostly adult tours, but has recurring family items: Familjedag i ateljéerna every Sunday, babyvisningar, free Thursday drop-in ateljé. JS-rendered with a 'Visa mer' button, so it needs a headless browser. Count = family…_
- **Nordiska museet – evenemang** — museum, gives events, family high, ~11 items  
  https://www.nordiskamuseet.se/evenemang/  
  e.g. Höstlov på Nordiska museet 24 okt–1 nov; Natt på Nordiska museet 27–28 okt; Arkivens dag 14 nov  
  _Page 1 of 5 shows 22 listings, 11 tagged 'Barn & familj'. The category filter runs in JS (no URL param). Each lov day is its own listing._
- **Skansen – kalender (dagens program)** — park, gives both, family high, ~14 items  
  https://www.skansen.se/kalender/  
  e.g. Halloween på Skansen 24 och 28–31 okt; Träffa en djurvårdare på Lill-Skansen (daily, För barn); Djurprat om säl  
  _Day-by-day program with a 'Välj datum' date picker and 'För barn' tags (about 14 items per day). The höstlov and Halloween overview is at https://www.skansen.se/se-och-gora/for-barn/hostlov/. Skansen itself is also a top permanent place._
- **Junibacken – kalendarium** — museum, gives both, family high, ~4 items  
  https://www.junibacken.se/infor-ditt-besok/kalendarium/  
  e.g. Babydrama: Titta! Pippi! (från 6 mån) 11:00 & 15:00; Teater: Hur gick det sen? (premiär 16 okt, från 3 år); Läslov 12 okt–1 nov  
  _Day-by-day program (date picker, cdate=YYYY-MM-DD param) of daily theatre shows and activities. Lov program: https://www.junibacken.se/lov-pa-junibacken/laslov-pa-junibacken/. Count = items per day._
- **Tekniska museet – kalendarium** — museum, gives events, family high, ~6 items  
  https://www.tekniskamuseet.se/pa-gang/  
  e.g. Höstlov på Tekniska museet 24 okt–1 nov; DEMOstage: testa spel med KTH 30 okt; Föräldralediga fredagar t.o.m. 18 dec  
  _13 listings, 6 for families (höstlov, Barnklubb, Helger på Tekniska, kurser på lov, Klubbverksamhet i Tensta). Server-rendered._
- **Scenkonstmuseet – evenemang** — museum, gives events, family high, ~17 items  
  https://scenkonstmuseet.se/evenemang/  
  e.g. Halloweendisco 30 okt; Efter föris: Musiklek 6 & 13 nov; Bebisföreställning VAU VAU 24–25 nov  
  _17 child/family events from Oct on: weekly Bebisvisning & musikstund, 'Efter föris' series, höstlov workshops (maskverkstad, spökhistorier). Marionetteatern is housed here. Server-rendered WordPress archive._
- **Polismuseet – kalendarium** — museum, gives events, family high, ~24 items  
  https://polismuseet.se/besok-polismuseet/kalendarium/  
  e.g. Barnvisning: Här är polisen! 24–31 okt 13:00; Familjevisning: Polisliv 24–31 okt 15:00; Från brott till bevis (11+) 24–31 okt  
  _Week-by-week calendar; 24 child/family showtimes in the höstlov week. Höstlov page: https://polismuseet.se/besok-polismuseet/hostlov2026/._
- **Etnografiska museet – kalendarium Barn & Familj** — museum, gives events, family high, ~25 items  
  https://www.etnografiskamuseet.se/kalendarium/barn--familj/  
  e.g. Sagostund 23 okt; Gör din egen japanska spöklykta 25–27 okt; Japanska spökhistorier 27 okt  
  _Server-rendered, 9 per page, 3 pages. Höstlov program: https://www.etnografiskamuseet.se/hostlov-2026/ (Yokai, Día de Muertos). Its sister museum Medelhavsmuseet has the same kind of filter: https://www.medelhavsmuseet.se/kalendarium/barn-och-familj/ ('Visnin…_
- **Royal Djurgården – kalender (alla aktörer på Djurgården)** — visit, gives events, family medium, ~18 items  
  https://royaldjurgarden.se/kalender/  
  e.g. Familjeaktiviteter på Vasamuseet (t.o.m. 31 dec); Lekstugan på Nordiska museet; Teater på Junibacken  
  _Djurgården-wide aggregator (Tekniska, Nordiska, Vasamuseet, Junibacken, Spritmuseum, Thielska, Waldemarsudde, Riksidrottsmuseum …), 18 per page, 6 pages (/kalender/page/N/). The Kategori filter (För barn / Familj / Höstlov) runs in JS with no URL param. Partl…_
- **Barnistan – Teater, dans och musik för barn i Stockholm (aktuella föreställningar)** — aggregator, gives events, family high, ~15 items  
  https://www.barnistan.se/stockholm/teaterdansmusik/aktuell-teater/  
  e.g. Hundliv 20–30 okt (Kulturhuset Stadsteatern, 3–10 år); Lorpan längtar 21 okt–22 nov (Dockteatern Tittut, 2–6 år); Humlan Djojj på äventyr 24 okt (Berwaldhallen…  
  _Same publisher as the existing Barnistan event list, but a separate curated list of all running children's theatre, dance and music productions, small stages included (Teater Bristol in Sundbyberg, Dockteatern Tittut, Konserthuset Sagolek). Good for finding s…_
- **Berwaldhallen – Barn & Ungdom** — kulturhus, gives events, family high, ~10 items  
  https://www.berwaldhallen.se/barn-och-ungdom  
  e.g. Humlan Djojj på äventyr med Radiosymfonikerna 24 okt; Lucia med Nacka Musikklasser 6 dec; Niklas & Radioapan 30 jan  
  _10 upcoming children's/youth concerts (includes Streetstar dance-school finals 29–31 okt). Full calendar: https://www.berwaldhallen.se/kalendarium._
- **Konserthuset Stockholm – För de minsta 0–5 år** — kulturhus, gives events, family high, ~23 items  
  https://www.konserthuset.se/barn-och-unga/for-de-minsta-0-5-ar/  
  e.g. Klassiskt med bebis 21–22 okt; Sagolek – Den lille prinsen 25 okt; Familjekonsert Jul-sing-along 13 dec (5–10 år)  
  _8 productions and 23 showtimes through May 2027, often sold out early. Sister page for 5–10 år: https://www.konserthuset.se/barn-och-unga/for-barn-5-10-ar/. The main calendar's 'Barn & familj' genre filter is POST-only, so use these pages._
- **Sjöhistoriska museet – kalender** — museum, gives events, family medium, ~3 items  
  https://www.sjohistoriska.se/besok/kalender  
  e.g. Vågar ni möta havets spöken? 24 okt–1 nov (höstlov); Skaparverkstaden Ruskpricken every weekend; Familjevisning: Paddla! (t.o.m. 13 dec)  
  _JS-rendered (SMTM platform, same as Vasamuseet), so it needs a headless browser. Has filters 'För barn' and 'Höstlov'. Few but recurring family items._
- **Naturhistoriska riksmuseet – kalendarium** — museum, gives events, family medium, ~4 items  
  https://www.nrm.se/vart-utbud/kalendarium  
  e.g. Höstlov 24 okt–1 nov: Skapa din egen dinosauriervärld i Labbet (3+); T-rex i Cosmonova daily; Ocean Dreams premiär 24 okt  
  _Day view with a date filter (mainly Cosmonova shows plus programs). The lov program is on a separate page, https://www.nrm.se/hostlov (dinosaur hunt, Labbet workshops, pop-up visningar). Count = family items per day._
- **Dockteatern Tittut – kalendarium höst 2026** — teater, gives events, family high, ~20 items  
  https://dockteaterntittut.se/kalendarium/  
  e.g. Babysalong 20 okt; Lorpan längtar 21–24 okt; Petras prick nypremiär 25 nov  
  _Puppet theatre for ages 2–7 (Lundagatan 33, Södermalm, plus Blå huset in Tensta). The schedule is published as an IMAGE ('Kalendarium höst 2026'), so it must be read manually or with OCR. Tickets via Nortic organiser 3717. Count is approximate._
- **Armémuseum – kalendern** — museum, gives events, family medium, ~3 items  
  https://armemuseum.se/kalender/  
  e.g. Höstlovsvisningar: Mysteriet på Armémuseum 24 okt–1 nov; Höstlov: Aktiviteter på Armémuseum 24 okt–1 nov; Interaktiv visning: Rädd eller beredd 7 nov–20 dec  
  _About 10 upcoming items with filters (Familjevisning, Höstlov, Workshop). JS-rendered (the template shows {{ }} without JS), so it needs a headless browser._
- **Livrustkammaren – kalender** — museum, gives events, family medium, ~2 items  
  https://livrustkammaren.se/besok/kalender/  
  e.g. Riddarmaskerad (Riddarklubben) 24 okt; Lilla klädkammaren 25 okt–1 nov (höstlov, free under 18)  
  _Small, but its family items are unique (Riddarklubben). The same agency runs Hallwylska museet (https://hallwylskamuseet.se/pa-gang/kalender/, 'Hallwyleen' familjevisning 24 okt–1 nov) and Historiska museet (https://historiska.se/besok-oss/pa-gang/, 'Höstlov:…_
- **Liljevalchs+ – kalender** — museum, gives events, family medium, ~2 items  
  https://liljevalchs.se/kalender/  
  e.g. Höstlovet på Liljevalchs 26 okt–1 nov; Skaparverkstad: Masker (t.o.m. 10 jan)  
  _6 upcoming items, 2 for children. The page <title> is stale ('Evenemang från 2018–2020'), but the content is current._
- **Vasamuseet – kalender** — museum, gives events, family medium, ~2 items  
  https://www.vasamuseet.se/besok/kalender  
  e.g. NPF-anpassad visning för barn och ungdomar 21 okt; Undergång – deckarspel på höstlovet 26–30 okt (från 10 år)  
  _JS-rendered (SMTM platform), filter 'Höstlov'/'Visning'. Few items, but Vasamuseet is a top family attraction._
- **Kista Galleria – aktuellt** — shopping, gives events, family medium, ~4 items  
  https://www.kistagalleria.se/aktuellt/  
  e.g. Scarlet + monsterrunda (Halloween familjedag) 24 okt; Bakluckeloppis 25 okt, 22 nov, 13 dec  
  _Shopping-centre events with the 'Kista Kids' club. Other Stockholm centres were checked and are weak or have no event page: Liljeholmstorget has only a loppis, Farsta/Gallerian/Skärholmen have no event page, Vällingby City's domain is broken._
- **Stockholms stad – Hitta lekplatser, parklekar och plaskdammar** — kommun, gives places, family high, ~498 items  
  https://parker.stockholm/hitta-lekplatser-parklekar-plaskdammar/  
  e.g. 498 lekplatser/parklekar/plaskdammar searchable by type and stadsdel  
  _PLACES source. JS search app (results load after a few seconds; the ?servicetyp= links return 0 without JS). Each place has its own page. Parklek events are in start.stockholm c=885._

### Sundbyberg — 11 total (4 new)

- **Sundbybergs stad – Lovaktiviteter (höstlov 2026)** — kommun, gives events, family high, ~18 items  
  https://www.sundbyberg.se/uppleva-och-gora/ung-i-sundbyberg/lovaktiviteter  
  e.g. Haunted House 27–29 okt (Kulturcentrum, 4–15 år); Familjelördag: Musikfest i Kulturhuset 24 okt (0–9 år); Hinderbana i simhallen v.44  
  _18 lov activities with date, place, age and sign-up info. Many are not in the existing kommun calendar (fritidsgårdar, simhall, Kulturcentrum, Marabouparken). The page is refreshed for each lov. The Kulturkalendern page was checked and is only a subset of the…_
- **Teater Bristol – barnteater i Sundbyberg** — teater, gives events, family high, ~82 items  
  https://www.teaterbristol.se/  
  e.g. God natt, Alfons Åberg 24 okt (från 2 år); Mamma Mu och Kråkans jul från 14 nov (36 föreställningar); Pettson får julbesök från 28 nov  
  _Children's theatre at Sturegatan 39. 6 family productions with about 82 showtimes this autumn ('Fler datum' expands each one). Prices 185–195 kr._
- **Marabouparken konsthall – program** — museum, gives both, family medium, ~1 items  
  https://marabouparken.se/  
  e.g. Textil + Kompost = Sant! höstlovsläger 28–30 okt (12+); Monsterklubben (kreativ verkstad för barn); utställning Éva Mag 24 okt–7 mar  
  _The program is on the homepage; https://marabouparken.se/evenemang/ currently says 'Fler evenemang kommer snart'. The konsthall reopens 24 okt. The sculpture park is a strong permanent place._
- **Sundbyberg – Parker, grönområden och naturreservat** — kommun, gives places, family medium, ~8 items  
  https://www.sundbyberg.se/bygga-bo-och-miljo/naturvard-parker/parker-gronomraden-och-naturreservat  
  e.g. Igelbäckens naturreservat; Lötsjön-Golfängarnas naturreservat; Tornparken  
  _PLACES: 3 nature reserves and 5 stadsdelsparker, with subpages. Sundbyberg has no lekplats list page (checked)._

### Södertälje — 20 total (10 new)

- **Södertälje kommun – Kulturlovet (höstlovsprogram)** — kommun, gives events, family high, ~61 items  
  https://www.sodertalje.se/kultur-och-fritid/kulturlov/  
  e.g. Skapandeverkstad på Verkstan 26–30 okt; Kryp-in sångstund 28 okt (Barnens hus); 'När mörkret faller' på Torekällberget 29–31 okt  
  _A seasonal kulturlov page with 61 activities across bibliotek, TIO14, Torekällberget, Futurum, Mosaik, fritidsgårdar, sporthallar and stadshuset. Each item has 'Plats:' and 'Datum och tid:' fields, so it is easy to parse. Only partly in the library calendar._
- **Futurum Järna – Aktiviteter (kulturhus: bibliotek, kulturskola, fritidsgård)** — kulturhus, gives events, family high, ~25 items  
  https://www.sodertalje.se/kultur-och-fritid/futurum/aktiviteter-pa-futurum/  
  e.g. Barnteater 'Nicke Nyfiken' 27 okt; Halloween knattedisco åk 1–5 27 okt; Sagostund med spöktema 29 okt  
  _A kulturhus in Järna with a dated activity list of about 25 items: sagoyoga, filmklubb 6+/10+, skaparverkstad, plus some senior items. It covers the Järna area, which our sources missed._
- **Tom Tits Experiment – Höstlov / program (science center)** — museum, gives both, family high, ~0 items ⚠️ not verified  
  https://www.tomtit.se/besok/planera-ditt-besok/lov/hostlov/  
  e.g. Höstlov program 24 okt–1 nov (per Barnistan/Destination Södertälje); 'Tom Tits för de allra minsta' (0–2 år) weekdays  
  _Sweden's largest science center and a must-have source and place. The URL comes from Destination Södertälje's höstlov guide; the homepage is https://www.tomtit.se/ and the English program page is /en/visiting/free-time-programs/. We could not load it today, s…_
- **Torekällbergets friluftsmuseum – Evenemang** — museum, gives both, family high, ~4 items  
  https://www.sodertalje.se/kultur-och-fritid/torekallberget/evenemang/  
  e.g. Höstlov på Torekällberget 24 okt–1 nov; 'När mörkret faller' 29–31 okt; Julstök på Berget (julmarknad) 5–6 dec  
  _An open-air museum with animals, Lillboden (lek & pyssel every weekend and lov) and free entry. There are few events, but all family-relevant. The skollov page is /evenemang/skollov/._
- **Destination Södertälje – Höstlov i Södertälje (guide)** — visit, gives events, family medium, ~7 items  
  https://www.destinationsodertalje.se/upptack-sodertalje/hostlov-i-sodertalje-2025/  
  e.g. Halloweenparad & spökhus i city 29 okt; Spökhus på Futurum i Järna; Kulturfestival 24 okt (~80 programpunkter)  
  _A curated lov guide that is not the same page as the existing evenemangskalender. The slug says 2025 but the content is for 2026 (updated 2026-10-15), so the URL is reused each year. It links Tom Tits, Torekällberget and Sydpoolen._
- **Södertälje City – evenemang i stadskärnan** — shopping, gives events, family medium, ~3 items  
  https://sodertaljecity.se/  
  e.g. Halloweenparad & spökhus 29 okt (/halloween2026/); Kulturfesten 24 okt; Julmarknad på Järnagatan 19–20 dec (/julmarknad/)  
  _The city-centre association. Events are published as articles on the start page (no calendar). It handles the big family city events: Halloween parade, julmarknad and sommar._
- **Destination Södertälje – För barnen och de lekfulla** — visit, gives places, family low, ~0 items  
  https://www.destinationsodertalje.se/upptack-sodertalje/for-barnen-och-de-lekfulla/  
  e.g. Tom Tits Experiment, Torekällberget, Skate- och parkourparken, Actic Sydpoolen (äventyrsbad), Hagabergs sommarcafé  
  _A family places guide. Use it for permanent places._
- **Destination Södertälje – Lekplatser (62 st)** — visit, gives places, family low, ~0 items  
  https://www.destinationsodertalje.se/upptack-sodertalje/lekplatser/  
  e.g. Badparken, Dalparken (tillgänglig lekplats), Brunnsängs gärde  
  _A playground guide (62 lekplatser) with highlighted utflyktslekplatser. Use it for places._
- **Södertälje kommun – Utflyktsmål i naturen** — kommun, gives places, family low, ~0 items  
  https://www.sodertalje.se/kultur-och-fritid/natur-och-friluftsliv/utflykter-i-naturen/  
  e.g. Farstanäs, Tullgarn, Lina, Bornsjön naturreservat m.fl. (~28 utflyktsmål)  
  _A list of nature reserves and excursion spots with subpages. Badplatser are at /natur-och-friluftsliv/badplatser/. Use it for places._
- **Naturkartan – Södertälje kommun** — natur, gives places, family low, ~0 items  
  https://www.naturkartan.se/sv/sodertalje  
  e.g. Naturreservat, leder (Ekoleden), badplatser  
  _The official kommun nature guide on Naturkartan. Use it for places._

### Täby — 11 total (4 new)

- **Täby kulturskola – Lovkurser (Studyalong kurskatalog)** — other, gives events, family medium, ~11 items  
  https://studyalong.se/?option=com_pa_coursemanager&task=coursefinder.show&Itemid=71&sid=83#subject=Lovkurser  
  e.g. TEATERKUL höstlovskurs 7–9 år 29 okt; KULTURLÄGER höstlovskurs 27–28 okt; SKAPA SPEL höstlovskurs 26–28 okt  
  _Täby kulturskola's booking catalogue (linked from taby.se 'Höstlovskurser!'). These are bookable, paid lov courses from several providers (Academy Musikstil, Ung kultur, Opus Norden, Musikhuset), not drop-in events. Needs a JS browser. Use the period filter L…_
- **Täby kommun – Lekplatser** — kommun, gives places, family high, ~0 items  
  https://www.taby.se/uppleva-och-gora/natur-och-friluftsliv/lekplatser  
  e.g. Cirkusleken; Havsleken; Flygleken  
  _PLACES: themed playgrounds, 14 shown plus 'Visa fler lekplatser'._
- **Naturkartan – Täby kommun** — natur, gives places, family medium, ~0 items  
  https://www.naturkartan.se/sv/taby  
  e.g. Vandringsleder, friluftsområden, badplatser, grillplatser  
  _PLACES: the official Täby nature guide (linked from taby.se). It has trails, naturreservat and utflyktsmål with map data._
- **Täby kommun – Friluftsgårdar** — kommun, gives places, family low, ~0 items  
  https://www.taby.se/uppleva-och-gora/natur-och-friluftsliv/friluftsgardar  
  e.g. Ensta krog friluftsgård; Skavlötens friluftsgård  
  _PLACES: two outdoor activity farms/huts with cafés, good family outing spots (skidåkning, grill)._

### Tyresö — 17 total (7 new)

- **Tyresö kommun – Höstlov 2026** — kommun, gives events, family high, ~24 items  
  https://www.tyreso.se/uppleva--gora/kultur-och-fritid-for-barn-och-unga/hostlov-2026.html  
  e.g. Maskverkstad för familjer 27–28 okt; Sagostund med nallesövning (bibliotek) 27 okt; Öppen bildverkstad på kulturskolan (födda 2014–2020) 26–29 okt  
  _24 lov sessions from the library, kulturskola, Medley simhall, fritidsgårdar and Passalen, with ages given. Many under-12 activities. The URL changes each lov (look for sportlov-2027 etc. in /kultur-och-fritid-for-barn-och-unga/). The existing tyreso.se/arkiv…_
- **Tickster – Tyresö kommun (kulturprogram: Familjelördagar, Kulturtimmen)** — ticketing, gives events, family medium, ~9 items  
  https://www.tickster.com/se/sv/events/by/l74k7rw5vbx2cbn/tyreso-kommun  
  e.g. Familjelördag: Giraffens ABC (Kulturcentrum Kvarnhjulet) 14 nov; Å bebis, bebis (biblioteket) 15 nov; Cirkusföreställning Unplugged (Scen Forellen) 14 nov  
  _Organiser feed for Tyresö kommun's own culture program: the Familjedagar series (free for children), Kulturtimmen and cirkus/teater. It is linked from tyreso.se/uppleva--gora/kultur-och-noje/kultur-i-tyreso.html, which also has a monthly PDF 'Månadsbladet'. I…_
- **Tyresö kommun – Naturguidningar** — natur, gives events, family medium, ~6 items  
  https://www.tyreso.se/uppleva--gora/natur-och-friluftsliv/naturguidningar.html  
  e.g. Norra Tyresta och Tyresö-Flaten 25 & 26 okt; Höstvandring i Alby naturreservat 5 nov; Människan och skogen 20 & 21 nov  
  _Guided nature walks with sign-up, about 6 upcoming. Family suitability is not stated; the easy 3 km walks fit families best. Naturkartan says these walks are also in tyreso.se's calendar._
- **Tyresö Centrum – Aktuellt (Iggeklubben m.m.)** — shopping, gives events, family medium, ~1 items  
  https://www.tyresocentrum.se/aktuellt/  
  e.g. Iggeklubben Halloweenfest + boksläpp 24 okt 12–15  
  _Shopping centre news feed. Its recurring kids' club 'Iggeklubben' runs about once a month (2026 series: 21 feb, 21 mar, 25 apr, 23 maj, 22 aug, 22 sep, 24 okt), plus jul/Halloween events. 11 of the last 20 posts were kids or family. Only 1 event is upcoming r…_
- **Tyresö kulturskola – Se & Göra** — other, gives events, family low, ~1 items  
  https://www.tyreso.se/tyreso-kulturskola/se--gora.html  
  e.g. Öppen kulturskola i Granängsringen, torsdagar 14–17.30 (gratis drop-in)  
  _A recurring free drop-in for kids (no specific dates); lov workshops appear on the höstlov page. Watch it for the vår/jul concerts._
- **Tyresö kommun – Badplatser och friluftsbad** — kommun, gives places, family low, ~0 items  
  https://www.tyreso.se/uppleva--gora/natur-och-friluftsliv/badplatser-och-friluftsbad.html  
  e.g. Strandbadet (lekplats, kiosk); Albysjön (lån av SUP och flytvästar); Kumlabadet  
  _Permanent places: 13 bathing places with facilities. Also /natur-och-friluftsliv/natur--och-friluftsomraden.html (8 areas: Alby, Barnsjön, Tyresö slottsområde …) and /uppleva--gora/idrottshallar-lokaler-och-anlaggningar/kommunala-lekplatser.html (map only)._
- **Naturkartan – Tyresö** — natur, gives places, family low, ~0 items  
  https://www.naturkartan.se/sv/tyreso  
  e.g. Miniguides: Kolardammarna, Tyresö slottspark, grillplatser  
  _The official kommun guide on Naturkartan: 14 map categories (naturreservat, nationalpark, badplats, grillplats, grotta …). Places load by JS or API._

### Upplands-Bro — 13 total (6 new)

- **Bio Kuben – biograf i Kulturhuset Kungsängen** — other, gives events, family high, ~16 items  
  https://biokuben.se/  
  e.g. Fåret Shaun och monstret på bondgården 30 okt; Lilla spöket Laban busar vidare 31 okt; Bamse och havets hemlighet 21 nov  
  _Cinema run by UMTS (förening) in Kulturhuset; many family films in höstlov. Static HTML schedule (same bio.se platform as Gröna Ladan Sigtuna)._
- **Öppna förskolan Bro & Kungsängen** — kommun, gives both, family medium, ~0 items  
  https://www.upplands-bro.se/forskola-och-skola/forskola/oppna-forskolan.html  
  e.g. Fredagar på Bro IP: rörelsesamling 10.15 + babyrytmik 11.00; sångstund 0–5 år; kulturevenemang för baby i Kulturhuset (anmälan)  
  _Recurring weekly program for 0–5 år (free, drop-in); dated items published via Facebook and kommun calendar._
- **Lekplatser och parker i Upplands-Bro** — kommun, gives places, family high, ~0 items  
  https://www.upplands-bro.se/uppleva-och-gora/lekplatser-och-parker.html  
  e.g. Drömparken (Kungsängen); Stjärnparken (Bro); Trafiklekplatsen i Målarparken  
  _PLACES: 14 lekplatser with own sub-pages (vikingatema, trafiklekplats, Nyckelbergsparken)._
- **Badplatser i Upplands-Bro** — kommun, gives places, family low, ~0 items  
  https://www.upplands-bro.se/uppleva-och-gora/badplatser.html  
  e.g. Lillsjö badplats (lekplats, beachvolley); Hällkana; Björknäs  
  _PLACES: 7 badplatser._
- **Naturkartan – Upplands-Bro kommun** — natur, gives places, family low, ~0 items  
  https://www.naturkartan.se/sv/upplands-bro  
  e.g. Upplands-Broleden; Lejondals naturreservat; Frölunda naturreservat  
  _PLACES: naturreservat, kulturmiljöer, vandring (JS site)._
- **Naturskyddsföreningen Upplands-Bro – aktiviteter** — natur, gives events, family low, ~1 items  
  https://upplands-bro.naturskyddsforeningen.se/  
  e.g. Höstsvampvandring Lillsjön–Örnässjön 25 okt  
  _Weak (1 upcoming) but only independent nature-organiser listing found for the kommun._

### Upplands Väsby — 13 total (7 new)

- **Höstlov i Väsby (kommun lovsida)** — kommun, gives both, family high, ~22 items  
  https://www.upplandsvasby.se/uppleva-och-gora/ung-i-kommunen/hostlov-i-vasby  
  e.g. Höstlovsteater: Bygget 26 okt (Messingen); Mördande magi – väsenvandring Gunnes gård 27–28 okt; Bygg och koda ett instrument 9–13 år 30 okt (Sigma)  
  _Static HTML lov page (26 okt–1 nov) = curated lov event list + tips (Gunnes gård, skridskor Vilundaparken, Fritidsbanken, lekplatser, Naturkartan). Event items come from the kommun calendar but pre-filtered for lov._
- **Vikingagården Gunnes gård – friluftsmuseum** — museum, gives both, family high, ~4 items  
  https://www.upplandsvasby.se/minisajter/gunnes-gard  
  e.g. Tema Hus och gård 24–25 okt; Mördande magi – en väsenvandring 27–28 okt; Höstlovsöppet 29–30 okt  
  _Venue minisite with own event list (feeds from kommun calendar ?query=gunnes), opening hours, visningar, djuren – also a strong PERMANENT place._
- **Scen Messingen (Upplands Väsby kommun) – Nortic biljetter** — ticketing, gives events, family medium, ~12 items  
  https://www.nortic.se/customer/organizereventlist/871  
  e.g. Babyonsdag: Oj min socka 21 okt; Höstlovsteater: Bygget 26 okt; Babyonsdag: Dansa med bebis 25 nov  
  _Kommunens scenkonstprogram i Messingen (category filter incl. Barnteater). Same program shown at https://www.upplandsvasby.se/uppleva-och-gora/motesplatser/kultur--och-aktivitetshus . Mix of family and adult (Riksteatern, författarkvällar)._
- **Upplands Väsby kulturskola – evenemang** — kommun, gives events, family high, ~9 items  
  https://www.upplandsvasby.se/skola/upplands-vasby-kulturskola/evenemang  
  e.g. Konst lovkurs 28 okt; Film – lovkurs 28 okt; Lördagsöppet på Kulturskolan (tema musik) 7 nov  
  _Free concerts, lovkurser and 'Lördagsöppet' prova-på (konst/film/musik) at Messingen; static HTML list._
- **Friluftsfrämjandet Upplands Väsby – äventyr** — förening, gives events, family medium, ~21 items  
  https://www.friluftsframjandet.se/upplands-vasby  
  e.g. Friluftscafé i Fresta söndagar 8–29 nov (gratis, ingen anmälan); Skridskoskola nivå 3–5 från 7 nov; Vildmarksäventyr Lodjursgruppen  
  _JS-rendered list; courses + free drop-in friluftscafé; some adult trips._
- **Lekplatser i Upplands Väsby + Törnskogens sagostig** — kommun, gives places, family high, ~0 items  
  https://www.upplandsvasby.se/trafik-och-resor/torg-och-allmanna-platser/lekplatser  
  e.g. Barnens Wäsby Verkstäder (Vilundaparken); Obelixparken (Björkvallavägen); Törnskogens sagostig (800 m, 10 stationer)  
  _PLACES: ~40 lekplatser by area + interactive map._
- **Naturkartan – Upplands Väsby kommun** — natur, gives places, family low, ~0 items  
  https://www.naturkartan.se/sv/upplands-vasby  
  e.g. Runby spårstart utegym; Vilundaparken; badplatser och vandring  
  _PLACES: kommun guide (promenad, utegym, vandring, badplats); also has an 'Evenemang' tab (JS site)._

### Vallentuna — 9 total (4 new)

- **Vallentuna kommun – Evenemang (ny kalender-URL)** — kommun, gives events, family high, ~139 items  
  https://www.vallentuna.se/uppleva-och-gora/evenemang-och-motesplatser/evenemang  
  e.g. Kulturhuskalas! Vallentuna kulturhus 24 okt; barnKUL: Sagan som rymde 24 okt; Lovbio: Nelly Rapp – Porten till underjorden 29 okt  
  _IMPORTANT: the existing URL vallentuna.se/evenemang-och-upplevelser/evenemangskalender/ now redirects to the 'Utställningar' page, not the calendar. This is the live calendar (139 hits, 16 pages), covering kulturhus, Caféscenen, libraries, KUBen Karby and kul…_
- **Vallentuna kommun – Höstlovsaktiviteter** — kommun, gives events, family medium, ~11 items  
  https://www.vallentuna.se/uppleva-och-gora/evenemang-och-motesplatser/hostlov  
  e.g. Laserdome (fritidsgårdarna) 26 okt; Halloweenfest på fritidsgården Mega 30 okt; Skattjakt på Vallentuna kulturhus hela lovet  
  _A seasonal lov page that gathers fritidsgård, kulturskola and library lov activities. Some items are not in the calendar, and some are youth (10+). Expect the same pattern for other lovs; the URL may change per lov._
- **Vallentuna kommun – Lekplatser och parker** — kommun, gives places, family high, ~0 items  
  https://www.vallentuna.se/uppleva-och-gora/lekplatser-och-parker  
  e.g. Biblioteksparkens lekplats; Lasseparken; Åbyholmsparken  
  _PLACES: 26 playgrounds and parks, each with its own subpage._
- **Naturkartan – Vallentuna kommun** — natur, gives places, family medium, ~0 items  
  https://www.naturkartan.se/sv/vallentuna  
  e.g. Vallentunasjön runt (ca 15 km); Barnäventyr; badplatser och grillplatser  
  _PLACES: the official nature guide, with the categories Barnäventyr, Badplats, Grillplats, Vandring, Pilgrimsled and 6 miniguider._

### Vaxholm — 9 total (4 new)

- **Vaxholms Fästnings Museum (Kastellet) – lovaktiviteter** — museum, gives both, family medium, ~1 items  
  https://www.vaxholmsfastning.se/  
  e.g. Höstlovshelg 24–25 okt 11.40–15.40: drop-in äventyr med Kalle Kanonkula, Dunderdraken & Sockerhäxan, Råttan Rasmus-spår, barnverkstad  
  _The archipelago's largest museum, on an island reached by ferry. Children 0–12 get in free, with free activities for 4–15 year-olds. It has no separate calendar: lov events are posted on the homepage, and it is open in winter only for lov and special events.…_
- **Vaxholms stad – Lekplatser** — kommun, gives places, family low, ~0 items  
  https://www.vaxholm.se/uppleva--gora/idrott-motion-och-friluftsliv/friluftsliv-och-motion/lekplatser  
  e.g. Lägrets lekplats (belyst, hinderbana från 6 år); Rindö lekplats (inhägnad); Överbybadets lekplats  
  _Permanent places: 12 municipal playgrounds with locations (Vaxön, Resarö, Rindö, Bogesund)._
- **Vaxholms stad – Badplatser** — kommun, gives places, family low, ~0 items  
  https://www.vaxholm.se/uppleva--gora/idrott-motion-och-friluftsliv/friluftsliv-och-motion/badplatser  
  e.g. Överbybadet (familjevänlig, lekplats); Tenöbadet; Eriksö badplats  
  _Permanent places: 12 bathing places across 6 islands, with facilities._
- **Naturkartan – Vaxholm** — natur, gives places, family low, ~0 items  
  https://www.naturkartan.se/sv/vaxholm  
  e.g. Miniguide 'Badplatser i Vaxholm'; vandring, paddling, naturhamnar  
  _Naturkartan city guide with 24 activity categories. Places load by JS or API; it had no events._

### Värmdö — 10 total (4 new)

- **Gustavsbergs Porslinsmuseum – kalendarium** — museum, gives events, family high, ~12 items  
  https://gustavsbergsporslinsmuseum.se/kalendarium  
  e.g. Familjedag i verkstan 25 okt; Höstlov = Lerlov 30 okt–1 nov (11–14); Jullov = Lerlov  
  _The best new Värmdö source. The calendar data is embedded in the page as JSON (Calendar.init(JSON.parse(...)): 31 event series with categories, incl. 'mest-för-barn-och-deras-nyfikna-vuxna'), so it is easy to scrape. There are recurring lov clay workshops eve…_
- **Porslinsriket Gustavsberg – kalendarium** — visit, gives events, family medium, ~6 items  
  https://www.porslinsriket.se/kalendarium/  
  e.g. Jul Kul i Porslinsriket (julmarknad, öppna ateljéer, för hela familjen) 28–29 nov; Fotoparken 'Min värld' (förskolebarns foton) t.o.m. 3 dec; Stig Lindberg-uts…  
  _Area calendar for the Gustavsberg Porslinsriket quarter (museum, Galleri Panncentralen, Värmdö kulturhus, ateljéer), with 6 upcoming items. Värmdö kommun's calendar links to it as an external calendar. It is mostly culture, plus some family markets and worksh…_
- **Värmdö kommun – Lekparker och spontanidrott** — kommun, gives places, family low, ~0 items  
  https://www.varmdo.se/upplevaochgora/naturochfriluftsliv/lekparkerochspontanidrott.4.18c983316e0536cb189a387.html  
  e.g. Äventyrsleken vid Ösbyträsk; Renparken (Renvägen 38); Båtparken Hemmesta; Vargparken Ingarö  
  _Permanent places: 11 public playgrounds with locations, plus a link to Värmdökartan._
- **Värmdö kommun – Badplatser** — kommun, gives places, family low, ~0 items  
  https://www.varmdo.se/upplevaochgora/naturochfriluftsliv/badplatserivarmdo.4.18c983316e0536cb189a176.html  
  e.g. Ösbyträsk; Trouville (Sandhamn); Djurö Havsbad (Vita grindarna); Grisslinge havsbad  
  _Permanent places: 15 municipal bathing places._

### Uppsala — 23 total (14 new)

- **KUBIK Uppsala – hitta aktiviteter för barn och unga** — aggregator, gives events, family high, ~230 items  
  https://www.kubikuppsala.se/hitta-aktiviteter/  
  e.g. Interaktivt spökäventyr, Sävjabiblioteket 21 okt; Digital skattjakt med Musse & Helium, Uppsala city 24 okt–1 nov; Leksaksbyte på höstlovet, Pumphuset 24 okt–1…  
  _Uppsala kommun's own service for activities for ages 0–25. It collects libraries, fritidsgårdar, allaktivitetshus, Biotopia, Uppsala Naturskola, city events and föreningar (230 activity pages seen). Needs a JS browser to render. The UI has filters for age (?s…_
- **Barnistan (Barn i stan) – evenemang Uppsala** — aggregator, gives events, family high, ~18 items  
  https://www.barnistan.se/uppsala/tips-u/evenemang-uppsala/  
  e.g. Museidagen på Gustavianum 8 nov; Ficklampsläsning, Stadsbiblioteket 29 okt; Uppsala kortfilmfestival familjevisningar, UKK 24–25 okt  
  _The Uppsala section of the Barnistan site the CEO liked. It is hand-curated and family-only. A few items are in Tierp (Kulturhuset Möbeln) and Knivsta (CIK), so check the venue before tagging the city._
- **Biotopia – kalender (inkl. Upplandsstiftelsen/Hammarskog)** — museum, gives events, family high, ~28 items  
  https://biotopia.nu/kalender/  
  e.g. Torsdagskul: Bygga och flyga drake 22 okt; Höstlov: Återbruksverkstad 24 okt–1 nov; Barnens sagostund i Hammarskogs herrgård 28 nov  
  _This is the municipal biology museum. Its calendar also carries Upplandsstiftelsen's nature program: Lördagar i Hammarskog, En höstnatt i Hammarskog, Bäbis i naturen barnvagnspromenader. About 9–12 of 28 items are explicitly for kids or babies. Each item has…_
- **Uppsala Konsert & Kongress – För hela familjen** — kulturhus, gives events, family high, ~24 items  
  https://ukk.se/tema/familj/  
  e.g. Familjekonsert Peter och vargen 24 okt; Från Aladdin till Elsa 30 okt; Saffransmysteriet – LasseMajas detektivbyrå 21 nov  
  _UKK's family theme page, with 24 shows through April 2027 (Bamse och Sjörövarskatten 21 feb, Djungelboken 23 jan, Barnens Julvärld 12 dec). Some general-audience concerts (Ghibli, Laleh) are mixed in, so filter them. The full calendar with Barn & familj tags…_
- **Uppsala universitet – kalendarium, typ Familjeaktivitet (Gustavianum, Evolutionsmuseet, B…** — museum, gives events, family high, ~12 items  
  https://www.uu.se/kalendarium?eventsType=familjeaktivitet  
  e.g. Höstlov – I Brunos fotspår (Gustavianum) 29 okt–1 nov; Tama djur och deras vilda släktingar, höstlov (Evolutionsmuseet) 27 okt; Museidag i regnskogen – tema el…  
  _One filtered URL covers all the university museums and gardens. The individual museum pages (uu.se/gustavianum/kalendarium, uu.se/evolutionsmuseet) do not list events properly. Results are paged 10 at a time ('Visar 10 av 12'). Linnéträdgården and Linnés Hamm…_
- **Uppsala slottshistoriska – kalendarium** — museum, gives events, family medium, ~10 items  
  https://slottshistoriska.uppsala.se/sv/kalendarium/  
  e.g. Höstlov: Ficklampsvisning i slottskällarens mörker 25–30 okt; Höstlov: Spökverkstad; Familjeverkstad: Drottning Kristina 400 år (18 okt)  
  _A new museum in Uppsala slott (opened 2025) with family workshops and lov programs (sportlov, påsklov and höstlov pages too). The calendar shows one month at a time, with 6 of 10 October items for families._
- **Uppsala konstmuseum – kalendarium** — museum, gives events, family medium, ~30 items  
  https://konstmuseum.uppsala.se/kalendarium/  
  e.g. Familjelördag: Magiska reliefer (från 3 år / från 5 år) 24 okt; Dansworkshop 'Vem får jag vara?' (15–25 år) 27–29 okt  
  _The calendar shows one month at a time, with about 6 family items in October. Familjelördagar recur (see /program-och-aktiviteter/familjelordagar/), and there is a seasonal page /hostlovet-pa-uppsala-konstmuseum/. Most other items are adult (Art Night, talks)._
- **Uppsala stadsteater – För barn & familjer** — teater, gives events, family medium, ~8 items  
  https://www.uppsalastadsteater.se/for-barn-familjer/  
  e.g. Monster och gudar (Ettan) 28–31 okt; Huller om buller (och lite snubbel), från 5 år, 28 nov  
  _Small but unique: the theatre's own children's productions plus Lovläger (holiday drama camps). The full repertoire is at /forestallningar/. Reginateatern (municipal guest stage) is closed autumn 2026, so it was not added._
- **Bror Hjorths Hus – kalender, Barn & Familj** — museum, gives events, family medium, ~6 items  
  https://brorhjorthshus.se/kalender/category/familj/  
  e.g. Höstlovskonstskola för barn 8–12 år 27–28 okt; Höstlov: Familjeverkstad 29 okt; Museidagen 8 nov  
  _A filtered family category of the museum calendar. Items are booking-based (konstskola 350 kr, familjeverkstad 50 kr)._
- **Gamla Uppsala museum – kalender** — museum, gives events, family medium, ~5 items  
  https://www.upplandsmuseet.se/gamla-uppsala-museum/gum/  
  e.g. Höstlov: Mat och snacks på vikingatiden 26 okt–1 nov; Vikingaskola: Eld 7–8 nov; Museidagen fri entré 8 nov  
  _This is a separate calendar from the existing Upplandsmuseet KalenderUpplandsmuseet: the GUM events are not in it (checked). gamlauppsalamuseum.se redirects here. The site's certificate fails strict SSL checks in Python, so use a browser or WebFetch._
- **Uppsala kulturskola – kalendarium** — other, gives events, family low, ~8 items  
  https://kulturskola.uppsala.se/kalendarium/  
  e.g. Halloweenkonsert, kulturskolans körsal 23 okt; MUKO möter unga solister, Nannaskolans aula 24 okt  
  _Kulturskola concerts (about 100 public concerts and shows a year). Month view. Some items are abroad (Erasmus+ in Berlin), so filter them. Lov/helgkurser page /amnen/lovkurser/ is empty right now._
- **Tickster – evenemang i Uppsala** — ticketing, gives events, family low, ~308 items  
  https://www.tickster.com/se/sv/events/in/uppsala  
  e.g. Textildetektiv, Uppsala slottshistoriska 22 okt; Uppsala Kortfilmfestival 19–25 okt  
  _The Tickster city page used for Norrtälje is missing for Uppsala. It has 308 events, but mostly adult (Katalin, Flustret 15+/18+), so it needs heavy filtering. Use it only to catch ticketed family shows not on organiser sites._
- **Uppsala kommun – Lekplatser** — kommun, gives places, family high, ~0 items  
  https://www.uppsala.se/kultur-idrott-fritid/plats/lekplatser/  
  e.g. Batteriparkens lekplats; Flogstaparkens lekplats; Vänge lekplats  
  _PLACES: 28 named stadsdels- and temalekplatser, with a map._
- **Uppsala kommun – Platser för aktiviteter** — kommun, gives places, family medium, ~0 items  
  https://www.uppsala.se/kultur-idrott-fritid/plats/  
  e.g. Uppsala simarena; allaktivitetshus; kulturhus Sävja/Gottsunda/Stenhagen  
  _PLACES: the kommun's directory of all leisure places (badhus/simhallar incl. the new Uppsala simarena, allaktivitetsplatser, kulturhus, museer, isbanor, lekplatser). Good seed for permanent places._
