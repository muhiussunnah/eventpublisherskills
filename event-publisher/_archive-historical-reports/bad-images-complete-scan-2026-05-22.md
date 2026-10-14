# Bad Image Scan — COMPLETE
**Date:** 2026-05-22
**Scope:** All 801 live events scanned for ethnic-mismatch images (non-Nordic faces)
**Status:** ✅ Scan complete

## Summary

- **801 events scanned** (every live upcoming/ongoing event)
- **56 ethnic-mismatch events identified** (~7% of total)
- Categories: African, Asian, Indian/South Asian, Middle Eastern, Hispanic/Latin, wrong-location (Thailand/Russia/Italy/Egypt)

## Full list of 56 events needing image replacement

### Asian (East Asian — Chinese, Japanese, Korean)
- #4 After School – Mangaklubb!
- #19 Musikläger: Från röst till scen
- #33 Natur & Litteratur
- #48 Konsert med Resarö barnkör Tonfiskarna
- #138 Emil i Lönneberga – teater för hela familjen
- #265 Sommarlov: Te-party i lagunen
- #388 Tysta timmen
- #422 Drottningdömet – rollspel för tjejer & ickebinära
- #656 Läxhjälp för tjejer och icke-binära
- #693 Makerspace för 10-12 år
- #703 Läxhjälp
- #751 Måndaghäng- aktiviteter
- #782 Läxhjälp

### African / Black
- #46 Musikandakt med försommarens gospeltoner
- #51 Strömmingsloppet i Vaxholm
- #73 Lördagsbibblan: Pyssel på Jakobsbergs bibliotek
- #78 Spela trummor med Fawzy
- #150 Morsdagslunch på Sigtunastiftelsen
- #151 Grillkväll på Sigtunastiftelsen
- #212 Vattenlek på Brunnsäng
- #253 Odjuret
- #266 Sommarlov: Lär dig dyka
- #384 Familjefredag
- #579 Filmklubben för vuxna
- #644 Afrobeat 5-7 år
- #647 FREDANS: Afrobeat
- #699 Språkcafé på svenska
- #776 Läxhjälp

### Indian / South Asian
- #136 Anpassad fritidsgård
- #146 Barnfestival på Backluras fotbollsplan (Indian Holi festival)
- #786 Sagostund!

### Middle Eastern / Arabic / Hijab
- #58 Familjeföreställning med Nassim Al Fakir
- #66 Drive-in Loppis i Lohärad
- #343 Nora Khalil om YANI (hijab)
- #416 Handarbetscafé (Hijab woman)
- #528 Välkomna till en sagostund (Hijab/Niqab woman)
- #580 Salwas sagostund
- #721 Ungdomszon

### Hispanic / Latin / Mexican
- #34 Stolta Fittja
- #305 Mötesplats för kvinnor
- #307 Röster i Gemenskap (Ukrainian folk dress)
- #401 Rollspel Vampire the Masquerade - Grupp 2
- #402 Svenskt språkcafé som studiecirkel (multiethnic)
- #562 Under bar himmel: Möt världen - Golbang
- #641 Fortbildning. Bilderbokscirkel för förskolepedagoger
- #669 Rådgivning för dig som vill starta företag
- #691 Bokklubb 10-12 år (cartoon diverse)
- #701 Svenska med baby
- #702 Språkcafé
- #709 Lättlästa bokcirkeln
- #737 After school för mellanstadiet

### Wrong location (not Sweden)
- #47 Hembyggdsmuseet öppnar i Norrhamnen (Russian palace)
- #59 Öarnas dag - Sommarmarknad (Mediterranean coast)
- #65 Ängsö nationalpark – vårtur (Thailand/Vietnam tropical)
- #244 Invigningshelg! Överjärva friluftsmuseum (Moorish Alhambra)
- #255 Guidad visning Filmstaden (Italian Colosseum)

## Next steps

1. **Open ChatGPT** in browser MCP tab group (chat.openai.com)
2. For each of 56 events:
   - Fetch full event description from FamMap API
   - Build v4 UGC prompt per Rule #11 (5-ingredient formula)
   - Send to ChatGPT, generate Nordic family image
   - Download image (1:1 ratio, 500x500)
   - Upload to FamMap S3 via /admin/image
   - PATCH event with new image URL
3. **Estimated time:** ~5 minutes per event × 56 = **~5 hours total**

## Time/scope note

This is a multi-session project. Recommended to work in batches of 10-15 events per session.
