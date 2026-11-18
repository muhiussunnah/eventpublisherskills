# Norrbotten, Västerbotten, Västernorrland, Jämtland + Gotland — permanent places final report (2026-11-18)

Source: client file `Famies - Vad ska vi hitta pa idag_3.html` (the last five regions). Published with the strict rules from 2026-11-05: every status, hours, season, price and address checked on an official, current source (evidence quote per fact), organizer → venue → recurring event, push notifications off. With this run **all 21 regions** have permanent places in the app.

| | Count |
|---|---|
| Places in the file for the five regions | 354 |
| Already in the app (not duplicated; 2 of them stay hidden since the 2026-11-05 audit) | 22 |
| Researched (42 research agents, one per group of ~8 places) | 332 (one item covered two ski areas → 333 rows) |
| **Published** | **196** (Gotland 24, Västernorrland 36, Jämtland 38, Västerbotten 49, Norrbotten 49) |
| Skipped (reasons below) | 137 — roughly: no published hours or season 83 (about 10 of them publish hours only week by week), booking-only or guided-only 37, no real photo 14, other 3 |
| Seasonal places with the last season copied to 2027 (official 2027 dates not out yet) | 65 |
| Organizers | 156 new, 40 reused |
| Published live events in the app | 1,248 → **1,444** (1,339 recurring, 105 one time) |

## Checks after publishing
- Every new event re-read from the API and compared field by field with the spec (title, description, days, start, duration, start/end date, isFree, ages 18–100 / child min–18, interests, venue, kommun, opening-hours count, organizer, logo): **196/196 OK**. The audit first reported three differences: "Robertsfors" (the app spells the kommun "Robertfors" — false alarm) and two reused organizers without a logo (Vilhelmina kommun, Ájtte) → logos added to those organizers.
- All 196 new events are in the live list and sit on published venues. Duplicate titles among all 1,444 published live events: 0. Duplicate cover-image URLs: 0.
- Duplicate photos: every event and venue image was compared (64-bit dHash, same image pipeline for both sides) with the covers of all 1,248 published live events and with the other images of its batch; distance ≤ 10 = duplicate. Seven hits were chain or shared photos (JumpYard Sundsvall, two Leo's Lekland photos, Leo's Skellefteå venue, Skuleskogen, Potatisbacken, Icehotel) → replaced with another official photo before publishing. The SHA-256 guard in the publisher stopped nothing.
- Sheet `Events` tab refreshed at the end: 1,444 published live events in A2:E1445 (1,339 recurring, 105 one time), no leftover rows; G23 Total = I292 Total = city sum = 1,444; checksum of the sheet rows equals the dashboard list. Region amounts now: Gotland 26, Västernorrland 40, Jämtland 40, Västerbotten 54, Norrbotten 56.

## Decisions taken in this run (same strict line as before)
- Hours published only week by week (swim halls, ice rinks) → not published; a recurring event would show hours nobody has promised.
- Ski hills and summer places whose 2026/27 or 2027 season is not on any official page (or only on Facebook) → not published. Announced seasons are used as published (e.g. Björkliden 4 Feb–2 May 2027, Riksgränsen 18 Feb–23 May 2027, Storklinten weekends 5 Dec–28 Feb, Kåbdalis 23 Dec–10 Jan).
- Nature places with no official statement about winter access are published for the snow-free season only (Skuleskogen north/south, Hoverberget, Hällingsåfallet, Brännaberget: 1 May–31 Oct 2027; Fatmomakke and Kengisforsen: 1 Jun–30 Sep 2027; Fjällbotaniska trädgården 15 Jun–15 Sep 2027).
- Places closed part of the year for a known reason end before the closure (Havremagasinet Boden: ends 31 Jan 2027, closed installation weeks 5–6).
- Mobile numbers are not used as organizer/venue phone even when they are the only number on the site (Havremagasinet, Ivars Bilmuseum).
- O'Learys Umeå was opened in a normal browser: the live page has no regular hours → skipped. O'Learys Luleå: 18+ evenings, bowling has start times only → skipped.
- Two places whose photos the image proxy could not fetch (Ivars Bilmuseum, Röbäcks 4H-gård) were published with the same official photos downloaded and cropped locally.

## Per region
| Region | In the file | Already in the app | Published now | Skipped |
|---|---|---|---|---|
| Gotland | 50 | 2 | **24** | 24 |
| Västernorrland | 61 | 4 | **36** | 21 |
| Jämtland | 76 | 4 | **38** | 35 |
| Västerbotten | 82 | 5 | **49** | 28 |
| Norrbotten | 85 | 7 | **49** | 29 |
| **Total** | 354 | 22 | **196** | 137 |

