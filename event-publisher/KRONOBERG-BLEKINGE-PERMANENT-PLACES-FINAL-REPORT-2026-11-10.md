# Kronoberg + Blekinge — permanent places final report (2026-11-10)

Source: client file `Famies - Vad ska vi hitta pa idag_2.html` (new regions Kronoberg and Blekinge). Published with the strict rules from 2026-11-05: every status, hours, season, price and address checked on an official, current source (evidence quote per fact), no booking-only / performance-only / escape-room places, `isFree` only when free for everyone, push notifications off.

| | Count |
|---|---|
| Places in the file for the two regions | 79 |
| Already in the app (not duplicated) | 5 |
| Researched (11 research agents, one per group) | 74 |
| **Published** | **53** (Kronoberg 30, Blekinge 23) |
| Skipped (reasons below) | 21 |
| Seasonal places with the 2026 season copied to 2027 (official 2027 dates not out yet) | 19 |
| Published live events in the app | 1205 → **1258** |

## Checks after publishing
- Every new event re-read from the API and compared field by field with the spec (title, description, days, start, duration, start/end date, isFree, ages 18–100 / child min–18, interests, venue, kommun, opening-hours count, organizer, logo): **53/53 OK**.
- Duplicate titles among all published live events: 0. Duplicate cover images: 0 (SHA-256 guard + exact URL check).
- Chain photos (Leo's Lekland, Actic, Boda Borg, Funplays, Wallride, Event Center, Cyberzone) compared with dHash against 137 existing chain images: closest distance 18 (duplicate threshold 10) → all unique.
- The duplicate-image guard stopped one publish: Blekingetrafiken uses the same photo for the Karlskrona and the Karlshamn archipelago boats → Sommarbåtarna från Fisktorget got its other official photos instead.
- Haganäsbadet hours were researched from a 10-day-old archive copy (almhult.se blocks scripts) → checked live in the browser before publishing: week 46 matches.

## Published places
| Region | Kommun | Place | Event window | Period | Free | Season | Event ID |
|---|---|---|---|---|---|---|---|
| Kronoberg | Alvesta | Huseby Bruk | alltid öppet | 2026-11-10 → 2027-12-31 | nej |  | 491434576481125881 |
| Kronoberg | Alvesta | Virda bad- och sportcenter Alvesta | mån, tis, ons, tor, fre, lör 14:30–16:00 | 2026-11-10 → 2027-12-31 | nej |  | 491436915736741078 |
| Kronoberg | Lessebo | Bergdalahyttan | mån, tis, ons, tor, fre 12:00–15:30 | 2026-11-10 → 2027-12-31 | ja |  | 491435368072120186 |
| Kronoberg | Lessebo | Grönåsens Älgpark | tis, ons, tor, fre, lör, sön 11:00–15:00 | 2027-04-03 → 2027-10-31 | nej | kopierad 2026 | 491435170218411820 |
| Kronoberg | Lessebo | Kosta Glasbruk | alla dagar 14:00–16:00 | 2026-11-10 → 2027-12-31 | nej |  | 491435097354962706 |
| Kronoberg | Lessebo | Kosta Safaripark | alla dagar 10:00–18:00 | 2026-11-10 → 2027-12-31 | nej |  | 491435231430084422 |
| Kronoberg | Lessebo | Lessebo Handpappersbruk | mån, tis, ons, tor, fre 10:30–16:00 | 2027-06-15 → 2027-08-28 | nej | kopierad 2026 | 491435299671410528 |
| Kronoberg | Lessebo | Skrufs Glasbruk | mån, tis, ons, tor, fre 12:00–15:30 | 2026-11-10 → 2027-12-31 | nej |  | 491435440390309779 |
| Kronoberg | Lessebo | Växjö Hyrkart Hagaslätt | lör, sön 14:00–17:00 | 2027-05-01 → 2027-09-30 | nej | kopierad 2026 | 491435510762342325 |
| Kronoberg | Ljungby | Buslandet Lagan | fre, lör, sön 11:00–18:00 | 2026-11-10 → 2027-12-31 | nej |  | 491434726419105290 |
| Kronoberg | Ljungby | Elinge Älgpark | tis, ons 11:00–15:00 | 2026-11-10 → 2027-04-30 | nej |  | 491434892958139920 |
| Kronoberg | Ljungby | Kronoskogsbadet Ljungby | alla dagar 10:00–18:00 | 2027-06-08 → 2027-08-23 | ja | kopierad 2026 | 491438856944518581 |
| Kronoberg | Ljungby | Laganland Älgpark | alla dagar 10:00–17:00 | 2027-04-01 → 2027-10-31 | nej | kopierad 2026 | 491434650527368708 |
| Kronoberg | Ljungby | Ljungby simhall och äventyrsbad | tis, ons, tor, fre, lör, sön 13:00–16:00 | 2026-11-10 → 2027-12-31 | nej |  | 491437520496657752 |
| Kronoberg | Ljungby | Minivärlden Ljungby | mån, tis, ons, tor, fre, lör 10:00–15:00 | 2027-06-29 → 2027-08-08 | nej | kopierad 2026 | 491437345954891085 |
| Kronoberg | Ljungby | Sagomuseet Ljungby | tor 12:00–16:00 | 2026-11-10 → 2027-12-31 | nej | kopierad 2026 | 491437285632410948 |
| Kronoberg | Markaryd | Hannabadet Markaryd | tis, ons, tor, fre, lör, sön 12:30–15:30 | 2026-11-10 → 2027-05-31 | nej |  | 491434964202587690 |
| Kronoberg | Markaryd | Markaryds Bowling | mån, tis, ons, tor, fre, lör 15:00–20:00 | 2026-11-10 → 2027-12-31 | nej |  | 491435029700839070 |
| Kronoberg | Uppvidinge | Hälsans Hus Åseda | mån, tis, ons, tor, fre 14:30–17:45 | 2026-11-10 → 2027-12-31 | nej |  | 491435643226851285 |
| Kronoberg | Uppvidinge | Sweden Zipline | tor, fre, lör 11:00–16:00 | 2027-04-01 → 2027-10-31 | nej | kopierad 2026 | 491435575757277134 |
| Kronoberg | Växjö | Actic Växjö Simhall | alla dagar 13:00–18:00 | 2026-11-10 → 2027-12-31 | nej |  | 491434154718692815 |
| Kronoberg | Växjö | Event Center Knock 'em Down Växjö | tis, ons, tor, fre, lör 15:45–21:00 | 2026-11-10 → 2027-12-31 | nej |  | 491434361514657252 |
| Kronoberg | Växjö | Leo's Lekland Växjö | alla dagar 10:00–19:00 | 2026-11-10 → 2027-12-31 | nej |  | 491434220015617494 |
| Kronoberg | Växjö | Smålands Spelhall Växjö | lör, sön 13:00–17:00 | 2026-11-10 → 2027-12-31 | nej |  | 491434429999252971 |
| Kronoberg | Växjö | Utvandrarnas hus Växjö | tis, ons, tor, fre, lör, sön 11:00–16:00 | 2026-11-10 → 2027-12-31 | nej |  | 491434086158599624 |
| Kronoberg | Växjö | Växjö 4H-gård | alltid öppet | 2026-11-10 → 2027-12-31 | ja |  | 491434510613775858 |
| Kronoberg | Växjö | Wallride Växjö | fre, lör, sön 14:00–18:00 | 2026-11-10 → 2027-12-31 | nej |  | 491434288215000541 |
| Kronoberg | Älmhult | Haganäsbadet Älmhult | tis, ons, tor, fre, sön 15:45–17:00 | 2026-11-10 → 2027-12-31 | nej |  | 491437212324365602 |
| Kronoberg | Älmhult | IKEA Museum Älmhult | alla dagar 11:00–17:00 | 2026-11-10 → 2027-12-31 | nej |  | 491437000277132511 |
| Kronoberg | Älmhult | Linnés Råshult | alltid öppet | 2026-11-10 → 2027-12-31 | ja |  | 491437130040509701 |
| Blekinge | Karlshamn | Abu-museet i Svängsta | ons, tor, fre, lör 13:00–16:00 | 2027-06-22 → 2027-08-09 | nej | kopierad 2026 | 491436474537903663 |
| Blekinge | Karlshamn | Asarums Bangolfklubb | alla dagar 15:00–21:00 | 2026-11-10 → 2027-12-31 | nej |  | 491436409400362459 |
| Blekinge | Karlshamn | Karlshamns museum | tis, ons, tor, fre 13:00–16:00 | 2026-11-10 → 2027-12-31 | nej |  | 491436137391359107 |
| Blekinge | Karlshamn | Kastellet i Karlshamn | alla dagar 10:00–18:00 | 2027-06-18 → 2027-08-16 | nej | kopierad 2026 | 491436209390781655 |
| Blekinge | Karlshamn | Laxens hus Mörrum | mån, tis, ons, tor, fre 09:00–16:00 | 2026-11-10 → 2027-02-28 | nej |  | 491436343457514881 |
| Blekinge | Karlshamn | Skärgårdsbåten till Tärnö | alla dagar 09:45–16:05 | 2027-06-01 → 2027-09-06 | nej | kopierad 2026 | 491436276684195116 |
| Blekinge | Karlskrona | Boda Borg Karlskrona | ons, tor, fre, lör, sön 10:00–17:00 | 2026-11-10 → 2027-12-31 | nej |  | 491435931451032623 |
| Blekinge | Karlskrona | Cyberzone Karlskrona | mån, tis, ons, tor, fre, lör 17:00–21:00 | 2026-11-10 → 2027-12-31 | nej |  | 491435853470532634 |
| Blekinge | Karlskrona | Drottningskärs kastell | alla dagar 09:45–17:00 | 2027-05-30 → 2027-08-31 | nej | kopierad 2026 | 491438914607809979 |
| Blekinge | Karlskrona | Funplays Karlskrona | alla dagar 10:00–19:00 | 2026-11-10 → 2027-12-31 | nej |  | 491435774651172861 |
| Blekinge | Karlskrona | Karlskrona Sommarland Barnens Gård | alla dagar 10:00–18:00 | 2027-06-13 → 2027-08-16 | nej | kopierad 2026 | 491435710511876071 |
| Blekinge | Karlskrona | Sommarbåtarna från Fisktorget | alla dagar 08:30–19:45 | 2027-06-01 → 2027-08-31 | nej | kopierad 2026 | 491437952325420449 |
| Blekinge | Olofström | Holjebadet Olofström | mån, ons, tor, fre 14:00–17:30 | 2026-11-10 → 2027-06-13 | nej |  | 491436835432596576 |
| Blekinge | Ronneby | Kallvattenkuren Ronneby | lör, sön 10:00–15:00 | 2026-11-10 → 2026-12-31 | ja |  | 491436068848043114 |
| Blekinge | Ronneby | Kulturcentrum Ronneby konsthall | tis, ons, tor, fre, lör, sön 11:00–15:00 | 2026-11-14 → 2027-12-31 | ja |  | 491436013105742924 |
| Blekinge | Ronneby | Naturum Blekinge | ons, tor, fre, lör, sön 12:00–15:00 | 2027-04-01 → 2027-09-30 | nej | kopierad 2026 | 491437697496286602 |
| Blekinge | Ronneby | Ronneby Brunnsbad | alla dagar 09:00–19:00 | 2027-06-06 → 2027-08-29 | nej | kopierad 2026 | 491437602184922461 |
| Blekinge | Ronneby | Ronneby Brunnspark | alltid öppet | 2026-11-10 → 2027-12-31 | ja |  | 491437648582313331 |
| Blekinge | Sölvesborg | Hanö | alla dagar 10:00–15:55 | 2026-11-10 → 2027-05-14 | nej |  | 491436598068545262 |
| Blekinge | Sölvesborg | Hälleviksbadet | alla dagar 09:00–19:00 | 2027-06-06 → 2027-08-30 | nej | kopierad 2026 | 491436713286076318 |
| Blekinge | Sölvesborg | Sölvesborgs museum | tis, ons, tor, fre, lör 10:00–17:00 | 2027-06-16 → 2027-08-15 | nej | kopierad 2026 | 491436657107568450 |
| Blekinge | Sölvesborg | Sölvesborgs slottsruin | alltid öppet | 2026-11-10 → 2027-12-31 | ja |  | 491436549079074450 |
| Blekinge | Sölvesborg | Victoriabadet | lör 10:00–15:00 | 2026-11-10 → 2027-05-30 | nej | kopierad 2026 | 491436774430640119 |

The venue keeps the full official hours per weekday; the event window is the slot that is open on every listed day.

## Skipped places
| Kommun | Place | Why |
|---|---|---|
| Lessebo | CRAFT Arena Kosta | official page: bowling and dart use booking times; no drop-in stated for padel/pingis/boule |
| Markaryd | Skåne-Smålands Järnväg – dressin och rälsbuss | Not drop-in: dressin rental is online booking only in fixed 3-hour slots (summer season 26 Jun–17 Aug 2026, closed now, 'öppnar igen sommar 2027' without dates); the räls |
| Tingsryd | Börjes Gård | season for ponies/minibilar not stated by any official source; only a tourism listing |
| Tingsryd | Tingsryds bowlinghall | lanes booked by phone, weekend hours only on request, only a named staff contact |
| Uppvidinge | Smalspåret – dressin & rälsbuss från Åseda | No published opening hours for dressin hire (only 'Öppet 17/6-16/8 dagligen', no times and no year); dressin hire is handed out at Virserum station (Hultsfred kommun, Kal |
| Växjö | Inlåst – Real Life Room Escape Game | escape room – booking-only, no drop-in (also marketed as an adult activity) |
| Växjö | O'Learys Växjö | no verifiable official hours: olearys.com (all Växjö pages) is behind a Vercel bot checkpoint (HTTP 429) for both curl and WebFetch, and the kommun page (upplev.vaxjo.se, |
| Växjö | Regionteatern Blekinge Kronoberg | theatre – dated performances, Familjedag and Scenlabb sessions only; no drop-in visit |
| Växjö | Växjö Minigolf – Spetsamossen | no published hours – 2026 season over; site only says it reopens 1 May, weekday hours and season end for 2027 not published |
| Växjö | Växjö domkyrka | church with no family offer (only services, choirs, lunch music); also a major renovation 2026–2032 is announced with no visitor-closure dates published |
| Växjö | Växjö teater | theatre building – performances only, no drop-in visit; client source is thatsup, no own official visitor page |
| Karlshamn | Karlshamns Bowlingcenter | address conflict (Idrottsvägen 3 vs Pilvägen 2), lanes booked by phone, only one low-res photo of the hall |
| Karlskrona | Blekinge museum – Grevagården | official site blekingemuseum.se offline since 2026-10-27; current hours only on third-party listings and a 2024 archive - re-check when the site is back |
| Karlskrona | Karlskrona Escape Room | Not drop-in: escape room, booked per group (brief: escape rooms are skipped) |
| Karlskrona | Karlskrona simhall | no verifiable current hours: karlskrona.se (the only official hours source) is behind a 'verify you're not a robot' wall; family-swim hours are published week-by-week wit |
| Karlskrona | Kungsholms fort – guidad båttur | Not drop-in: booking-only guided tour (summer only) to an active military area that cannot be visited on your own |
| Karlskrona | Prästgårdens Escape Room i Wämöparken | Not drop-in: escape room, booking/pre-order required (brief: escape rooms are skipped) |
| Karlskrona | Äventyrsminigolf på Dragsö Camping | seasonal outdoor minigolf without published season dates: dragso.se only toggles 'Minigolf/Biljardgolf: ÖPPEN / STÄNGD FÖR SÄSONGEN' on the contact page and reception hou |
| Olofström | Halens Camping – äventyrsgolf & båtuthyrning | no drop-in activity with published hours: campsite/accommodation; canoe/pedal-boat rental booked online, äventyrsgolf not on operator's site (operator only lists KolleGol |
| Sölvesborg | Fornhaga Islandshästar | not drop-in: booked farm rides/riding camps only, no published opening hours (calendar shows only 2025 events); only contact is a private mobile |
| Sölvesborg | Mystikfabriken – escape room | not drop-in: escape room / murder mystery, booking-only, no fixed opening hours |

## Same session: the three leftovers from the 2026-11-05 audit
- **parentMaxAge**: all 1,205 published live events checked; 83 still had 18 → PATCHed to 100 and re-read (0 errors).
- **46 events ending before April 2027**: re-checked on the official sources. Extended: Norrvikens trädgårdar (Juldrömmar weekends to 13 Dec), Trelleborgs Sjöfartsmuseum (season 6 Mar–28 Nov 2027), Naturum Fjärås Bräcka (winter–summer 2027 to 5 Sep). Hovfjället: start date corrected. Älvkarleby Sportfiske not extended (only a 2024 page states the yearly rule). The other 41 have no newer official period yet and keep their end date.
- **Events tab** (gid 1719318267) refreshed once at the end: 1,258 published live events (1,144 recurring, 114 one time), rows A2:E1259, no leftover rows; G23 Total = I292 Total = 1258; Kronoberg 31, Blekinge 26; row-by-row hash of the sheet equals the dashboard list.

## Follow-ups
- Seasonal places with the 2026 season copied into 2027 — confirm when the 2027 dates are published:
  - Grönåsens Älgpark (Lessebo): 2027-04-03 → 2027-10-31
  - Lessebo Handpappersbruk (Lessebo): 2027-06-15 → 2027-08-28
  - Växjö Hyrkart Hagaslätt (Lessebo): 2027-05-01 → 2027-09-30
  - Kronoskogsbadet Ljungby (Ljungby): 2027-06-08 → 2027-08-23
  - Laganland Älgpark (Ljungby): 2027-04-01 → 2027-10-31
  - Minivärlden Ljungby (Ljungby): 2027-06-29 → 2027-08-08
  - Sagomuseet Ljungby (Ljungby): 2026-11-10 → 2027-12-31
  - Sweden Zipline (Uppvidinge): 2027-04-01 → 2027-10-31
  - Abu-museet i Svängsta (Karlshamn): 2027-06-22 → 2027-08-09
  - Kastellet i Karlshamn (Karlshamn): 2027-06-18 → 2027-08-16
  - Skärgårdsbåten till Tärnö (Karlshamn): 2027-06-01 → 2027-09-06
  - Drottningskärs kastell (Karlskrona): 2027-05-30 → 2027-08-31
  - Karlskrona Sommarland Barnens Gård (Karlskrona): 2027-06-13 → 2027-08-16
  - Sommarbåtarna från Fisktorget (Karlskrona): 2027-06-01 → 2027-08-31
  - Naturum Blekinge (Ronneby): 2027-04-01 → 2027-09-30
  - Ronneby Brunnsbad (Ronneby): 2027-06-06 → 2027-08-29
  - Hälleviksbadet (Sölvesborg): 2027-06-06 → 2027-08-30
  - Sölvesborgs museum (Sölvesborg): 2027-06-16 → 2027-08-15
  - Victoriabadet (Sölvesborg): 2026-11-10 → 2027-05-30
- Kallvattenkuren Ronneby ends 31 Dec 2026 (no 2027 hours yet); Laxens hus Mörrum ends 28 Feb 2027; Hanö boat ends 14 May 2027; Elinge Älgpark winter hours end 30 Apr 2027; Hannabadet ends 31 May 2027; Victoriabadet ends 30 May 2027 (summer closed); Holjebadet ends 13 Jun 2027 — re-check for the next period.
- Blekinge museum: official site offline since 27 Oct 2026 (hosting security shutdown) → publish when blekingemuseum.se/oppettider is back. Karlskrona simhall: hours behind a robot check → read by hand. O'Learys Växjö: site bot-blocked → check in a normal browser. Växjö Minigolf: re-check in April 2027.
- From the audit re-check: Klättercentret Solna closes for good on 19 Dec 2026 (event ends then); Filmmuseet ends 21 Nov unless new dates appear; Drottningholm has extra days 31 Dec–6 Jan.
- Sagomuseet Ljungby is published as every Thursday 12–16; red-day Thursdays (24 Dec, Ascension Day) are closed.
