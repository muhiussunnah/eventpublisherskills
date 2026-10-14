# Österåker Source #1 — osteraker.se events scrape
**Date:** 2026-05-27
**Source:** https://www.osteraker.se/arkivevenemangkrisochinfo/evenemang.4.592cfecd176fc0db87818e.html
**Municipality ID:** 172600240698852664

## Events found (18 unique on first page, may need "Se fler" for more)

### Already exists — SKIP (duplicate)
- Slöjdfröjdig mönsterskärning och karvsnitt (30-31 maj 2026)
- Horisonten – för dig med funktionsnedsättning (31 maj)
- Vi möts – dialog med näringslivet i Österåker (the existing one)

### To publish — adult/business (tag 18,18)
1. **Nätverksfrukost för företagare** (27 maj 2026, 07.30-09.30, Restaurang Å vid Åkersberga Golfklubb) — business breakfast
   - URL: /natverksfrukostforforetagare.5.77c924619b9d91e3e21a6d4.html
2. **NY PLATS: Vi möts – dialog med näringslivet i Österåker** (27 maj 2026, 08.30-09.15, Espresso House Åkersberga Centrum) — CHECK: similar to existing "Vi möts" but new location
   - URL: /nyplatsvimotsdialogmednaringslivetiosteraker.5.77c924619b9d91e3e22654.html
3. **Anhöriggrupp för dig som har en partner med neurologisk sjukdom** (27 maj 2026, 10.30-12.00, Åkersberga Fyren) — caretaker support
   - URL: /anhoriggruppfordigsomharenpartnermedneurologisksjukdom.5.77c924619b9d91e3e2d2f9.html
4. **Drop in för vägledning** (27 maj 2026, 13.00-15.00, Åkersberga Centrum) — career guidance
   - URL: /dropinforvagledning.5.77c924619b9d91e3e2a225.html
5. **Kom och prata framtidens Österåker med oss** (28 maj 2026, 11.00-14.00, Åkersberga) — civic dialogue
   - URL: /komochprataframtidensosterakermedoss.5.77c924619b9d91e3e2cee8.html
6. **Nya bygglovsregler – kom och ställ dina frågor på Ljusterö** (28 maj 2026, 15.00-, Ljusterö) — building permit info
   - URL: /nyabygglovsreglerkomochstalldinafragorpaljustero.5.77c924619b9d91e3e2cb2d.html
7. **Linedance och öppen dans på Ekbacken** (28 maj 2026, 18.00-21.30, Ekbacken Åkersberga) — line dancing, mixed adult
   - URL: /linedanceochoppendanspaekbacken.5.77c924619b9d91e3e2197f9.html
8. **Campfire i Båthuset på Runö Möten & Events** (29 maj 2026, 17.00-23.00, Båthuset Runö) — campfire event
   - URL: /campfireibathusetparunomotenevents.5.44fe6fa019e40e754cd330.html
9. **Campfire med livemusik i Båthuset på Runö Möten & Events** (29 maj 2026, 17.00-23.) — campfire + live music
   - URL: /campfiremedlivemusikibathusetparunomotenevents.5.44fe6fa019e40e754cd9c0.html
10. **Digital vägledning** (30 maj 2026, 11.00-14.30, Österåkers bibliotek) — digital help
    - URL: /digitalvagledning.5.77c924619b9d91e3e28a63.html
11. **Operasångerska lär oss ta höga C på Ljusterö** (30 maj 2026, 13.00-15.00, Ljusterö) — opera workshop
    - URL: /operasangerskalarosstahogacpaljustero.5.44fe6fa019e40e754cdba.html

### To publish — family/all ages (tag 0,18)
12. **Tävling i hundkapplöpning** (30 maj 2026, 13.00-15.00, Åkers Kanal Greyhound) — dog racing family event
    - URL: /tavlingihundkapplopning.5.77c924619b9d91e3e29c05.html
13. **Morsdagsbrunch på Runö Möten & Events** (31 maj 2026, 11.30-14.00, Runö) — Mother's Day brunch family
    - URL: /morsdagsbrunchparunomotenevents.5.44fe6fa019e40e754cd96d.html
14. **Slöjdalster och fika på Norrö** (31 maj 2026, 12.00-15.00, Tingshuset Norrö) — craft + fika
    - URL: /slojdalsterochfikapanorro.5.44fe6fa019e40e754cd1fa8.html

### Multi-date: combine into ONE event
15. **Konsert: Klang i kristallen – nytt datum** (31 maj 2026, two times: 15.00-16.15 AND 19.00-20.20) — concert, both at Åkersberga Bibliotek
    - URLs (2 instances - combine as 1 event with 2 dates):
      - /konsertklangikristallennyttdatum.5.77c924619b9d91e3e2b9ee.html
      - /konsertklangikristallennyttdatum.5.77c924619b9d91e3e2ba0e.html

## Next steps
1. Click "Se fler evenemang" to load more events from later dates (Jun-Dec 2026)
2. For each event: open detail page, scrape description + image, search dashboard, publish
3. Each publish via Dashboard UI: + Add Event button, fill form, push notifications OFF
4. After all source 1 done → move to source 2 (bibliotek.osteraker.se)

## API Discovery (in progress)
- POST /admin/events requires: title, description, images, dates, placeId (BigInt string), lat, lng, childMinAge, childMaxAge, parentMinAge, parentMaxAge, isFree, ctaLink
- shouldNotifyUsers + municipalityId may NOT be POST fields (got "additional properties" error)
- Likely needs to use Dashboard UI for proper publishing
- Or capture exact POST schema by submitting a real event through the UI with XHR spy installed

## Key blocker
The POST /admin/events endpoint schema needs to be discovered by spying on a real dashboard event creation flow. Then bulk script can be written.