## Published places
| Region | Kommun | Place | Event window | Period | Free | Season | Event ID |
|---|---|---|---|---|---|---|---|
| Gotland | Gotland | Bergmancenter | alla dagar 11:00–17:00 | 2027-06-01 → 2027-08-30 | nej | kopierad 2026 | 497410260261176927 |
| Gotland | Gotland | Bläse Kalkbruk | alla dagar 10:30–16:00 | 2027-06-13 → 2027-08-16 | nej | kopierad 2026 | 497409968220177990 |
| Gotland | Gotland | Bungemuseet | alla dagar 11:00–16:00 | 2027-06-01 → 2027-08-31 | nej | kopierad 2026 | 497409895323174465 |
| Gotland | Gotland | Etelhems Krukmakeri | alla dagar 10:00–18:00 | 2027-06-01 → 2027-08-31 | nej |  | 497414291566135052 |
| Gotland | Gotland | Fenomenalen Science Center | tor, fre, lör, sön 12:00–16:00 | 2026-11-18 → 2027-06-13 | nej |  | 497415891525338965 |
| Gotland | Gotland | Fornsalen – Gotlands Museum | alla dagar 11:00–16:00 | 2026-11-18 → 2027-12-31 | nej |  | 497412323305096910 |
| Gotland | Gotland | Gotlands Fiskerimuseum Kovik | alltid öppet | 2026-11-18 → 2027-12-31 | ja |  | 497414351385298707 |
| Gotland | Gotland | Gotlands Försvarsmuseum | mån, tis, ons, tor, fre, lör 10:00–15:00 | 2027-06-28 → 2027-08-07 | nej | kopierad 2026 | 497410049069581900 |
| Gotland | Gotland | Gotlands Hesselby Jernväg – Hesselby station | sön 11:00–15:15 | 2027-06-06 → 2027-08-29 | nej |  | 497410423167944299 |
| Gotland | Gotland | Högt & Lågt klätterpark Klintehamn | alla dagar 10:00–17:00 | 2027-06-20 → 2027-08-16 | nej | kopierad 2026 | 497410680480106105 |
| Gotland | Gotland | Kotteland lekland | alla dagar 10:00–18:00 | 2026-11-18 → 2027-12-31 | nej |  | 497412575189829341 |
| Gotland | Gotland | Kulturreservatet Norrbys museigård | alla dagar 11:00–17:00 | 2027-06-22 → 2027-08-09 | nej | kopierad 2026 | 497410766127793792 |
| Gotland | Gotland | Naturum Gotland | tis, ons, tor, fre, lör, sön 11:00–16:00 | 2027-05-01 → 2027-09-30 | ja |  | 497414142852892415 |
| Gotland | Gotland | Petes museigård | alla dagar 11:00–17:00 | 2027-06-19 → 2027-08-09 | nej | kopierad 2026 | 497414058891314936 |
| Gotland | Gotland | Roma Kungsgård | tor, fre, lör, sön 10:00–16:00 | 2026-11-18 → 2026-12-20 | ja |  | 497410587936982642 |
| Gotland | Gotland | S:ta Karins kyrkoruin | alla dagar 09:00–17:00 | 2027-05-01 → 2027-10-04 | nej | kopierad 2026 | 497413908173194994 |
| Gotland | Gotland | Stavgard Vikingagård | alla dagar 11:00–16:00 | 2027-06-26 → 2027-08-08 | nej | kopierad 2026 | 497414213686298373 |
| Gotland | Gotland | Stora Karlsö – båten från Klintehamns hamn | alla dagar 09:30–15:00 | 2027-05-06 → 2027-08-29 | nej |  | 497410327235823204 |
| Gotland | Gotland | Tingstäde fästning | alla dagar 11:00–16:00 | 2027-06-28 → 2027-08-22 | nej | kopierad 2026 | 497410111606654547 |
| Gotland | Gotland | Uncle Joes nöjescenter | alla dagar 12:00–18:00 | 2026-11-18 → 2027-12-31 | nej |  | 497412478997661398 |
| Gotland | Gotland | Visby domkyrka Sankta Maria | alla dagar 09:00–17:00 | 2026-11-18 → 2027-12-31 | nej |  | 497412850596218603 |
| Gotland | Gotland | Visby ringmur – världsarvet Hansestaden Visby | alltid öppet | 2026-11-18 → 2027-12-31 | ja |  | 497415934877665115 |
| Gotland | Gotland | Visbytåget – avgång Inre hamnen | alla dagar 10:30–17:55 | 2027-07-04 → 2027-08-13 | nej | kopierad 2026 | 497412723928237796 |
| Gotland | Gotland | Äventyrsgolf på Sudersand Resort | alla dagar 10:00–18:00 | 2027-06-07 → 2027-09-05 | nej | kopierad 2026 | 497410194049893978 |
| Västernorrland | Härnösand | Härnösands Bilmuseum | alla dagar 11:00–17:00 | 2027-06-13 → 2027-08-31 | nej | kopierad 2026 | 497411438810269353 |
| Västernorrland | Härnösand | Härnösands Golf & Glass | alla dagar 12:00–18:00 | 2027-05-01 → 2027-09-30 | nej | kopierad 2026 | 497411612722890413 |
| Västernorrland | Härnösand | Härnösands Simhall | alla dagar 11:30–14:30 | 2026-11-18 → 2027-12-31 | nej |  | 497411247927494302 |
| Västernorrland | Härnösand | Parkaden Bowling | mån, tis, tor, fre, lör 15:00–21:00 | 2026-11-18 → 2027-05-31 | nej |  | 497411712203392689 |
| Västernorrland | Härnösand | Västernorrlands museum och Murberget friluftsmuseum | tis, ons, tor, fre, lör, sön 10:00–16:00 | 2026-11-18 → 2027-12-31 | ja |  | 497411307302061730 |
| Västernorrland | Kramfors | Hornöberget vid Högakustenbron | alltid öppet | 2026-11-18 → 2027-12-31 | ja |  | 497411365133125285 |
| Västernorrland | Kramfors | Mannaminne | alla dagar 12:00–18:00 | 2027-05-30 → 2027-08-31 | nej | kopierad 2026 | 497415426460911424 |
| Västernorrland | Kramfors | Skulebergets Linbana | alla dagar 10:00–16:00 | 2027-06-01 → 2027-08-31 | nej | kopierad 2026 | 497415352632772413 |
| Västernorrland | Kramfors | Skuleskogens nationalpark, Entré Syd | alltid öppet | 2027-05-01 → 2027-10-31 | ja |  | 497415477673363266 |
| Västernorrland | Kramfors | Ådalshallen | mån, tis, ons, tor, fre 15:00–18:00 | 2026-11-18 → 2027-12-31 | nej |  | 497411179895883419 |
| Västernorrland | Sollefteå | Hallsta ski – Hallstabacken | alla dagar 14:00–17:00 | 2026-12-18 → 2027-04-08 | nej |  | 497415579628504902 |
| Västernorrland | Sollefteå | Junsele Djurpark | alla dagar 10:00–16:00 | 2027-06-21 → 2027-08-16 | nej | kopierad 2026 | 497411817354593973 |
| Västernorrland | Sollefteå | Nämforsens Hällristningsmuseum | tis, ons, tor, fre, lör, sön 10:30–17:15 | 2027-06-15 → 2027-08-15 | ja | kopierad 2026 | 497411897675515576 |
| Västernorrland | Sollefteå | Risöbadet | alla dagar 10:00–18:30 | 2027-06-28 → 2027-08-15 | nej | kopierad 2026 | 497415528172783428 |
| Västernorrland | Sollefteå | Sollefteå Aquarena | alla dagar 10:00–16:00 | 2026-11-18 → 2027-12-31 | nej |  | 497411963911964347 |
| Västernorrland | Sundsvall | Enjoy Bowling | alla dagar 14:00–17:00 | 2026-11-18 → 2027-12-31 | nej |  | 497414440740751129 |
| Västernorrland | Sundsvall | Gudmundstjärn naturreservat och kulturmiljö | alltid öppet | 2026-11-18 → 2027-12-31 | ja |  | 497414626128987939 |
| Västernorrland | Sundsvall | Himlabadet | alla dagar 10:00–18:00 | 2026-11-18 → 2027-12-31 | nej |  | 497410847858001543 |
| Västernorrland | Sundsvall | JumpYard Sundsvall | alla dagar 10:00–19:00 | 2026-11-18 → 2027-12-31 | nej |  | 497410980490282639 |
| Västernorrland | Sundsvall | Leo's Lekland Sundsvall | alla dagar 10:00–19:00 | 2026-11-18 → 2027-12-31 | nej |  | 497410918506858123 |
| Västernorrland | Sundsvall | Strike Club | alla dagar 14:00–19:00 | 2026-11-18 → 2027-12-31 | nej |  | 497411116402509463 |
| Västernorrland | Sundsvall | Sundsvalls Klätterhall | alla dagar 10:00–18:00 | 2026-11-18 → 2027-12-31 | nej |  | 497411053664110227 |
| Västernorrland | Sundsvall | Sundsvalls museum i Kulturmagasinet | alla dagar 11:00–16:00 | 2026-11-18 → 2027-12-31 | ja |  | 497414506431940380 |
| Västernorrland | Sundsvall | Svartviks industriminnen | alltid öppet | 2026-11-18 → 2027-12-31 | ja |  | 497414565336745759 |
| Västernorrland | Timrå | Skeppshamn – Åstöns naturreservat | alltid öppet | 2026-11-18 → 2027-12-31 | ja |  | 497415832394041169 |
| Västernorrland | Timrå | Timrå simhall | mån, tis, ons, tor, fre 13:00–19:30 | 2026-11-18 → 2027-05-31 | nej |  | 497415762634377038 |
| Västernorrland | Ånge | Ljungandalens Bad & Sport | tis, tor, fre 17:00–20:00 | 2026-11-18 → 2027-12-31 | nej |  | 497415645814622025 |
| Västernorrland | Ånge | Slalombacke Getberget | lör, sön 10:00–15:00 | 2026-12-26 → 2027-03-28 | nej | kopierad 2026 | 497415696137881419 |
| Västernorrland | Örnsköldsvik | Aktivator Park | alla dagar 10:00–17:00 | 2027-06-20 → 2027-08-23 | nej | kopierad 2026 | 497414872846337837 |
| Västernorrland | Örnsköldsvik | Bjästabacken | lör, sön 10:00–16:00 | 2026-12-25 → 2027-03-14 | nej | kopierad 2026 | 497415272395736890 |
| Västernorrland | Örnsköldsvik | City Games Örnsköldsvik | tis, ons, tor, fre, lör 14:00–21:00 | 2026-11-18 → 2027-12-31 | nej |  | 497414788549216042 |
| Västernorrland | Örnsköldsvik | Skuleskogens nationalpark – Entré Nord | alltid öppet | 2027-05-01 → 2027-10-31 | ja |  | 497415168284722999 |
| Västernorrland | Örnsköldsvik | Varvsberget utsiktsplats | alltid öppet | 2026-11-18 → 2027-12-31 | ja |  | 497414988835620658 |
| Västernorrland | Örnsköldsvik | Äventyrens Hus – Baazinga Lekland | alla dagar 11:00–16:00 | 2026-11-18 → 2027-12-31 | nej |  | 497414711021700903 |
| Västernorrland | Örnsköldsvik | Örnsköldsviks Minigolfbana | alla dagar 12:00–19:00 | 2027-05-11 → 2027-08-23 | nej | kopierad 2026 | 497415113297397557 |
| Västernorrland | Örnsköldsvik | Örnsköldsviks museum och konsthall | tis, ons, tor, fre, lör 12:00–16:00 | 2026-11-18 → 2027-12-31 | ja |  | 497414940978612016 |
| Jämtland | Berg | Hoverberget naturreservat | alltid öppet | 2027-05-01 → 2027-10-31 | ja |  | 497416981071300492 |
| Jämtland | Berg | Klövsjö/Storhogna skidområde | alla dagar 09:00–15:00 | 2026-12-18 → 2027-04-04 | nej |  | 497417030111102863 |
| Jämtland | Bräcke | Brattbytorpet | fre, lör, sön 11:00–15:00 | 2027-06-19 → 2027-08-16 | nej | kopierad 2026 | 497417441480050594 |
| Jämtland | Härjedalen | Funäsdalsberget & Funäsgondolen | alla dagar 09:00–15:00 | 2026-12-18 → 2027-04-18 | nej |  | 497416283692762991 |
| Jämtland | Härjedalen | Lofsdalen skidanläggning | alla dagar 09:00–16:00 | 2026-12-11 → 2027-04-11 | nej |  | 497418167639902145 |
| Jämtland | Härjedalen | Lopme Laante – samisk park på Funäsdalsberget | alla dagar 10:00–15:30 | 2027-07-01 → 2027-08-16 | nej | kopierad 2026 | 497417947623491512 |
| Jämtland | Härjedalen | Ramundberget skidområde | alla dagar 09:00–15:00 | 2026-12-19 → 2027-04-11 | nej |  | 497418023683000251 |
| Jämtland | Härjedalen | SkiStar Vemdalen – Björnrike | alla dagar 09:00–15:00 | 2026-12-18 → 2027-04-11 | nej |  | 497416209461970796 |
| Jämtland | Härjedalen | SkiStar Vemdalen – Vemdalsskalet | alla dagar 09:00–15:00 | 2026-12-18 → 2027-04-18 | nej |  | 497416159491032938 |
| Jämtland | Härjedalen | Sonfjällets nationalpark – entré Nyvallen | alltid öppet | 2027-06-25 → 2027-09-30 | ja | kopierad 2026 | 497418226620204995 |
| Jämtland | Härjedalen | Svegsbadet | tis, ons, tor, fre, lör, sön 11:00–15:30 | 2026-11-18 → 2027-12-31 | nej |  | 497416350373807986 |
| Jämtland | Härjedalen | Tänndalen skidområde | alla dagar 09:00–15:00 | 2026-12-19 → 2027-04-18 | nej |  | 497418092293425086 |
| Jämtland | Krokom | Almåsa Alpin | lör, sön 11:00–15:00 | 2026-12-20 → 2027-03-23 | nej | kopierad 2026 | 497417167826880406 |
| Jämtland | Krokom | Glösa Älgriket | alltid öppet | 2026-11-18 → 2027-12-31 | ja |  | 497417102236354450 |
| Jämtland | Ragunda | Döda fallet naturreservat | alltid öppet | 2027-05-01 → 2027-10-31 | ja |  | 497417244767192985 |
| Jämtland | Ragunda | Inomhusbadet i Stugun | tor 16:30–19:00 | 2026-11-18 → 2027-04-24 | nej |  | 497417382029985694 |
| Jämtland | Ragunda | Thailändska Paviljongen | alla dagar 10:00–16:00 | 2027-05-31 → 2027-08-29 | nej |  | 497417326019250076 |
| Jämtland | Strömsund | Hällingsåfallets naturreservat | alltid öppet | 2027-05-01 → 2027-10-31 | ja |  | 497418343423182789 |
| Jämtland | Strömsund | Ivars Bilmuseum | alla dagar 10:00–17:00 | 2027-06-01 → 2027-08-29 | nej |  | 497431015262815494 |
| Jämtland | Strömsund | Lusthuset & Yxskaftkälens Järnvägar | alla dagar 10:00–18:00 | 2027-07-04 → 2027-08-09 | nej | kopierad 2026 | 497418443465721800 |
| Jämtland | Åre | Bydalsfjällen | alla dagar 10:00–16:00 | 2026-12-19 → 2027-04-18 | nej | kopierad 2026 | 497416013638305634 |
| Jämtland | Åre | Fröå gruva kulturreservat | alltid öppet | 2026-11-18 → 2027-12-31 | ja |  | 497417866186885044 |
| Jämtland | Åre | Holiday Club Åre – Aktivitetsbad & Saunaworld | alla dagar 10:00–21:00 | 2026-11-18 → 2027-12-31 | nej |  | 497412032010684094 |
| Jämtland | Åre | JumpYard Åre | alla dagar 10:00–18:00 | 2026-11-18 → 2027-12-31 | nej |  | 497417515702454182 |
| Jämtland | Åre | Ristafallet | alltid öppet | 2026-11-18 → 2027-12-31 | ja |  | 497417776084846513 |
| Jämtland | Åre | SkiStar Åre – Duved & Tegefjäll skidområde | alla dagar 09:30–15:00 | 2026-12-18 → 2027-04-04 | nej |  | 497412186151356104 |
| Jämtland | Åre | SkiStar Åre – Åre Björnen skidområde | alla dagar 09:30–15:00 | 2026-12-18 → 2027-04-11 | nej |  | 497412137447098053 |
| Jämtland | Åre | SkiStar Åre – Åre by skidområde | alla dagar 09:30–15:00 | 2026-12-11 → 2027-05-02 | nej |  | 497412088340186818 |
| Jämtland | Åre | Trillevallens skidområde | alla dagar 09:30–15:00 | 2026-12-19 → 2027-04-11 | nej |  | 497416093355247462 |
| Jämtland | Åre | Tännforsen naturreservat | alltid öppet | 2026-11-18 → 2027-12-31 | nej |  | 497417676134582189 |
| Jämtland | Åre | Åre Bike Park | fre, lör, sön 10:00–16:00 | 2027-06-05 → 2027-09-27 | nej | kopierad 2026 | 497412242648630987 |
| Jämtland | Åre | Åre Klätterhall | alla dagar 11:00–19:00 | 2026-11-18 → 2027-12-31 | nej |  | 497417613345851306 |
| Jämtland | Östersund | Gustavsbergsbacken och Silverling | tis, ons, fre, lör, sön 10:00–16:00 | 2026-12-25 → 2027-04-11 | nej | kopierad 2026 | 497416758253094788 |
| Jämtland | Östersund | Multi Challenge | ons, tor, fre, lör, sön 10:00–16:00 | 2026-11-18 → 2027-12-31 | nej |  | 497416495656109945 |
| Jämtland | Östersund | Sommarhagen | alla dagar 11:00–16:00 | 2027-06-15 → 2027-08-16 | nej | kopierad 2026 | 497416702485628801 |
| Jämtland | Östersund | Storsjöbadet | alla dagar 10:00–18:00 | 2026-11-18 → 2027-12-31 | nej |  | 497416425661564789 |
| Jämtland | Östersund | Teknikland | alla dagar 10:00–16:00 | 2027-06-22 → 2027-08-16 | nej | kopierad 2026 | 497416616611448701 |
| Jämtland | Östersund | Östersunds Klättercenter | alla dagar 11:30–17:00 | 2026-11-18 → 2027-12-31 | nej |  | 497416902268716936 |
| Västerbotten | Bjurholm | Älgens Hus | tis, ons, tor, fre, lör, sön 11:00–17:00 | 2027-06-08 → 2027-08-15 | nej | kopierad 2026 | 497421810652972076 |
| Västerbotten | Dorotea | Borgafjällbackarna | fre, lör, sön 09:30–16:00 | 2026-12-11 → 2027-04-25 | nej |  | 497422901130069081 |
| Västerbotten | Dorotea | Husvagnsmuseet i Dorotea | mån, tis, ons, tor, fre, lör 13:00–16:00 | 2027-06-15 → 2027-08-15 | nej | kopierad 2026 | 497420955325334534 |
| Västerbotten | Lycksele | Ansia Badpark | alla dagar 12:00–16:30 | 2027-06-22 → 2027-08-09 | nej | kopierad 2026 | 497422787581871190 |
| Västerbotten | Lycksele | Skogs- och samemuseet på Gammplatsen | tis, ons, tor, fre, sön 12:00–16:00 | 2026-11-18 → 2027-12-31 | nej |  | 497422727670432851 |
| Västerbotten | Malå | Tjamstanbackarna | lör, sön 10:00–16:00 | 2026-12-19 → 2027-04-04 | nej |  | 497421876520322096 |
| Västerbotten | Nordmaling | Olofsfors Bruk | tis, ons, tor, fre, lör, sön 11:00–16:00 | 2027-06-15 → 2027-08-15 | nej | kopierad 2026 | 497421944795202611 |
| Västerbotten | Norsjö | Norsjö hembygdsområde | alla dagar 12:00–16:00 | 2027-06-15 → 2027-08-09 | ja | kopierad 2026 | 497422021358027831 |
| Västerbotten | Robertsfors | Robertsfors Bruksmuseum | ons, tor, fre, lör, sön 11:00–16:00 | 2027-06-06 → 2027-08-23 | nej | kopierad 2026 | 497422096184411194 |
| Västerbotten | Skellefteå | Boda Borg Skellefteå | tis, ons, tor, fre, lör, sön 12:00–17:00 | 2026-11-18 → 2027-12-31 | nej |  | 497427681210565774 |
| Västerbotten | Skellefteå | Bonnstan – Skellefteå kyrkstad | alltid öppet | 2026-11-18 → 2027-12-31 | ja |  | 497421372658582554 |
| Västerbotten | Skellefteå | Bowlingkompaniet | alla dagar 13:00–21:00 | 2026-11-18 → 2027-12-31 | nej |  | 497420659232638970 |
| Västerbotten | Skellefteå | Eddaparkens Äventyrsgolf (Skellefteå Bangolfklubb) | alla dagar 10:00–22:00 | 2027-06-15 → 2027-08-16 | nej | kopierad 2026 | 497420898467349506 |
| Västerbotten | Skellefteå | Exploratoriet – Science Center i Skellefteå | mån, fre, lör, sön 13:00–16:00 | 2026-11-18 → 2027-12-31 | nej |  | 497427559382811782 |
| Västerbotten | Skellefteå | LEGO-museet på Bureå Camping | alla dagar 11:00–15:00 | 2027-06-13 → 2027-08-16 | nej | kopierad 2026 | 497421257516549139 |
| Västerbotten | Skellefteå | Leo's Lekland Skellefteå | alla dagar 10:00–19:00 | 2026-11-18 → 2027-12-31 | nej |  | 497427617952072842 |
| Västerbotten | Skellefteå | Sara kulturhus | alla dagar 10:00–16:00 | 2026-11-18 → 2027-12-31 | ja |  | 497421319307035671 |
| Västerbotten | Skellefteå | Skellefteå Adventurepark | alla dagar 10:00–17:00 | 2027-06-22 → 2027-08-16 | nej | kopierad 2026 | 497420798332536830 |
| Västerbotten | Skellefteå | Trampolinhuset Skellefteå | tis, ons, tor, fre, lör, sön 14:00–17:00 | 2026-11-18 → 2027-12-31 | nej |  | 497420583911327734 |
| Västerbotten | Skellefteå | WasteLand – Skellefteå Climate Action Park | alla dagar 06:00–23:59 | 2026-11-18 → 2027-12-31 | ja |  | 497421426664440861 |
| Västerbotten | Sorsele | Nalovardo skidanläggning | lör, sön 10:00–16:00 | 2026-12-12 → 2027-04-18 | nej |  | 497421108249658380 |
| Västerbotten | Sorsele | Potatisbacken i Ammarnäs | alltid öppet | 2026-11-18 → 2027-12-31 | ja |  | 497421031938491401 |
| Västerbotten | Storuman | Fjällbotaniska trädgården i Hemavan | alltid öppet | 2027-06-15 → 2027-09-15 | ja |  | 497422336056656963 |
| Västerbotten | Storuman | Hemavan Alpint – skidområdet i Hemavan | alla dagar 10:00–16:00 | 2026-12-18 → 2027-05-02 | nej |  | 497421491768427553 |
| Västerbotten | Storuman | Naturum Vindelfjällen Hemavan | alla dagar 09:00–16:00 | 2027-06-22 → 2027-08-15 | ja | kopierad 2026 | 497422255039480896 |
| Västerbotten | Storuman | Tärnaby Alpint – Ingemarbacken | alla dagar 09:00–16:00 | 2026-11-18 → 2027-04-30 | nej |  | 497422192804398142 |
| Västerbotten | Storuman | Utsikten Storuman | alltid öppet | 2026-11-18 → 2027-12-31 | ja |  | 497422400489555014 |
| Västerbotten | Umeå | Bildmuseet | ons, tor, fre, lör, sön 12:00–17:00 | 2026-11-18 → 2027-12-31 | ja |  | 497420071660980190 |
| Västerbotten | Umeå | Gokart Umeå – Alvik Ring | alla dagar 13:00–18:00 | 2027-06-12 → 2027-08-16 | nej | kopierad 2026 | 497420496787245042 |
| Västerbotten | Umeå | Guitars – The Museum | mån, tis, ons, tor, fre, lör 12:00–16:00 | 2026-11-18 → 2027-12-31 | nej |  | 497420146512529378 |
| Västerbotten | Umeå | Holmöns båtmuseum | alla dagar 10:45–17:00 | 2027-06-13 → 2027-08-16 | nej | kopierad 2026 | 497420354138965994 |
| Västerbotten | Umeå | IKSU sport | alla dagar 07:45–21:00 | 2026-11-18 → 2027-12-31 | nej |  | 497418879262296026 |
| Västerbotten | Umeå | Leo's Lekland Umeå | alla dagar 10:00–19:00 | 2026-11-18 → 2027-12-31 | nej |  | 497418722655373266 |
| Västerbotten | Umeå | Megazone Umeå | alla dagar 13:00–20:00 | 2026-11-18 → 2027-12-31 | nej |  | 497418807069935574 |
| Västerbotten | Umeå | Navet | alla dagar 13:00–18:00 | 2026-11-18 → 2027-12-31 | nej |  | 497418521462998987 |
| Västerbotten | Umeå | Norrbyskärs museum | alla dagar 10:00–15:00 | 2027-06-13 → 2027-08-16 | nej | kopierad 2026 | 497420247167436774 |
| Västerbotten | Umeå | Röbäcks 4H-gård | mån, tis, ons 14:00–20:00 | 2026-11-18 → 2026-12-31 | ja |  | 497431067649672457 |
| Västerbotten | Umeå | Umedalens skulpturpark | alltid öppet | 2026-11-18 → 2027-12-31 | ja |  | 497427415644013694 |
| Västerbotten | Umeå | Umelagun | alla dagar 10:00–19:00 | 2027-06-10 → 2027-08-15 | nej | kopierad 2026 | 497418659136833486 |
| Västerbotten | Umeå | Umeå Bangolfklubb – bangolfbanorna i Hedlundadungen | alla dagar 12:00–21:00 | 2027-06-22 → 2027-08-30 | nej | kopierad 2026 | 497427494555649154 |
| Västerbotten | Umeå | Umeå Energicentrum | alla dagar 10:00–17:00 | 2027-06-15 → 2027-08-15 | ja | kopierad 2026 | 497427341404832890 |
| Västerbotten | Umeå | Zip Adventure Park Umeå | alla dagar 11:00–18:00 | 2027-06-12 → 2027-08-16 | nej | kopierad 2026 | 497420426801088494 |
| Västerbotten | Vilhelmina | Fatmomakke kyrkstad | alltid öppet | 2027-06-01 → 2027-09-30 | ja |  | 497422647936713808 |
| Västerbotten | Vilhelmina | Kittelfjällsliftarna | alla dagar 09:00–16:00 | 2026-12-18 → 2027-04-11 | nej |  | 497422460057060425 |
| Västerbotten | Vilhelmina | Kyrkstan i Vilhelmina | alltid öppet | 2026-11-18 → 2027-12-31 | ja |  | 497422534405293132 |
| Västerbotten | Vilhelmina | Vilhelmina simhall | tis, tor, fre 16:00–18:30 | 2026-11-18 → 2027-12-31 | nej |  | 497422587672953934 |
| Västerbotten | Vindeln | Vindelns simhall | sön 11:00–15:00 | 2026-11-18 → 2027-04-30 | nej |  | 497421182161683471 |
| Västerbotten | Vännäs | Vännäs Motormuseum | alla dagar 12:00–16:00 | 2027-06-28 → 2027-08-15 | nej | kopierad 2026 | 497421650430559272 |
| Västerbotten | Vännäs | Vännäsbadet | alla dagar 11:00–18:30 | 2027-06-17 → 2027-08-22 | nej | kopierad 2026 | 497421564095005732 |
| Norrbotten | Arjeplog | Galtis skidanläggning | lör, sön 10:00–16:00 | 2026-12-27 → 2027-04-25 | nej |  | 497423272460190824 |
| Norrbotten | Arjeplog | Jäckvik Fjällcenter | fre, lör, sön 10:00–16:00 | 2027-01-29 → 2027-04-25 | nej | kopierad 2026 | 497423346212832363 |
| Norrbotten | Arjeplog | Silvermuseet | tis, ons, tor, fre 12:30–16:00 | 2026-11-18 → 2027-12-31 | nej |  | 497430223260779750 |
| Norrbotten | Arvidsjaur | Lappstaden i Arvidsjaur | alltid öppet | 2026-11-18 → 2027-12-31 | ja |  | 497430755752838397 |
| Norrbotten | Arvidsjaur | Sparbanken Nord sport- och simhall | lör, sön 12:00–16:00 | 2026-11-18 → 2027-12-31 | nej |  | 497430850795767040 |
| Norrbotten | Boden | Försvarsmuseum Boden | ons, tor, fre, lör, sön 11:00–16:00 | 2026-11-18 → 2027-12-31 | nej |  | 497430026178823386 |
| Norrbotten | Boden | Havremagasinet länskonsthall | ons, tor, fre, lör, sön 12:00–16:00 | 2026-11-18 → 2027-01-31 | nej |  | 497430098991940830 |
| Norrbotten | Boden | Rödbergsfortet | alla dagar 10:00–16:00 | 2027-06-23 → 2027-08-22 | nej | kopierad 2026 | 497429947644675286 |
| Norrbotten | Boden | Storklinten | lör, sön 10:00–16:00 | 2026-12-05 → 2027-02-28 | nej |  | 497430162393040098 |
| Norrbotten | Gällivare | Dundret Gällivare | lör, sön 10:00–16:00 | 2026-12-05 → 2027-05-02 | nej |  | 497423411065160814 |
| Norrbotten | Gällivare | Naturum Laponia | ons, tor, fre, lör, sön 10:00–18:00 | 2027-04-01 → 2027-09-27 | ja | kopierad 2026 | 497427202019722356 |
| Norrbotten | Gällivare | Sjöparksbadet | alla dagar 13:00–17:00 | 2026-11-18 → 2027-12-31 | nej |  | 497423488013862001 |
| Norrbotten | Haparanda | Simhallen Aspen Haparanda | tis, ons, tor, fre 16:00–20:00 | 2026-11-18 → 2027-12-31 | nej |  | 497430954638345475 |
| Norrbotten | Jokkmokk | Kåbdalis Skidliftar | alla dagar 10:00–16:00 | 2026-12-23 → 2027-01-10 | nej |  | 497430340139255019 |
| Norrbotten | Jokkmokk | Ájtte Fjällträdgård | alla dagar 10:00–17:00 | 2027-06-08 → 2027-08-30 | ja | kopierad 2026 | 497430277996446952 |
| Norrbotten | Kalix | Kalix SportCity – badet | mån, tis, ons, tor, fre 14:00–17:00 | 2026-11-18 → 2027-12-31 | nej |  | 497427277550748791 |
| Norrbotten | Kalix | Siknäsfortet | ons, tor, fre, lör, sön 11:00–16:00 | 2027-06-24 → 2027-08-30 | nej | kopierad 2026 | 497430486268806384 |
| Norrbotten | Kalix | Vassholmen – flottningsmuseum och Café Flottaren | alla dagar 10:00–15:00 | 2027-07-01 → 2027-09-06 | nej | kopierad 2026 | 497430404999972077 |
| Norrbotten | Kiruna | Björkliden skidområde | alla dagar 10:00–16:00 | 2027-02-04 → 2027-05-02 | nej |  | 497429445376771266 |
| Norrbotten | Kiruna | Esrange Visitor Center | alla dagar 08:00–18:00 | 2026-11-18 → 2027-12-31 | nej |  | 497429313432356028 |
| Norrbotten | Kiruna | ICEHOTEL Jukkasjärvi | alla dagar 11:00–18:00 | 2026-11-18 → 2027-04-10 | nej |  | 497422969681773660 |
| Norrbotten | Kiruna | Kin museum för samtidskonst | tis, ons, tor, fre, lör 12:00–16:00 | 2026-11-18 → 2027-12-31 | nej |  | 497423193682773093 |
| Norrbotten | Kiruna | Midnattssolsbadet | tis, ons, tor, fre, lör, sön 11:00–17:30 | 2026-11-18 → 2027-12-31 | nej |  | 497423125835711586 |
| Norrbotten | Kiruna | Márkanbáiki – samiskt friluftsmuseum | alla dagar 10:00–16:00 | 2026-11-18 → 2027-12-31 | nej |  | 497423051554587743 |
| Norrbotten | Kiruna | Riksgränsen skidområde | alla dagar 09:00–16:00 | 2027-02-18 → 2027-05-23 | nej |  | 497429519683060933 |
| Norrbotten | Kiruna | STF Aurora Sky Station – linbanan på Nuolja | alla dagar 09:30–16:00 | 2027-06-12 → 2027-09-20 | nej | kopierad 2026 | 497429379249374399 |
| Norrbotten | Luleå | 360 Trampoline Center | tis, ons, tor, fre, lör, sön 14:00–19:00 | 2026-11-18 → 2027-12-31 | nej |  | 497428885445575851 |
| Norrbotten | Luleå | Arcusbadet | alla dagar 10:00–17:00 | 2027-06-19 → 2027-08-09 | nej | kopierad 2026 | 497429189557781686 |
| Norrbotten | Luleå | Flygmuseet F 21 | tor 10:00–16:00 | 2026-11-18 → 2026-12-17 | nej |  | 497427849771254933 |
| Norrbotten | Luleå | Friluftsmuseet Hägnan | alltid öppet | 2026-11-18 → 2027-12-31 | ja |  | 497429256205272248 |
| Norrbotten | Luleå | Hertsö badhus | mån, fre, lör, sön 11:00–15:30 | 2026-11-18 → 2027-05-02 | nej |  | 497429075548210355 |
| Norrbotten | Luleå | Klätterhuset | alla dagar 11:00–16:00 | 2026-11-18 → 2027-12-31 | nej |  | 497428959785419951 |
| Norrbotten | Luleå | Kulturens hus | alla dagar 12:00–16:00 | 2026-11-18 → 2027-12-31 | ja |  | 497427769651659922 |
| Norrbotten | Luleå | Leo's Lekland Luleå | alla dagar 10:00–19:00 | 2026-11-18 → 2027-12-31 | nej |  | 497428815174206631 |
| Norrbotten | Luleå | Norrbottens Järnvägsmuseum | mån, tis, ons, tor, fre 10:00–16:00 | 2027-06-22 → 2027-08-14 | nej | kopierad 2026 | 497427925939815576 |
| Norrbotten | Luleå | Ormbergets friluftsområde | alltid öppet | 2026-11-18 → 2027-12-31 | nej |  | 497428067329803420 |
| Norrbotten | Luleå | Pontusbadet | alla dagar 12:00–15:30 | 2026-11-18 → 2027-06-06 | nej |  | 497429015401890993 |
| Norrbotten | Luleå | Turbåtarna i Luleå skärgård – Södra hamnplan | alla dagar 09:15–16:40 | 2027-06-19 → 2027-08-16 | nej | kopierad 2026 | 497428005581259930 |
| Norrbotten | Pajala | Kengisforsen | alltid öppet | 2027-06-01 → 2027-09-30 | ja |  | 497430563116844276 |
| Norrbotten | Piteå | Norrstrands pool & camping | alla dagar 10:00–18:00 | 2027-06-13 → 2027-08-09 | nej | kopierad 2026 | 497429789083206864 |
| Norrbotten | Piteå | Piteå museum | tis, ons, tor, fre 13:00–16:00 | 2026-11-18 → 2027-12-31 | nej |  | 497429593267930312 |
| Norrbotten | Piteå | Swensbylijda | alltid öppet | 2026-11-18 → 2027-12-31 | ja |  | 497429870175880403 |
| Norrbotten | Piteå | Öjeby kyrkstad | mån, tis, ons, tor, fre 10:00–17:00 | 2027-06-29 → 2027-07-31 | ja | kopierad 2026 | 497429668832511179 |
| Norrbotten | Piteå | Öjeby simhall | lör, sön 10:00–14:00 | 2026-11-18 → 2027-05-30 | nej |  | 497429740420891854 |
| Norrbotten | Älvsbyn | Bagerimuseet Älvsbyn | mån, tis, ons, tor, fre 10:00–16:00 | 2027-06-22 → 2027-07-31 | ja | kopierad 2026 | 497430702376125690 |
| Norrbotten | Älvsbyn | Älvsby Bowling – Forum Älvsbyn | mån, tis, tor, fre 15:00–19:00 | 2026-11-18 → 2027-12-31 | nej |  | 497430630242485495 |
| Norrbotten | Överkalix | Brännabergets utsiktsplats | alltid öppet | 2027-05-01 → 2027-10-31 | ja |  | 497428594528650399 |
| Norrbotten | Överkalix | Jockfallet | alltid öppet | 2026-11-18 → 2027-12-31 | ja |  | 497428673322845345 |
| Norrbotten | Övertorneå | Polcirkeln i Juoksengi | alltid öppet | 2026-11-18 → 2027-12-31 | ja |  | 497428737655080100 |

