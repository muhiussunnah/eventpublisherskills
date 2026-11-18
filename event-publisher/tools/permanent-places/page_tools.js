// Page-side tools for a permanent-places run (paste into the dashboard tab AFTER helpers.js).
// Used for the 5-region run of 2026-11-18 (196 places). Nothing here contains a token: the helpers read
// localStorage.auth_token at call time.
//
// Transfer of spec files without spending model tokens:
//   1. create a file input once:  const i = document.createElement('input'); i.type = 'file'; i.multiple = true;
//      i.id = '__specfile'; document.body.appendChild(i);   -> find its ref with the browser `find` tool
//   2. upload batchN.json with the browser file_upload tool (ref of that input)
//   3. await __prep('batchN.json', <len>, <checksum>)   (len + checksum printed by cs.py; specs are ASCII JSON)
//   4. no `flagged`, no `pairs`  ->  __queueRun(__batches['batchN.json'], 'bN')  or  __chainAfter('batchN.json', 'bN', 'bN-1')
//   5. __saveIds()  (ids survive a reload in localStorage.__n5_ids)   6. await __auditPublished(specs, __bg.bN.done)
(() => {
  window.__batches = window.__batches || {};
  window.__batchHashes = window.__batchHashes || [];          // [[specKey, eventImageHash], ...] of every prepared batch
  window.__ref2 = window.__ref2 || { out: [] };               // [[imageUrl, hash], ...] of all published live events

  window.__readSpecs = async () => { const out = {}; for (const file of document.getElementById('__specfile').files) { out[file.name] = await file.text(); } return out; };
  window.__cs = (t) => { let s = 0; for (let i = 0; i < t.length; i++) s = (s + t.charCodeAt(i) * (i % 97 + 1)) % 1000000007; return s; };
  window.__loadBatch = async (name, len, cs) => {
    const files = await __readSpecs(); const t = files[name]; if (!t) return 'no file ' + name;
    if (t.length !== len || __cs(t) !== cs) return 'CHECKSUM MISMATCH ' + t.length + ' ' + __cs(t);
    __batches[name] = JSON.parse(t); return 'ok ' + __batches[name].length;
  };

  // 64-bit dHash. IMPORTANT: use ONE pipeline for both sides (proxy 96x96 cover PNG -> 9x8): hashing the same picture
  // once from a browser resize and once from a proxy resize gives distances of 8-16, i.e. false "different".
  window.__dhashBlob = async (blob) => {
    const bm = await createImageBitmap(blob, { resizeWidth: 9, resizeHeight: 8, resizeQuality: 'high' });
    const c = new OffscreenCanvas(9, 8); const x = c.getContext('2d'); x.drawImage(bm, 0, 0);
    const d = x.getImageData(0, 0, 9, 8).data; let h = 0n;
    for (let r = 0; r < 8; r++) for (let k = 0; k < 8; k++) {
      const i = (r * 9 + k) * 4, j = i + 4;
      const a = d[i] * 299 + d[i + 1] * 587 + d[i + 2] * 114, b = d[j] * 299 + d[j + 1] * 587 + d[j + 2] * 114;
      h = (h << 1n) | (a > b ? 1n : 0n);
    }
    return h;
  };
  window.__dh2 = async (url) => {
    const r = await fetch('https://wsrv.nl/?url=' + encodeURIComponent(url) + '&w=96&h=96&fit=cover&output=png');
    if (!r.ok) throw new Error('wsrv ' + r.status); return await __dhashBlob(await r.blob());
  };
  window.__ham = (a, b) => { let x = a ^ b, n = 0; while (x) { n += Number(x & 1n); x >>= 1n; } return n; };
  window.__nearest = (h) => { let best = 99, bu = ''; for (const [u, rh] of __ref2.out) { const d = __ham(h, rh); if (d < best) { best = d; bu = u; } } return [best, bu]; };
  window.__rawOf = (wu) => decodeURIComponent(wu.slice('https://wsrv.nl/?url='.length).split('&')[0]);

  // reference hashes: cover of every published live event (1,248 images took ~4 min with 6 workers)
  window.__buildRef = async () => {
    const all = []; for (let p = 1; p < 60; p++) { const r = await __P.api('GET', '/admin/events?isEnd=false&limit=100&page=' + p); const ev = r.j.data.events; all.push(...ev); if (ev.length < 100) break; }
    const urls = [...new Set(all.filter((e) => e.place && e.place.isPublished).map((e) => (e.images || [])[0]).filter(Boolean))];
    const out = []; const err = []; let i = 0;
    const w = async () => { while (i < urls.length) { const u = urls[i++]; try { out.push([u, await __dh2(u)]); } catch (e) { err.push(u); } } };
    await Promise.all([w(), w(), w(), w(), w(), w()]);
    window.__ref2 = { out, err }; return out.length + ' hashed, ' + err.length + ' failed';
  };

  // returns [key, distEventToNearestPublished, distVenueToNearestPublished, distToNearestInBatches, thatKey] per spec
  window.__dupCheck2 = async (specs) => {
    const res = []; let i = 0;
    const w = async () => { while (i < specs.length) { const s = specs[i++]; try {
      const he = await __dh2(__rawOf(s.img.event)); const hv = s.img.venue === s.img.event ? he : await __dh2(__rawOf(s.img.venue));
      const [de] = __nearest(he); const [dv] = __nearest(hv); let inb = 99, ik = '';
      for (const [k2, h2] of __batchHashes) { if (k2 === s.key) continue; const dd = __ham(he, h2); if (dd < inb) { inb = dd; ik = k2; } }
      res.push({ key: s.key, he, de, dv, inb, ik });
    } catch (e) { res.push({ key: s.key, err: e.message }); } } };
    await Promise.all([w(), w(), w(), w()]);
    for (const r of res) if (r.he !== undefined && !__batchHashes.some((x) => x[0] === r.key)) __batchHashes.push([r.key, r.he]);
    return res.map((r) => r.err ? [r.key, 'ERR ' + r.err] : [r.key, r.de, r.dv, r.inb, r.ik]);
  };
  // load + checksum + duplicate check; distance <= 10 = duplicate (known duplicates measured 0, 2, 0, 3)
  window.__prep = async (name, len, cs) => {
    const ld = await __loadBatch(name, len, cs); if (!ld.startsWith('ok')) return { ld };
    const r = await __dupCheck2(__batches[name]); const hs = __batchHashes; const pairs = [];
    for (let i = 0; i < hs.length; i++) for (let j = i + 1; j < hs.length; j++) { const d = __ham(hs[i][1], hs[j][1]); if (d <= 10) pairs.push([hs[i][0], hs[j][0], d]); }
    return { ld, n: r.length, flagged: r.filter((x) => typeof x[1] !== 'number' || x[1] <= 10 || x[2] <= 10), pairs };
  };

  window.__chainAfter = (name, tag, afterTag) => {
    (async () => { while (!(__bg[afterTag] && !__bg[afterTag].running)) await new Promise((z) => setTimeout(z, 2000)); __queueRun(__batches[name], tag); })();
    return tag + ' will start after ' + afterTag;
  };
  window.__saveIds = () => {
    const all = {}; try { Object.assign(all, JSON.parse(localStorage.__n5_ids || '{}')); } catch (e) {}
    for (const tag of Object.keys(__bg)) for (const d of __bg[tag].done) if (d.ok) all[d.key] = [d.ids.org, d.ids.place, d.ids.event, (d.steps.find((x) => x.startsWith('org ')) || '').split(' ')[1]];
    localStorage.__n5_ids = JSON.stringify(all); return Object.keys(all).length;
  };

  // field-by-field re-read of what was published; one line per place: "<key> <eventId> OK" or the differing fields.
  // "noLogo" = the spec has a logo but the (reused) organizer has none -> upload it and PATCH the organizer.
  window.__auditPublished = async (specs, done) => {
    const byKey = Object.fromEntries(specs.map((s) => [s.key, s])); const out = [];
    for (const d of done.filter((x) => x.ok)) {
      const s = byKey[d.key]; const issues = [];
      const e = (await __P.api('GET', '/admin/events/' + d.ids.event)).j?.data;
      const p = (await __P.api('GET', '/admin/places/' + d.ids.place)).j?.data;
      if (!e) { out.push(d.key + ' NO EVENT'); continue; }
      if (e.title !== s.event.title) issues.push('title');
      if (e.description !== s.event.description) issues.push('desc');
      const r = e.recurrence || {}; const sr = s.event.recurrence;
      if (JSON.stringify([...(r.days || [])].sort()) !== JSON.stringify([...sr.days].sort())) issues.push('days');
      if ((r.startTime || '').slice(0, 5) !== sr.startTime.slice(0, 5)) issues.push('start');
      if (r.durationMinutes !== sr.durationMinutes) issues.push('duration');
      if (String(r.startDate).slice(0, 10) !== sr.startDate || String(r.endDate).slice(0, 10) !== sr.endDate) issues.push('dates');
      if (!!e.isFree !== !!s.event.isFree) issues.push('isFree');
      if (e.parentMinAge !== 18 || e.parentMaxAge !== 100 || e.childMaxAge !== 18 || e.childMinAge !== (s.event.childMinAge || 0)) issues.push('ages');
      if (!e.isRecurring) issues.push('notRecurring');
      if (!(e.images || []).length) issues.push('noImage');
      const ints = (e.interests || []).map((x) => x.interestId || x.id || x);
      if (JSON.stringify([...ints].sort()) !== JSON.stringify([...s.event.interestIds].sort())) issues.push('interests');
      if (e.place?.placeId !== d.ids.place) issues.push('place');
      if (!p) issues.push('noVenue'); else {
        if (p.isPublished !== true) issues.push('unpublished');
        if ((p.municipality?.name || p.municipality) !== s.venue.municipality) issues.push('kommun');
        if ((p.openingHours || []).length !== (s.venue.openingHours || []).length) issues.push('hours');
        if (p.owner?.organizationId !== d.ids.org) issues.push('org'); // organizer is `owner` on a place
        if (s.org.logoUrl && !p.owner?.avatar) issues.push('noLogo');
      }
      out.push(d.key + ' ' + d.ids.event + ' ' + (issues.join(', ') || 'OK'));
    }
    return out;
  };

  // Images the proxy cannot fetch (host not resolvable for wsrv, wp.com 400): prepare them with localimg.py, upload the
  // jpgs + local_<i>.json through the same file input, then turn the "local:<file>" names into blob: URLs, which the
  // publisher's getBlob() can fetch like any other URL (no helper patch needed).
  window.__localSpecs = async (names) => {
    const by = {}; for (const f of document.getElementById('__specfile').files) by[f.name] = f;
    window.__localUrls = window.__localUrls || {}; const specs = [];
    const fix = (u) => { if (!u || !u.startsWith('local:')) return u; const f = by[u.slice(6)]; if (!f) throw new Error('missing ' + u); return (__localUrls[u] = __localUrls[u] || URL.createObjectURL(f)); };
    for (const n of names) { const s = JSON.parse(await by[n].text())[0]; s.img.event = fix(s.img.event); s.img.venue = fix(s.img.venue); s.org.logoUrl = fix(s.org.logoUrl); specs.push(s); }
    return specs;   // e.g. __batches['local.json'] = await __localSpecs(['local_193.json']); __chainAfter('local.json', 'bl', 'b10')
  };
  return 'page tools ok';
})();
