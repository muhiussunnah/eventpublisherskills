# Duplicate Image Report — Live Events (ongoing + upcoming)
**Date:** 2026-08-30
**Scope:** All 1178 live events (status = ongoing 857 + upcoming 321). Method: perceptual hash
(16×16 grayscale average-hash) of each event's `images[0]`, fetched via wsrv.nl proxy (fammap S3
blocks CORS). Groups events whose image is visually identical, even when stored at different URLs.

## Headline numbers

| Metric | Value |
|---|---|
| Live events | **1178** |
| Images successfully hashed | 1160 |
| **Dead images (source 404 — broken everywhere)** | **18** |
| Unique images | 931 |
| **Duplicate image groups (same image on ≥2 events)** | **98** |
| **Live events sharing a duplicated image** | **327** |
| **Redundant events needing a fresh image** | **229** (= 327 − 98 keepers) |

Near-duplicate clustering (Hamming ≤ 6) barely widens this to 101 clusters / 342 events, so the
exact-hash groups below capture essentially all of it.

### Where the duplicates come from

| Image host | Dup groups | Events in them | Nature |
|---|---|---|---|
| images.unsplash.com | 59 | 229 | Generic stock photos reused across many unrelated events — worst offender, also violates image-rules (no stock) |
| fammap-storage S3 | 28 | 71 | Same venue/re-hosted image reused across sibling events |
| uploads.naturkartan-cdn.se | 11 | 27 | Same nature-site image across nearby nature events |

### Two kinds of duplicate

- **69 groups** reuse the *exact same URL* (literal copy-paste of one link).
- **29 groups** use the *same image at different URLs* (only caught by content-hashing, not URL match).

### The 18 dead images (separate problem — fix alongside)

17 × images.unsplash.com photo URLs return **404**, 1 × barnistan.se returns 404. These live events
show a blank/broken image in BOTH dashboard and app right now. (Listed at the end.)

---

## Duplicate groups (most-reused first)

Format: **G# — N× — [SAME-URL | same-img] — host** then the events sharing that one image.

**G1 — 7× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1511497584788-876760111969`
- Värmdö bibliotek i Gustavsbergs hamn med barnavdelning studio och scen för familj
- Bommersvik camping och ställplats för husvagn och husbil i Sörmland Nykvarn
- Furusund skärgårdsstigar vandring för familj i Norrtälje
- Naturum i Tyresta nationalpark guidade turer och utställningar för familj
- Lovö Prästgård ekologisk gårdsbutik med kor får och höns på Drottningholm
- Elfviks gård öppet med djur hästar får höns hela sommarlovet på Lidingö
- Sommarboken UNG läs tre böcker och få en bok i present 13-20 år

**G2 — 7× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1465146633011-14f8e0781093`
- Garns-Ekskogen naturmiljö i nordöstra Vallentuna med vandring sjöar och paddling
- Frösunda kyrka medeltidskyrka i norra Vallentuna med kulturhistorisk omgivning
- Nationalstadsparken med Haga Brunnsviken Ulriksdal och Bergshamra för familj
- Venngarns slott Bollhallen med gratis sommarfritidsgård för barn
- Bäverstigen ny aktivitetsstig för barn på Bommersvik i Nykvarn
- Åsavallen Edsbro hembygdsförening med fordonsutställning och kulturevenemang
- Adelsöleden 16 km vandringsled med Hovgården världsarv för familj

**G3 — 6× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1524429656589-6633a470097c`
- Sagolek Den lille prinsen musikalisk berättelse för 1-3 år på Konserthuset Stockholm
- Storstugan ungdomscentrum med kulturskolans dansaktiviteter för unga i Vaxholm
- Vandring runt Vallentunasjön 15 km led för familj och cyklist genom Täby och Vallentuna
- Funhouse lekland med lekställningar bollhav TV-spel och pysselhörna i Södertälje
- Botkyrka-Salem Hemslöjdsförening på Vällinge med hantverksförsäljning och kaffe
- Edsberg slott öppet med visning för barn och vuxna onsdagar och söndagar i Sollentuna

**G4 — 6× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1454372182658-c712e4c5a1db`
- Björklingebadet vid Långsjön i Björklinge norr om Uppsala med hopptorn
- Gustavs udde badplats i Vallentuna socken vid Vallentunasjön familjebad
- Långsjöns badplats i Össeby-Garns socken Vallentuna naturlig insjöbad
- Kalmarsand badplats vid Kungsängen Upplands-Bro med sandstrand brygga café och lekplats
- Landsort öns Kapell Pestkyrkogården och Strandlabyrinten för familj
- Håknäsbadet naturbad på Vätö med sandstrand och gräsmatta i Norrtälje

**G5 — 6× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1476231682828-37e571bc172f`
- Ostmakeriet Rindö mejerikafé med handgjord ost smörgås och kaffe i Vaxholm
- Naturskyddsföreningens familjevandring vid Hällkana friluftsgård i Upplands-Bro
- Kulturhuset Älta med program för familj och barn i Nacka
- Bo gård Lidingös äldsta gård från järnåldern besöksmål för familj
- Kulturstigar i Kallhäll-Stäket för familj historia genom 4 stigar
- Järfälla Musikkår blåsmusik konsert i Regementsparken sommar

**G6 — 6× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1439066615861-d1af74d74000`
- Rindöbadet Grönviken på södra Rindö med liten sandstrand grillplats och dock
- Myrholmsmaren badplats på Tynningö i Vaxholm med brygga toalett och simskola
- Lövnäsbadet vid södra Yngern sandstrand med brygga och lekplats
- Görvälns naturreservat med Görvälnsbadet och Kallhällsbadet för familj
- Södran badplats med sandstrand hopptorn och gungor för barn Ekerö
- Adelsö badplats sandstrand och brygga vid Hovgården världsarv

