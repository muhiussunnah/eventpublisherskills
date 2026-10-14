# Famies Event Publishing - Exception Rules

## Rule #1: Duplicate Image Handling
**When:** Multiple events have the same image (same source image used for different events), making the app look repetitive and bad.

**Action:** Generate a unique, kid-friendly image using ChatGPT (already logged in on the browser).

**Image Prompt Format:**
```
authentic vertical 1:1 photo of Nordic children [activity/description-based keywords]
```

**Requirements:**
- Size: 500x500 (1:1 ratio) — this is the best size for Famies event cards
- Style: Authentic photo, NOT illustrated/cartoon
- Children: Nordic children specifically (targeted audience is Swedish kids and parents)
- Content: Based on the event description/activity (e.g., "reading books in a library", "playing piano", "painting outdoors")
- Always use "vertical 1:1" in the prompt

**Process:**
1. Detect if the same image is being used by multiple events
2. Keep the original image on ONE event
3. For the other event(s), go to ChatGPT in browser
4. Generate image with the prompt format above, tailored to that event's description
5. Download the generated image
6. Upload it to the event on the Famies dashboard (edit the event, replace image)

## Rule #2: Recurring Events — Single Event with Multiple Date Ranges
**When:** A source event has multiple dates (e.g., every Saturday in May, or specific recurring dates).

**Action:** Create ONLY ONE event on the Famies dashboard with multiple date ranges — do NOT create separate events for each date occurrence.

**Requirements:**
- One event = one title + one description + one image + one venue
- Multiple date ranges within that single event (use "Add Date Range" button for each date)
- Each date range should have the correct start and end time

**Process:**
1. Identify all dates for the recurring event from the source page
2. Create a single event with the first date
3. Use "+ Add Date Range" to add each additional date
4. Set the correct time (start and end) for each date range
5. Confirm all dates are added before publishing/updating

**Why:** Creating separate events for each date makes the app look cluttered and repetitive. Users see the same event multiple times, which is a bad experience. One event with multiple dates is cleaner.

## Rule #3: Text-Heavy Image Replacement
**When:** The source event's image contains prominent text (event titles, logos with text, banners with text, poster-style images). The Famies app uses 1:1 square image cards, so text-heavy images get cropped and look bad on mobile — text gets cut off and becomes unreadable.

**Action:** Do NOT use the source text-heavy image. Instead, generate a unique, kid-friendly image using ChatGPT based on the event description.

**How to Detect:**
- Image has large text/title overlaid on it (e.g., "LÄSMYS", "KLÄDBYTARDAGEN", poster-style)
- Image is a flyer/poster with event details as text
- Image where text is the primary visual element (not just a small watermark/logo)

**Image Prompt Format:**
```
authentic vertical 1:1 photo of Nordic children [activity based on event description]
```

**Requirements:**
- Same as Rule #1: Size 500x500, authentic photo style, Nordic children, based on description
- Generate a DIFFERENT style if this event's generated image might look similar to another nearby event's generated image
- The image should visually represent the EVENT ACTIVITY, not the text content

**Process:**
1. Check if the source event image is text-heavy
2. If yes, do NOT use it — generate a new image via ChatGPT
3. Use the event description to determine what activity to depict
4. Generate and upload the image to the Famies dashboard

**Why:** Text-heavy images get cropped in the 1:1 card layout on mobile, making them look unprofessional and unreadable. A clean activity-based photo looks much better on the Famies app.

## Rule #4: Skip Irrelevant / Senior-Only Events
**When:** The source event is clearly irrelevant to the Famies target audience (families with children, age range 0–49).

**Action:** Do NOT publish the event. Skip it entirely.

**Events to SKIP:**
- Events targeted at seniors (50–60+ years), e.g., "senior träff", "pensionärsaktivitet", events explicitly for elderly
- Events that are very irrelevant to families/children, e.g., lawyer help, legal advice ("advokat"), advocacy events
- Any event where the target audience is clearly NOT families or children/young people

**Events to PUBLISH (even if not explicitly for kids):**
- Events for age range 0–49 (children, teens, young adults, parents)
- General community/culture events that families could attend
- Events that don't specify a narrow senior-only audience

**Why:** Famies is a family app. Publishing senior-only or irrelevant professional events (lawyer, advocate) clutters the feed and confuses users. Only events relevant to families and younger audiences should be published.

## Rule #5: All Images Must Be Audience-Targeted (Kids + Parents)
**When:** ANY event image — whether from the source or AI-generated — is being used on the Famies dashboard.

**Core Principle:** The Famies app is for families with children (target: 0–12 years). Every image must feel relevant to THIS audience when users scroll the events feed. The image should not just represent the event topic generically — it must show kids and/or parents engaging with that topic.

**BAD examples (topic-only, no family connection):**
- Swedish flag alone for "Fira nationaldagen" → feels like a news article, not a family event
- Just birds or forest scenery for a nature event → no family connection
- A generic landscape or object photo → users scroll past, feels irrelevant

**GOOD examples (same topic BUT family-targeted):**
- "Fira nationaldagen" → Nordic kids waving small Swedish flags, families celebrating together outdoors
- Nature/bird event → A toddler pointing excitedly at a flying bird, parent and child birdwatching together
- Art exhibition → Kids painting at an easel, family looking at art together
- Music event → Children playing instruments, family dancing together

**Image Prompt Format (updated):**
```
authentic vertical 1:1 photo of Nordic children/families [engaging with the event activity in a way that feels warm, relatable, and relevant to parents browsing a family events app]
```

**Requirements:**
- ALWAYS include kids and/or parents in the image — never just objects, scenery, or flags alone
- The image must make a parent scrolling the Famies app think "this is for us / my kids would love this"
- Show ENGAGEMENT — kids doing, touching, watching, playing, reacting — not just standing
- Nordic children (Swedish target audience)
- Authentic photo style, 500x500, 1:1 ratio

