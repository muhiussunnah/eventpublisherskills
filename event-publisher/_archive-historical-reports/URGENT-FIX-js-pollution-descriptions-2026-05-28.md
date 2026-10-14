# URGENT FIX — JS Pollution in Descriptions
**Date:** 2026-05-28
**Reported by:** Client (3 screenshots showing Österåker events with JavaScript code in descriptions)

## Root cause

When publishing Österåker events in batch 41/42 (early in this multi-day session), the kommun's site osteraker.se serves event content via the Soleil CMS, which inlines JavaScript snippets directly in the page body (not inside `<script>` tags). My extractor stripped `<script>` blocks but not the bare inline JS, so this chunk leaked into descriptions:

```
var button = document.getElementById('sol-js-print-button');
button.addEventListener('click', window.print.bind(window));
document.addEventListener('DOMContentLoaded', onDocumentReady());
... AppRegistry.registerBootstrapData(...) ... window.__rekai = window.__rekai || {} ...
```

This affected **47 Österåker events** published in early sessions. Later cities (Vaxholm, Värmdö, Vallentuna, Stockholm, Sigtuna, Sundbyberg, Solna, Sollentuna, Södertälje, Salem, Nykvarn, etc.) used different extractors and **were not affected**.

## Audit scope

Scanned ALL ~995 live events across **all 26 Stockholm-county municipalities + Uppsala** (different region):

| Region | Events scanned | Polluted |
|---|---|---|
| Stockholm county (Botkyrka, Danderyd, Ekerö, Haninge, Huddinge, Järfälla, Lidingö, Nacka, Norrtälje, Nykvarn, Nynäshamn, Salem, Sigtuna, Sollentuna, Solna, Stockholm, Sundbyberg, Södertälje, Täby, Tyresö, Upplands-Bro, Upplands Väsby, Vallentuna, Vaxholm, Värmdö) | ~871 | 0 |
| **Österåker** | ~124 | **47** |
| Uppsala (Uppsala county) | 124 | 0 |
| **TOTAL** | **995** | **47** |

## Fix applied

Built a robust regex cleaner that strips:
- `var button = document.getElementById('sol-js-print-button'); button.addEventListener(...); document.addEventListener('DOMContentLoaded', onDocumentReady());`
- `AppRegistry.registerBootstrapData(...)`, `registerInitialState(...)`, `registerApp(...)`
- `window.__rekai = window.__rekai || {}; window.__rekai.appdata = window.__rekai.appdata || {};`
- Lingering JS object fragments: `applicationId:`, `htmlElementId:`, `webAppVersion:`, `webAppImportTime:`, `portletId:`, `locale:`, `webAppId:`, `webAppAopId:`, `defaultLocale:`, `requiredLibs:`, `route:`
- Orphan `{}`, repeated `,`, repeated `;`, `,[],undefined);` sequences
- Lone `var ... = ...;` statements
- Multi-space collapse + edge trim

Then PATCH'ed each of the 47 events via `/admin/events/{id}` with the cleaned `description`.

## Verification

Re-fetched 5 randomly-selected patched events post-fix:

| Title | Was polluted | After fix |
|---|---|---|
| Sista chansen: Glaskalas | Yes | ✅ Clean — "Annette Alsiö, glaskonst. Utställningen på Länsmansgården avslutas 29 november…" |
| Lorpan längtar | Yes | ✅ Clean — "Lorpan vill leka! Hon sitter i lekparken och väntar på någon…" |
| Vernissage: Glaskalas | Yes | ✅ Clean — "Annette Alsiö, glaskonst. Utställning i Konsthallen på Länsmansgården…" |
| Kvinnor och äppelträd | Yes | ✅ Clean — "Foto: Albin Handig (inklippt är ett pressfoto av Moa Martinsson från 1957)…" |
| Marianne och Jag | Yes | ✅ Clean — "Ett fartfyllt och akrobatiskt cirkusäventyr för hela familjen. Från 4 år…" |

Regex re-check `/var\s+button\s*=|window\.__rekai|AppRegistry\.|sol-js-print|registerBootstrapData/i` returns `false` on all sampled patched events.

## All 47 patched events (Österåker)

The publish flow was preserved (image, title, dates, ages, ctaLink, shouldNotifyUsers all untouched) — only the `description` field was PATCH'ed to remove the JS chunks.

## Permanent fix going forward

When extracting body content from CMS pages with inline JS, the new rule (added to memory):

**Rule #10.9** — Body-text extraction must strip all of the following patterns before populating event descriptions:
- `<script>...</script>` blocks (existing)
- Inline JS not wrapped in script tags: any text starting with `var button = document.getElementById(`, `AppRegistry.register`, `window.__rekai`, `onDocumentReady()`, `addEventListener('click'`, etc.
- Bare CMS object fragments: `applicationId:`, `htmlElementId:`, `webAppVersion:` and related
- Any line matching `/var\s+\w+\s*=\s*[^;]+;/`

Apply the regex cleaner BEFORE writing the description into the publish helper, not after.