**G7 — 6× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1445264718234-a623be589d37`
- Svartsö skärgårdsö i mellanskärgården med jordbrukslandskap utan bilar för familj
- Rönninge by Skavlötens naturreservat med 3 enkla vandringsleder för familj
- Ljusterö opera festival sista helgen i augusti i Österåkers skärgård
- Nynäs Boat båthyra med Terhi 450c utan båtkörkort i Nynäshamn
- Vidbynäs naturreservat skogsområde med gamla träd för familjevandring
- Glamping på Birka Vikingastaden övernattning i tält juni-september

**G8 — 6× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1508739773434-c26b3d09e071`
- Skogsmulles spår om allemansrätten vid Björnö naturreservat med tio stationer för barn
- Orkesta hembygdsförening med farmstead och kulturhistoria i Vallentuna landsbygd
- Linkuddens naturreservat vandring på Blidö för familj i Norrtälje
- Stridsbåt till Siaröfortet med fika och guidning i bergrummen från andra världskriget
- Sommar på Birka Vikingastaden museum och restaurang öppna dagligen 23 juni-31 augusti
- Linnéträdgården sommarskattjakt med karta för yngre barn Uppsala juni-augusti

**G9 — 6× — same-img — images.unsplash.com**  
`images.unsplash.com/photo-1519681393784-d120267933ba`
- Möja naturstig 12 km tvärs över skärgårdsön i Värmdö med fina vyer
- Tyresö kyrka från 1641 med historisk byggnad och familjevisningar i Tyresö
- Notholmen vid Tyresö slottspark med bad fiske picknick och café över bron
- Tegelhagsskogen naturreservat vid Edsviken för familjevandring i Sollentuna
- Skogåshallen badfritids drop-in simning för barn 7-12 år sommar
- Germaniaviken sandbadplats med trampoliner för barn i Danderyd

**G10 — 6× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1500375592092-40eb2168fd21`
- Överbybadet på Resarö Vaxholm med sandstrand brygga lekplats och bytehytter
- Lillsjöbadet i Upplands-Bro med discgolf minigolf kanot och tillgänglighetsanpassad badramp
- Långholmens strandbad sandstrand och gräsytor för familj i Stockholm
- Edsviken Tegelhagen badplats med ramp för rullstol i Sollentuna
- Hökmossebadet barnvänlig sandstrand med lekutrustning och sommarkiosk
- Saltsjöbadens friluftsbad anrikt utomhusbad med hopptorn och kajakuthyrning Nacka

**G11 — 5× — same-img — fammap-storage.s3.eu-north-1.amazonaws.com**  
`fammap-storage.s3.eu-north-1.amazonaws.com/campaign/172600240698852664/57e63693-7b34-4383-a8a8-973961210013.webp`
- Eslövs Bowling
- Sim, Motion & Bowling Örkelljunga
- Big Bowl Malmö
- Lunds Bowlinghall
- O'Learys Järntorget

**G12 — 5× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1498050108023-c5249f4df085`
- Storvretabadet vid Fyrisån i Storvreta Uppsala med sandstrand och gräsytor
- Frölunda naturreservat med fin badplats fiske och bär- och svampplockning Upplands-Bro
- Tyresö Strand Strandbadet vid Erstaviken med 70-metersbryggor och lekplats
- Stora Vika badplats etablerad sjöbadplats i Nynäshamn
- Badudden i Skogås sandstrand vid Drevviken för familj

**G13 — 5× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1502209524164-acea936639a2`
- Skogsö badplats mellan Tynningö och Rindö i Vaxholm med barnvänlig sandstrand
- Badberget vid Landsnoravägen klippbad och liten sandstrand i Sollentuna
- Linanäs naturstig på Ljusterö med skog strand klippor och utsiktsplatser
- Bommersvik familjedestination med tennis boule pingis badstrand och naturstig
- Långsjöbadet familjebadplats med utmärkt vattenkvalitet i Huddinge

**G14 — 5× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1502082553048-f009c37129b9`
- Hjälmö Västergården visitor farm med guidade turer och djur i Värmdös skärgård
- Svindersviks brygghus sommarteater och evenemang för familj i Nacka
- Friluftsfrämjandet Lidingö Strövare barnverksamhet i naturen
- Norrbybadet i Jordbro mellanstort bad med bryggor och lekplats
- Familjelördag Vem räddar Alfons Åberg på Kulturcentrum Kvarnhjulet Tyresö

**G15 — 5× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1426604966848-d7adac402bff`
- Linnéstigarna åtta vandringsleder runt Uppsala i Carl von Linnés fotspår
- Gustavianum Uppsala universitetsmuseum med dagliga guidade visningar för barn
- Hörningsholm slott på norra Mörkö historisk slott vid Skanssundet
- Östanå slottspark öppet för besökare vid Furusundsleden i Österåker
- Trehörningen kulturmiljö med Oscarsbron från 1900 i Nynäshamn

**G16 — 5× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1513836279014-a89f7a76ae86`
- Nämdö skärgårdsö med vandring fiske och Sveriges första marina nationalpark intill
- Tivoliparken i Bergshamra Solna landtunga vid Brunnsviken för familj
- Skaparverkstan vid gamla ladan Edsvik kreativ workshop för barn
- Bolbynsslingan 1,7 km kort familjeled i Nykvarn
- Kaggeholm discgolf petanque och beachvolley för familj i Ekerö