**Apply this rule to:**
1. AI-generated images (Rule #1, #3) — always generate with family audience in mind
2. Source images that are generic/non-family — replace with a generated family-targeted image
3. Source images that already show kids/families engaging — keep as-is, these are perfect

**Why:** Famies users are parents looking for activities for their kids. When they scroll the events feed, every card image should immediately communicate "this is a family-friendly event." A Swedish flag or a lone bird doesn't do that. But kids waving flags or a child watching birds — that creates instant relevance and engagement.

## Rule #6: Missing Organizer/Venue — Use the Source Website
**When:** An event does not have a specific arranger/organizer name, or does not have a real physical address/venue.

**Action:** Use the SOURCE WEBSITE (where the event was scraped from) as both the organizer and the venue.

**Process:**
1. Check if the event has a specific organizer name (e.g., "Bibliotek Vallentuna", "Kultur Vallentuna") → If yes, use it
2. If NO specific organizer → Create an organizer using the source website name (e.g., "Vallentuna kommun" for vallentuna.se events)
3. Check if the event has a specific venue/address → If yes, use it
4. If NO specific venue/address → Create a venue using the source website name as the venue name
5. Then publish the event with these

**Example:**
- Source: vallentuna.se, event has no specific arranger or location
- Organizer: "Vallentuna kommun" (or use existing one if already created)
- Venue: "Vallentuna kommun" (or use existing one if already created)

**Why:** Every event on the Famies dashboard requires an organizer and a venue. When the source doesn't provide these details, the source website itself is the best fallback — it tells users where the event information came from.

## Rule #7: No Image Provided — Generate via ChatGPT
**When:** An event has all required information (title, description, date, venue, organizer) but the source does NOT provide any image.

**Action:** Generate a relevant, family-targeted image using ChatGPT, then use it to publish the event.

**Process:**
1. Notice the source event page has no image at all
2. Go to ChatGPT in the browser
3. Generate an image based on the event description, following Rule #5 (audience-targeted: kids + parents)
4. Upload the generated image to the Famies dashboard event
5. Publish the event as normal

**Image Prompt Format (same as Rule #5):**
```
authentic vertical 1:1 photo of Nordic children/families [engaging with the event activity]
```

**Requirements:**
- Follow all Rule #5 guidelines (kids/parents in image, engagement, Nordic, 500x500)
- Image must be relevant to the event topic/activity
- Never publish an event without an image — always generate one if missing

**Why:** Every event on Famies needs an image for the card layout. A missing image would break the UI or look unprofessional. Generating a relevant family-targeted image ensures consistent quality across all events.


## Rule #8: City-Aware Duplicate Check (Multi-City Context)

**When:** Working with event sources from multiple cities (27+ Swedish municipalities). A single event title may exist on the dashboard but belong to a DIFFERENT city than the one currently being processed.

**Action:** Before skipping an event as a "duplicate", verify the existing event belongs to the SAME city as the one being published. If it's from a different city, it is NOT a duplicate — publish the new event.

**The Problem:**
Yesterday published "Bim Bam Bom" under Vallentuna kommun. Today processing Haninge kommun — the same event title "Bim Bam Bom" exists in Haninge too but as a DIFFERENT event (different venue, different organizer, different date). Searching the dashboard by title alone would show the Vallentuna version and incorrectly mark the Haninge event as a duplicate.

**City Verification Steps:**
1. Search the Famies dashboard by event title
2. If no results → NOT a duplicate, proceed to publish
3. If results found → for each matching event, check:
   - **Venue city** (e.g., "Vallentuna bibliotek" vs "Haninge kulturhus")
   - **Organizer** (e.g., "Kultur Vallentuna" vs "Kultur Haninge")
   - **Source URL / CTA link** (vallentuna.se vs haninge.se)
4. If ALL matching events are from DIFFERENT cities → NOT a duplicate, publish the new event
5. If ANY matching event is from the SAME city → IS a duplicate, SKIP

**Examples:**

**Scenario A — Publish (different cities):**
- Currently processing: "Bim Bam Bom" from haninge.se (target city: Haninge)
- Dashboard search shows: "Bim Bam Bom" under Vallentuna bibliotek, organizer "Kultur Vallentuna"
- Decision: Different city → PUBLISH the Haninge version

**Scenario B — Skip (same city):**
- Currently processing: "Kreativt skrivande" from vallentuna.se (target city: Vallentuna)
- Dashboard search shows: "Kreativt skrivande" under Vallentuna bibliotek
- Decision: Same city → SKIP as duplicate

**Scenario C — Publish (no match):**
- Currently processing: "Sommarfest" from botkyrka.se
- Dashboard search shows no results
- Decision: Not a duplicate → PUBLISH

**Why:** Famies covers 27+ Swedish cities. Many Swedish events share names (e.g., "Sommarfest", "Familjedag", "Bokcirkel") across different municipalities but are genuinely separate local events. Skipping them as duplicates would leave users in other cities without local events. City context is as important as title when determining duplicates.

**Implementation Note:** Always track the "current city context" when batch-processing events from a source URL. The city/municipality of the source URL determines the city context for ALL events scraped from that source. Use this city context to compare against the venue/organizer/source URL of matching events on the dashboard.


---

## Rule #9: Image Prompt Writing Style (Authentic Nordic UGC-Style)

**Context:** All images must look like authentic real Swedish/Nordic family moments — NOT cartoonish, illustrated, or studio-staged. Images should feel like a candid phone snapshot from a real Swedish home or public space.

### The Required Prompt Formula (5-part structure)

```
Authentic vertical 1:1 photo of Nordic [subject] + [activity + setting] + [realism details] + [natural light] + [mood]. Real life, not staged.
```

### 5 Ingredients Explained

1. **Subject** — Nordic/Scandinavian children, parents, families (specify ages, hair, skin naturally)
2. **Activity + Setting** — concrete action in a real Swedish/Nordic environment (home kitchen, förskola, park, biblioteket, lekplats, skog)
3. **Realism details** — slight motion blur, imperfect framing, everyday clothes, real textures, visible toys/books/snacks
4. **Natural light** — soft window light, overcast Nordic daylight, lamp glow, golden hour through trees
5. **Mood** — warm, calm, joyful, cozy, curious, focused — never posed or plastic

### Strict DON'Ts

- ❌ NO cartoon, illustration, anime, 3D render, CGI, Pixar, digital art
- ❌ NO studio lighting, white backdrops, professional photoshoot look
- ❌ NO overly perfect/staged compositions — must feel candid
- ❌ NO HD/4K/8K/hyperrealistic tags — these push toward plastic look
- ❌ NO models, stock photo aesthetic, or commercial vibes
- ✅ ALWAYS end the prompt with "Real life, not staged."
- ✅ ALWAYS use 1:1 aspect ratio (500x500 output) — Famies event cards are square
- ✅ ALWAYS specify Nordic/Swedish/Scandinavian subjects

### Client-Approved Sample Prompts (1:1)

**1. Barnkalas (Children's party)**
Authentic vertical 1:1 photo of Nordic children around age 5–7 at a cozy Swedish birthday party at home. Kids laughing, blowing out candles on a simple homemade cake. Balloons tied to chairs, paper plates, juice glasses, one child in a paper crown. Warm window light, slight motion blur from movement, imperfect framing. Joyful, real, candid. Real life, not staged.

**2. Helgplaner (Weekend plans)**
Authentic vertical 1:1 photo of a Nordic family of four packing a weekend bag in a bright Swedish hallway. Parents helping two kids zip jackets, one child holding a stuffed animal, rain boots by the door. Overcast Nordic daylight through the window, soft shadows. Calm, everyday energy. Real life, not staged.

**3. Efter skolan (After school)**
Authentic vertical 1:1 photo of a Nordic child age 8 at the kitchen table eating a mellanmål — yogurt with berries and a knäckebröd sandwich. Backpack on the floor, jacket on the chair. Soft afternoon light from a window, slightly messy kitchen counter in background. Quiet, tired-happy mood. Real life, not staged.

**4. Enkel middag (Simple dinner)**
Authentic vertical 1:1 photo of a Nordic family around a small wooden dining table eating pannkakor with jam. Two kids age 4 and 7, parents serving, milk glasses, a simple IKEA-style kitchen in background. Warm evening lamp light. Cozy, real, unposed. Real life, not staged.

**5. Gratis aktiviteter (Free activities)**
Authentic vertical 1:1 photo of Nordic kids age 5–9 playing at a public Swedish lekplats on an overcast day. Kids climbing the wooden play structure, one on a swing, parents chatting on a bench in the background. Jackets, rubber boots, slightly muddy ground. Natural gray daylight. Real, candid. Real life, not staged.

**6. Regniga dagar (Rainy days)**
Authentic vertical 1:1 photo of a Nordic child age 6 sitting by a rainy window inside a cozy Swedish apartment, drawing with crayons on paper. Raindrops on the glass, soft lamp light, a blanket on the sofa nearby. Calm, focused mood. Slight reflection in the window. Real life, not staged.

**7. Lekplatser (Playgrounds)**
Authentic vertical 1:1 photo of Nordic children age 3–7 on a Swedish neighborhood playground in spring. Kids in overalls, one on a slide, one digging in sand, a parent kneeling to help. Birch trees in background, soft morning light. Candid, joyful, real. Real life, not staged.

**8. Utflykter nära (Nearby outings)**
Authentic vertical 1:1 photo of a Nordic family walking on a forest path in the Swedish countryside. Two kids age 4 and 8 ahead of parents, one holding a stick, autumn leaves on the ground. Soft dappled sunlight through birch and pine trees. Peaceful, adventurous mood. Real life, not staged.

**9. Lov (School holidays)**
Authentic vertical 1:1 photo of Nordic siblings age 5 and 9 in pajamas on a Swedish living room floor, building a pillow fort with blankets from the sofa. Morning light through the window, toys scattered, parent reading in background. Relaxed, playful. Real life, not staged.

**10. Aktiviteter (Activities)**
Authentic vertical 1:1 photo of a Nordic child age 7 at a Swedish kommun-run pottery workshop, hands muddy with clay, focused on shaping a bowl. Other kids working in soft background blur, wooden tables, warm overhead light. Curious, immersive mood. Real life, not staged.

**11. Orkar inte planera (Can't be bothered to plan)**
Authentic vertical 1:1 photo of a Nordic parent age 35 on a Swedish living room sofa with a tired smile, two young kids age 3 and 6 climbing on them with a picture book. Messy blankets, a cup of kaffe on the side table. Soft evening light. Warm, imperfect, real. Real life, not staged.

**12. Vardagsvinster (Everyday wins)**
Authentic vertical 1:1 photo of a Nordic child age 4 proudly holding up a drawing to a parent in a Swedish kitchen. Parent kneeling, smiling, fridge covered in other drawings and magnets in background. Afternoon light. Tender, authentic moment. Real life, not staged.

### Adaptation Examples (applying the formula to Famies events)

**Event: Sagostund på biblioteket**
`Authentic vertical 1:1 photo of Nordic children age 3–5 sitting cross-legged on a colorful rug at a Swedish public library storytime. A librarian reading a picture book, kids watching intently, one with thumb in mouth. Soft indoor library light, bookshelves in background. Calm, curious mood. Real life, not staged.`

**Event: Pianokurs för nybörjare**
`Authentic vertical 1:1 photo of a Nordic child age 8 at an upright piano in a Swedish music school room, concentrated, small hands on the keys. Sheet music on the stand, wooden floor, natural daylight from a window. Focused, gentle mood. Real life, not staged.`

### Why This Rule Matters

Famies is a brand built on **real Swedish family life**. Users scroll the app to find events for their real kids — the images must feel like something a Swedish parent would actually photograph, not a stock illustration or a commercial shoot. Authentic UGC-style Nordic images drive trust, engagement, and conversion. Any cartoon/illustrated/staged image breaks the brand feel and must be regenerated.

## Rule #10: Bulk Image Fix via API (Not UI Clicking)
**When:** Many already-published events (10+) need images fixed/added/replaced. Clicking through the dashboard UI for each is slow and brittle.

**Action:** Use the Famies admin API directly to upload images and PATCH events. Drive it from the ChatGPT tab (so `fetch` on the ChatGPT origin can also read generated image blobs).

**The three-endpoint flow per event:**
1. `GET https://api.fammap.app/admin/events/{id}` — fetch the full event so you can PATCH with the complete body
2. `POST https://api.fammap.app/admin/image` with `multipart/form-data` `file=…` — returns `{data: {image: "https://fammap-storage.s3…/event/…webp"}}`
3. `PATCH https://api.fammap.app/admin/events/{id}` with the full body + `images: [s3Url]`

All three need headers: `Authorization: Bearer <JWT>`, `Platform: web`, `Version: 0.0.0`.

**PATCH body must include ALL of these** (partial body = 400):
`placeId, title, description, images, lat, lng, address, isFree, parentMinAge, parentMaxAge, childMinAge, childMaxAge, ctaLink, ctaText, dates`

**Why:** Publishing 67 images took ~45 minutes via API vs. an estimated 8+ hours via UI clicking, with zero page-navigation fragility. Each PATCH is independent so rate-limit or crash recovery is trivial.

## Rule #10.5: Image Source Priority — SOURCE FIRST, ChatGPT only as Fallback (CORRECTED v4 FINAL — 2026-05-27)

**When:** Choosing the image for any event being published or fixed.

**Image source priority — ALWAYS in this order:**

1. **DEFAULT — Use the real source-page image** (e.g., vallentuna.se/.../event.jpg, destinationX.se og:image, svenskakyrkan event photo)
   - Provided it passes the quality gate:
     - Is a clean photo, NOT a text-heavy poster/flyer
     - Resolution is reasonable (not pixelated/tiny)
     - Content is relevant (shows the activity, venue, or family-friendly context)
     - Not a generic placeholder, watermark, or logo
   - If source image passes → re-host via fammap S3 and publish

2. **FALLBACK — Generate via ChatGPT** ONLY IF the source image fails the quality gate:
   - Image has heavy text overlay (event title, dates, large logos with text) — text gets cropped in 1:1 card
   - Image is blurry, pixelated, or poor resolution
   - Image is a generic placeholder, default site logo, or default building photo shared across many events
   - No source image exists at all
   - Source image is on a venue/site that blocks hotlinking / CORS / wsrv.nl proxy fails

3. **ABSOLUTELY FORBIDDEN — Stock photo libraries** (no exceptions, not even as fallback):
   - ❌ Unsplash (images.unsplash.com)
   - ❌ Pexels, Pixabay
   - ❌ Any "opensource" / "royalty-free" image database
   - ❌ Wikimedia, Flickr, Google Images, any web stock library
   - ❌ Any AI image site OTHER than the user's logged-in ChatGPT tab

**Why this priority order matters:**
- Source images carry authenticity — they ARE the event, photographed at the venue
- They preserve attribution and accuracy (right person, right place, right activity)
- ChatGPT generation is slower and produces approximations — only use when source fails
- Stock photos break Famies' authentic Nordic UGC brand feel

**Decision flow per event:**
1. Fetch source detail page → find primary content image (og:image, hero img, body img)
2. Inspect: clean photo? readable size? activity-relevant? non-text-heavy? no shared default?
3. **If YES → use source image** (re-host via wsrv.nl → fammap S3 → publish)
4. **If NO → generate via ChatGPT** using Rule #9 UGC 5-ingredient formula
5. Never publish without an image

**ChatGPT fallback process:**
1. Open the logged-in ChatGPT tab in the user's browser
2. Generate using Rule #9 (UGC 5-ingredient formula) — Nordic subjects, real venue, candid feel
3. Re-host via tmpfiles.org → fammap-storage S3 via wsrv.nl proxy
4. POST/PATCH event with the fammap-storage URL

**If ChatGPT is not accessible AND source image fails the quality gate:**
- STOP publishing that event
- ASK the user to open / re-login the ChatGPT tab
- Do NOT fall back to Unsplash or any stock library

**Cross-reference:** Rules #1, #3, #5, #7, #9, #10, #11 reference ChatGPT — those still apply, but only WHEN the fallback condition is triggered. Source image FIRST.

---

## Rule #10.6: In-Depth Coverage Per City — Exhaust ALL Sources + Web Search (NEW v4 FINAL — 2026-05-27)

**When:** Publishing events for any Swedish municipality.

**Rule:** Every city MUST receive IN-DEPTH event coverage. Surface-level scraping of one source is NOT acceptable. Each city is treated as a "complete coverage" mission, not a "few events to publish" task.

**Mandatory completeness checklist per city:**

1. **ALL official kommun sources** — main events calendar, kultur kalendar, fritid pages, library pages, all linked sub-pages
2. **ALL pagination/show-more** — click "Nästa", "Visa fler", page 2/3/4/etc until source is exhausted
3. **ALL tourism / destination sites** — destinationX.se, hejaX.se, visit-X.se if they exist
4. **Svenska kyrkan church events** — svenskakyrkan.se/{kommun}
5. **All municipality venues** — bibliotek, kulturhus, teater, museum, idrottshall, badhus, ungdomsgård
6. **Ticketmaster + Tickster + Billetto** — search by city name
7. **Local cultural associations** — hembygdsförening, konstförening, scouter, körer, idrottsklubbar
8. **Local Facebook event pages** — kommun page, kulturhus page, museum page (if accessible)
9. **Local specific venues from destinations site** — for Vaxholm: Vaxholms fästning, Vaxholms slott, Bogesunds slott. For Värmdö: Artipelag, Gustavsberg porslinsmuseum, etc.
10. **WEB SEARCH for hidden/unique events** — explicit Google/Bing search for "events {city} 2026", "evenemang {city} sommar 2026", "{city} familjedag", "{city} festival", "{city} marknad" to surface events not on official kommun calendar

**Mandatory web search step after kommun sources:**
- Use WebSearch tool with queries like:
  - "evenemang {city} 2026 sommar"
  - "{city} familjeaktiviteter juni juli 2026"
  - "{city} barn aktiviteter 2026"
  - "{city} marknad 2026"
  - "{city} festival 2026"
  - "{city} öppet hus 2026"
  - "konsert {city} 2026"
  - "teater {city} 2026"
- Cross-reference results with what's already published — publish any new genuine events
- Local newspapers (mitti.se, dagensindustri.se, lokaltidningen), local blogs, Facebook public events ALL searchable via web search

**FORBIDDEN behavior:**
- ❌ Publishing only "a few" events from a city because the official calendar showed limited results
- ❌ Stopping coverage when one source has been processed if other sources exist
- ❌ Skipping web search step — every city gets web search
- ❌ Treating any city as "done" without going through the full 10-step checklist

**Why:** Famies users expect their city to have rich event coverage. A user opening Vallentuna and seeing 8 new events when the calendar had 70+ visible (and other sources/web has dozens more) damages trust. A user opening any city should see comprehensive, diverse, accurate event coverage. The goal is parity across all cities.

**Effort estimate per city:** Plan for 30-60 events per active city (or however many genuinely exist). NEVER cap at "10 events good enough."

---

## Rule #10.7: Complete the City BEFORE Reporting (NEW v4 FINAL — 2026-05-27)

**When:** Working through any city's event publishing job.

**Rule:** Do NOT pause mid-city to ask the user questions, request approval, or seek confirmation. Complete the entire city's in-depth coverage (per Rule #10.6) end-to-end, then deliver a SINGLE final report at the end.

**Forbidden mid-city behaviors:**
- ❌ "Should I continue?" / "Continue korbo?"
- ❌ Asking for direction halfway through
- ❌ Multiple interim status reports per city
- ❌ Treating each batch as "done" and waiting for user

**Required behavior:**
- ✅ Complete all 10 source-checklist steps per Rule #10.6 in one continuous flow
- ✅ Trust your own judgment for category filtering, age tagging, image decisions
- ✅ Only one consolidated FINAL report per city when truly done
- ✅ Final report MUST include the exact before/after/total live event numbers, e.g. "Vallentuna: 30 → 71 (+41 net new). 71 total live events published."

**Final report mandatory fields:**
1. Events BEFORE this session (count)
2. Events AFTER this session (current live count)
3. Net new events published this session
4. Total live events on dashboard for this city
5. Rule audit results (issues, duplicate images)
6. Sources processed (all 10 from Rule #10.6 checklist)
7. Remaining work for next session (if any)

**Why:** The user does not want to be a babysitter during one city's work. They want clean before/after numbers and confidence that everything was done. Mid-flow questions break the trust-and-execute relationship.

---

## Rule #11: UGC 5-Ingredient Image Prompt Formula
**When:** Generating event images via ChatGPT. Replace or supplement the older "authentic vertical 1:1 photo of Nordic children…" template with this richer formula for brand-quality results that feel like real phone snaps, not stock photos.

**Formula (all 5 ingredients in every prompt):**

1. **Subject** — who (Nordic Swedish babies 0-2, preschoolers 3-5, kids 6-10, tweens 9-12, teens 13-17, family with kids of mixed ages, young adults with support needs, etc.)
2. **Activity + Venue** — what and where, with the real Swedish place name + address where known (e.g., "at Brandbergens bibliotek", "at Vega aktivitetshus on Moränvägen")
3. **Realism anchors** — "authentic candid 1:1 UGC phone photo, not staged, natural light, slight motion blur"
4. **Emotional tone** — warm, cozy, curious, joyful, focused — never posed or sterile
5. **Closing tag** — always end with: "Real life, not staged."

**Process:**
1. Identify the event activity and venue from the event description
2. Choose the right subject age range based on the event's childMinAge/childMaxAge
3. Compose the prompt using all 5 ingredients
4. Generate in ChatGPT at 1:1 (500x500) aspect ratio
5. Verify it looks like a real phone snap, not a stock photo or illustration

**Why:** The 5-ingredient formula produces consistently authentic images that match the Famies brand — real Swedish family moments that parents trust and engage with.

---

## Rule #28: Age Classification — Read Like a Swedish Parent (v3.0)

**Supersedes:** All previous age classification rules (v1.0 fixed-canonical-table, v2.0 Type A/B/C/D + regex + headroom + snap). This is a complete rewrite as of 2026-05-18.

**When:** Setting `childMinAge` / `childMaxAge` on every event POST or PATCH.

### The Core Principle

The agent reads the event title and description and asks ONE question:

> **"Which children, if any, does this event genuinely fit for?"**

Not "is it allowed for kids?" Not "does the description mention kids?" Not "what does a regex match?"

**Genuine fit.** Like a Swedish parent reading the description and asking "is this for my kid?"

The agent thinks before answering. It considers the actual content of the event, the venue, the time of day, the language used, and the implicit signals a Swedish parent would pick up on.

### Step 0: Parent age — always fixed

- `parentMinAge: 18`
- `parentMaxAge: 100`

Never changes. Never touch these values.

### Step 0.5: FORBIDDEN values (v3 FINAL — 2026-05-21)

**FORBIDDEN values — NEVER use these:**
- `childMaxAge=17` is **NEVER** allowed. If you'd write 17, write **18** instead.
- `childMinAge=17` is **NEVER** allowed.

**Allowed `childMaxAge` values:** 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, **18**, OR null.
(Note: 17 is skipped entirely. Use 18 as the "open upward" marker.)

**Allowed `childMinAge` values:** 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, OR null.

**Why childMaxAge=17 is forbidden:** The app renders childMaxAge=17 as a "max 17" badge, which looks wrong. Using 18 instead produces correct badge display ("För alla åldrar" when combined with childMinAge=0, or "X-18 år" for specific ranges).

**API note on null:** The API currently stores null as 0,0 (not true null). Until the backend is fixed, use `18, 18` for adult-only events instead of null,null.

### Step 1: Read the entire description carefully

Read the title, description, venue name, and start time. Build a mental picture of the event.

Ask:
- What actually happens at this event?
- Who is doing the activity?
- What language and tone is used?
- Is there a stated age in the source text?
- Are there concrete child elements (pony rides, face painting, kids' performance) or only soft language ("hela familjen välkommen")?

### Step 2: Pick ONE of four answers

There are exactly four possible outputs. No other answers are valid.

#### Answer A: Specific kid age range
**Output:** `childMinAge=X, childMaxAge=Y` where X and Y are the real ages this event fits.

Use this when the event is genuinely for children of a specific age. The range reflects REAL fit, not a safety net.

**Examples:**
| Event | childMinAge | childMaxAge | Why |
|---|---|---|---|
| Babybabbel | 0 | 1 | Babies are 0-1. Period. (v3 FINAL) |
| Sagostund för småbarn | 1 | 4 | Toddlers' attention span |
| Knattefotboll | 3 | 6 | "Knatte" = preschool ages |
| Bakworkshop för barn från 5 år | 5 | 12 | Stated age min, kid baking tops at ~12 |
| Barnteater 6-9 år | 6 | 9 | Exact stated range |
| Mellanstadiedisko | 10 | 12 | Grades 4-6 = ages 10-12 |
| Läxhjälp årskurs 7-9 | 13 | 16 | Grades 7-9 = ages 13-16 |
| Konfirmationsläger | 14 | 15 | Standard Swedish confirmation age |

#### Answer B: Family event — för alla åldrar (Type 2 in v3 FINAL)
**Output:** `childMinAge=0, childMaxAge=18`

Use this ONLY when the event is a genuine all-ages family event with **concrete child elements**. Not just "hela familjen välkommen" — there must be something specifically for children at the event.

Children participate in activities AND adults consume their own content (food, drinks, shopping, culture for adults).

**Examples (genuine all-ages):**
- Julmarknad with tomtebesök, ponnyridning, glögg, hantverkare
- Midsommarfirande with dans runt midsommarstången
- Nationaldagsfirande with barnaktiviteter
- Familjedag with ponnyridning + ansiktsmålning + hoppborg
- Familjefestival with kid activities AND adult food/culture

**NOT examples (look like family events but aren't):**
- "Konstutställning — hela familjen välkommen" → Answer D (adults)
- "Stickkafé — alla välkomna" → Answer D (adults)
- "Föreläsning om svensk historia — barn i sällskap av vuxen" → Answer D (adults)
- "Sopplunch i församlingshemmet" → Answer D (adults)

#### Answer C: Adults only
**Output:** `childMinAge=18, childMaxAge=18`

Use this for events with clear adult content or broad adult appeal.

**Examples:**
- Vinprovning, ölprovning, champagneprovning
- Stand-up comedy
- Nattklubb, dans för vuxna
- Concerts (unless explicitly for kids)
- Major adult-targeted lectures, big food events
- Festivals targeting adult demographics

#### Answer D: Niche adult — same output as Answer C
**Output:** `childMinAge=18, childMaxAge=18`

For art exhibitions, knitting circles, book clubs, small lectures, soup lunches, community events with adult-only content.

Same backend output as Answer C (`18, 18`). The agent does NOT need to distinguish between broad adult and niche adult — both are tagged `18, 18`.

### Step 3: Three biases to apply

These biases were explicitly confirmed by the CEO (2026-05-18).

#### Bias 1: When uncertain, lean toward kids
If the description is thin or ambiguous, and the agent has to guess, lean toward picking a kid age range (Answer A or B), not adult-only (Answer C/D).

**Reasoning:** Famies is a family app. Cost of false positive (kid range on adult event) = parent reads, realizes it's not for kids, closes the event. Cost of false negative (adult range on kid event) = kid family never discovers it. The first cost is low. The second cost is high.

**BUT:** Lean toward kids only AFTER actually thinking. Not a blind default. If the description clearly signals adult content ("vinprovning", "nattklubb"), respect that.

**Example:** "Pyssel på Tyresö bibliotek, varje onsdag kl 15" — no ages stated, vague description. The word "pyssel" in Swedish strongly implies kids' crafts. Time is 15:00 (after school). Lean kids → guess `3, 12`.

#### Bias 2: Real fit, not safety net
Age ranges should reflect the children who genuinely enjoy the event, not the widest range that's technically allowed.

| Wrong | Right | Why |
|---|---|---|
| Knattefotboll → 0,12 | Knattefotboll → 3,6 | "Knatte" = preschool. 10-year-olds bored. |
| Babybabbel → 0,12 | Babybabbel → 0,1 | Babies are 0-1. Period. (v3 FINAL) |
| Konfirmation → 0,18 | Konfirmation → 14,15 | Standard Swedish confirmation age |
| Sagostund småbarn → 0,18 | Sagostund småbarn → 1,4 | Toddler attention span |

A wide range makes the filter useless. Parents trust narrow, accurate ranges.

#### Bias 3: "Hela familjen välkommen" on adult content = adult event
Soft family wording does NOT earn a kid age range. The agent looks at the CONTENT of the event, not the marketing wording.

If a parent reads the description and the actual content is for adults, the event is adult — regardless of whether the marketing says "barn välkomna" or "hela familjen välkommen".

**5-Second Test:** "Can I name in 5 seconds something a 4-year-old would specifically DO at this event?"
- Yes (ponnyridning, ansiktsmålning, barnteater) → kid or family event
- No (the only kid content is "they can come") → adult event

### Step 4: Stated age in source text is HIGHEST PRIORITY

This is the one hard rule. **If the source text states a numeric age, use it directly.** Override the agent's own judgment.

Patterns to detect:
- "5+", "från 5 år", "from 5 years", "ages 5+"
- "5-10 år", "5–10 years", "ages 5-10"
- "årskurs 7-9" (= grades 7-9 = ages 13-16 in Sweden)
- "för barn 3-7 år"

**If stated:** Use the stated range. Apply Bias 2 (real fit) only when the source is unclear about the upper bound.

**Examples:**
- "Bakworkshop från 5 år" → `childMinAge=5, childMaxAge=12` (5 stated, 12 = real fit upper)
- "Pyssel 4-7 år" → `childMinAge=4, childMaxAge=7` (both stated)
- "Konsert för barn 3-5 år" → `childMinAge=3, childMaxAge=5`
- "Läxhjälp årskurs 7-9" → `childMinAge=13, childMaxAge=16`

**CRITICAL: Do NOT confuse non-age numbers with ages.** These are NOT ages:
- "kl 18:00" → a time, not an age
- "18 deltagare" → participant count
- "anmälan senast 18 mars" → a date
- "lokal 5B" → a room number

### Step 4.5: Performer-to-audience mapping (v3 FINAL — 2026-05-21)

When the text describes children as PERFORMERS (utövare), the audience is broader than the performers.

**The principle: YOUNGER children pull DOWN (siblings come along), OLDER children pull UP (younger kids look up to them).**

**Sibling-effect downward:** 2-3 years younger than performers. Younger siblings come along when they have a relation to the performers.

**Cool-factor upward:** Starts around age 3. Younger children find older children's events exciting. Older children do NOT find younger children's events exciting.

**Performer patterns (NOT the target audience):**
- "förskolebarn ställer ut" → kids are the performers, NOT the audience
- "eleverna från Musikskolan spelar konsert" → performers
- "konfirmander framför musical" → performers
- "barnen visar sina verk" → performers
- "elever från lågstadiet sjunger" → performers

| What the text describes | Audience range | Why |
|---|---|---|
| Bebisar (0-1) visar/showar | `0-3` | Sibling effect only — no cool-factor upward for babies |
| Småbarn 1-3 visar | `1-5` | Own age + a few years up |
| Förskolebarn 3-5 ställer ut | `3-8` | Own age + sibling effect to slightly older |
| Förskoleklass (6) uppträder | `3-10` | Younger preschool + slightly older |
| Lågstadiet (7-9) konsert | `4-12` | Preschoolers look up + mellanstadiet |
| Mellanstadiet (10-12) musical | `5-15` | Younger kids look up + teens |
| Tonåringar (13-15) uppträder | `6-18` | School kids look up + all older |
| Gymnasiet (14-18) framför | `7-18` | School kids look up + all older |

**Example:**
- Text: "Förskolebarn ställer ut sina målningar på Tyresö bibliotek."
- Performers: 3-5 year olds
- Audience: 3-5 + sibling effect → 3-8
- Output: `childMinAge=3, childMaxAge=8`
- NOT: `childMinAge=3, childMaxAge=5` (that's the performers, not the audience)

### Step 4.6: Critical Swedish baby vocabulary (v3 FINAL — 2026-05-21)

These Swedish words mean BABIES (age 0-1), NOT toddlers. Common bug: agent groups all "small kids" as 1-3. Don't do this.

**Always tag `childMinAge=0, childMaxAge=1`:**
- bebis, bebisar, baby, babys
- spädbarn, nyfödd, nyfödda
- babybabbel, babysång, babyrytmik, babysim, babymassage
- öppna förskolan för bebis
- amningsstöd, BVC-grupp, mödragrupp
- föräldragrupp för nyblivna föräldrar

**Tag as TODDLERS (1-3), NOT babies:**
- småbarn, småbarnsföräldrar
- tumlare, krypare
- ettåringar, tvååringar, treåringar

A new parent with a 6-month-old who can't find their baby's events will leave the app. Babies are 0-1. Period.

### Step 5: Swedish grade-to-age conversion

When source text mentions "årskurs" or "klass", convert using this table:

| Swedish term | Grade | Age |
|---|---|---|
| Förskoleklass | Grade 0 | 6 |
| Årskurs 1-3 (lågstadiet) | Grades 1-3 | 7-9 |
| Årskurs 4-6 (mellanstadiet) | Grades 4-6 | 10-12 |
| Årskurs 7-9 (högstadiet) | Grades 7-9 | 13-16 |
| Gymnasiet | Grades 10-12 | 16-19 |

### Step 6: Sanity checks on output (updated v3 FINAL — 2026-05-21)

Before submitting, verify ALL of these:

1. **FORBIDDEN check:** `childMaxAge` must NOT be 17. Use 18 instead.
2. **FORBIDDEN check:** `childMinAge` must NOT be 17.
3. **Rule #52 check:** If `childMinAge=0` AND `childMaxAge` is 2-16 → **INVALID** (shows "Max X y/o" badge). Exception: `0,1` is valid for baby events.
4. **Parent age check:** `parentMinAge=18`, `parentMaxAge=100` always.

**Valid combinations with childMinAge=0:**
- `0, 1` → Baby events (shows "0-1 år" badge) ✅
- `0, 18` → Family/all-ages events (shows "För alla åldrar") ✅

**Invalid with childMinAge=0:**
- `0, 2` through `0, 16` → Shows "Max X y/o" badge ❌
- `0, 17` → FORBIDDEN (childMaxAge=17 not allowed) ❌

**Note:** Ranges like `3,18` or `10,18` are perfectly valid. Do NOT convert specific ranges to 0,18 — keep the accurate childMinAge.

### Complete Worked Examples

**Example 1: Clear kid event with numeric age**
Input: "Knattefotboll för 3-6 åringar varje lördag på Tyresövallen."
→ Step 4: Numeric age stated → 3-6. Answer A. Output: `3, 6`

**Example 2: Adult event with family-welcome wording**
Input: "Konstutställning: 'Ljus och rörelse' — abstrakta verk. Hela familjen välkommen."
→ 5-Second Test: What does a 4-year-old DO? Look at abstract paintings — not engaging. Bias 3 applies. Answer D. Output: `18, 18`

**Example 3: Genuine all-ages family event**
Input: "Julmarknad i Tyresta. Glögg, knäck, tomtebesök, ponnyridning och hantverkare."
→ Concrete child elements: tomtebesök, ponnyridning. Answer B (Type 2). Output: `0, 18`

**Example 4: Thin description, uncertain — kid-lean bias**
Input: "Pyssel på Tyresö bibliotek, varje onsdag kl 15."
→ "Pyssel" = kids' crafts, 15:00 = after school. Bias 1: lean kids. Answer A. Output: `3, 12`

**Example 5: Niche adult**
Input: "Stickkafé på bibliotek varje onsdag kl 14. Kaffe och fika ingår."
→ Knitting circle, coffee. Nothing for kids. Answer D. Output: `18, 18`

**Example 6: Grade conversion**
Input: "Läxhjälp för elever i årskurs 7-9."
→ Step 5: Grade 7-9 = ages 13-16. Answer A. Output: `13, 16`

**Example 7: Senior event — skip entirely**
Input: "Soft dans för seniorer 65+."
→ Rule #4: Senior-only event, skip entirely. Do NOT publish.

**Example 8: Youth center event disguised as adult**
Input: "Fritidsgård — öppet hus. Spelkvällar, häng och fika."
→ "Fritidsgård" = youth center (ages ~10-16 in Sweden). Answer A. Output: `10, 16` (childMaxAge=17 is FORBIDDEN, use 16 for real fit or 18 if open upward)

### Anti-patterns (what NOT to do) — updated v3 FINAL

- ❌ `childMaxAge=17` — **FORBIDDEN**. Use 18 instead.
- ❌ `childMinAge=17` — **FORBIDDEN**.
- ❌ Wide safety-net ranges: "Babybabbel → 0,12" (use 0,1)
- ❌ Tagging "Babybabbel" as 0,2 or 1,3 (it's 0,1 — babies are 0-1. Period.)
- ❌ Adult event tagged as kids because of "hela familjen välkommen"
- ❌ Skipping the stated numeric age and using own estimate
- ❌ `childMinAge=0` with `childMaxAge` 2-16 (Rule #52 violation — shows "Max X y/o" badge)
- ❌ Snapping to bucket boundaries (Rule #58 is deprecated)
- ❌ Defaulting to 18+ when uncertain (Bias 1 says lean kids)
- ❌ Confusing times/dates/room numbers with ages ("kl 18:00" ≠ age 18)
- ❌ Tagging youth center events (fritidsgård, ungdomsgård) as adult
- ❌ Tagging "Förskolebarns utställning" as 3-5 (that's the performers — audience is 3-8)
- ❌ Setting `childMinAge=18, childMaxAge=18` when API supports null (use null,null when backend allows)
- ❌ Converting specific ranges to 0,18 — keep accurate childMinAge

---

## Rule #28 Appendix: Swedish Keyword → Age Cheat Sheet

These are common Swedish event keywords and their typical age mappings, learned from 500+ real event corrections. Use as guidance, not as a rigid lookup — always read the full description.

### Baby signals (0-1 — v3 FINAL: babies are 0-1. Period.)
- babybabbel, babyrytmik, babysång, babymassage, spädbarnsträff
- bebisrytmik, bebisgympa, öppen bebisgrupp, babysim
- bebis, bebisar, baby, babys, spädbarn, nyfödd, nyfödda
- amningsstöd, BVC-grupp, mödragrupp, föräldragrupp för nyblivna
- → Always: childMinAge=0, childMaxAge=1

### Toddler signals (1-3 — NOT babies)
- småbarn, småbarnsföräldrar, tumlare, krypare
- ettåringar, tvååringar, treåringar
- småbarnsmusik, småbarnsgrupp
- → Typically: childMinAge=1, childMaxAge=3

### Preschool signals (typically 1-5 or 3-6)
- sagostund (för småbarn), knattekör, knattefotboll, miniknatte
- förskoleålder, småbarnsgympa, rytmik för små
- "småbarn", "förskola", "knatte"

### School-age signals (typically 6-12)
- pyssel (utan "småbarn"), barnteater, barnkonsert, barnfilm
- lov-aktivitet, sportlov, påsklov, sommarlov + activity
- "barn", "barnen", "barnens"

### Tween/Teen signals (typically 10-16 or 10-18)
- fritidsgård, ungdomsgård, ungdomshörna, ungdomens hus → 10,16 or 10,18
- mellanstadiedisko, högstadiedisko, ungdomsdisko
- läxhjälp (högstadiet), gaming/e-sport for youth
- "ungdom", "tonåring", "ung"
- NOTE: childMaxAge=17 is FORBIDDEN. Use 16 (if real fit ends at 16) or 18 (if open upward)

### Adult signals (→ 18,18)
- vinprovning, ölprovning, champagneprovning, whiskeyprovning
- stickkafé, bokcirkel, sopplunch, konstutställning
- föreläsning (without "barn" qualifier), paneldiskussion
- nattklubb, pub, bar, stand-up comedy
- senior, pensionär, 65+, PRO (but also check Rule #4 — may need to skip entirely)
- digitala fixaren, datorhjälp, cv-hjälp (adult services)

### "Hela familjen" — ALWAYS check content, not just the label
- With concrete kid activities → Answer B (0,18)
- Without concrete kid activities → Answer D (18,18)

---

## Rule #51: Soft Sanity Warning (Updated 2026-05-18)

**Supersedes:** Rule #51 v1.34.0 (hard validation gate).

Rule #51 is now a **soft warning system**, not a hard publish gate. The agent uses Rule #28 v3.0's reasoning to pick the right age. Rule #51 only flags suspicious cases for the agent to reconsider — it does NOT block publish (except Rule #52 violations and parent age errors).

### What Rule #51 checks

**Hard blocks (must fix before publish):**
1. Rule #52 violation: `childMinAge=0` AND `childMaxAge<17` → shows "Max X y/o" badge
2. Parent age wrong: `parentMinAge` must be 18, `parentMaxAge` must be 100

**Soft warnings (log and reconsider, but still publish):**
3. Event tagged `18,18` but title/description contains kid words (barn, baby, knatte, förskol, sagostund, barnteater, barnkonsert)
4. Event tagged for young kids but title/description contains adult signals (vinprovning, nattklubb, konstutställning, stickkafé, sopplunch, bokcirkel, föreläsning)

### How to use warnings
- If `block: true` → fix before publish
- If warnings present → re-read the description and verify. The event still publishes.
- The agent's Rule #28 v3.0 judgment takes priority over the warning regex

---

## Rule #52: childMinAge=0 + childMaxAge Rules (REVISED v4 FINAL — 2026-05-22)

**Previous v3:** `childMinAge=0` with `childMaxAge=2-16` was forbidden ("Max X y/o" badge fear).

**v4 REVISION (client decision 2026-05-22):** **childMinAge=0 is now PREFERRED for any kid event.** Babies should never be excluded.

**Valid combinations:**
- `0, 1` → Baby events ✅
- `0, 2` to `0, 16` → Specific kid range starting from baby (NEW v4 — VALID) ✅
- `0, 18` → Family/all-ages events ("För alla åldrar") ✅
- `X, Y` where X ≥ 2 → Specific older-kid range (still valid for events where babies don't fit, e.g. "Stadsvandring 10,18", "Lådbilslandet 3,10") ✅

**FORBIDDEN:**
- `0, 17` → childMaxAge=17 not allowed → use 0, 18 instead ❌
- `childMinAge=1` → use **0** instead (NEW v4) ❌
- `childMinAge=17` ❌
- `childMaxAge=17` ❌

**The "Max X y/o" badge:** If mobile renders 0,X as "Max X y/o", that's a mobile rendering concern — data side stays correct. Mobile team should update rendering to "0-X år" or "upp till X år" to match description-source-of-truth principle.

---

## Rule #59: Lessons Learned — Common Misclassification Patterns (2026-05-18)

**When:** Reviewing or correcting age classifications on existing events.

These patterns were identified from 90+ real corrections across 537 active events. They represent the most common age classification mistakes.

### Pattern 1: Norrtälje kommun — Broad 0,12 ranges
Many Norrtälje events were imported with `0, 12` which violates Rule #52 and is usually too broad. Fix by reading the actual event content:
- Family events → `0, 17`
- Baby events → `1, 2` or `0, 2` (check Rule #52)
- Specific kid activities → narrow to real fit (e.g., `3, 8`)

### Pattern 2: 0,18 is now the standard all-ages (v3 FINAL update)
`childMinAge=0, childMaxAge=18` is the correct output for Type 2 family events. This is NOT an anomaly — it is the v3 FINAL standard. 18 is used as an "open upward" marker since childMaxAge=17 is forbidden.

### Pattern 3: Youth center events tagged as adult
Events at "fritidsgård", "ungdomsgård", "ungdomens hus" are for teens (~10-16), NOT adults. Even if the description doesn't explicitly say "for kids", the venue type tells you. Use childMaxAge=16 (real fit) or 18 (if open upward). NEVER use 17 (FORBIDDEN).

### Pattern 4: Senior service events tagged as kids
Events like "Digitala fixaren" (digital help for seniors), "Datorhjälp" (computer help), "Soft dans för seniorer 65+" should either be tagged `18, 18` or skipped entirely per Rule #4 if senior-only.

### Pattern 5: Baby events with overly wide ranges (updated v3 FINAL)
Babybabbel, babyrytmik, babymassage should be `0, 1` — NOT `0, 2`, `0, 18`, or `0, 12`. Babies are 0-1. Period. Toddler events (småbarn) should be `1, 3`.

### Pattern 6: Library storytime vs. general library events
- "Sagostund för småbarn" → `1, 4` (toddler storytime)
- "Sagostund" (general) → `3, 8` (general kids' storytime)
- "Bokprat" / "Bokcirkel" → `18, 18` (adult book discussion)

### Pattern 7: "Öppen verksamhet" at different venues
- Öppen verksamhet at förskola/familjecentral → `0, 5` (parent-child groups)
- Öppen verksamhet at fritidsgård → `10, 16` or `10, 18` (youth drop-in — never use 17)
- Öppen verksamhet at seniorträff → `18, 18` or skip (Rule #4)

### Pattern 8: Swedish holiday events (updated v3 FINAL)
- Nationaldagsfirande with barnaktiviteter → `0, 18` (all-ages)
- Midsommar with stångresning → `0, 18` (all-ages)
- Julmarknad with tomte/pyssel → `0, 18` (all-ages)
- Valborg/Valborgsmässoafton → usually `0, 18` if community bonfire
- Lucia-event at church → `0, 18` if processional, check content

---

## Rule #61: Pricing Tiers ≠ Target Audience (NEW v4 FINAL — 2026-05-22)

**When:** Event description has pricing info with age tiers.

**Problem:** Agent mistakenly reads pricing age tiers as target audience.

**Examples of pricing tiers (NOT target audience):**
- "Pris: 295 kr/vuxen, **barn 0-2 år gratis**, barn 3-12 år 95 kr"
- "Fri entré för 0-14 år"
- "Vuxna 100 kr, barn 0-6 år gratis"

**Rule:** Pricing age tiers tell you about COST, not who the event targets.
- The actual target audience is determined by the activity, venue, content, and "Målgrupp:" line.
- A Mother's Day lunch with "barn 0-2 år gratis" pricing is still a FAMILY event → tag `0, 18`, not `0, 2`.
- A city walk with "Fri entré 0-14 år" is still for older kids who can walk → tag `10, 18`, not `0, 14`.

**Always check:** Does desc say "Pris:" / "Entré" / "kostar" with age numbers? Skip those for audience — use the rest of the description.

---

## Rule #62: Lectures / Författarsamtal = Adult Event (NEW v4 FINAL — 2026-05-22)

**When:** Description contains "föreläser", "föreläsning", "författarsamtal", "författarbesök", "författarmöte", "paneldiskussion", "seminarium" — even if the topic is about children, parenting, or kids.

**Rule:** The AUDIENCE of a lecture is adults. Topic doesn't change audience type.

**Examples:**
- "Föreläser författaren Fatima Åsard om barns upplevelser..." → `18, 18` (lecture audience = adults)
- "Författarsamtal om barnböcker" → `18, 18` (book talk for adults)
- "Föreläsning om hur barn upplever stress" → `18, 18` (parent-focused lecture)
- "Seminarium om att förstå tonåringar" → `18, 18` (adult educational seminar)

**Exception:** "Föreläsning för barn 6-12 år" — explicitly for kids → use stated range. But this is rare.

---

## Rule #63: "Hela familjen" → 0,18 (NEW v4 FINAL — 2026-05-22)

**When:** Description contains "hela familjen", "för hela familjen", "familjedag", "familjesöndag", "familjelördag", "familjefredag", "familjefestival", OR is a community celebration (julmarknad, midsommar, nationaldag, valborg) with concrete kid AND adult content.

**Rule:** ALWAYS tag `0, 18` ("Alla åldrar" / "För alla åldrar").

**Reasoning:** Family events explicitly welcome everyone. Don't exclude any user. Let parents decide if they want to bring babies/toddlers.

**Examples:**
- "Familjelördag" → `0, 18`
- "Familjesöndag på Östberga bibliotek" → `0, 18` (NOT 3,10 narrow)
- "Återbruksdagen — kom hela familjen" → `0, 18`
- "Julmarknad med tomtebesök, ponnyridning, glögg" → `0, 18`
- "Mors Dag familjelunch" → `0, 18`

**Exception:** If "hela familjen välkommen" appears on a clearly ADULT event (vinprovning, författarsamtal), it doesn't override adult content. The 5-Second Test still applies — "Can a 4-year-old DO something here?"

---

## Rule #64: childMinAge=1 is FORBIDDEN (NEW v4 FINAL — 2026-05-22)

**When:** Setting childMinAge.

**Rule:** Replace `childMinAge=1` with `childMinAge=0`. Babies must always be included if any kid range is mentioned.

**Examples:**
- "Barn 1-5 år" → tag `0, 5` (NOT 1,5)
- "För 1-3 åringar" → tag `0, 3` (NOT 1,3)
- "Småbarn 1-3 år" → tag `0, 3` (NOT 1,3)
- "Familjehäng 1-6 år" → tag `0, 6` (NOT 1,6)

**Exception 1:** Pure baby events stay `0, 1` (not 0,X wider).

**Exception 2:** If desc explicitly says babies are excluded ("ej för bebisar", "vi tar inte emot bebisar"), keep childMinAge=2 or higher. This is rare.

**Why:** Babies (0-12 mo) can attend most kid events with parents. Excluding them via childMinAge=1 means baby families never discover these events. The wider 0,X is always more inclusive.

---

## Rule #65: Active Events Need Parent Judgment (NEW v4 FINAL — 2026-05-22)

**When:** Event is an active/focus-requiring activity with description that mentions wide age range or pricing tier.

**Active event types:**
- City walks / stadsvandring (1+ hour walking)
- Courses (DJ-kurs, gitarrkurs, dans-kurs)
- Sports / orienteering / running events
- Workshops requiring concentration (3+ hours)
- Long museum tours / guided historical visits

**Rule:** Apply Swedish parent judgment — narrow to realistic age range that can ACTUALLY participate.

**Examples:**
- "Stadsvandring 0-14 år (fri entré)" → `10, 18` (10+ can walk and follow history)
- "DJ-kurs från åk 8 till år 2 i gymnasiet" → `14, 18` (grade conversion)
- "Workshop i orienteering" (no stated age) → infer from venue/content
- "3-timmars konstworkshop för barn" → narrow to focus-capable kids (`6, 12` or similar)

**Why:** Babies/toddlers can't realistically do 1-hour walking tours or 3-hour workshops. Tagging them as 0,X creates false-positive matches for baby families who'd find the event unsuitable.

**Compare with Rule #63:** Family events (familjedag, julmarknad) = `0, 18` because all ages CAN engage (kid corners, ponnyridning, etc.). Active focused events = narrow.

---

## Summary of Age Classification Rules (v4 FINAL)

| Rule | Status | Purpose |
|---|---|---|
| Rule #28 v4.0 | **ACTIVE** | Read Like a Swedish Parent — core age classification (see Agent_System_Prompt_v4_FINAL.md) |
| Rule #51 | **ACTIVE (soft)** | Sanity warnings |
| Rule #52 v4 | **ACTIVE (revised)** | childMinAge=0 PREFERRED. childMinAge=1 FORBIDDEN. |
| Rule #59 | **ACTIVE** | Lessons learned from real corrections |
| Rule #61 v4 | **ACTIVE (new)** | Pricing tiers ≠ target audience |
| Rule #62 v4 | **ACTIVE (new)** | Lectures/föreläsningar = adult event |
| Rule #63 v4 | **ACTIVE (new)** | "Hela familjen" → 0,18 |
| Rule #64 v4 | **ACTIVE (new)** | childMinAge=1 FORBIDDEN — use 0 |
| Rule #65 v4 | **ACTIVE (new)** | Active events need parent judgment |
| Rule #10.5 v4 (CORRECTED) | **ACTIVE (new 2026-05-27)** | Image source priority — SOURCE FIRST, ChatGPT only as fallback (stock libraries FORBIDDEN even as fallback) |
| Rule #10.6 v4 | **ACTIVE (new 2026-05-27)** | IN-DEPTH per city — all sources + web search for hidden events |
| Rule #10.7 v4 | **ACTIVE (new 2026-05-27)** | Complete city fully BEFORE reporting — don't ask user in between, single final report with exact before/after/total live numbers |

**Note:** Rules #58 and #60 were previously deprecated/revoked and have been removed from this file as of 2026-05-22.

### v3 FINAL Quick Reference (2026-05-21)

| Event Type | childMinAge | childMaxAge | Badge Display |
|---|---|---|---|
| Baby event | 0 | 1 | "0-1 år" |
| Specific kids | X (1-16) | Y (1-16 or 18) | "X-Y år" |
| Family / all-ages (Type 2) | 0 | 18 | "För alla åldrar" |
| Adult-only (Type 3) | 18 | 18 | "18+" (use null,null when API supports it) |
| "From X years" open upward | X | 18 | "X-18 år" |

**FORBIDDEN:** childMaxAge=17, childMinAge=17 — NEVER use these values.