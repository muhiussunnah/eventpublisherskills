# Image Replacement — Session Progress
**Date:** 2026-05-22
**Status:** Identification complete (56 events), generation pipeline proven, 0/56 patched

## ✅ What's done

1. **Full scan of 801 live events** for ethnic-mismatch images
2. **56 events identified** (full list saved in `bad-images-complete-scan-2026-05-22.md`)
3. **ChatGPT workflow proven** on event #4 (After School – Mangaklubb) — image generated successfully
4. **v4 UGC prompt formula validated** — produces clean Nordic family-style images

## Generated image example (event #4)

Prompt used:
```
Generate an image with this prompt: Authentic vertical 1:1 photo of Nordic teens age 10-14 at an after-school manga club at a Swedish library. Kids sitting around a table reading manga books, drawing manga characters in their sketchbooks, sharing books with each other. Warm afternoon library light, books and snacks on the table, bookshelves in background. Curious, focused, social mood. Real life, not staged. Size: 1:1 square, 500x500.
```

Result: Nordic teens around a library table with manga books, natural light, candid feel ✅

## Per-event workflow (~5 min each, multi-session)

1. Fetch description from FamMap API
2. Build v4 UGC prompt (per Rule #11 — 5 ingredients)
3. Send to ChatGPT, wait ~30 sec for generation
4. Right-click → save image (or download via JS)
5. Upload image to FamMap via `POST /admin/image` (multipart)
6. PATCH event with new image URL from S3 response

## Code snippets for next session

### Upload image to FamMap S3
```javascript
window.__uploadImage = function(blob) {
  var fd = new FormData();
  fd.append('file', blob, 'image.png');
  var x = new XMLHttpRequest();
  x.open('POST', 'https://api.fammap.app/admin/image', false);
  x.setRequestHeader('Authorization', 'Bearer ' + window.__token);
  x.setRequestHeader('Platform', 'web');
  x.setRequestHeader('Version', '0.0.0');
  x.send(fd);
  if (x.status !== 200) return {ok:false, status:x.status};
  return JSON.parse(x.responseText).data.image; // returns S3 URL
};
```

### Patch event with new image
```javascript
window.__patchImage = function(eventId, newImageUrl) {
  var x = new XMLHttpRequest();
  x.open('GET', 'https://api.fammap.app/admin/events/'+eventId, false);
  x.setRequestHeader('Authorization', 'Bearer ' + window.__token);
  x.setRequestHeader('Platform', 'web');
  x.setRequestHeader('Version', '0.0.0');
  x.send();
  var d = JSON.parse(x.responseText).data;
  var body = {
    title: d.title, description: d.description, 
    images: [newImageUrl],  // <-- replace image
    dates: d.dates.map(function(dt) { return {eventDateId: dt.eventDateId, startDate: dt.startDate, endDate: dt.endDate}; }),
    placeId: d.placeId, lat: d.lat, lng: d.lng,
    childMinAge: d.childMinAge, childMaxAge: d.childMaxAge,
    parentMinAge: 18, parentMaxAge: 100,
    isFree: d.isFree, ctaLink: d.ctaLink
  };
  var px = new XMLHttpRequest();
  px.open('PATCH', 'https://api.fammap.app/admin/events/'+eventId, false);
  px.setRequestHeader('Authorization', 'Bearer ' + window.__token);
  px.setRequestHeader('Platform', 'web');
  px.setRequestHeader('Version', '0.0.0');
  px.setRequestHeader('Content-Type', 'application/json');
  px.send(JSON.stringify(body));
  return {ok: px.status === 200};
};
```

## Recommendation for next session

1. **Restart with fresh context budget** — open new chat
2. **Reference this file + bad-images-complete-scan list**
3. **Process in batches of 10** — manageable per session
4. **6 sessions × 10 events = 60 events** (covers all 56 with buffer)

## Bonus finding

While reviewing event #4, noticed it's tagged **18,18** but description says "Passar dig som fyllt 10 år" → should be **10,18** per v4 rules. This is a separate age-tag bug. Likely many other events have similar tag bugs that need a separate pass.