**G17 — 5× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1518495973542-4542c06a5843`
- Markim medeltidskyrka i Vallentuna landsbygd med kulturhistoria och sommaröppet
- Ytterjärna kulturcentrum antroposofiska center vid Järnafjärden för familj
- Singö Runt Röd Led 26 km vandring och cykel genom skärgårdsbyar Norrtälje
- Artipelag konsthall promenad med upplevelser för familj i Nacka
- Stocksundsskogen utforska skog och natur för barn i Danderyd

**G18 — 5× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1505118380757-91f5f5632de0`
- Fysingenbadet naturlig badplats vid Löwenström sjukhus och sjön Fysingen
- Sättrabadet liten badplats vid Mälaren i västra Upplands Väsby för familj
- Norrviken Sollentunaholm sandstrand med stora gräsytor för familj
- Lundhagen badplats familjevänlig sandstrand i Ekerö Mälaren
- Nora strand strandpromenad och lekplats med dagvattendamm

**G19 — 5× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1416879595882-3373a0480b5b`
- Ingegerdsleden pilgrimsled i Upplands Väsby med familjevänlig kulturvandring
- Slottsrundan i Sigtuna upptäck flera slott på en utflykt för familj
- Kulturhuset Fisksätra mötesplats för alla med program för familj
- Lidingö museum permanent utställning om öns historia och guidade vandringar
- Ekebyhovsbacken vinterområde och sommarvandring för familj i Ekerö

**G20 — 5× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1443890484047-5eaa67d1d630`
- Runmarö skärgårdsö med vandring bad fiske och historiska byggnader i Värmdö
- Kungsängens IP med fem fotbollsplaner Drömparken och friidrottsbanor Upplands-Bro
- Nykvarns Folkets park med utegym minigolf och boule för familj
- Spontanidrott i Hallstaviks sporthall för barn och unga sommar Norrtälje
- Älmsta kanal promenadväg och Hallstavik parkourbana för familj Norrtälje

**G21 — 5× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1497436072909-60f360e1d4b1`
- Paradise Adventure Golf i Täby Centrum Sveriges största inomhus minigolf
- En dag på landet runt Sigtuna med picknick och djurupplevelser för familj
- Turingeleden 3,8 km vandringsled vid Lilla Turingen för familj i Nykvarn
- Gålö gård med djur ridning för barn café och bageri i Haninge
- Rönninge by hembygdsmuseum öppet hela sommaren med 4H-gård i Salem

**G22 — 5× — SAME-URL — uploads.naturkartan-cdn.se**  
`uploads.naturkartan-cdn.se/3b80a7cc7235e071ad0c2b377a8402dc.jpg`
- Sörmlandsleden etapp 3 från Alby friluftsgård till Tyresta by 13 km vandring
- Sörmlandsleden etapp 2 från Skogshyddan till Alby friluftsgård 6,5 km familjevandring
- Barnvagnsslingan i Tyresta nationalpark anpassad för småbarn och barnvagn
- Grodstigen och Fågelstig kort vandring i Tyresta nationalpark för småbarnsfamilj
- Alby friluftsgård vid Albysjön med bad lekplats grillplatser discgolf och café

**G23 — 5× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1473448912268-2022ce9509d8`
- Karby Gård Täby Kulturcentrum med konstutställningar pyssel och kafé för familj
- Kulturvaket 2026 festival på Stallbacken Kultur med barnkör symfoniorkester
- Odensala hembygdsförening vid Herresta farmstead för familj
- Bosön simbassäng öppen för allmänheten på Lidingö
- Årsta slott vandringsspår i Fredrika Bremers fotspår för familj i Haninge

**G24 — 5× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1509316785289-025f5b846b35`
- Östra Järvafältet naturreservat med vandringsstigar för familj i Sollentuna
- Rönninge gård och Uttringe gård historiska 1900-tals byggnader för familj
- Yxlö bilåtkomlig skärgårdsö för familj i Nynäshamn
- Kultur för barn och unga på Haninge kulturhus teater musik dans film
- Drottningholms slottspark vandring och picknick i Ekerö världsarv

**G25 — 5× — same-img — fammap-storage.s3.eu-north-1.amazonaws.com**  
`fammap-storage.s3.eu-north-1.amazonaws.com/event/172600240698852664/40639b47-1c71-432f-b4b7-e5f42079fe9a.webp`
- Elvis, Elvis, Elvis! på UKK
- Sven Ingvars – Igår. Idag. Imorgon. 70 år.
- Eva Dahlgren – Revalution Club Tour i Uppsala
- Hans Zimmers musik – Lords of the Sound
- Stad i ljus – Py Bäckman på Reginateatern

**G26 — 4× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1544551763-77ef2d0cfc6c`
- Wiks slott medeltidsslott vid Lårstaviken med slottsguidning kafé och badplats
- Åbynäsbadet havsbad vid Åby kvarn i Hölö med sandstrand och hopptorn
- Rådmansholmens badplats Blidö lugn långgrund med sandbotten för småbarn
- Mörbybadet familjebad i Danderyd med vattenrutschkana barnpool och bubbelpool

