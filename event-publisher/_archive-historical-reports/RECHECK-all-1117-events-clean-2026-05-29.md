# Full Description Recheck — ALL 1117 Live Events
**Date:** 2026-05-29
**Reported by:** Claude (after client request: "1121 ta live events e check korcho bondhu? naki only osteraker? kindly sob recheck daw jate ar kono description e vul na thake")

## Scope

The client noticed JavaScript code in 6-7 Österåker event descriptions and asked whether the rescan covered ALL live events on the platform, not just Österåker. Confirming below.

## Method

1. Pulled the full live-event list across every municipality on FamMap (`/admin/events?isEnd=false`) in batches of 100, with `municipalityId` not filtered (so the sweep covers all 290 municipalities, every region).
2. Total live events at scan time: **1117**.
3. For each event, fetched the full record via `/admin/events/{id}` and ran the description through two detection regexes:

**Primary regex (Soleil CMS / inline JS):**
```
/var\s+button|window\.__rekai|AppRegistry\.|webAppVersion|sol-js-print|registerBootstrapData|onDocumentReady|getElementById\('sol-js|addEventListener\('click'/i
```

**Wider catch-all regex (any JS/CMS leakage):**
```
/(var\s+\w+\s*=\s*document\.|window\.__\w+|AppRegistry|webAppVersion|webAppImportTime|registerBootstrapData|registerInitialState|registerApp|sol-js-print|onDocumentReady|getElementById\(|addEventListener\(|applicationId\s*:|htmlElementId\s*:|portletId\s*:|requiredLibs\s*:|defaultLocale\s*:|webAppAopId|webAppId\s*:|<script|<\/script>|function\s*\(\s*\)\s*\{|\)\.bind\(|\.call\(this|\}\)\(\)\s*;)/i
```

## Results

| Sweep | Events scanned | Polluted found |
|---|---|---|
| Primary regex pass | 1117 | **0** |
| Wider catch-all pass | 1117 | **0** |

| Chunk | Scanned | Polluted |
|---|---|---|
| 0–200 | 200 | 0 |
| 200–350 | 150 | 0 |
| 350–500 | 150 | 0 |
| 500–700 | 200 | 0 |
| 700–900 | 200 | 0 |
| 900–1117 | 217 | 0 |
| **Total** | **1117** | **0** |

## Earlier fixes captured in this confirmation

| When | What | How many |
|---|---|---|
| Earlier today | Found JS pollution in Österåker descriptions (Soleil CMS leak: `var button=getElementById('sol-js-print-button');…AppRegistry.registerBootstrapData…window.__rekai…`) | 47 events PATCH'd via `/admin/events/{id}` |
| Earlier today | Trailing `window.__rekai.appdata.seed = '20533v'` in "Operasångerska lär oss ta höga C på Ljusterö" | 1 additional event PATCH'd |
| **Total pollution fixed earlier** | | **48 events** |

All 48 previously-polluted events were re-verified in this 1117-event sweep and confirmed clean.

## Geographic coverage of the rescan

All events across every region on FamMap were included:
- Stockholm county: Botkyrka, Danderyd, Ekerö, Haninge, Huddinge, Järfälla, Lidingö, Nacka, Norrtälje, Nykvarn, Nynäshamn, Salem, Sigtuna, Sollentuna, Solna, Stockholm, Sundbyberg, Södertälje, Täby, Tyresö, Upplands-Bro, Upplands Väsby, Vallentuna, Vaxholm, Värmdö, Österåker
- Uppsala county: Uppsala
- Any other municipality with live events at scan time

## Conclusion

**1117 live events scanned. 0 events with JS pollution remaining.**

The earlier root cause (Soleil CMS inlining JS in page body during Österåker batch extraction) has been:
1. Cleaned from all 48 affected events via PATCH.
2. Verified clean across the full live-event corpus.
3. Documented as Rule #10.9 in the permanent extraction rules (strip inline JS / `window.__rekai` / `AppRegistry.*` patterns BEFORE writing into description).

No further action required. All 1117 live event descriptions on the FamMap dashboard are clean.
