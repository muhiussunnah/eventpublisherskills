# Permanent places — corrections applied (2026-11-05)

Follow-up to `PERMANENT-PLACES-ACCURACY-AUDIT-2026-11-05.md`. The user approved all fixes. Every change is reversible; nothing was deleted.

| | Count |
|---|---|
| Events hidden (closed, booking/ticket-only, unverifiable, duplicates) | 273 |
| — first pass (audit verdicts + duplicate copies) | 174 |
| — second pass (no regular drop-in hours or no published season, found while fixing) | 99 |
| Events corrected | 638 |
| — recurrence (days, hours, season dates) | 601 |
| — isFree | 174 |
| — description rewritten from the official source | 121 |
| — title | 12 |
| — ctaLink (dead, casino spam or missing) | 57 |
| Events moved to their own correct venue | 6 |
| Venue addresses / map pins / kommun corrected | 13 |
| Published live events after the fixes | 1212 (was 1484) |

Every corrected event also got `parentMaxAge: 100` where it had 18 or 99.

## How hiding works (reversible)
- Venue had no other events → venue `isPublished:false` (`PATCH /admin/places/{id}`). Re-publish: PATCH `isPublished:true`.
- Venue shared with other events, or a general venue with past events → the event was moved to an unpublished holding venue `[Dold] <venue> – ej aktuell`. Re-publish: PATCH the event `placeId` back to the original venue.

## Holding venues
| Original venue | Holding venue |
|---|---|
| 178316519871120801 | 487837411036923252 |
| 185717206598846112 | 487837593019385205 |
| 187991706086442842 | 487837625768510838 |
| 248678996634535313 | 487837658643465591 |
| 427718020366894381 | 487837745398449528 |
| 377312454805325496 | 487837787492484473 |
| 377371173417158342 | 487837829443913082 |
| 429867006406198753 | 487837871420507515 |
| 429887652028777506 | 487837904035415420 |
| 186703520404113140 | 475592282393838746 |
| 253228975550137400 | 487837957194024317 |
| 259199720268793095 | 487837990085756286 |
| 253319603671827571 | 487838077453108607 |
| 184929995582375506 | 487838110328063360 |