**G27 — 4× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1508923567004-3a6b8004f3d7`
- MINI När elefanten fick sin snabel musikkonsert för de yngsta Konserthuset Stockholm
- Stäketskogens naturreservat med vandring och historiska minnen i Upplands-Bro
- Kulturvandring Mölna till Gångsätra med Skärsätra gård och Wallenberg på Lidingö
- Cedergrenska tornet öppet torn historisk visning i Danderyd Stocksund

**G28 — 4× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1542273917363-3b1817f69a2d`
- Familjegudstjänst i Kungsängens kyrka söndagar med barn och familj Upplands-Bro
- Kulturåret 2026 i Södertälje med teater cirkus film och dining för familj
- Kulturvandring Torsvik till Mosstorp med Carl Milles och Hersby vattentorn
- Eldgarnsö naturreservat 6 km vandringsled runt ön för familj

**G29 — 4× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1470071459604-3b5ec3a7fe05`
- Broängarnas naturreservat Natura 2000 med fågelskådning vandring och kulturmiljöer
- Hammarbybacken sommaräventyr med höghöjdsbana zipline och rälsracer
- Hembygdsgården loppis lördagar sommar 11-14 i Norrtälje
- Höst på Birka Vikingastaden öppet på turbåtdagar 4 september till 25 oktober

**G30 — 4× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1441974231531-c6227db76b6e`
- Lejondals naturreservat vid Lejondalssjön Upplands-Bro med vandringsleder och bad
- Riksidrottsmuseet på Östermalm med interaktiv kroppslaboratorium för barn
- Ormteatern Haninge kulturskola barnteater och drama för unga
- Altorpsskogen i Djursholm motionsspår och stigsystem för familj

**G31 — 4× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1493246507139-91e8fad9978e`
- Gröna Udden badplats i Kungsängen med beachvolley utegym och grill
- Långholmens klippbad Stockholms mest kända stadsstrand med klipphällar
- Salems kyrka från 1100-talet vid Bornsjöns södra strand
- Edsviken strandpromenad vandring för barnfamilj i Danderyd

**G32 — 4× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1516627145497-ae6968895b74`
- Drömparken lekplats vid Kungsängens IP med tillgänglighetsanpassad gunga grillplats
- Sätunaparken Märsta lekplats med klätternätlabyrint karusell och björnar
- Blidö idrottsplats med fotboll padel minigolf utegym och lekplats
- Långsjöparken temalekpark om Huddinges historia för barn i Stuvsta

**G33 — 4× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1447752875215-b2761acb3c5d`
- Medeltidsmuseet under Strömparterren i Stockholm med medeltida stadsruiner
- Familjerummet ny mötesplats för barn 6-12 år och föräldrar i Tureberg
- Ekbacken kulturpark promenad längs Åkers kanal i Österåker
- Biografmysteriet LasseMajas Detektivbyrå familjeföreställning på Teater Bristol Sundbyberg

**G34 — 4× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1510784722466-f2aa9c52fff6`
- Österby Gård i Sigtuna besök djur picknick på landet för familj
- Salemsdagen 30 augusti vid Skönviksparken Rönninge familjefestival
- Öppen kulturskola i Huddinge gratis kreativa aktiviteter för barn
- Prova på spelskapande och ljuddesign för spel och film 10-15 år på Kulturcentrum

**G35 — 4× — same-img — fammap-storage.s3.eu-north-1.amazonaws.com**  
`fammap-storage.s3.eu-north-1.amazonaws.com/event/172600240698852664/ed76c238-657a-445f-bf4b-ab2b351dd564.webp`
- Robert Wells – 40 år vid flygeln
- Maksim – Segmenti World Tour i Uppsala
- Tomas Ledin – Symphonia Politropou
- Chopins pianokonsert – Uppsala Kammarorkester

**G36 — 3× — same-img — fammap-storage.s3.eu-north-1.amazonaws.com**  
`fammap-storage.s3.eu-north-1.amazonaws.com/campaign/172600240698852664/768ef2cd-852f-4cba-8428-24c01d0e9e15.webp`
- Österlenbadet
- Tolvåkerbadet
- Oxievångsbadet

**G37 — 3× — same-img — fammap-storage.s3.eu-north-1.amazonaws.com**  
`fammap-storage.s3.eu-north-1.amazonaws.com/campaign/172600240698852664/5fb4815e-9e74-428d-bd73-ba557e0f25c4.webp`
- 4H-Gården i Eslöv
- Kungshaga gård
- Rosengårdsbadet

**G38 — 3× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1490604001847-b712b0c2f967`
- Skokloster slott Sveriges största privata palats med barockmuseum norr om Uppsala
- Skavlöten vid Rönningesjön Löttinge med gräsytor för bollspel och picknick
- Åkers kanal promenad från 1820-talet med bäver och häger i Österåker

**G39 — 3× — SAME-URL — uploads.naturkartan-cdn.se**  
`uploads.naturkartan-cdn.se/d13fed0e0d48a815fdbe24fe71e21f22.jpg`
- Friluftsfrämjandet familjeäventyr vandringar Hågadalen och Sunnerstaåsen Uppsala
- Sunnerstaåsens friluftsområde vid Fyrisån med Sunnerstastugan kafé och MTB-banor
- Sunnerstabadet vid Mälaren Ekoln 9 km söder om Uppsala med långgrund sandstrand

**G40 — 3× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1490725263030-1f0521cec8ec`
- Fångarna på Kastellet familjeaktivitet på Vaxholms Kastell med utmaningar och tävling
- Norra båtlinjen dagsresa med m/s Rex från Norrtälje hamn till Lidö och Arholma
- Babblarna och Klonks Klapp-kalas på Nacka Aula 18 oktober

