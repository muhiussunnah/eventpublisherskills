# Image Rules for Famies Events

Famies is a family app for Swedish parents with kids aged 0–12. The event card layout uses a 1:1 square image.
Every image must make a parent scrolling the feed think "this is for us."

## Image Decision Tree

When you have a source event image, evaluate it in this order:

### 1. Is the image text-heavy?
Images that are posters, flyers, or banners where text is the primary visual element (event titles, dates,
large logos with text) get cropped badly in the 1:1 card layout — text gets cut off and becomes unreadable.

→ **REPLACE** with a generated image

How to detect: Large text overlaid on the image, flyer/poster layout, text is the main visual element
(not just a small watermark or logo in the corner).

### 2. Does the image show families/kids engaging?
The gold standard. If the source image already shows children or parents actively participating in the
event activity, it's perfect.

→ **KEEP** the source image

### 3. Is the image generic (no family connection)?
A Swedish flag alone, just birds, just a landscape, just a building, an object without people —
these don't communicate "family event" to parents scrolling the feed.

→ **REPLACE** with a generated image showing families/kids engaging with that same topic

### 4. Is the same image used by multiple events?
Reusing the same image across events makes the app look repetitive. Keep the original on one event
and generate unique alternatives for the others.

→ **GENERATE** unique images for the duplicates

### 5. Is there no image at all?
Every event needs an image. Never publish without one.

→ **GENERATE** an image based on the event description

## Image Generation via ChatGPT

### IMPORTANT — ChatGPT is the ONLY allowed image source for replacements

When the source image is unusable (text-heavy, poor quality, no people, duplicate, missing),
the replacement image MUST be generated via the logged-in ChatGPT tab in the user's browser.

**FORBIDDEN sources (NEVER use):**
- ❌ Unsplash (images.unsplash.com)
- ❌ Pexels, Pixabay, or any "free stock photo" site
- ❌ Any "opensource" / royalty-free image database
- ❌ Wikimedia, Flickr, or any web-image proxy (wsrv.nl is only for re-hosting ChatGPT output)

**Reasoning:** Stock photos are generic, often non-Nordic, often staged, often used elsewhere
on the web — they break the authentic UGC brand feel that Famies depends on. ChatGPT image
generation produces unique, on-brand, Nordic family imagery that no other event has.

If the ChatGPT tab is not open or login expired, ASK the user to open it / log in.
Do NOT fall back to stock photos under any circumstance.

### Prompt Format
\`\`\`
authentic vertical 1:1 photo of Nordic children/families [engaging with the event activity in a way that feels warm, relatable, and relevant to parents browsing a family events app]
\`\`\`

### Examples of Good Prompts
- Nationaldagen event: "authentic vertical 1:1 photo of Nordic children waving small Swedish flags at an outdoor celebration, families gathered together, warm summer day"
- Nature/bird event: "authentic vertical 1:1 photo of a Nordic toddler pointing excitedly at a flying bird in a meadow, parent crouching beside them, warm natural light"
- Art exhibition: "authentic vertical 1:1 photo of Nordic children painting at easels in a bright art studio, colorful artwork visible, engaged and happy"
- Music event: "authentic vertical 1:1 photo of Nordic children playing musical instruments together in a cozy room, smiling, family music session"
- Library storytime: "authentic vertical 1:1 photo of Nordic children sitting in a circle on colorful cushions in a library, listening to a storyteller, captivated expressions"

### Requirements
- Size: 500x500 pixels (1:1 ratio)
- Style: Authentic photo, NOT illustrated/cartoon
- Subjects: Nordic children and/or families (Swedish target audience)
- Content: Based on event description/activity
- Engagement: Show kids DOING something — touching, watching, playing, reacting — not just standing
- Each generated image should be distinct from other nearby events' images

### BAD Image Examples (avoid these)
- A Swedish flag by itself → no family connection
- Just birds or forest → no people, no engagement
- A generic landscape → feels like stock photo, not a family event
- An empty building exterior → doesn't invite families
- Just food on a plate → where are the kids?

### GOOD Image Examples (aim for these)
- Kids waving Swedish flags at a parade → nationaldagen ✓
- Toddler pointing at a bird with parent → nature event ✓
- Children painting together → art event ✓
- Family dancing in a park → music event ✓
- Kids running in a meadow → outdoor event ✓

## Image Transfer Technical Process

To get a ChatGPT-generated image onto the Famies dashboard:

### Step 1: Capture from ChatGPT and upload to tmpfiles.org
\`\`\`javascript
(async () => {
  const imgs = document.querySelectorAll('img');
  const bigImgs = Array.from(imgs).filter(img => img.width > 200 && img.height > 200);
  const targetImg = bigImgs[bigImgs.length - 1];
  const resp = await fetch(targetImg.src, { credentials: 'include' });
  const blob = await resp.blob();
  const bitmap = await createImageBitmap(blob);
  const canvas = document.createElement('canvas');
  canvas.width = 500; canvas.height = 500;
  canvas.getContext('2d').drawImage(bitmap, 0, 0, 500, 500);
  const dataUrl = canvas.toDataURL('image/jpeg', 0.85);
  const arr = dataUrl.split(',');
  const bstr = atob(arr[1]);
  const u8arr = new Uint8Array(bstr.length);
  for (let i = 0; i < bstr.length; i++) u8arr[i] = bstr.charCodeAt(i);
  const uploadBlob = new Blob([u8arr], { type: 'image/jpeg' });
  const formData = new FormData();
  formData.append('file', uploadBlob, 'event-image.jpg');
  const uploadResp = await fetch('https://tmpfiles.org/api/v1/upload', { method: 'POST', body: formData });
  const json = await uploadResp.json();
  return JSON.stringify(json);
})();
\`\`\`

The response contains a URL like \`https://tmpfiles.org/12345/event-image.jpg\`.
Convert it to a download URL: \`https://tmpfiles.org/dl/12345/event-image.jpg\`

### Step 2: Upload to Famies dashboard via wsrv.nl proxy
\`\`\`javascript
(async () => {
  const proxyUrl = 'https://wsrv.nl/?url=' + encodeURIComponent('https://tmpfiles.org/dl/XXXXX/event-image.jpg') + '&w=500&h=500&fit=cover&output=jpg';
  const resp = await fetch(proxyUrl);
  const blob = await resp.blob();
  const file = new File([blob], 'event-image.jpg', { type: 'image/jpeg' });
  const input = document.querySelector('input[type="file"]');
  const dt = new DataTransfer();
  dt.items.add(file);
  input.files = dt.files;
  input.dispatchEvent(new Event('change', { bubbles: true }));
  return 'Image uploaded: ' + blob.size + ' bytes';
})();
\`\`\`

The wsrv.nl proxy is needed because tmpfiles.org doesn't set CORS headers, but the Famies
dashboard needs to fetch the image from JavaScript. wsrv.nl acts as a CORS-friendly image proxy.