## Hidden events
| Event ID | Place | Kommun | Original venue | Method | Reason |
|---|---|---|---|---|---|
| 442327199563941362 | Askersunds skärgårdstrafik (Trulsan & Pricken) | Askersund | 442327190638462449 | venue unpublished | audit: UNCLEAR — No mention of Trulsan, Pricken, båttur or skärgårdstrafik anywhere on visitaskersund.se (göra, aktiv |
| 442245014785918229 | Kompislandet | Avesta | 442244999174718740 | venue unpublished | audit: UNCLEAR — No 'Kompislandet' or 'lekland' on avesta.se or visitdalarna.se/sv/avesta; domains kompislandet.se/.n |
| 442234806613345398 | I.C.E. Äventyrsarena & lekland | Borlänge | 442234789903238261 | venue unpublished | audit: NOT_A_VISITOR_PLACE — Tre verksamheter under samma namn – alltjänst och åkeri, event och aktiviteter samt frisörsalong. Ev |
| 442234752120947821 | O'Learys Event Center Borlänge | Borlänge | 442234736786572396 | venue unpublished | audit: UNCLEAR — HTTP 429 Too Many Requests (olearys.se och olearys.com, 5 försök); kupolen.se ECONNREFUSED; visitdal |
| 435880129818822558 | Borås Escape Game | Borås | 435878294634661789 | venue unpublished | audit: NOT_A_VISITOR_PLACE — Borås Escape Game - Escape Rooms in Central Borås (time-slot booked escape rooms, 3 games) |
| 429259544997168761 | Cirkus Cirkör | Botkyrka | 186703520404113140 | moved to holding 475592282393838746 | audit: NOT_A_VISITOR_PLACE — Chilla med Cirkör: träningshallen öppnar tre söndagar per termin. Drop-in träning 100 SEK/pass (60 S |
| 442346303947573101 | S/S Boxholm II | Boxholm | 442346294820767596 | venue unpublished | audit: UNCLEAR — Not mentioned on boxholm.se 'Besök Boxholm', 'Aktiviteter' or 'Sommen 365' pages; www.boxholm2.se /  |
| 436014880005326040 | Kronetorps mölla | Burlöv | 436014876515665111 | venue unpublished | audit: SEASON_ONLY — Mölleföreningen guidar följande dagar: 7 juni 12–16 Öppet hus, 5 juli 11–16 Mölledagen, 2 augusti 12 |
| 442327534923712011 | Stora Valla (Degerfors IF) | Degerfors | 442327522726675978 | venue unpublished | audit: NOT_A_VISITOR_PLACE — Stora Valla är en fotbollsanläggning i Degerfors, där Degerfors IF spelar sina hemmamatcher. Publikr |
| 442313073726883530 | Enköpings Bangolf | Enköping | 442313065178891977 | venue unpublished | audit: UNCLEAR — Kommunens Upplev Enköping-sidor nämner varken bangolf eller minigolf. Inga domäner funna: enkopingsb |
| 436015867982022084 | 4H-Gården i Eslöv | Eslöv | 436015862722364867 | venue unpublished | audit: UNCLEAR — (no official source retrievable) noje.se listing returned HTTP 403; 4h.se farm list is a JS map; esl |
| 436015879575078344 | Medborgarhuset Eslöv | Eslöv | 436015876018308551 | venue unpublished | audit: NOT_A_VISITOR_PLACE — Listed under 'de hus och lokaler som går att hyra' ... 'Medborgarhuset som fungerar för allt från te |
| 442234593895023702 | Falun Bowling & Krog | Falun | 442234578543871061 | venue unpublished | audit: CLOSED_PERMANENT — Tack för allt, vi kommer sakna er! Den 24 juni 2025 lämnade Heymakers (inkl. Coppergrill) in en ansö |
| 435950343432472427 | Backa Teater | Göteborg | 435950339892479850 | venue unpublished | audit: NOT_A_VISITOR_PLACE — Cross 5 nov 19:00 / 6 nov 13:00 (slutsålt) / 7 nov 18:00; Mira går genom rummen 5–7 nov; Dr Rönnerst |
| 435951350753298381 | Gothenburg Escape Game | Göteborg | 435951347003590604 | venue unpublished | audit: NOT_A_VISITOR_PLACE — Intense teambuilding in central Gothenburg (startsidan; escape rooms spelas i bokade tidsluckor) |
| 435950323400476513 | GöteborgsOperan | Göteborg | 435950319843706720 | venue unpublished | audit: NOT_A_VISITOR_PLACE — Familjedans, Dansa med bebis, Häxan Hillary går på Operan, Guld! (06 feb – 17 apr 2027, Lilla scenen |
| 435951451475314677 | Göteborgsutkiken (Läppstiftet) | Göteborg | 435951447725606900 | venue unpublished | audit: UNCLEAR — Fastighetsägarens sida nämner ingen utsiktsplattform/utkik: endast 'Med utsikt över staden, älven oc |
| 435951323901364163 | VR World Gothenburg | Göteborg | 435951318415214530 | venue unpublished | audit: NOT_A_VISITOR_PLACE — Vi har slutat med fasta drop-in tider. (Telefontider måndag–fredag 9–12; aktiviteter arrangeras med  |
| 442382435905210257 | Brandbergen Bowlingcenter | Haninge | 442382426795181968 | venue unpublished | audit: UNCLEAR — Sökning 'bowling haninge' gav 1 sökträff: Ballbreaker Kungsholmen, Lindhagensgatan 114, Stockholm –  |
| 429382584133257096 | Prison Island | Huddinge | 429381580578916231 | venue unpublished | audit: MOVED — Stockholm-anläggningen anges med adress 'Saltmätaregatan 19A, 113 59 Stockholm'. Kungens Kurva-sidan |
| 442158046353852373 | Virserums Konsthall | Hultsfred | 442158029887014868 | venue unpublished | audit: CLOSED_RENOVATION — 'Vi har tillfälligt stängt!' 'Konsthallen har tillfälligt stängt pga. omfattande renovering men verk |
| 442157988120135633 | Hanåsa Padel | Högsby | 442157973054195664 | venue unpublished | audit: NOT_A_VISITOR_PLACE — 'Den 30 april 2021 invigdes Högsbys nya padelbana, som drivs av Hanåsa Aktivitetsförening.' 'Padelba |
| 445128123051181160 | Stäketfläcken | Järfälla | 445128110308885607 | venue unpublished | audit: UNCLEAR — Järfälla kommun badplatser: Bonäsbadet, Brukets friluftsbad, Görvälnbadet, Kallhällsbadet, Ängsjö fr |
| 442144381261088540 | Byteatern Kalmar Länsteater | Kalmar | 442144364207048475 | venue unpublished | audit: NOT_A_VISITOR_PLACE — Barlastgatan 8, 39231 Kalmar ... BILJETTER (nortic.se) ... växel [tel] (kontorstid) ... AKTU |
| 461272953426838567 | Kungsörs badhus | Kungsör | 461272944182592550 | venue unpublished | audit: CLOSED_RENOVATION — Badhuset är stängt tills vidare på grund av fel i maskinrummet. (sidan uppdaterad 2 november 2026) |
| 436014765366609100 | Tolvåkerbadet | Kävlinge | 436014761851782347 | venue already unpublished 2026-10-19 | audit: CLOSED_PERMANENT — Badhus: Harjagersbadet (enda badhuset som listas; Medley sköter driften). Tolvåker listas endast som |
| 442382501856445568 | Gångsätrahallen | Lidingö | 442382492536702079 | venue unpublished | audit: CLOSED_PERMANENT — "Simhallen och gymmet i Gångsätrahallen stängde den 19 juni 2025."; "En utredning pågår om hur simha |
| 442337667850471095 | Linköping Konsert & Kongress | Linköping | 442337657641535158 | venue unpublished | audit: NOT_A_VISITOR_PLACE — Biljettkassan: Onsdagar kl. 10:00–13:00 (biljettfrågor & köp av vissa biljetter). Telefontider gälla |
| 471560126763927390 | Världsarvsgården Bommars | Ljusdal | 471560110632634205 | venue unpublished | audit: NOT_A_VISITOR_PLACE — SOMMARTID ÖPPET FÖR GUIDNING. ALLA BESÖK BEHÖVER FÖRBOKAS. Pris 300 kr/pers, kaffe ingår. Gratis för |
| 442331422372431420 | Kaveltorps gruvmuseum | Ljusnarsberg | 442331397500208699 | venue unpublished | audit: NOT_A_VISITOR_PLACE — För att besöka museet krävs förbokning via SMS till [tel]. (Gruvstugutorget, 714 31 Kopparbe |
| 442246661385782575 | Cassels konsert- & kulturhus | Ludvika | 442246648811259182 | venue unpublished | audit: NOT_A_VISITOR_PLACE — Sajten listar endast evenemang (21 nov Anders Ekborg, 3 dec 'I ett vinterland', 6 dec Loa Falkman &  |
| 434579404157388518 | Sea4fun | Lysekil | 434577539302721251 | venue unpublished | audit: NOT_A_VISITOR_PLACE — Vi kör turer så länge vädret tillåter. Turen tar ca 2 tim. För bokning av sälsafari ring [namn]. Pr |
| 442365551935784674 | Sea4fun Sälsafari | Lysekil | 442365542574098145 | venue unpublished | audit: NOT_A_VISITOR_PLACE — Vi kör turer så länge vädret tillåter. För bokning av sälsafari ring [namn]. Pris för sälsafari: vu |
| 436014418774492276 | Malmö Live Konserthus | Malmö | 436014415276442739 | venue unpublished | audit: NOT_A_VISITOR_PLACE — Biljettcenter: torsdag 16.00 – 18.00 (över disk); tisdag–torsdag 12.00–14.00 per telefon; öppet 2 ti |
| 436014407433094256 | Malmö Opera | Malmö | 436014402299266159 | venue unpublished | audit: NOT_A_VISITOR_PLACE — Tors: kl 15.00–18.00 (biljettkassa i foajén); tis–fre 12.00–13.00 per telefon. Foajén öppnar två tim |
| 445125218436940991 | Leksaksmuseet | Nacka | 445125204193084606 | venue unpublished | audit: CLOSED_PERMANENT — Enligt ett officiellt inlägg på museets Facebook sida, så är museet permanent stängt sedan 13 septem |
| 471549145656624651 | Halls gård | Nordanstig | 471549134273283594 | venue unpublished | audit: NOT_A_VISITOR_PLACE — 'Bokning av tur sker i första hand via knappen "BOKA TURRIDNING"'; 'Hallsturen … Bokningsbar 1 oktob |
| 442340203911218930 | Escape House Norrköping | Norrköping | 442340195078014705 | venue unpublished | audit: NOT_A_VISITOR_PLACE — 'Adress: Prästgatan 14, 602 32 Norrköping.' 'Personalen är på plats när det finns bokningar, så boka |
| 442340238472283897 | Klätterhallen Norrköping | Norrköping | 442340226518517496 | venue unpublished | audit: UNCLEAR — No website in app; WebSearch 'Klätterhallen Norrköping klättring öppettider' returned no climbing gy |
| 442340111141603038 | Laserdome Norrköping | Norrköping | 442340098969732829 | venue unpublished | audit: CLOSED_PERMANENT — Laserdome's city selector lists only Stockholm, Göteborg, Malmö, Linköping, Helsingborg, Halmstad, U |
| 441812572925101555 | Leos Lekland Norrköping | Norrköping | 441812559075509746 | venue unpublished | audit: CLOSED_PERMANENT — Official list 'Alla lekland' has 27 locations and Norrköping is not among them (nearest: Linköping,  |
| 442340075129308887 | Louis De Geer konsert & kongress | Norrköping | 442340066489042646 | venue unpublished | audit: NOT_A_VISITOR_PLACE — 'Torsdagar biljettkassa kl. 15-18'; 'Röda helgdagar och klämdagar stängt'; 'Vi öppnar ytterdörrarna  |
| 442384499913819141 | Lekrymden | Norrtälje | 442384490485023748 | venue unpublished | audit: UNCLEAR — Busplejset i Norrtälje AB, Baldersgatan 25, 761 50 Norrtälje – Ej verifierat företag; enda omdöme 20 |
| 429458955983423049 | Roslagen Escape | Norrtälje | 429458162899256904 | venue unpublished | audit: NOT_A_VISITOR_PLACE — Från 300 kr/person. Boka via bokningskalendern ... 2–6 spelare, 60 minuters spel. |
| 442255160664688049 | Nässjö Järnvägsmuseum | Nässjö | 442255141261837744 | venue unpublished | audit: NOT_A_VISITOR_PLACE — Vi har inte några fasta öppettider i dagsläget, endast förbokning gäller. Juni–augusti: Efter överen |
| 433849948254013023 | Kamelridning | Orust | 433848870452102750 | venue unpublished | audit: NOT_A_VISITOR_PLACE — Alla gårdsbesök och aktiviteter hos oss måste förbokas. ... Gårdsbesök & kamelridning 150:- per pers |
| 442154420042500021 | Biologiska museet i Oskarshamn | Oskarshamn | 442154404582295476 | venue unpublished | audit: NOT_A_VISITOR_PLACE — Museet drivs av ideella krafter och har därför inga fasta öppettider. Kontakta [namn] för att boka i |
| 442380087346628170 | Villa Skönvik (Salems Hembygdsförening) | Salem | 442380074704995913 | venue unpublished | audit: UNCLEAR — Kommun page only mentions the association's Lundby Parstuga, 'öppen under sommarhalvåret av värdar f |
| 445123151341323951 | Lilla Steninge | Sigtuna | 445123139186230958 | venue unpublished | audit: UNCLEAR — Stenladan (butiker och restaurang): Måndag–fredag 11:00–18:00, Lördag–söndag 10:00–17:00 ... Slottsp |
| 436016019060852204 | Skillinge Teater | Simrishamn | 436016013952189931 | venue unpublished | audit: NOT_A_VISITOR_PLACE — Under sommaren har vi öppet tisdagar till söndagar i vår matsal. Under vintern håller vi ofta öppet  |
| 436015839980848572 | Äventyrscampen i Sövde | Sjöbo | 436015836449244603 | venue unpublished | audit: UNCLEAR — Website unreachable 2026-11-05 (connect ECONNREFUSED for aventyrscampen.se and www.aventyrscampen.se |
| 442355514018399647 | Laserdome Skövde | Skövde | 442355502014301598 | venue unpublished | audit: UNCLEAR — Laserdome.se lists arenas in Stockholm, Göteborg, Malmö, Linköping, Helsingborg, Halmstad, Umeå, Kri |
| 445128172510414792 | Ålstaparken | Sollentuna | 445128159885559751 | venue unpublished | audit: UNCLEAR — Sollentuna kommun search 'Ålstaparken': 'Visar 0 av 0 träffar'. Kommun page 'Lekplatser i Rotebro oc |
| 445128704851477680 | Vasalundshallen | Solna | 445128692151125167 | venue already unpublished 2026-10-19 | audit: NOT_A_VISITOR_PLACE — Sporthall med fyra hallar (A–D) för basket, volleyboll, bordtennis. 'Boka tid i Vasalundshallen'. A- |
| 442373251948119957 | Bouldering Sthlm | Stockholm | 442373243148470164 | venue unpublished | audit: OPEN — Mån — tis 10:00–22:00, Ons — fre 12:00–22:00, Lör — sön 10:00–20:00. Bouldering Sthlm AB, Slakthusga |
| 430215746082080383 | Cirkus Arena & Restaurang | Stockholm | 185717206598846112 | moved to holding 487837593019385205 | audit: NOT_A_VISITOR_PLACE — Built in 1892 as a permanent venue for travelling circus troupes … now a beloved arena for concerts, |
| 445106618602915218 | Creativity House - Fridhemsplan | Stockholm | 445106605592184209 | venue unpublished | audit: NOT_A_VISITOR_PLACE — Bokningsbara tider (inte detsamma som fasta öppettider): Fridhemsplan Drottningholmsvägen 31 – månda |
| 445112513747519247 | Creativity House - Karlaplan | Stockholm | 445112504830428942 | venue unpublished | audit: NOT_A_VISITOR_PLACE — Bokningsbara tider (inte detsamma som fasta öppettider): Karlaplan Karlavägen 70 – måndag stängt, ti |
| 445323292690122703 | Dockteatern Tittut | Stockholm | 445323280274982862 | venue unpublished | audit: NOT_A_VISITOR_PLACE — Scenkonst av hög kvalitet för de allra yngsta, sedan 1977. Hemmascen: Lundagatan 33, Södermalm. Bilj |
| 430230014550640617 | Dramaten | Stockholm | 430228075146414056 | venue unpublished | audit: NOT_A_VISITOR_PLACE — Vardagar öppnar biljettkassan två timmar innan föreställning när vi spelar på Stora eller Lilla scen |
| 442373183681627338 | Exit Games Gamla stan | Stockholm | 442373174907143369 | venue unpublished | audit: OPEN — Gamla Stan: Österlånggatan 41, 111 31 Stockholm. Alla dagar 10:30–21:00. Priset är per person och ru |
| 445323671007954560 | Fasching | Stockholm | 445323658592814719 | venue unpublished | audit: NOT_A_VISITOR_PLACE — Fasching är en konsertlokal, klubb, restaurang och bar på Kungsgatan 63 i centrala Stockholm. (Site  |
| 445112379664008621 | Kronobergsbadet | Stockholm | 445112370738529708 | venue unpublished | audit: CLOSED_PERMANENT — (Mitt i, 2025-10-01) Polismyndigheten förlänger inte hyresavtalet med Stockholms stad ... Badet är ö |
| 445123110698518347 | Laserdome Aspudden | Stockholm | 445123101823371082 | venue unpublished | audit: NOT_A_VISITOR_PLACE — Vi har inga fasta öppettider då vi enbart har öppet efter bokningar. / Vi finns på Instrumentvägen 2 |
| 445125147217659377 | Laserdome Farsta | Stockholm | 445125129534473712 | venue unpublished | audit: NOT_A_VISITOR_PLACE — Vi har inga fasta öppettider då vi enbart har öppet efter bokningar. / Vi finns på Mårbackagatan 31- |
| 445120979312609137 | Lumenia Escape Room | Stockholm | 445120970244523888 | venue unpublished | audit: NOT_A_VISITOR_PLACE — Boka online! / Läs mer & boka. Vuxen 319 kr, under 18 299 kr. Telefon [tel] (vardagar 06.30- |
| 445323601567057840 | Maxim Teater | Stockholm | 445323589059643311 | venue unpublished | audit: CLOSED_PERMANENT — Maxim är stängt tillsvidare – I VÄNTAN PÅ ATT NY ÄGARE TAR ÖVER. Höstens program markerat INSTÄLLT.  |
| 430596695940695159 | Medeltidsmuseet | Stockholm | 178333934176732583 | venue unpublished | audit: CLOSED_RENOVATION — Medeltidsmuseet under Norrbro har stängt för flytt. Vi ses i Gamla stan på stadsvandringar och förel |
| 445323628519655195 | Mälarhöjdens dansskola | Stockholm | 445323619459958554 | venue unpublished | audit: NOT_A_VISITOR_PLACE — Nu är anmälan öppen till höstterminen 2026! / Schema hösten 2026 / 'Vi har kurser för alla 3 år ända |
| 442373156200547683 | PlayLand STHLM | Stockholm | 442373144095786338 | venue unpublished | audit: UNCLEAR — Playland STHLM, Fridhemsgatan 49-51, 112 46 Stockholm. Ej verifierat företag. Senaste recension 2016 |
| 445323427780265482 | Pygméteatern | Stockholm | 445323415214130697 | venue unpublished | audit: NOT_A_VISITOR_PLACE — Vi spelar 3 föreställningar, samtliga även på turné. ... Einstein funderar... tis 27/10 13.00, sön 1 |
| 429855049544402862 | Spela Paintball | Stockholm | 429854003812140973 | venue unpublished | audit: NOT_A_VISITOR_PLACE — Våra tjänster har endast öppet efter bokningar ... Bokningsbara tider i Farsta (Inomhus aktiviteter) |
| 442373290485384950 | SpelaPaintball Farsta (inomhus) | Stockholm | 442373278305126133 | venue unpublished | audit: NOT_A_VISITOR_PLACE — Våra tjänster har endast öppet efter bokningar ... Bokningsbara tider i Farsta (Inomhus aktiviteter) |
| 445119044933158859 | Vällingby simhall | Stockholm | 445119035999291338 | venue unpublished | audit: CLOSED_RENOVATION — Vällingby sim- och idrottshall har stängt för en stor renovering. Vi räknar med att öppna igen i aug |
| 431625064958428509 | Moga Fritid Bad- och Friskvårdsanläggning | Svenljunga | 431621349610390876 | venue unpublished | audit: CLOSED_RENOVATION — OBS! Simhallen Moga Fritid har stängt på grund av omfattande renovering från sommaren 2026 och cirka |
| 434467909591402156 | Everts Sjöbod | Tanum | 434466767524365995 | venue unpublished | audit: NOT_A_VISITOR_PLACE — Krabb- och makrillfiske 750 SEK per person ... För bokning eller eventuella frågor kontakta [namn]. Skä |
| 433070648810571279 | Badhuset i Tibro | Tibro | 433069672980579854 | venue unpublished | audit: NOT_A_VISITOR_PLACE — Badhuset är öppet för bokningar under perioden 28 september 2026 till och med den 1 juni 2027. ... 1 |
| 435862534386386814 | Saab Car Museum | Trollhättan | 435860304795043709 | venue unpublished | audit: CLOSED_RENOVATION — Saab Car Museum är tillfälligt stängt på grund av renovering av tak och takfönster. Stängt för avvec |
| 442363808707544733 | Upp & Ner Lekland | Trollhättan | 442363799958226588 | venue unpublished | audit: CLOSED_PERMANENT — TTELA: "Upp och ner lekland i Trollhättan stänger för gott". Facebook-sidan (10 jan 2025): leklandet |
| 445115146310813132 | Tibblebadet | Täby | 445115134214440395 | venue unpublished | audit: CLOSED_PERMANENT — Tjänsteutlåtande KS – Återställning efter rivning av Tibblebadet (KS 2024-04-25); kommunstyrelsen be |
| 442363688003864166 | Paradis Paintball & Äventyr | Uddevalla | 442363679195825765 | venue unpublished | audit: NOT_A_VISITOR_PLACE — 'paintbollpark ute i skogen', 'bokar en tre- eller femkamp tillsammans med familjen', 'kanske sumobr |
| 435798019842017095 | Stellas Lekland Uddevalla | Uddevalla | 435797387013818182 | venue unpublished | audit: UNCLEAR — Operator site lists only Skövde: 'Stellas Lekland på Stallsikens handelsområde i Skövde', Titanvägen |
| 426615896685970906 | Hembygdsgård | Upplands Väsby | 187991706086442842 | moved to holding 487837625768510838 | audit: UNCLEAR — Kommun page only: 'Mer information hittar du på Salems Hembygdsförenings hemsida' (hembygd.se/salem  |
| 426624619336730562 | Örnäs Islandshästar | Upplands-Bro | 426623575466739649 | venue unpublished | audit: NOT_A_VISITOR_PLACE — SIF-auktoriserad ridskola ... Ridskola, Ridläger, Ridkurser, Uteritter, Företag & Event, Bed & Break |
| 442379940504044863 | Örnäs gård | Upplands-Bro | 442379927904355646 | venue unpublished | audit: NOT_A_VISITOR_PLACE — SIF-auktoriserad ridskola ... Ring [namn] skicka ett mail om du vill veta mer. |
| 441654365254616131 | Reginateatern | Uppsala | 441654352269050946 | venue unpublished | audit: CLOSED_RENOVATION — Nu vet vi att Reginateatern inte kommer att öppna sitt hus under hösten 2026. Medan renoveringen påg |
| 441662335799560141 | Vårdsätra naturpark | Uppsala | 441662323149539276 | venue unpublished | audit: NOT_A_VISITOR_PLACE — Hela skogen är ett försöksområde för vetenskapliga studier. Det är förbjudet att beträda reservatet  |
| 442346211345729374 | Wadstena–Fogelsta Järnväg | Vadstena | 442346198796371805 | venue unpublished | audit: SEASON_ONLY — Du kan åka med vår fina rälsbuss genom Vadstena de flesta helger i juli och augusti. |
| 436014930949342440 | Fotevikens Museum | Vellinge | 436014927400961255 | venue unpublished | audit: UNCLEAR — sedan 2024 Fotevikens Vikingaby ... valde 2024 att ta sin hand från verksamheten |
| 436014958480753904 | Kungshaga gård | Vellinge | 436014953346925807 | venue unpublished | audit: NOT_A_VISITOR_PLACE — Observera att aktiviteten måste förbokas. ... För bokning av rundvandring mejla Kungshaga 4H. |
| 442158256085829604 | Björkbackens Äventyrsgolf | Vimmerby | 442158244434053091 | venue unpublished | audit: UNCLEAR — July 2023 reviewer: "Mini golf and playground" (minigolf costs extra); booking listings: "12-hole mi |
| 442158222724335585 | Vimmerby simhall | Vimmerby | 442158211047393248 | venue unpublished | audit: CLOSED_PERMANENT — I kommunen finns Gullringens simhall som sköts av Gullringens Simhallsanläggnings ekonomisk förening |
| 442382265507415710 | Gustavsbergs Konsthall | Värmdö | 442382256112174749 | venue unpublished | audit: UNCLEAR — Värmdö kommun "Konst och museum" lists only Fotoparken, Gustavsbergs porslinsmuseum and Artipelag –  |
| 442161765669701628 | Aktiveum – Ankarsrums Industrimuseum | Västervik | 442161753657214971 | venue unpublished | audit: UNCLEAR — "Aktiveum anordnar guidade visningar av industrimuseet och Bruksparken vid våra öppettider eller eft |
| 461453771893933719 | Frösåkers Brygga | Västerås | 461453766592333462 | venue unpublished | audit: NOT_A_VISITOR_PLACE — Startsida: "KONFERENSHOTELL - DAGKONFERENS - BRÖLLOP/HÖGTIDSDAGAR - EVENT - GÄSTHAMN". Aktiviteter a |
| 442352835544253552 | Hönö Bowling | Öckerö | 442352822793569391 | venue unpublished | audit: UNCLEAR — No bowling hall listed on ockero.se (Idrottsanläggningar) or on Visit Öckerö (vastsverige.com/visito |
| 431703668958463352 | Nöje.se | Öckerö | 431701838060881269 | venue unpublished | audit: UNCLEAR — noje.se returns HTTP 403; no bowling on ockero.se or Visit Öckerö; web searches for Hönö bowling fou |
| 441711877249074626 | Adolfsbergs lekmiljöer | Örebro | 441711864942986689 | venue unpublished | audit: UNCLEAR — Kommunens lista över lekplatser och lekmiljöer (22 st, t.ex. Svalsjöns lekplats, Svampens lekmiljöer |
| 441714771604047304 | Almbyparken | Örebro | 441714758761088455 | venue unpublished | audit: UNCLEAR — "Almbyparken" finns inte bland kommunens 31 parker eller i lekplatslistan; Almby har bara "Svalsjöns |
| 442322877266560459 | Andy's Lekland Örebro | Örebro | 442322865505732042 | venue unpublished | audit: CLOSED_PERMANENT — 20 Nov 2017: Leo's Lekland acquired Andy's Lekland (5 centres incl. Örebro). Today andyslekland.se d |
| 441696271703508349 | Aqua Nova | Örebro | 441696259414197628 | venue already unpublished 2026-10-19 | audit: UNCLEAR — Kommunens Svampen-sida nämner bara "Nedanför vattentornet Svampen finns en stor och populär lekplats |
| 441727992729732588 | Bettorps naturreservat | Örebro | 441727980046157291 | venue unpublished | audit: UNCLEAR — ÖREBRO KOMMUN: Arvaby, Berga äng, Björkön (kn) ... Öknaskogen (kn) – no 'Bettorp' in the list |
| 442322947361768913 | Fagerlinds Tid – Örebro Escape Room | Örebro | 442322935659660752 | venue unpublished | audit: NOT_A_VISITOR_PLACE — Ja! Här finns ingen "drop-in" eller liknande. … Priset är 290:- per person, lägsta pris för bokning  |
| 441686696753399125 | MegaFun | Örebro | 441686684111766868 | venue unpublished | audit: UNCLEAR — megafun.se = 'Byggföretag: Allt du behöver veta!' (byggblogg, inget om lekland/Örebro). WebSearch 'M |
| 441694997037745527 | O'Learys Örebro | Örebro | 441694984781989238 | venue unpublished | audit: UNCLEAR — Official O'Learys location page returns HTTP 404 (site_check); olearys.com then rate-limited (429).  |
| 442322904756028878 | Strike & Co Örebro | Örebro | 442322896216425933 | venue unpublished | audit: UNCLEAR — This domain has been purchased and parked by a customer of Loopia. (SPF 2023 invitation: 'Strike & C |
| 442322834618877384 | Teater Martin Mutter | Örebro | 442322825718564295 | venue unpublished | audit: NOT_A_VISITOR_PLACE — Offentliga föreställningar – Här visas offentliga speltillfällen. ... Teater Martin Mutter, Beväring |
| 441708646284428727 | Tysslingen | Örebro | 441708633667962294 | venue unpublished | audit: OPEN — Tysslingen är kanske mest känd för den stora mängden sångsvanar |
| 441721421396215250 | Åstabadet | Örebro | 441721409400505809 | venue unpublished | audit: CLOSED_PERMANENT — Vid Åstabadet kan vi just nu inte rekommendera bad på grund av dåliga förhållanden vad gäller vatten |
| 441685010878072143 | Örebro läns museum | Örebro | 441684998496486734 | venue unpublished | audit: CLOSED_RENOVATION — Museibyggnaden är stängd för renovering sedan 2018 ... Vi räknar med att kunna välkomna er under slu |
| 442376290855585379 | Österåkers Bowlinghall | Österåker | 442376282257262178 | venue unpublished | audit: UNCLEAR — Kommunens sida 'Hallar och idrottsanläggningar' nämner ingen bowlinghall; ingen officiell webbplats  |
| 442318216681784997 | Östhammars Bowlinghall | Östhammar | 442318204551857828 | venue unpublished | audit: UNCLEAR — Kommunens idrottssida ("Simhallar, gym, sporthallar, idrottsplatser och ishallar") nämner ingen bowl |
| 436015621826708882 | Svenska VävstolsMuseet | Östra Göinge | 436015618303493521 | venue unpublished | audit: UNCLEAR — Website unreachable (connection refused on https://www.vavmuseum.se and https://vavmuseum.se, 2026-1 |
| 427970066991056881 | Tyresö kommun | Tyresö | 248678996634535313 | moved to holding 487837658643465591 | duplicate of 442382310864618997 |
| 429454141811623177 | Norrtälje Bangolf | Norrtälje | 429453476888610056 | venue unpublished | duplicate of 442384428266718621 |
| 432025488509142419 | DVVJ | Bengtsfors | 432024320076711314 | venue unpublished | duplicate of 442363933681026776 |
| 427764882117526550 | Ekerö kommun | Järfälla | 427764101238785045 | venue unpublished | duplicate of 442376377467962697 |
| 433153863701268003 | Falkängen Kinnekulle | Götene | 433152914354112034 | venue unpublished | duplicate of 442360046861452720 |
| 427332554987701781 | Kungliga Slottet | Stockholm | 178316519871120801 | moved to holding 487837411036923252 | duplicate of 442369857850213962 |
| 442309743130740358 | Funplays Uppsala | Uppsala | 442309727762810501 | venue unpublished | duplicate of 442265717828519780 |
| 441621050946520480 | Busfabriken | Uppsala | 441621036652332447 | venue unpublished | duplicate of 442265717828519780 |
| 442308828856354225 | Fyrishov | Uppsala | 442308776133952944 | venue unpublished | duplicate of 442265663185127055 |
| 441232818954077278 | Fyrishov äventyrsbad | Uppsala | 441232164416160861 | venue unpublished | duplicate of 442265663185127055 |
| 445117282796996214 | Färsna 4H-gård | Norrtälje | 445117270381856373 | venue unpublished | duplicate of 429512598698886757 |
| 434587633121789676 | Fritid Lysekils kommun | Lysekil | 434586237769123563 | venue unpublished | duplicate of 442363910436194000 |
| 427315636918584592 | Lidingö stad | Lidingö | 253228975550137400 | moved to holding 487837957194024317 | duplicate of (Gångsätrahallen closed; mislabeled) |
| 428041665027016195 | Statens fastighetsverk | Stockholm | 428040706729215490 | venue unpublished | duplicate of 442369810966284014 |
| 434905913485198516 | Hållöfärjan | Sotenäs | 434903500149785779 | venue unpublished | duplicate of 442365522298832605 |
| 427751489369310490 | JumpYard | Nacka | 187172203450631962 | venue unpublished | duplicate of 442379817325725478 |
| 429397142646326923 | JumpYard | Nacka | 187172203450631962 | venue unpublished | duplicate of 442380008409827307 |
| 427300884553172765 | JumpYard | Nacka | 187172203450631962 | venue unpublished | duplicate of 442373386014852368 |
| 427739684425204780 | Kallhälls 4H-gård | Järfälla | 427718020366894381 | moved to holding 487837745398449528 | duplicate of 442379847658931839 |
| 427785129532884205 | Kungliga Slottet | Stockholm | 178316519871120801 | moved to holding 487837411036923252 | duplicate of 442376330718250487 |
| 442309771593287557 | Latitude-59 | Uppsala | 442309759639521156 | venue unpublished | duplicate of 442265762028094563 |
| 429283913106490954 | Lek & Bus - Nacka | Nacka | 429282741578663497 | venue unpublished | duplicate of 442382230728247111 |
| 442380117369456012 | Lådbilslandet Nykvarn | Nykvarn | 442380108116821387 | venue unpublished | duplicate of 426607936274466736 |
| 442335079285425753 | Göta kanal i Söderköping | Söderköping | 442335065897207384 | venue unpublished | duplicate of 441819157504231008 |
| 430224815786329285 | Kulturhuset Stadsteatern | Stockholm | 377312454805325496 | moved to holding 487837787492484473 | duplicate of 442369965509608549 |
| 428061444131555058 | Sigtuna kommun | Sigtuna | 428060477025715953 | venue unpublished | duplicate of 442376407289463960 |
| 429352997781275743 | Medley | Upplands Väsby | 259199720268793095 | moved to holding 487837990085756286 | duplicate of 442382182720243699 |
| 434569760529745633 | Kosterhavets nationalpark | Strömstad | 434568274806605536 | venue unpublished | duplicate of 442352706997225453 |
| 432062182872614299 | Not Quite | Åmål | 432055797992687000 | venue unpublished | duplicate of 442363875858351820 |
| 434972584195425863 | Odenbadet Falköping | Falköping | 434969688615716422 | venue unpublished | duplicate of 442360082135549363 |
| 442309812353533009 | Race4all Gokart | Uppsala | 442309798713656400 | venue unpublished | duplicate of 442265794483619119 |
| 429238787596387510 | Racehall | Botkyrka | 429236376962106549 | venue unpublished | duplicate of 442380037602182975 |
| 431549606090802501 | Ragnerud Vandringsdestination | Färgelanda | 431540848165946692 | venue unpublished | duplicate of 442363736280303226 |
| 430201818467828795 | Kungliga Slottet | Stockholm | 178316519871120801 | moved to holding 487837411036923252 | duplicate of 442370073705875094 |
| 428077923988178894 | Kungliga Slottet | Stockholm | 178316519871120801 | moved to holding 487837411036923252 | duplicate of 442369891782133155 |
| 429499759733016495 | Roslags Museum | Norrtälje | 429498845173417902 | venue unpublished | duplicate of 442384340656097242 |
| 442369930839491842 | Stockholms stadsmuseum | Stockholm | 442369918189470977 | venue unpublished | duplicate of 430619439344420101 |
| 430199118216856858 | Stromma Stockholm | Stockholm | 430198261245052185 | venue unpublished | duplicate of 442370104282351100 |
| 427086212767975421 | Sundbybergs stad | Sundbyberg | 253319603671827571 | moved to holding 487838077453108607 | duplicate of 442373357728466355 |
| 428016504865326922 | Haninge kommun | Haninge | 428015316543506249 | venue unpublished | duplicate of 442382406066930805 |
| 435848526702872429 | Visit Trollhättan Vänersborg | Vänersborg | 435847577255053162 | venue unpublished | duplicate of 442360170543089129 |
| 442363849190966983 | Tumlaren – Sotenäs simanläggning | Sotenäs | 442363836079572678 | venue unpublished | duplicate of 434910042282558649 |
| 427962257054401786 | Medley | Upplands Väsby | 259199720268793095 | moved to holding 487837990085756286 | duplicate of 442382345123693868 |
| 427293853205169174 | Medley | Upplands Väsby | 259199720268793095 | moved to holding 487837990085756286 | duplicate of 442373422790509741 |
| 441822929030776478 | Tåkern naturum | Ödeshög | 441822909879584413 | venue unpublished | duplicate of 442348317330933628 |
| 428036728733861616 | Kungliga Slottet | Stockholm | 178316519871120801 | moved to holding 487837411036923252 | duplicate of 442373317563811413 |
| 441184704121571018 | Upplandsmuseet | Uppsala | 377371173417158342 | moved to holding 487837829443913082 | duplicate of 441184329268233929 |
| 429877204319503616 | VREX City | Stockholm | 429867006406198753 | moved to holding 487837871420507515 | duplicate of 429868029313058274 |
| 427043663902704690 | Vallentuna kommun | Vallentuna | 427040060139930673 | venue unpublished | duplicate of 442376190251009954 |
| 435719220102203176 | Vilanbadet Skara | Skara | 435718530063697703 | venue unpublished | duplicate of 442355581907404197 |
| 427278805409760720 | Medley | Upplands Väsby | 259199720268793095 | moved to holding 487837990085756286 | duplicate of 442379894156985817 |
| 427034787606201642 | Medley | Upplands Väsby | 259199720268793095 | moved to holding 487837990085756286 | duplicate of (operator "Medley", not a place) |
| 429400706152170893 | Yoump Sverige | Huddinge | 184929995582375506 | moved to holding 487838110328063360 | duplicate of 442379968790430871 |
| 442324937550628308 | Gustavsvik Äventyrsgolf | Örebro | 442324924749612499 | venue unpublished | duplicate of 441726092802295267 |
| 428055272750089239 | Dammstugan | Sigtuna | 428053161480061974 | venue unpublished | duplicate of 442376459558881276 |
| 434944485026203197 | Åsle Tå Upplevelsemuseum | Falköping | 434943665106880060 | venue unpublished | duplicate of 442360112342926777 |
| 427179865368725006 | Nynäshamns kommun | Nynäshamn | 427178818428503565 | venue unpublished | duplicate of 442382473729443497 |
| 445121087919916469 | Laserdome Vasastan | Stockholm | 445121075328615860 | venue unpublished | duplicate of 430015035549451869 |
| 442352766128523251 | John Scott's Bowling Partille | Partille | 442352753352673266 | venue unpublished | duplicate of 434547084285216462 |
| 429917923310602044 | Tolv Stockholm | Stockholm | 429887652028777506 | moved to holding 487837904035415420 | duplicate of (Bodyflight: booking-only, wrong venue) |
| 445118974879892668 | VREX | Stockholm | 445118965946025147 | venue unpublished | duplicate of 442373224206992429 (VREX Bromma) |
| 442230093398443056 | Avesta Visentpark | Avesta | 442230078835819567 | venue unpublished | Stängt för säsongen; öppnar maj 2027 men varken datum eller öppettider (2026 eller 2027) är publicerade |
| 431608533000160594 | Buaskogen Adventure | Bollebyggd | 431607303699989841 | venue unpublished | Säsongsstängt; öppnar 'någon gång i april' 2027 utan datum, och inga öppettider eller öppetdagar publiceras (biljetter bokas online) |
| 442151235634628490 | Greby Gokart | Borgholm | 442151221424326537 | venue unpublished | Säsongen slut 31 okt 2026; inga drop-in-tider för sommaren 2026 eller 2027 publicerade |
| 442151186292836226 | Köpingbadens Äventyrsgolf | Borgholm | 442151170362869633 | venue unpublished | Inga öppettider för äventyrsgolfen publiceras; campingen (där banan ligger) är stängd till 27 maj 2027 |
| 442150854204622688 | Naturum Trollskogen | Borgholm | 442150841529435999 | venue unpublished | Naturum stängt sedan 2 okt 2026; ordinarie öppettider upphör, bara enstaka evenemang och inget 2027-datum |
| 442352583735019404 | Borås Djurpark | Borås | 442352570967558027 | venue unpublished | Stängt för säsongen; 2027 års öppetdagar och tider ej publicerade (öppetdagar varierar, ej dagligen) |
| 442348271755626359 | Boxholms Bruksmuseum | Boxholm | 442348263065028470 | venue unpublished | Inga publicerade öppettider; endast 'öppet sommartid' utan datum eller tider, och museets webbplats svarar inte |
| 426977534895228350 | Cedergrenska tornet | Danderyd | 426951216711370173 | venue unpublished | Tornet är en bokningsbar festvåning/konferensanläggning utan publika öppettider eller drop-in-besök |
| 442376330718250487 | Kina slott | Ekerö | 442376318923867638 | venue unpublished | Vinterstängt; öppnar sommaren 2027 men datum och tider är inte publicerade, och 2026 års tider gick inte att bekräfta |
| 442259972865164788 | Parken Zoo | Eskilstuna | 442259957119747571 | venue unpublished | Stängt efter säsongen 2026; säsongen 2027 har inga publicerade datum och 2026 års säsongsdatum gick inte att hämta |
| 432152548967744945 | Jonslundsbadet | Essunga | 432151138708522416 | venue unpublished | Sommarbad stängt till 6 juni 2027; inga officiella öppettider eller slutdatum publiceras (bara på Facebook/Instagram) |
| 442360112342926777 | Åsle Tå | Falköping | 442360103048349112 | venue unpublished | Museet är stängt till 2027 och varken öppningsdatum eller öppettider är publicerade (inga 2026-datum att kopiera heller) |
| 442342511952824080 | Reijmyre Glasbruk | Finspång | 442342500032612111 | venue unpublished | Inga publika öppettider; besök sker via bokade visningar/upplevelser (produktionsvisning 200 kr i fasta tidsluckor, glasblåsning 1 100 kr) e |
| 441819197442393703 | Rejmyre glasbruk | Finspång | 441819185186637414 | venue unpublished | Inga publika öppettider; besök sker via bokade visningar/upplevelser (produktionsvisning 200 kr i fasta tidsluckor, glasblåsning 1 100 kr) e |
| 442257319338739131 | Isaberg Mountain Resort | Gislaved | 442257306470614458 | venue unpublished | Aktiviteterna är stängda för säsongen; skidsäsongens 2026/27 datum och tider är inte publicerade och höghöjdsbanan kräver förbokad starttid  |
| 442252388288464264 | Furuvik | Gävle | 442252376259200391 | venue unpublished | Stängt för säsongen; säsongsdatum och dagliga öppettider för 2027 ej publicerade, 2026 års slutdatum och dagstider går inte att få fram |
| 435877273044813713 | Liseberg | Göteborg | 435867936071124871 | venue unpublished | Stängt nu; jul 14 nov–30 dec 2026 bara utvalda dagar och sommar 2027 ej publicerad; öppetdagar och tider kan inte verifieras |
| 442360013164414381 | Råbäcks Mekaniska Stenhuggeri | Götene | 442360000237569452 | venue unpublished | Öppet bara sista helgfria lördagen i månaden mars–nov 11–15, annars bara bokade grupper; går inte att visa som veckorecurrens |
| 462631128788927946 | Experience Wildpark | Habo | 462631125030831561 | venue unpublished | Inga publicerade öppettider eller drop-in; aktiviteterna bokas i förväg i bokningssystemet |
| 442325217545586153 | Hallsbergs Modelljärnväg | Hallsberg | 442325204761347560 | venue unpublished | Öppet endast enstaka utvalda datum (ca en lördag i månaden 12–15 samt vissa byggkvällar måndagar), inga regelbundna veckotider |
| 436015059982910738 | Filborna Arena | Helsingborg | 436015054865859857 | venue unpublished | Tider för allmänt bad går inte att verifiera (filbornaarena.se är en JS-app, kommunens sida hänvisar dit); anläggningen är gym/simhall med a |
| 432463128580621805 | Ångaren Trafik | Hjo | 432461379195143660 | venue unpublished | Inga regelbundna öppettider – endast enstaka biljettförsedda ångbåtsturer på utvalda sommardatum (14 juni–16 aug 2026), inga turer resten av |
| 442331367552878136 | Måltidens Hus i Grythyttan | Hällefors | 442331358585456183 | venue unpublished | University campus building; only a weekday lunch restaurant is open to the public and no opening times are published |
| 442257515892213193 | Härjedalens Fjällmuseum | Härjedalen | 442257501262480840 | venue unpublished | Closed for the season until 14 Dec 2026; winter-season opening hours not yet published |
| 436015711224104364 | Söderto Fotbollsgolf | Hörby | 436015707717666219 | venue unpublished | Closed for the season; no 2027 season dates or opening hours published |
| 436013955664610349 | Skånes djurpark | Höör | 436013950497227820 | venue unpublished | Seasonal park; open dates and times are only in a JavaScript calendar that could not be read, so no correct weekly window can be set |
| 442144205016434436 | Escape Room Kalmar | Kalmar | 442144192802621187 | venue unpublished | Escape rooms endast som förbokade pass (onsdag-söndag), inga drop-in-öppettider |
| 442144155221657342 | Kalmar Gokart | Kalmar | 442144146304567037 | venue unpublished | Säsongen slut 31 okt 2026; drop-in för 2027 ej publicerat (endast korta helgpass, övrig tid bokade race) |
| 442255044725736873 | Eriksberg Vilt & Natur | Karlshamn | 442255030389605800 | venue unpublished | Safariparken för dagsgäster kräver förbokad tid (13-17), inga drop-in-öppettider |
| 442327350483387899 | Alfred Nobels Björkborn (Nobelmuseet i Karlskoga) | Karlskoga | 442327338202465786 | venue unpublished | Endast två enstaka öppna lördagar kvar (7 och 21 nov 2026), övrig tid bokning; sommar 2027 ej publicerad |
| 441823056202073766 | Kinda kanal | Kinda | 441823037017327269 | venue unpublished | Endast bokade båtkryssningar med M/S Kind enligt turlista, inga drop-in-öppettider; inga turer förrän säsongstart mitten av maj 2027 |
| 442329610097559066 | Tivedstorp | Laxå | 442329597489481241 | venue unpublished | Stängt för vintern (byn tar inte emot gäster); kafé öppnar igen maj 2027 men inga datum eller öppettider är publicerade |
| 442229832135246874 | Leksand Sommarland | Leksand | 442229810786239513 | venue unpublished | Stängt för säsongen; 2027 års säsongsdatum och dagliga öppettider är inte publicerade (öppetdagar varierar i juni/augusti) |
| 435773526599829311 | Läckö slott | Lidköping | 435770898717378366 | venue unpublished | Slottet har nu bara enstaka guidade visningar fre-sön till 22 nov och är sedan stängt; sommarens dagliga öppettider för 2027 är inte publice |
| 442322737126475198 | Frövifors pappersbruksmuseum | Lindesberg | 442322725332092349 | venue unpublished | Utanför sommarsäsongen tar museet bara emot förbokade besök på vardagar; sommarens öppetdagar och tider är inte publicerade. |
| 442337590826272424 | Baronia Escape Room | Linköping | 442337580508284583 | venue unpublished | Escape room med endast förbokade spel (60 min), inga drop-in-öppettider. |
| 442335271611041408 | Gokartuthyrningen Motorstadion Sviestad | Linköping | 442335258700973695 | venue unpublished | Stängt för säsongen och öppnar 'våren 2027' utan datum; inga fasta öppettider publicerade, körning bokas online. |
| 442337704986838719 | Vidingsjö Minigolf och Glass | Linköping | 442337691405682366 | venue unpublished | Stängt för säsongen; öppnar 11 april 2027 men klockslag publiceras inte (vidingsjo.com, linkopingsbgk.com/oppettider: 'Öppettider för året ä |
| 442331506183013958 | Bångbro Herrgård | Ljusnarsberg | 442331494011143749 | venue unpublished | Hotell- och konferensanläggning; middagar och julbord endast mot förbokning, inga publika öppettider eller café |
| 436014614170338460 | Sherlocked Escape Room Malmö | Malmö | 436014610663900315 | venue unpublished | Escape room, booking-only sessions; no drop-in opening hours |
| 442242479027160303 | Klätterpark Sälen (Svansjön) | Malung-Sälen | 442242467023062254 | venue unpublished | Closed for the season with no 2026 or 2027 dates published; entry by pre-booked 2.5 h climbing sessions |
| 431598623864685902 | M/S Bellevue - Göta kanal | Mariestad | 431597171368822093 | venue unpublished | Scheduled boat tours (Wed/Sat in season) that must be pre-booked; no drop-in hours |
| 434483835254638258 | Qvarnstensgruvan i Lugnås | Mariestad | 434481626173441713 | venue unpublished | Public guided tours are summer-only with no published dates or tour times; rest of the year private visits by booking only |
| 442229971218367526 | Tomteland (Santaworld) | Mora | 442229954608923685 | venue unpublished | Duplicate of 442240169953756373 (same park, Sagolandet Tomteland, Sollerön) |
| 442140871106791143 | Ölands Djur & Nöjespark | Mörbylånga | 442140859253688038 | venue unpublished | Closed for the season 1 Oct 2026-30 Apr 2027; 2027 opening dates and summer hours not published yet |
| 442329703815087653 | Alntorps ö | Nora | 442329694126245412 | venue unpublished | Island reachable only by the summer boat M/S Plaskus, which has stopped for the season; 2027 season dates not published |
| 442322763877746113 | Nora Bergslags Veteran-Jernväg | Nora | 442322755321365952 | venue unpublished | Heritage train rides only on timetable days in summer and special weekends (booked tickets); no regular drop-in opening hours; 2027 timetabl |
| 441819272814036595 | Färgargården | Norrköping | 441819260264679026 | venue unpublished | No published opening hours or season for Färgargården; cannot confirm when visitors can enter |
| 442340314540181257 | Äventyrsgolf i Norrköping | Norrköping | 442340302661912328 | venue unpublished | Closed for the season since 20 Sep 2026; 2027 opening date and golf opening hours not published |
| 442384428266718621 | BangolfParken Norrtälje | Norrtälje | 442384415599920540 | venue unpublished | Closed for the season; reopens April 2027 but exact date and hours not yet published (also duplicate of 429454141811623177) |
| 442237095545701552 | Dalhalla | Rättvik | 442237085286433967 | venue unpublished | Ingen drop-in: tillträde till kalkbrottet endast via guidade visningar sommartid (tider ej publicerade) eller förbokade gruppvisningar; anna |
| 442230028269290539 | Vidablick utsiktstorn | Rättvik | 442230013840884778 | venue unpublished | Säsongsöppet sommartid, stängt nu; inga officiella öppettider eller datum för 2027 (hänvisas bara till Facebook) |
| 442369891782133155 | Rosersbergs slott | Sigtuna | 442369880298128802 | venue unpublished | Slottet stängt för säsongen 2026, öppnar bara i samband med guidade visningar sommartid; 2027 års datum och tider ej publicerade |
| 435736262314329902 | Skara Sommarland | Skara | 435734798158300973 | venue unpublished | Closed for the season; official 2026/2027 season dates and daily closing times are not published (site only says early June-late August, ope |
| 442246816298206530 | Flatenbergs hytta | Smedjebacken | 442246803748848961 | venue unpublished | No published drop-in hours: the hytta is shown only in summer and times are given by phone ([tel]); closed now |
| 461452177865475586 | Konsthallen Meken | Smedjebacken | 461452172370937345 | venue unpublished | Konsthall open only during exhibitions; none running or announced since SKÖR ended 13 Sep 2026, so no known reopening date |
| 442376146722522169 | Väsjöbacken | Sollentuna | 442376134919750712 | venue unpublished | Winter-only ski slope that opens when there is enough snow (no date set); operator hours not available (vasjobacken.se/.com unreachable) |
| 442365522298832605 | Hållö fyr | Sotenäs | 442365509648811740 | venue unpublished | Stängd för säsongen 2026; öppet bara sommartid (2026: 22 jun-16 aug) och inga klockslag publiceras; dubblett av 434905913485198516 |
| 436014857096037584 | Uppåkra Arkeologiska Center | Staffanstorp | 436014851978986703 | venue unpublished | Inga ordinarie öppettider: besökscentrum öppet sporadiskt (skolbesök, enstaka butiksdagar i dec), sommarens visningstider ej publicerade |
| 430024402554357120 | Exit Games Stockholm | Stockholm | 430023672980342143 | venue unpublished | Escape rooms bokas online i förväg (60-min-pass, minst 800 kr per bokning), ingen drop-in |
| 445323244321408100 | Filmhuset | Stockholm | 445323230832526435 | venue unpublished | No drop-in hours for families: Bio Victor/Cinemateket screenings are ticketed programme events only (Unga Cinemateket Sundays); the library  |
| 430045128799847585 | Fox in a box | Stockholm | 177771663432123742 | venue unpublished | Escape rooms are booking-only (pre-booked games), no drop-in hours |
| 442369965509608549 | Marionetteatern | Stockholm | 442369956508632164 | venue unpublished | Theatre with ticketed performances on a schedule only, no drop-in hours; duplicate of 430224815786329285 |
| 445323503705556194 | Mimteatern | Stockholm | 445323491248473313 | venue unpublished | Children's mime theatre with ticketed scheduled performances only (many are school shows), no drop-in hours |
| 445323365964613277 | Mittiprickteatern | Stockholm | 445323352786110108 | venue unpublished | Children's theatre with scheduled performances only (weekends/holidays at Påfågeln, weekdays for schools), no drop-in hours |
| 445123077026645990 | Skärisbiografen | Stockholm | 445123064737335269 | venue unpublished | Biograf med endast biljetterade filmvisningar (sön familjevisningar, mån/lör kvällsbio), inga drop-in-öppettider |
| 445323322218022710 | Teater Tre | Stockholm | 445323312680175413 | venue unpublished | Barnteater med endast biljetterade föreställningar enligt spelschema, inga drop-in-öppettider |
| 445323460026074487 | Unga Klara | Stockholm | 445323450966377846 | venue unpublished | Theatre with ticketed performances only (spelschema via Tickster); no drop-in opening hours |
| 445128241842259590 | ZebraDans | Stockholm | 445128229217404549 | venue unpublished | Dance stage with ticketed performances only (biljetter via Kulturbiljetter); no drop-in opening hours |
| 445121052838757961 | Zita Folkets Bio | Stockholm | 445121043728729672 | venue unpublished | Cinema with scheduled screenings only; no drop-in opening hours |
| 442352706997225453 | Naturum Kosterhavet | Strömstad | 442352694204598252 | venue unpublished | Closed for the season; reopening only given as 'end of February 2027' and no 2027 opening hours published |
| 427778786050737651 | Drottningholms Slottsteater | Sundbyberg | 185892249534498479 | venue unpublished | Visit only by guided tour at set times (13.45 and 14.45, May-4 Oct) or booked private tour; no drop-in opening hours |
| 445323554951562319 | Teater Bristol | Sundbyberg | 445323542544811086 | venue unpublished | Theatre open only at performances (kassa/café 1 h before shows); no drop-in opening hours |
| 436015253004780866 | First Camp Röstånga – Söderåsen | Svalöv | 436015249498342721 | venue unpublished | Campsite for booked guests only (pool only for staying guests); no day-visit hours; closed 21 Sep-31 Dec and 2027 opening date not published |
| 436014919473726692 | Svedala friluftsbad | Svedala | 436014915984065763 | venue unpublished | Outdoor pool closed for the season (open June-August only); no daily hours published and summer 2027 may be affected by badhus construction |
| 442342618882410271 | Fix Bowlingcenter | Söderköping | 442342610133092126 | venue unpublished | Startsidan: 'Insamlingen är avslutad ... Vi återkommer inom kort med öppningsdatum' – att hallen är öppen nu kan inte bekräftas |
| 442342658795407142 | Söderköpings Friluftsbad | Söderköping | 442342646791309093 | venue unpublished | Stängt för säsongen, öppnar maj 2027; säsongsdatum och öppettider är inte publicerade |
| 426996352531072962 | Hembygdsgård | Upplands Väsby | 187991706086442842 | venue unpublished | No published opening times: museum open 'sommartid' and café May-mid September without days/times; record also has wrong address/kommun (Sto |
| 441634888290960886 | Uppsala Konsert & Kongress | Uppsala | 441634875934541301 | venue unpublished | Endast biljetterade föreställningar; huset har bara vardagslunch och biljettkassa, inget drop-in för familjer |
| 441640510847747704 | Uppsala Stadsteater | Uppsala | 441640498684266103 | venue unpublished | Endast biljetterade föreställningar; huset öppet bara i samband med föreställningar |
| 462631972305405585 | Hooks Herrgård | Vaggaryd | 462631966886364816 | venue unpublished | Hotell och spa; barn tas bara emot under skollov med förbokning online, inga drop-in-tider |
| 432360493919798741 | Vara Konserthus | Vara | 432359320378705364 | venue unpublished | Endast biljetterade föreställningar; ons–fre 13–16 är bara biljettkassans tider |
| 427019293729785338 | Bogesunds slott | Vaxholm | 427018046553490937 | venue unpublished | The castle interior can only be seen on ticketed guided tours booked via Billetto (summer weekends 13:00 and 15:00, plus 12–13 Dec). There a |
| 442158306308425703 | Vimmerby Adventure | Vimmerby | 442158293020870630 | venue unpublished | It is closed for the season ('tack för denna säsong!'). No 2026 or 2027 season dates or hours are published, so it cannot be scheduled. |
| 442161811706382335 | Västerviks Skärgårdstrafik | Västervik | 442161799677118462 | venue unpublished | Säsongsstängd till maj 2027 utan datum och utan publicerad tidtabell; resor kräver förköpt biljett |
| 461272836548363265 | Hälla Gokart | Västerås | 461272829342548992 | venue unpublished | Stängt för säsongen, öppnar 'våren 2027' utan datum; inga öppettider publicerade |
| 442242654718166267 | Idre Fjäll Sommar | Älvdalen | 442242645994013946 | venue unpublished | Endast sommaraktiviteter; sommarsäsong 2027 utan publicerade datum eller öppettider |
| 436015291927921998 | Upzone Ängelholm | Ängelholm | 436015288379540813 | venue unpublished | Booking-only high-ropes course with no published opening hours; outdoor season only (closed in winter) |
| 442348384951502724 | Ellen Keys Strand | Ödeshög | 442348373081622403 | venue unpublished | Guided tours only (May-September); no published tour times or drop-in hours, closed now |
| 441702841116034460 | Conventum | Örebro | 441702828558288283 | venue unpublished | Event arena with no public drop-in hours; only open during ticketed events |
| 441698421930231174 | Hallagårdens Djurpark | Örebro | 441698408583955845 | venue unpublished | Closed for the season; no opening hours or season end published for 2027 |
| 441727392944260585 | Käglan naturreservat | Örebro | 441727380722058728 | venue unpublished | Cannot confirm a place 'Käglan naturreservat' exists; Käglan is an unmarked forest area with no visitor facilities |
| 441726092802295267 | Äventyrsgolf Gustavsvik | Örebro | 441726080856917474 | venue unpublished | Closed for the season; no season dates or opening hours published |
| 441697165820069248 | Örebro Konserthus | Örebro | 441697153941800319 | venue unpublished | Concert venue with no drop-in opening hours; open only for ticketed performances |
| 441692188984771947 | Örebro Teater | Örebro | 441692176846456170 | venue unpublished | Theatre with no drop-in opening; open only for ticketed performances |
| 442257415086310851 | Moose Garden | Östersund | 442257402092357058 | venue unpublished | Booking-only guided tours, no drop-in hours; main season ended, closed late Sep-Oct |
| 436015610351093135 | Immelns Kanotcenter | Östra Göinge | 436015606785934734 | venue unpublished | Open by arrangement/booking outside mid-June-August; summer fixed hours not published |
| 442370036577896239 | Storkyrkan | Stockholm | 442370027585308462 | venue unpublished | duplicate of 430206808062199646 (Storkyrkan) |
| 442261399784162936 | Varbergs fästning | Varberg | 442261386681157239 | venue unpublished | duplicate of 486683801863357590 (Hallands kulturhistoriska museum) |

## Events moved to their own venue
| Event | New venue ID | Old venue ID |
|---|---|---|
| 427749763002172961 Leo's Lekland Barkarby | 487855164493956483 | 184408384697566772 |
| 435898123416537027 Leo's Lekland Borås | 487855198618813828 | 184408384697566772 |
| 427308615494305301 Leo's Lekland Täby/Arninge | 487855232768836997 | 184408384697566772 |
| 430052341895431889 Klättercentret Telefonplan | 487855266826585478 | 428032702118135789 |
| 430049351616726978 Klättercentret Akalla | 487855300699784583 | 428032702118135789 |
| 427929194798810117 Drottningholms slott (existing venue reused) | 379548563769689140 | 178316519871120801 |

## Corrected events
Full list with old and new values: `audits/permanent-places-fixes-2026-11-05.csv`.

## Follow-ups
- Events whose published span ends before April 2027 because the next season or period is not published yet. Re-check and extend:
  - 2026-11-15: Dalslands konstmuseum (Mellerud), 434238770846402204
  - 2026-11-21: Filmmuseet i Kristianstad (Kristianstad), 436015381543421288
  - 2026-11-22: Naturum Västervik (Västervik), 442161589777369072
  - 2026-11-22: Saltskog gård (Södertälje), 429195149294208500
  - 2026-11-28: Sim, Motion & Bowling Örkelljunga (Örkelljunga), 436015330976892250
  - 2026-11-29: Norrvikens trädgårdar (Båstad), 436015342318290270
  - 2026-11-29: Trelleborgs Sjöfartsmuseum (Trelleborg), 436014969880872180
  - 2026-11-30: Älvkarleby Sportfiske (Älvkarleby), 442315567886534143
  - 2026-12-06: Kungliga Slottet (Stockholm), 427929194798810117
  - 2026-12-06: Löfstad slott (Norrköping), 441814071147267601
  - 2026-12-06: Ostindiefararen Götheborg (Göteborg), 435951102282729351
  - 2026-12-11: Skänninge museum (Mjölby), 442346239036524387
  - 2026-12-12: Stadsmuseet Näktergalen (Vimmerby), 442158181485938654
  - 2026-12-13: Nossebro bad och camping (Essunga), 442360145578591677
  - 2026-12-13: Väsby Konsthall (Upplands-Bro), 427270182591825612
  - 2026-12-16: Bergööska huset (Hallsberg), 442325173530559974
  - 2026-12-16: Målilla Älgpark (Hultsfred), 442158145809188827
  - 2026-12-18: Birkagården (Stockholm), 445121160271660153
  - 2026-12-19: Klättercentret (Solna), 428033567520491502
  - 2026-12-19: Tavlebords Honungsgård (Orust), 433844485307270743
  - 2026-12-20: Hassela Ski Resort (Nordanstig), 471546697592374776
  - 2026-12-20: Naturum Fjärås Bräcka (Kungsbacka), 486680341730330235
  - 2026-12-20: NoraGlass (Nora), 442329674052306465
  - 2026-12-30: Gröna Lund (Stockholm), 430730440509261546
  - 2026-12-31: Armémuseum (Stockholm), 430580809796192017
  - 2026-12-31: Badet Vårgårda (Vårgårda), 442355382057207064
  - 2026-12-31: Carolina Rediviva (Uppsala), 441629250819229429
  - 2026-12-31: Fyrishov (Uppsala), 442265663185127055
  - 2026-12-31: Nääs slott (Lerum), 434899109996955008
  - 2026-12-31: Vadsbo Museum (Mariestad), 434493834257270456
  - 2027-01-03: Tjolöholms slott (Kungsbacka), 442260121259640421
  - 2027-01-06: Sagolandet Tomteland (Mora), 442240169953756373
  - 2027-01-06: Vadstena slott (Vadstena), 441819074524120662
  - 2027-01-10: BRIO Lekoseum (Osby), 436015587450193289
  - 2027-01-31: Mölndals stadsmuseum (Mölndal), 435695958274115341
  - 2027-01-31: Sancta Birgitta Klostermuseum (Vadstena), 442346145352550228
  - 2027-02-13: Naturum Abisko (Kiruna), 442250100002030937
  - 2027-02-21: Arena Skövde Upplevelsebad (Skövde), 442355479843210652
  - 2027-02-28: Ulricehamn Ski Center (Ulricehamn), 442355292626257120
  - 2027-03-15: Behrn Arena (Örebro), 441699069203613066
  - 2027-03-21: Vedbobacken (Västerås), 461455362340456212
  - 2027-03-28: Gränby ishallar (Uppsala), 441650079279908747
  - 2027-03-28: Hovfjället (Torsby), 486676671051630269
  - 2027-03-28: Klackbergsbacken (Norberg), 461452767660115516
  - 2027-03-28: Åmåls simhall (Åmål), 432039400327644566
  - 2027-03-31: Mullsjö Alpin (Mullsjö), 462631241020114493
- 89 seasonal events use the 2026 season dates copied into 2027 (`copied_2026_pattern`); confirm when the 2027 dates are out.
- Some events the audit found correct (1 Oct 2026 batch) still have parentMaxAge 18; that bulk change was outside the approved fix list and was not made.