**G41 — 3× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1594736797933-d0501ba2fe65`
- Lekplats Lägret i Vaxholm renoverad belyst lekplats med klätterställningar karusell
- Edsbergsparken vid Edsviken med utegym lekplats och utsiktsplattform
- Drevviksparken upprustad modern lekpark i Länna Huddinge 2026

**G42 — 3× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1533587851505-d119e13fa0d7`
- Hemmesta motionsspår 2.5 km belyst vandringsled vid Värmdövallen
- Skepptuna hembygdsförening med farmstead för familj i Sigtuna kommun
- Spontanidrott basketplan vid Danderyds gymnasium öppen för alla

**G43 — 3× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1552083375-1447ce886485`
- Björkvik Havsbad i Värmdö med klippor sandstrand och fina solplatser
- Bollstanäsbadet vid Norrviken i Upplands Väsby med sandstrand för familj
- Upplandsleden längs Mälarens strand vid Sättra Gård med bad grillplats och bänkar

**G44 — 3× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1471922694854-ff1b63b20054`
- Bergsjöns badplats i Kårsta Vallentuna med insjöbad och fina sandstränder
- Underåsbadet vid Mälaren i Enhörna långgrunt perfekt för lek i vattnet
- Nickstabadet med vattenrutschkana hopptorn beachvolley minigolf och lekplats

**G45 — 3× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1477601263568-180e2c6d046e`
- Veckoaktiviteter på Sigma Centrum för barn med lekstunder filmvisning och pyssel
- Mörkö ö kulturhistoriskt landskap med jordbruk och skärgårdsmiljö för familj
- Söderby näridrottsplats med multisports arena fotboll basket lekutrustning utegym

**G46 — 3× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1523712999610-f77fbcfc3843`
- Birgittavandringen pilgrimsled genom Upplands Väsby för familjegrupp och pilgrimer
- Ruskpricken kreativ verkstad för barn på Sjöhistoriska museet i Stockholm
- Nynäshamns Hembygdsgård öppet friluftsmuseum söndagar sommar

**G47 — 3× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1560582861-45078880e48e`
- Fritidsbanken Värmdö gratis utlåning av sport och fritidsutrustning i 14 dagar
- Hallwylska palatset visning av storslaget privathem i Stockholm City
- Dalarö historisk skärgårdsidyll med marint kulturreservat i Haninge

**G48 — 3× — SAME-URL — uploads.naturkartan-cdn.se**  
`uploads.naturkartan-cdn.se/c9fc4ae3184c9055107ab72ef0e47495.jpg`
- Tyresta by lanthandel café och kulturmiljö vid Tyresta nationalpark
- Tyresta gård med småjordbruk lantraser och lammbete i Tyresta nationalpark
- Tjäderstigen äventyrsstig samla bokstäver och få diplom på Naturum Tyresta

**G49 — 3× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1596464716127-f2a82984de30`
- Rålambshovsparkens lekplats på Kungsholmen med pyssel skatepark och plaskdamm
- Skansholmen sommardestination med simning lekplats minigolf och fiske i Norrtälje
- Långängens lekplats stor familjepark med klätterställningar på Lidingö

**G50 — 3× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1587582423116-ec07293f0395`
- Vasaparkens parklek mitt i Stockholm med klättertorn cyklar och pyssel
- Sommargågatan på Centralvägen i Solna 30 maj-augusti med lekplats och uteservering
- Ålstaparken lekpark med flygledare-tema studsmattor och linbana i Järfälla

**G51 — 3× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1502691876148-a84978e59af8`
- Smedsuddsbadet vid Rålambshovsparken i Stockholm med vattenlek för barn
- Rosersbergsbadet liten badplats vid Mälaren nära Rosersberg slott
- Badet i Bergshamra Solna upprustat och nyrenoverat öppet sommaren 2026

**G52 — 3× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1560859251-d563a49c5e4a`
- Haga lekplats vid Koppartälten i Hagaparken Solna med vattenlek sommaren
- Krumelurparken stor lekplats i Malmparken för familj i Sollentuna
- Tuppen lekplats i Järnvägsparken centrala Åkersberga för familj

**G53 — 3× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1600880292203-757bb62b4baf`
- Bagarbyparken största lekplats i Tureberg för stora och små barn
- Lidö Värdshus gästhamn med grunt vatten lekplats och gräsytor för familj
- Skärsätra lekplats med klätterställningar och gungor för barn i Lidingö