## Skipped places
| Region | Kommun | Place | Reason |
|---|---|---|---|
| Gotland | Gotland | Bottarve museigård | hours could not be verified on a current official page (own site blocks access; only an undated listing and a 2025 guide) |
| Gotland | Gotland | Båttur till Gotska Sandön (från Fårösund) | booking-only boat trip: tickets must be bought in advance via the booking service (no tickets on board) |
| Gotland | Gotland | Fängelsetornet Kajsarn (Kajsartornet) | no reliable season: page now says 'stängt för säsongen' with no reopening date; the summer hours text (ons–sön 10–15 t.o.m. 17 augusti) was an unchanged 2025 text with no start date; run by volunteer association with only a pri… |
| Gotland | Gotland | Fårö Krukmakeri | the family activities (ceramic painting, wheel-throwing) are booked online; only the shop and cafe are drop-in |
| Gotland | Gotland | Fårö Museum | official site has an expired SSL certificate and hours depend on volunteers; 2026 dates only from a third-party post - re-check before summer 2027 |
| Gotland | Gotland | Gangvidefarm | no published hours: pony riding (the only drop-in activity) says 'Tider för sommaren 2027 kommer snart'; paddling and tractor trips are booked activities |
| Gotland | Gotland | Gotland Gokart | no published hours: season closed ('Drop in har stängt för säsongen'); drop-in hours are only published week by week during the season and no 2027 season dates exist |
| Gotland | Gotland | Gotlands Djurpark | no published season hours: official Tider & priser page only lists scattered single days (e.g. 29-30 May, week 35 Friday 11-15) and refers to Facebook/Instagram; only a personal email on the site |
| Gotland | Gotland | Gotlands Veteranbilmuseum | no defined season/dates on official site: 'Varje dag: 12 - 16' but 'Vid lågsäsong: säkrast ring före besök' – opening now (Nov) is not confirmed, no season span published to restrict it to |
| Gotland | Gotland | Hemsebadet | public swim hours are published week by week only; only an exterior photo |
| Gotland | Gotland | Högt & Lågt Fårö | no real photo of this place on any official page (new 2026 park; site shows only chain-generic photos from other Högt & Lågt parks and a drawn park map) |
| Gotland | Gotland | Kokoloko minigolf & pool (First Hotel Kokoloko) | hotel facility: minigolf/pool are hotel amenities with no published public opening hours (pool for non-guests only June-mid-Sept, no hours); not a drop-in family place per brief (hotel/spa) |
| Gotland | Gotland | Kustparksbadet | no real photo of the swim hall on any official page (Gotlands IdrottsCenter site has only 880x200 banners of cottages; Region Gotland and gotland.com have no photos) |
| Gotland | Gotland | Lilla Karlsö | booking-only guided boat trip (pre-booking and payment at least 4 days ahead, max 6 people); no drop-in visit |
| Gotland | Gotland | Länsteatern på Gotland | theatre – performances only with booked tickets, no drop-in visit (not drop-in rule) |
| Gotland | Gotland | Solbergabadet | public swim hours are published week by week only (no fixed schedule to publish) |
| Gotland | Gotland | Stenkyrka Djurpark (B&M Gård) | hours unclear (site points to Facebook, may close in bad weather) and the address pin could not be verified |
| Gotland | Gotland | Suders Islandshästar | booking-only riding tours/lessons (contact by phone), no drop-in visit with published hours |
| Gotland | Gotland | Terra Nova utomhuspool | no official photo of the Terra Nova pool: the only pool photo on wisbysim.se is captioned 'Melonenbadet' (the sister pool), Gotlandshem pages show only housing; summer-only pool, season 2026 over |
| Gotland | Gotland | Tingstäde Kajak | booking-only self-service kayak rental (book and pay online, codes for lockers); no staffed drop-in and no opening hours published on the official site |
| Gotland | Gotland | Trampolinparken i Fårösund (GTTK Arena) | not drop-in: trampoline sessions are booked in advance via Bokadirekt (110-min pass), open only on weekends and school holidays with no published per-weekday hours; the club is also moving the park to a new hall in Visby (no op… |
| Gotland | Gotland | Visby Klätterklubb – klätterhallen i silon | hours unclear: club hall, deviations only in a Facebook group and access for non-members not stated |
| Gotland | Gotland | Visby ishall | public skating hours vary by week and the season end is not published; only one official photo |
| Gotland | Gotland | Äventyrsgolf på Slite Strand Resort | hours unclear: only the bar hours are published, not the minigolf/reception hours |
| Västernorrland | Härnösand | Hemsö fästning | Guided-tour-only site, currently closed to the public ('fortsatt stängt för allmänheten', tours 'Återupptas senare i höst'); no published tour times or season dates on the official site → no published hours |
| Västernorrland | Härnösand | Härnösands domkyrka | church with no published visiting hours and no drop-in family offer (official parish pages list no opening hours) |
| Västernorrland | Härnösand | Vårdkasbacken | no published hours: official site only says the hill traditionally opens 26 December depending on snow; no weekday lift hours on any official page |
| Västernorrland | Kramfors | Flogstabadet | No published hours: official kommun page only says 'Stängt för säsongen'; no 2026 season dates or weekday hours on kramfors.se or hogakusten.com, next season not announced |
| Västernorrland | Kramfors | Höga Kusten-båtarna – M/S Kusttrafik till Ulvön | Boat trip that must be booked: tickets are booked and paid online or by phone (no ticket sale on board mentioned); per brief booked boat trips → skip |
| Västernorrland | Kramfors | Högbonden – båttur med M/S Ronja | Boat trip that must be booked (same operator Höga Kusten-Båtarna, tickets booked/paid online or by phone); 2026 season over and no next-season timetable published |
| Västernorrland | Kramfors | Via Ferrata Skuleberget | no current published hours or season: the official site's start times are labelled 'STARTTIDER 2018' and it says exact opening dates are hard to give (weather-dependent). Also 40 kg minimum weight, minors only with guardian; se… |
| Västernorrland | Sundsvall | Drakstaden Skatepark | hours unclear/outdated: official site gives two conflicting schedules (sidebar Mon-Thu 17.30-21, page Mon-Thu 17-20) under a COVID-era note 'flexibla öppettider ... se facebook för aktuella tider'; site last updated years ago, … |
| Västernorrland | Sundsvall | Galtströms bruk | no current official page states access or hours (owner page only calls it an excursion destination; the destination site is unmaintained since 2022) |
| Västernorrland | Sundsvall | Gärdehov Arena – allmänhetens åkning | no fixed published hours: public skating times are only in a daily-updated booking calendar and 'kan ändras med kort varsel' (no weekly schedule) |
| Västernorrland | Sundsvall | Sidsjöbacken | no published hours: 2026/27 lift hours and opening date not yet published (official page: opening expected mid-December, 'uppdateras löpande'); recheck after opening |
| Västernorrland | Sundsvall | Sundsvall Äventyrsgolf | not drop-in: a slot must be booked online to get an entry code (self-service hall) |
| Västernorrland | Sundsvall | Äventyrsgolfen Granlo | season over and no season dates published: live site says 'Stängt för säsongen ... Vi öppnar igen våren/sommaren 2027. Exakt öppningsdatum släpps här'; 2026 season start/end dates were never published (archived pages only show … |
| Västernorrland | Ånge | Boda Borg Torpshammar | Booking-only, not drop-in: 'Öppettider – förbokas alltid', 'Förbokning krävs, senast dagen innan'; season April–November. |
| Västernorrland | Ånge | Camp Mid Adventure | Booking-based activity camp: the only drop-in is the climbing park with two start times (10 and 14) during 1 July–16 August (no year given); everything else booked. No drop-in place with real opening hours; contact is a mobile … |
| Västernorrland | Ånge | Naturum Ånge | only a three-week holiday opening is published (21 Dec-10 Jan, closed on four holidays inside it); publish when the regular 2027 hours are out |
| Västernorrland | Örnsköldsvik | Fiskevistet – Surströmmingsmuseum i Skeppsmalen | no published hours: the official site only says the museum keeps the restaurant's hours '11.00-20.00' with no weekdays or season dates; the restaurant is now 'stängd för säsongen' and hogakusten.com just says 'Se hemsidan'. No … |
| Västernorrland | Örnsköldsvik | Solbergsbacken | season dates not published (only end of November to April); premiere date announced on Facebook only |
| Västernorrland | Örnsköldsvik | Trysunda – fiskeläge och ö | Only reachable by M/F Ulvön; in the current timetable (1 Nov-23 Dec 2026) every Trysunda trip requires prebooked tickets and there is no same-day return; next season's timetable not published -> no drop-in visit with published … |
| Västernorrland | Örnsköldsvik | Ulvön – Ulvöhamn med båt från Köpmanholmen | winter timetable allows a same-day visit without pre-booking only on two weekdays with different departure times; publish when the summer timetable is out |
| Västernorrland | Örnsköldsvik | Åsbacken | season dates not published (asbacken.se: 'Stängt för säsongen!' + only 'Preliminära ordinarie öppettider för säsongen 2026/2027', no opening date) and only ONE usable official photo (hogakusten.com); the Google Sites photos on … |
| Jämtland | Berg | Hoverbergsgrottan | no published hours: official site hoverbergsgrottan.se is offline (Loopia 'not available'); Länsstyrelsen only says the cave is open in the summer months for a fee, no days/times on any official page |
| Jämtland | Berg | Svenstaviks simhall | no real photo: berg.se simhall page has no photo of the hall and the only related news image is a Pexels stock photo |
| Jämtland | Berg | Åsarna Skicenter | not a family activity venue: restaurant, outlet store, cabins/hostel and conference; trails/activities around the village are not run as a visitable attraction with hours |
| Jämtland | Bräcke | Kälarne Badet | no published hours on any official page: Bräcke kommun only says 'Öppet bad på måndagar och torsdagar under terminstid, se Kälarne badet på Facebook' (no times); hours only on a Facebook page |
| Jämtland | Bräcke | Svedjebacken | season dates not published and the hours text is unchanged since Feb 2025 |
| Jämtland | Härjedalen | Aktivitetshuset Lofsdalen | no published hours: lofsdalen.com Aktivitetshuset page lists no opening hours, operator site mpxgruppen.com has none, old domain aktivitetlofsdalen.se is now spam |
| Jämtland | Härjedalen | Björnrike Ski Club – Valle lekland, Björnbadet & bowling | no published hours: official site lists no opening hours for lekland/bowling; Björnbadet is booked in time slots ('Boka tid i vårt bad') |
| Jämtland | Härjedalen | FlipIt Vemdalen trampolinpark | hours are only shown as a rolling next-7-days list; no standing schedule |
| Jämtland | Härjedalen | Klätterparken Vemdalsskalet (Puls) | booking only: Puls sells the climbing park as booked 2-hour sessions ('Pris enligt offert'), summer season only, no weekday drop-in hours |
| Jämtland | Härjedalen | Myskoxcentrum Härjedalen | booking-only guided tours, no drop-in visit |
| Jämtland | Härjedalen | Nyvallens fäbod | same site as #182 (Nyvallen main entrance, covered there); the fäbod itself publishes no opening hours (nyvallen.com has contact info only) |
| Jämtland | Härjedalen | Trumvallen Fjällridning | Booking-only guided riding tours / sleigh rides / cattle drives; no drop-in visit with published hours |
| Jämtland | Krokom | Skärvångens Bymejeri | not a family activity: cheese farm shop only; dairy study visits must be booked (no drop-in visit of animals/production) |
| Jämtland | Krokom | Åkersjöns skidanläggning | no published hours: official site (sportcampingakersjon.com) has an 'Öppettider Skidlift' heading with no hours under it; Krokom kommun page says to contact the facility for opening hours |
| Jämtland | Ragunda | Hammarstrands Kälk- och Rodelbana | no published hours: naturbanan 'STÄNGD FÖR SÄSONGEN! Välkommen säsongen 2027!' with times only added ad hoc ('Vi lägger till tider löpande', 'preliminära', may close at short notice); konstbanan paused for 2026/27 |
| Jämtland | Strömsund | Korallgrottan – guidade grottturer | booking-only guided full-day tour ('Förbokning krävs'), no drop-in visit |
| Jämtland | Strömsund | Nordic Husky Farm | mainly booked husky tours; official site has no published drop-in opening days/hours ('Kontakta oss gärna för bokning och öppettider' on kommun page) |
| Jämtland | Strömsund | Strömsunds hembygdsgård med Jätten Jorm | no published opening hours: kommun/Visit Strömsund page has none, hembygd.se/strom blocks scripts (403) and its 2025 archived copy gives no hours (only Kafé Tomten lunch, 'följ de på Facebook') |
| Jämtland | Strömsund | Strömsunds simhall | no real photo of this pool on any official page (kommun uses a stock underwater photo; Hjalmar Strömerskolan site has none); otherwise ready to publish |
| Jämtland | Åre | Gruvbacken i Huså | no published hours: official page only says the lift reopens 'omkring jul & årskiftet 26/27', no weekday lift hours or season dates |
| Jämtland | Åre | Naturum Vålådalen | no dated season on the live official site (last dated season is summer 2025 in an archive); winter opening not announced yet |
| Jämtland | Åre | O'Learys Åre – bowling & äventyrsgolf (Holiday Club) | No real photo of this place on any official page (olearys.se/are and holidayclub.se only show generic chain stock images); sports bar with evening-weighted hours (Mon-Tue from 18:00). |
| Jämtland | Åre | Åre Bergbana & Åre Museum | winter single-ride ticket for non-skiers not confirmed and no official opening hours for Åre Museum |
| Jämtland | Åre | Åre Chokladfabrik | retail chocolate shop only: the official site describes a factory shop (products, webshop) and no visitor activity — no viewing window into production, café or tasting is mentioned on any official page, so the client's 'watch t… |
| Jämtland | Åre | Åre Klätterpark (SkiStar, Björnen) | Booking-only (time slots booked in advance), age limit 7 yrs/120 cm; closed for the season now — not drop-in. |
| Jämtland | Åre | Åre Sleddog Adventures | no published hours: dog-sled tour operator (tours by arrangement); the official site lists no opening hours or drop-in visit |
| Jämtland | Östersund | Bowlinghallen Kök & Bar | no real photo of this hall on its official site (only stock-like images) |
| Jämtland | Östersund | Frösö kyrka | church with no family offer on the official parish page (visits/guided tours only) |
| Jämtland | Östersund | Frösötornet | no published hours: kommun page gives no opening hours for the tower/lift; café (hejvisp.se) only refers to Facebook/Instagram for hours |
| Jämtland | Östersund | Locknekratern Meteoritcenter | closed for season; only the 2027 premiere day (Tue 22 June 2027 11-16) is published, no weekday hours or season end on any official page (rest is on Facebook) |
| Jämtland | Östersund | M/S Thomée – båtturer på Storsjön | season over (last departure 9 Oct 2026); trips are booked theme cruises, no public timetable for 2027 |
| Jämtland | Östersund | Stadsmuseet Östersund | official site gamlaostersund.se is offline (connection refused 2026-11-18); Visit Östersund gives no hours and only says 'Öppettider – se gamlaostersund.se'; newest archived copy is from 2023 -> no current official hours |
| Jämtland | Östersund | Vinterparken | 2027 season not announced and ice-dependent; no official end date |
| Jämtland | Östersund | Östersund Arena – allmänhetens åkning | public skating times are published week by week and vary |
| Jämtland | Östersund | Östersunds Hyrkart – Motorstadion | closed for season; no published weekday hours (drop-in only when the booking calendar is free, weather-dependent), next season not dated |
| Västerbotten | Bjurholm | Agnäsbacken | no published hours: site says the opening will be announced on Facebook; hours widget only shows the current week (all 'Stängt'); last season was weekends 10-15:30 (wayback) - recheck when the season opens |
| Västerbotten | Dorotea | Nattvarden – skulpturgruppen vid Dorotea kyrka | Church grave chapel with a sculpture group: no published opening hours (only 'Kapellet är öppet året runt'), no family offer, and only one official photo. |
| Västerbotten | Lycksele | Bocksliden | no published season dates – 2026/27 opening only announced on Facebook (data filled in below for later) |
| Västerbotten | Lycksele | Trollringen Gokart | no real photo of the place on any official site (club gallery empty/points to a private Flickr; visitlycksele uses Pixabay stock); also season year not stated on club page |
| Västerbotten | Malå | Entré Malå – utkikstornet i Nölviken | exact location could not be verified (only a kommun news item; map pin approximate) and only one photo |
| Västerbotten | Nordmaling | Ålidberget | season dates not published (site says waiting for winter; opening announced on Facebook) |
| Västerbotten | Norsjö | Norsjö simhall | public swim hours are published week by week only (two weeks ahead) |
| Västerbotten | Skellefteå | Bygdsiljumsbacken | no published hours: official opening-hours page shows only 'Säsongen 2025/2026 Stängt för säsongen.' – no 2026/27 season dates or weekday lift hours |
| Västerbotten | Skellefteå | Byske Havsbad – utebad & äventyrsgolf | no published hours: kommun page gives only the season (13 June–16 August) and its hours widget shows only the current week ('Closed for the season'); no daily hours on any official page or archived copy |
| Västerbotten | Skellefteå | Eddahallen | no real photo of the place: every image on the official kommun pages (Eddahallen page, badhus overview) is a stock photo, and Visit Skellefteå has no Eddahallen page |
| Västerbotten | Skellefteå | Finnfors kraftverksmuseum | no published hours: operator page (Skellefteå Kraft) only says it 'will reopen in June 2026' (stale) with no opening hours or 2026/2027 season dates; Visit Skellefteå page is gone (404) |
| Västerbotten | Skellefteå | Kartway Skellefteå (Skellefteå Kart Arena) | no published hours: the official page shows the 2026 drop-in span (2026-06-20 to 2026-08-09) but every weekday as 'Stängt'; 2026 daily drop-in hours appear nowhere official and no archived 2026 copy exists |
| Västerbotten | Skellefteå | Vitbergsbacken | no published hours for 2026/27: the live kommun page only shows 'Stängt för säsongen' with no weekday hours and no season dates; last season's hours are visible only in archived copies of the weekly widget, and no season start … |
| Västerbotten | Skellefteå | Vitbergsbadet | no published hours: the kommun page gives only the 2026 season (13 June–16 August) and its hours widget now shows only 'Stängt för säsongen'; 2026 daily hours were never written on the page and no in-season archived copy exists |
| Västerbotten | Sorsele | Naturum Vindelfjällen Ammarnäs | Closed for the season; official page only says it plans to reopen 'i början av mars 2027' with no dates and no opening hours published (re-check in early 2027). |
| Västerbotten | Storuman | Simhallen i Storuman | official site storuman.se unreachable (connection refused/timeout); current autumn hours unverifiable - only a wayback copy of 2026-06-16 (pre-summer schedule); official images only 462 px and not loadable. Data below is ready … |
| Västerbotten | Umeå | Bowlingcentrum Umeå | no real photo of the place on any official page (own site and visitumea show only stock bowling images; site gallery is empty); site shows no 2025/26 content |
| Västerbotten | Umeå | Bräntberget | no published lift hours: UHSK/Umeå kommun pages only say the hill is closed for the season and hopes to reopen end of December, no weekday hours or season dates |
| Västerbotten | Umeå | Kassjöbacken | no season dates published (2026/27 not announced and no 2025/26 span either; last season opened only in March 2026 due to little snow). Weekend hours 10-15 exist; data below is ready once the season is announced |
| Västerbotten | Umeå | Mickelbo Gård | no published hours: official site says closed until Advent after Halloween weekend 7–8/11; no Advent/jul or summer opening hours published on any page (hours & prices page lists only prices) |
| Västerbotten | Umeå | Norrlandsoperan | Not drop-in: opera/concert/dance venue with ticketed performances only (theatre rule). |
| Västerbotten | Umeå | O'Learys Umeå – bowling | regular opening hours are not shown on the live official page (only holiday deviations); sports bar and nightclub profile with age limits in the evening |
| Västerbotten | Vilhelmina | Trappstegsforsen | no official operator or visitor page; only one photo (adults posing) |
| Västerbotten | Vilhelmina | Vilhelmina museum | three-week summer opening run by a different association each year; 2027 not confirmed |
| Västerbotten | Vindeln | Bubergsgården – Bubergets skidanläggning | 2026/27 season not announced; weekly hours only in hidden page markup while the page says closed for the season |
| Västerbotten | Vindeln | Forsknäckarna | Rafting tours that must be booked in advance (Trollforsturen 12+, Glassturen 9+); no drop-in visit with published opening hours. |
| Västerbotten | Vännäs | Middagsberget | no published hours: season 26/27 not open yet and 'Planerade öppettider' on middagsberget.se is empty (last season per wayback 2026-02-09: v.3-8 Sat-Sun 10:30-15:30, Tue-Thu 18-20:30) - recheck when hours are posted |
| Västerbotten | Åsele | Torvsjö kvarnar | no published hours: Länsstyrelsen page only says exhibition and café open 'under juli och augusti' (no days/times, no operator contact); free access to the area not stated officially |
| Norrbotten | Arjeplog | Båtsuoj Samecenter | No drop-in visit with published hours: summer-only guided tours/overnight stays (1 Jun–28 Aug), no opening hours on batsuoj.se; only private mobile numbers listed |
| Norrbotten | Arvidsjaur | Prästberget | no 2026/27 season dates published: the kommun page says 'Prästberget är stängt för säsongen!' and gives only weekday lift hours, with no opening/closing dates on any official page (neither this nor last season); also no officia… |
| Norrbotten | Boden | Paglabacken | no published hours: the operator's Pagla page (Storklintens AK Skalp) only says the lift is closed for the season, no weekday lift hours for 2026/27 or any earlier season on any official page; kommun page only says open 'when c… |
| Norrbotten | Gällivare | Gällivare kulturmuseum | Closed until further notice (tillsvidare stängt), no reopening date |
| Norrbotten | Haparanda | Kukkolaforsen & Tornedalens fiskemuseum | no published hours: Haparanda stad and HaparandaTornio pages only say the museum is open daily in summer (pre-booked groups otherwise); no dates or times on any official page |
| Norrbotten | Haparanda | Sandskär – dagstur till Haparanda skärgårds nationalpark | Booked guided boat tour only (Innala Archipelago, pre-booked day trip, cancelled if too few participants) – no drop-in visit |
| Norrbotten | Jokkmokk | Arctic Camp Jokkmokk – utebad och äventyrsgolf | pool season dates not published (only: open in high season) |
| Norrbotten | Jokkmokk | Jokkmokkguiderna – hundspann | booking-only guided tours (dog-sled tours Dec–Mar and canoe rental/tours), no drop-in visit with published opening hours |
| Norrbotten | Jokkmokk | Polcirkeln vid E45 (Jokkmokk) | no official visitor page or operator for the Arctic Circle marker itself: the only official source (Jokkmokks kommun) lists just the seasonal Polcirkelns café och butik (mid-June to mid-August, no hours) with a single photo of … |
| Norrbotten | Kalix | Rudträskbacken | no published hours: kommun page says closed for season, no 2026/27 hours or season dates; only one official photo |
| Norrbotten | Kiruna | Husky Tours Lapland | Booking-only dog-sled tours and kennel visits (pre-booking required); no drop-in visit with published hours; official site blocks scripts (HTTP 454). |
| Norrbotten | Kiruna | LKAB:s Visitor Centre – gruvtur | booking-only guided mine tour (bus tour with tickets/limited places, advance booking), no drop-in visit |
| Norrbotten | Kiruna | Luossabacken | season dates not published (kommun page still shows 2025/26 hours); opening announced on Facebook |
| Norrbotten | Luleå | Explore Luleå – höghöjdsbana | booking only: fixed start times booked in advance (10, 11, 13, 14), season 1 May–Sept, no drop-in |
| Norrbotten | Luleå | Isbanan i Luleå | ice-dependent with no official opening dates (opens when the ice is safe) |
| Norrbotten | Luleå | Kartway Luleå – gokart | no published hours: season 2026 (20 jun–9 aug) is over and the official page now lists every weekday as 'Stängt'; no 2026 weekday hours are retrievable (no archived copy) and the 2027 season is not announced |
| Norrbotten | Luleå | Måttsundsbacken | No published hours: official site only says closed for the season and points to Facebook/Instagram; no weekday lift hours or 2026/27 season dates on any official page (no archived copy with hours) |
| Norrbotten | Luleå | Norrbottensteatern | Theatre – performances with tickets only, no drop-in visit |
| Norrbotten | Luleå | O'Learys Luleå – bowling | not family-focused / no usable hours or photo: O'Learys Luleå Event Center is a sportbar + nightclub with 18-year age limit Fri–Sat (minors with guardian only until 22); bowling only lists start times ('Tisdag från 16.00 …'), n… |
| Norrbotten | Pajala | Laestadiusmuseet & Laestadiuspörtet | no published opening hours; visits outside summer by booking via Pajala församling |
| Norrbotten | Pajala | Pajala Badhus | currently closed (driftstörning v.47), hours table empty and hours only posted week by week; no real photo (page banner is a Pexels stock image) |
| Norrbotten | Pajala | Sattajärvi Skidcenter | no published hours: site only shows 'Open 6 april 2024 11–15' and refers to a Facebook group; no weekday hours or 2026/27 season |
| Norrbotten | Piteå | Bowlingarenan Piteå | No real photo of the place on any official source: bowlingarenan.se uses only Unsplash stock images (plus one dart-board photo and an opening-hours poster). |
| Norrbotten | Piteå | Kartway Piteå | no published hours: season 2026 (20 jun–9 aug) is over and kartway.se/pitea now lists every weekday as 'Stängt'; no weekday drop-in hours on any official page (no recent archive copy); only a mobile number |
| Norrbotten | Piteå | Lindbäcksstadion | no published hours: official site lindbacksstadion.se is unreachable (expired TLS certificate, newest archive copy 2020) and the pitea.se Lindbäcksstadion page gives no slope/lift opening hours or season |
| Norrbotten | Älvsbyn | Kanisbacken | season dates not published; current hours only in an archived copy |
| Norrbotten | Älvsbyn | Älvsbyns Sportcenter – simhallen | hours published only week by week |
| Norrbotten | Överkalix | Storlappbergets skidanläggning | opening date not announced (kommun page says not opened for the season) |
| Norrbotten | Övertorneå | Hanhivittikko fäbod | season end not published and the map position could not be verified (not in OpenStreetMap) |

## Follow-ups
- Seasonal places with the last season copied into 2027 — confirm when the official 2027 dates are published:
  - Bergmancenter (Gotland): 2027-06-01 → 2027-08-30
  - Bläse Kalkbruk (Gotland): 2027-06-13 → 2027-08-16
  - Bungemuseet (Gotland): 2027-06-01 → 2027-08-31
  - Gotlands Försvarsmuseum (Gotland): 2027-06-28 → 2027-08-07
  - Högt & Lågt klätterpark Klintehamn (Gotland): 2027-06-20 → 2027-08-16
  - Kulturreservatet Norrbys museigård (Gotland): 2027-06-22 → 2027-08-09
  - Petes museigård (Gotland): 2027-06-19 → 2027-08-09
  - S:ta Karins kyrkoruin (Gotland): 2027-05-01 → 2027-10-04
  - Stavgard Vikingagård (Gotland): 2027-06-26 → 2027-08-08
  - Tingstäde fästning (Gotland): 2027-06-28 → 2027-08-22
  - Visbytåget – avgång Inre hamnen (Gotland): 2027-07-04 → 2027-08-13
  - Äventyrsgolf på Sudersand Resort (Gotland): 2027-06-07 → 2027-09-05
  - Härnösands Bilmuseum (Härnösand): 2027-06-13 → 2027-08-31
  - Härnösands Golf & Glass (Härnösand): 2027-05-01 → 2027-09-30
  - Mannaminne (Kramfors): 2027-05-30 → 2027-08-31
  - Skulebergets Linbana (Kramfors): 2027-06-01 → 2027-08-31
  - Junsele Djurpark (Sollefteå): 2027-06-21 → 2027-08-16
  - Nämforsens Hällristningsmuseum (Sollefteå): 2027-06-15 → 2027-08-15
  - Risöbadet (Sollefteå): 2027-06-28 → 2027-08-15
  - Slalombacke Getberget (Ånge): 2026-12-26 → 2027-03-28
  - Aktivator Park (Örnsköldsvik): 2027-06-20 → 2027-08-23
  - Bjästabacken (Örnsköldsvik): 2026-12-25 → 2027-03-14
  - Örnsköldsviks Minigolfbana (Örnsköldsvik): 2027-05-11 → 2027-08-23
  - Brattbytorpet (Bräcke): 2027-06-19 → 2027-08-16
  - Lopme Laante – samisk park på Funäsdalsberget (Härjedalen): 2027-07-01 → 2027-08-16
  - Sonfjällets nationalpark – entré Nyvallen (Härjedalen): 2027-06-25 → 2027-09-30
  - Almåsa Alpin (Krokom): 2026-12-20 → 2027-03-23
  - Lusthuset & Yxskaftkälens Järnvägar (Strömsund): 2027-07-04 → 2027-08-09
  - Bydalsfjällen (Åre): 2026-12-19 → 2027-04-18
  - Åre Bike Park (Åre): 2027-06-05 → 2027-09-27
  - Gustavsbergsbacken och Silverling (Östersund): 2026-12-25 → 2027-04-11
  - Sommarhagen (Östersund): 2027-06-15 → 2027-08-16
  - Teknikland (Östersund): 2027-06-22 → 2027-08-16
  - Älgens Hus (Bjurholm): 2027-06-08 → 2027-08-15
  - Husvagnsmuseet i Dorotea (Dorotea): 2027-06-15 → 2027-08-15
  - Ansia Badpark (Lycksele): 2027-06-22 → 2027-08-09
  - Olofsfors Bruk (Nordmaling): 2027-06-15 → 2027-08-15
  - Norsjö hembygdsområde (Norsjö): 2027-06-15 → 2027-08-09
  - Robertsfors Bruksmuseum (Robertsfors): 2027-06-06 → 2027-08-23
  - Eddaparkens Äventyrsgolf (Skellefteå Bangolfklubb) (Skellefteå): 2027-06-15 → 2027-08-16
  - LEGO-museet på Bureå Camping (Skellefteå): 2027-06-13 → 2027-08-16
  - Skellefteå Adventurepark (Skellefteå): 2027-06-22 → 2027-08-16
  - Naturum Vindelfjällen Hemavan (Storuman): 2027-06-22 → 2027-08-15
  - Gokart Umeå – Alvik Ring (Umeå): 2027-06-12 → 2027-08-16
  - Holmöns båtmuseum (Umeå): 2027-06-13 → 2027-08-16
  - Norrbyskärs museum (Umeå): 2027-06-13 → 2027-08-16
  - Umelagun (Umeå): 2027-06-10 → 2027-08-15
  - Umeå Bangolfklubb – bangolfbanorna i Hedlundadungen (Umeå): 2027-06-22 → 2027-08-30
  - Umeå Energicentrum (Umeå): 2027-06-15 → 2027-08-15
  - Zip Adventure Park Umeå (Umeå): 2027-06-12 → 2027-08-16
  - Vännäs Motormuseum (Vännäs): 2027-06-28 → 2027-08-15
  - Vännäsbadet (Vännäs): 2027-06-17 → 2027-08-22
  - Jäckvik Fjällcenter (Arjeplog): 2027-01-29 → 2027-04-25
  - Rödbergsfortet (Boden): 2027-06-23 → 2027-08-22
  - Naturum Laponia (Gällivare): 2027-04-01 → 2027-09-27
  - Ájtte Fjällträdgård (Jokkmokk): 2027-06-08 → 2027-08-30
  - Siknäsfortet (Kalix): 2027-06-24 → 2027-08-30
  - Vassholmen – flottningsmuseum och Café Flottaren (Kalix): 2027-07-01 → 2027-09-06
  - STF Aurora Sky Station – linbanan på Nuolja (Kiruna): 2027-06-12 → 2027-09-20
  - Arcusbadet (Luleå): 2027-06-19 → 2027-08-09
  - Norrbottens Järnvägsmuseum (Luleå): 2027-06-22 → 2027-08-14
  - Turbåtarna i Luleå skärgård – Södra hamnplan (Luleå): 2027-06-19 → 2027-08-16
  - Norrstrands pool & camping (Piteå): 2027-06-13 → 2027-08-09
  - Öjeby kyrkstad (Piteå): 2027-06-29 → 2027-07-31
  - Bagerimuseet Älvsbyn (Älvsbyn): 2027-06-22 → 2027-07-31
- Events that end before April 2027 (hours published only that far, or a short winter season) — extend when new hours appear:
  - Flygmuseet F 21 (Luleå): ends 2026-12-17
  - Roma Kungsgård (Gotland): ends 2026-12-20
  - Röbäcks 4H-gård (Umeå): ends 2026-12-31
  - Kåbdalis Skidliftar (Jokkmokk): ends 2027-01-10
  - Havremagasinet länskonsthall (Boden): ends 2027-01-31
  - Storklinten (Boden): ends 2027-02-28
  - Bjästabacken (Örnsköldsvik): ends 2027-03-14
  - Almåsa Alpin (Krokom): ends 2027-03-23
  - Slalombacke Getberget (Ånge): ends 2027-03-28
- Skipped **because the public hours are only published week by week or as a rolling list** (address, organizer and photos were verified) — publishable the day the user decides how such places should be shown:
  - Solbergabadet, Hemsebadet, Visby ishall (Gotland)
  - Gärdehov Arena – allmänhetens åkning (Sundsvall), Östersund Arena – allmänhetens åkning (Östersund)
  - FlipIt Vemdalen trampolinpark (Härjedalen), Norsjö simhall (Norsjö)
  - Älvsbyns Sportcenter – simhallen (Älvsbyn), Pajala Badhus (Pajala; also closed for a fault in week 47 and without a real photo)
- Skipped **because no real photo of the place exists on an official page** (hours were found) — publish when the place or the kommun provides one:
  - Högt & Lågt Fårö, Kustparksbadet, Terra Nova utomhuspool (Gotland)
  - Svenstaviks simhall (Berg), Strömsunds simhall (Strömsund), O'Learys Åre – bowling & äventyrsgolf (Åre), Bowlinghallen Kök & Bar (Östersund)
  - Trollringen Gokart (Lycksele), Eddahallen (Skellefteå), Bowlingcentrum Umeå (Umeå), Bowlingarenan Piteå (Piteå)
- Simhallen i Storuman: storuman.se was unreachable on 18 Nov, so the autumn hours could not be verified → re-check.
- Ski hills and other winter places without published 2026/27 hours on 18 Nov (see the skipped table: Vitbergsbacken, Bubergsgården, Kanisbacken, Rudträskbacken, Prästberget, Paglabacken, Sattajärvi Skidcenter, Lindbäcksstadion and others) → re-check in mid-December when the lifts open.
- Region Gotland's organizer was created without an e-mail: the address is already stored on an old organizer ("ICA Maxi Arena") and the database allows each e-mail once → correct the old organizer, then add the e-mail to Region Gotland.
- The app's kommun list has three spelling mistakes that the dashboard cannot edit: "Robertfors" (Robertsfors), "Vaggaryd" (Vaggeryd), "Lilla edet" (Lilla Edet) → developer.
- Härjedalens Fjällmuseum and Moose Garden (already in the app before this run) stay hidden, as decided in the 2026-11-05 audit.
- Open question to the user: what "hours off" should mean in the dashboard for places without verifiable hours. Until answered, such places are skipped and listed here.