**G54 — 3× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1500534623283-312aade485b7`
- Gålö gård med djur ridning för barn café och bageri
- Kultopia i parken på Sjödalsparken 13 september för hela familjen
- Kanalens dag i Åkersberga sista helgen i augusti familjeaktiviteter längs kanalen

**G55 — 3× — same-img — fammap-storage.s3.eu-north-1.amazonaws.com**  
`fammap-storage.s3.eu-north-1.amazonaws.com/campaign/172600240698852664/e55b5156-0463-4ed3-8232-19907b89dce4.webp`
- Point_197 onsdagar: Drop-in-sport
- Point_197 torsdagar: Skapande & Pyssel
- Point_197 måndagar: Fotboll för tjejer

**G56 — 3× — same-img — fammap-storage.s3.eu-north-1.amazonaws.com**  
`fammap-storage.s3.eu-north-1.amazonaws.com/event/172600240698852664/ec836af9-e3de-46f0-831a-f892483746b6.webp`
- Grymlings – Det bästa för dig
- Disco Inferno – Sveriges Största Discoshow
- Bo Kaspers Orkester – Il magnifico

**G57 — 3× — same-img — fammap-storage.s3.eu-north-1.amazonaws.com**  
`fammap-storage.s3.eu-north-1.amazonaws.com/event/172600240698852664/23bb96fa-e551-4d92-9bd2-46d12f539dec.webp`
- Ana Moura – Fado utan gränser
- Seinabo Sey i Uppsala
- Från Broadway till Duvemåla – 10-årsjubileum

**G58 — 3× — same-img — fammap-storage.s3.eu-north-1.amazonaws.com**  
`fammap-storage.s3.eu-north-1.amazonaws.com/event/172600240698852664/db1ca7d6-364a-4230-8807-449676fc34ff.webp`
- Niklas Strömstedt – Tyck OM mig
- Bruch och Brahms – Uppsala Kammarorkester
- Älskade stråkar – Uppsala Kammarorkester

**G59 — 3× — same-img — fammap-storage.s3.eu-north-1.amazonaws.com**  
`fammap-storage.s3.eu-north-1.amazonaws.com/event/172600240698852664/45b57842-d989-4700-9d05-2adaba2eb2b4.webp`
- Jävla karlar – Musikal på UKK
- Slutspelat – Ett komiskt sorgearbete på UKK
- Dick So So på Reginateatern

**G60 — 2× — same-img — fammap-storage.s3.eu-north-1.amazonaws.com**  
`fammap-storage.s3.eu-north-1.amazonaws.com/campaign/172600240698852664/3fbd8770-98f1-4440-a477-7fd2b2b57b47.webp`
- Christinehof slott
- Landskrona Citadellet

**G61 — 2× — same-img — fammap-storage.s3.eu-north-1.amazonaws.com**  
`fammap-storage.s3.eu-north-1.amazonaws.com/campaign/172600240698852664/7109d444-2129-4080-bae3-d352f0a5b3e9.webp`
- Äventyrscampen i Sövde
- First Camp Röstånga – Söderåsen

**G62 — 2× — same-img — fammap-storage.s3.eu-north-1.amazonaws.com**  
`fammap-storage.s3.eu-north-1.amazonaws.com/campaign/172600240698852664/b7538854-717f-4678-904a-368062e81121.webp`
- MultiLevel Ziplines & Klätterpark
- Klättercentret Malmö

**G63 — 2× — same-img — fammap-storage.s3.eu-north-1.amazonaws.com**  
`fammap-storage.s3.eu-north-1.amazonaws.com/campaign/172600240698852664/7fececa2-a913-4eb9-bdfc-9e1762ce883a.webp`
- Klippans Gokart
- GoKartCity Malmö

**G64 — 2× — same-img — fammap-storage.s3.eu-north-1.amazonaws.com**  
`fammap-storage.s3.eu-north-1.amazonaws.com/campaign/172600240698852664/98e87590-deeb-4ff6-a98a-023a6a795a1d.webp`
- Funplays Hyllinge
- Funplays Malmö

**G65 — 2× — same-img — fammap-storage.s3.eu-north-1.amazonaws.com**  
`fammap-storage.s3.eu-north-1.amazonaws.com/campaign/172600240698852664/ffd20a0d-7e02-4086-8bbf-8ac1a9202cd1.webp`
- Laserdome & Prison Island Helsingborg
- Laserdome Malmö

**G66 — 2× — same-img — fammap-storage.s3.eu-north-1.amazonaws.com**  
`fammap-storage.s3.eu-north-1.amazonaws.com/campaign/172600240698852664/5c22df77-47d4-4da4-8a32-c2361b9c74d9.webp`
- Escape House Lund
- Gothenburg Escape Game

**G67 — 2× — same-img — fammap-storage.s3.eu-north-1.amazonaws.com**  
`fammap-storage.s3.eu-north-1.amazonaws.com/event/172600240698852664/bd9cae39-bcfb-4fc0-aa97-a15b84d65386.webp`
- Klättercentret Telefonplan
- Klättercentret Solna

**G68 — 2× — same-img — fammap-storage.s3.eu-north-1.amazonaws.com**  
`fammap-storage.s3.eu-north-1.amazonaws.com/event/172600240698852664/a8b05bbb-4457-4e8b-abaa-9893fa343556.webp`
- Kallhälls 4H-gård
- Järfällabadet

**G69 — 2× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1519315901367-f34ff9154487`
- Actic Mörbybadet
- Huddingehallen simhall med Jungle barnbassäng och vattenrutschkana

**G70 — 2× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1518998053901-5348d3961a04`
- Uppsala Slottshistoriska nytt museum med Slottsliv utställning och gratis entré
- Hilma af Klint utställning på Adelsö gamla prästgård sommaren

**G71 — 2× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1580757468214-c73f7062a5cb`
- Bror Hjorths Hus ateljémuseum i Uppsala med familjevisningar och kreativa workshops
- Tolvmansgården Rimbo hembygdsgård med vykortsutställning och textilhantverk

**G72 — 2× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1472214103451-9374bd1c798e`
- Gratis bilfärja från Vaxholm till Rindö med kort överfart för utflykt i skärgården
- Ubbysjön fågelrik sjö mellan Ormsta och Lindholmen i Vallentuna med fågeltorn

**G73 — 2× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1554907984-15263bfd63bd`
- Jarlabankes bro infocentral Runriket med utomhusutställning och rundrake i Täby Vallentuna
- Battery Landsort underjordisk kalla kriget bunker museum med guidade turer

**G74 — 2× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1519331379826-f10be5486c6f`
- Stora Wäsby slott med barockpark från 1750-talet i Upplands Väsby
- Djursholms slottspark engelsk landskapspark med lekplats och picknick

**G75 — 2× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1501339847302-ac426a4a7cbb`
- Härnevi kyrka med sommarcafé i idyllisk by miljö Upplands-Bro
- Ekebyhovs slott guidad visning historisk miljö och fika i Ekerö

**G76 — 2× — SAME-URL — uploads.naturkartan-cdn.se**  
`uploads.naturkartan-cdn.se/b2a49e59aaf6516f2650eebe29fb34af.jpg`
- Värtans strandpromenad 7 km cykel och vandring förbi Hägernäs i Täby
- Hägernäsbadet vid Värtan i Täby med grill lekplats och beachvolleybollplan

**G77 — 2× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1503919545889-aef636e10ad4`
- Tantolundens lekplats vid Årstaviken med zipline klätterväggar och balansgång
- Lekplatser i Danderyd över 30 platser för stora och små äventyr

**G78 — 2× — SAME-URL — uploads.naturkartan-cdn.se**  
`uploads.naturkartan-cdn.se/e88a4cb03c5c46aa628653a618800963.jpg`
- Enstaleken tillgänglighetsanpassad lekplats vid Stolpaskogen Täby med utegym
- Ensta krog friluftsgård vid Stolpaskogen Täby med eldstäder och utegym

**G79 — 2× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1468413253725-0d5181091126`
- Eriksdalsbadet Sveriges nationella simarena på Södermalm med vattenrutschbanor
- Kvarnparksbadet utomhusbad i Danderyd öppet mitten av maj till slutet av augusti

**G80 — 2× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1471286174890-9c112ffca5b4`
- Liljevalchs barn och ungdomsprogram konstworkshops på Djurgården Stockholm
- Nåttarö dagsutflykt skärgård med sandstränder båttur från Nynäshamn

**G81 — 2× — SAME-URL — uploads.naturkartan-cdn.se**  
`uploads.naturkartan-cdn.se/6259d4e5549faa1f50c0e6c7b6660012.jpg`
- Stolpaleden 3 km vandringsled genom Stolpaskogen med Jättegranen i Täby
- Stolpaskogens naturreservat i Täby med 84 hektar skog och vandringsleder

**G82 — 2× — SAME-URL — uploads.naturkartan-cdn.se**  
`uploads.naturkartan-cdn.se/a1b8418559baec8a7975d140ef508212.jpg`
- Sturehovs herrgård vid Bornsjön med slottspark och café för familj
- Bornsjön naturreservat Stockholms läns största med 11 km naturstig och Sturehovs herrgård

**G83 — 2× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1478131143081-80f7f84ca84d`
- Ingmarsö skärgårdsby med 1800-tals bebyggelse promenad och cykel
- Grundprogram i kreativt skapande (5–9 år)

**G84 — 2× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1507525428034-b723cf961d3e`
- Brännholmen badplats i östra naturreservatet på Ljusterö Österåker
- Taxingebadet vid Taxinge Slott barnvänlig sandstrand med lekplats

**G85 — 2× — SAME-URL — images.unsplash.com**  
`images.unsplash.com/photo-1418065460487-3e41a6c84dc5`
- Sjön Muskan i Ösmo med Sörmlandsleden 4 km vandring för familj
- Familjelördag Stockholm Jazz Festival familjekonsert i Tyresö 17 oktober

**G86 — 2× — SAME-URL — uploads.naturkartan-cdn.se**  
`uploads.naturkartan-cdn.se/00315d1842f0b3c952748cf7cdb0827f.jpg`
- Långängens gård café i 1700-tals byggnad med naturreservat omkring
- Långängen-Elfviks naturreservat med bad grillplatser och stigar för familj

**G87 — 2× — SAME-URL — uploads.naturkartan-cdn.se**  
`uploads.naturkartan-cdn.se/8b307506b043255ba33a8065d2097ad7.jpg`
- Tjäderstigen äventyrsstig med hemligt lösenord i Tyresta nationalpark
- Tyresta nationalpark – familjeaktiviteter och äventyrsstigar

**G88 — 2× — SAME-URL — uploads.naturkartan-cdn.se**  
`uploads.naturkartan-cdn.se/f10248dfd911a866c7a97eef440c55c6.jpg`
- Vandringens dag barn och familjevandring på Rudan 13 september
- Rudans friluftsområde naturreservat med bad mtb och vandring i Haninge

**G89 — 2× — SAME-URL — uploads.naturkartan-cdn.se**  
`uploads.naturkartan-cdn.se/48eb6b0ea311788e968ce7fb5fefed7b.jpg`
- Häringe-Hammersta naturreservat med vandringsstigar för familj
- Häringe-Hammersta naturreservat med vandringsstigar för familj

**G90 — 2× — same-img — fammap-storage.s3.eu-north-1.amazonaws.com**  
`fammap-storage.s3.eu-north-1.amazonaws.com/campaign/172600240698852664/ecb9631b-68a3-41f8-bdaa-2d8194c84561.webp`
- Fritidsgården Huset i Salem – ungdomsverksamhet
- Biograf Gröna Ladan – 100-åriga biografen i Sigtuna stad

**G91 — 2× — same-img — fammap-storage.s3.eu-north-1.amazonaws.com**  
`fammap-storage.s3.eu-north-1.amazonaws.com/event/172600240698852664/edbd7485-acf3-456b-b2f5-0c0dc4fba3f6.webp`
- IT-hjälp i Sigma Centrum
- IT-hjälp i Sigma Centrum

**G92 — 2× — same-img — fammap-storage.s3.eu-north-1.amazonaws.com**  
`fammap-storage.s3.eu-north-1.amazonaws.com/event/172600240698852664/33ce86cf-0fc8-4b41-b9ba-5021b8e5742d.webp`
- Kulturnatt i oktober på Vaxholms Fästnings Museum
- Tommy Körberg – Unplugged i Uppsala

**G93 — 2× — same-img — fammap-storage.s3.eu-north-1.amazonaws.com**  
`fammap-storage.s3.eu-north-1.amazonaws.com/event/172600240698852664/81b6e59f-138e-4091-9fca-c3cdc7f626c1.webp`
- Militärhistorisk vandring på Fredriksborgs fästning
- Arkeologidagen 2026 på Gamla Uppsala museum

**G94 — 2× — same-img — fammap-storage.s3.eu-north-1.amazonaws.com**  
`fammap-storage.s3.eu-north-1.amazonaws.com/event/172600240698852664/d373dbd2-cb16-4959-bf4a-42f6ab385338.webp`
- Viktor Norén & Linus Wahlgren – Våra liv, våra musikaler
- Doktor Glas på Reginateatern

**G95 — 2× — same-img — fammap-storage.s3.eu-north-1.amazonaws.com**  
`fammap-storage.s3.eu-north-1.amazonaws.com/event/172600240698852664/3b5aee9d-1d32-48c3-b3b5-4d8fb039bfdc.webp`
- The Simon & Garfunkel Story på UKK
- A Tribute to Dire Straits på UKK

**G96 — 2× — same-img — fammap-storage.s3.eu-north-1.amazonaws.com**  
`fammap-storage.s3.eu-north-1.amazonaws.com/event/172600240698852664/5a78ed52-046c-4373-9348-642d9dbd9935.webp`
- Louisa Lyne & di Yiddishe Kapelye – Cohen in Yiddish
- Sawdust Symphony på Reginateatern

**G97 — 2× — same-img — fammap-storage.s3.eu-north-1.amazonaws.com**  
`fammap-storage.s3.eu-north-1.amazonaws.com/event/172600240698852664/b59bd545-62f3-4a9d-bc7f-076943cf0e88.webp`
- Lördagar i Hammarskog – Naturskolan Uppsala
- Lekutställningen Lill-Disa på Disagården

**G98 — 2× — same-img — fammap-storage.s3.eu-north-1.amazonaws.com**  
`fammap-storage.s3.eu-north-1.amazonaws.com/event/172600240698852664/787f50b9-4f23-481e-8ee5-913d226c5bd3.webp`
- Sista chansen: Glaskalas
- Vernissage: Glaskalas

---

## The 18 dead images (source 404 — broken in dashboard AND app)

1. Familjekonsert LasseMaja och Konsertmysteriet på Konserthuset Stockholm 2027  _(images.unsplash.com)_
2. Djungelboken The Musical familjeföreställning på Göta Lejon Stockholm hela hösten  _(images.unsplash.com)_
3. Aktivitetscenter Täby med laserdome bowling arkad och darklight minigolf  _(images.unsplash.com)_
4. Täby stories digital utställning bland hästar och hus på Stockholms läns museum  _(images.unsplash.com)_
5. Farsta simhall äventyrsbad för småbarn med rutschkana i södra Stockholm  _(images.unsplash.com)_
6. Lill-Skansen barnens del av Skansen med smådjur höns och kaninhopp  _(images.unsplash.com)_
7. Evert Lundquists Ateljémuseum besök i Drottningholm Ekerö  _(images.unsplash.com)_
8. Pythagoras Industrimuseum Barnens Pythagoras 500 kvadratmeter med teknik och uppfinningar  _(images.unsplash.com)_
9. Fjärilshuset Haga Ocean i Hagaparken 400 fjärilar i tropisk regnskog och 30m långt akvarium  _(images.unsplash.com)_
10. Hagabergs sommarcafé familjevänligt med luncher och fika i Södertälje  _(images.unsplash.com)_
11. Jungfrusund hamn med O Learys bowling och shuffleboard för familj  _(images.unsplash.com)_
12. Drottningholms slottspark guidad visning sommaren 2026 för familjer  _(images.unsplash.com)_
13. Millesgården barnspår upptäck skulpturer djur och antikens gudar i sommar 2026  _(images.unsplash.com)_
14. Såpbubbleworkshop och prova-på-cirkus med Cirkus Cirkör i Åkerbyparken Täby 30 augusti  _(images.unsplash.com)_
15. Kalle Kanonkula äventyr på Vaxholms Fästnings Museum sommar 25 maj till 1 september  _(www.barnistan.se)_
16. Arkeologidagen på Gunnes gård – gratis visning  _(wsrv.nl)_
17. Arkeologi, demokrati och vikingatid  _(wsrv.nl)_
18. Tema Lera  _(wsrv.nl)_

