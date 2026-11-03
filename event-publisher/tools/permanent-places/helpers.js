(() => {
  const B = 'https://api.fammap.app';
  const H = () => ({ Authorization: 'Bearer ' + localStorage.auth_token, Platform: 'web', Version: '0.0.0' });
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
  const norm = (s) => String(s || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^a-z0-9]+/g, ' ').trim();

  async function api(method, path, body, ms = 60000) {
    const c = new AbortController(); const t = setTimeout(() => c.abort(), ms);
    try {
      const o = { method, headers: { ...H() }, cache: 'no-store', signal: c.signal };
      if (body !== undefined) { o.headers['Content-Type'] = 'application/json'; o.body = JSON.stringify(body); }
      const r = await fetch(B + path, o); let j = null; try { j = await r.json(); } catch (e) {}
      return { s: r.status, j };
    } catch (e) { return { s: 0, err: String(e) }; } finally { clearTimeout(t); }
  }
  async function getBlob(url, ms = 60000) {
    const c = new AbortController(); const t = setTimeout(() => c.abort(), ms);
    try { const r = await fetch(url, { cache: 'no-store', signal: c.signal }); if (!r.ok) throw new Error('img ' + r.status); return await r.blob(); }
    finally { clearTimeout(t); }
  }
  async function sha(b) { const d = await crypto.subtle.digest('SHA-256', await b.arrayBuffer()); return [...new Uint8Array(d)].map((x) => x.toString(16).padStart(2, '0')).join(''); }
  async function upload(blob, name) {
    const fd = new FormData(); fd.append('file', new File([blob], name, { type: 'image/jpeg' }));
    const c = new AbortController(); const t = setTimeout(() => c.abort(), 90000);
    try {
      const r = await fetch(B + '/admin/image', { method: 'POST', headers: H(), body: fd, signal: c.signal, cache: 'no-store' });
      const j = await r.json().catch(() => null);
      if (r.status !== 200 || !j?.data?.image) throw new Error('upload ' + r.status + ' ' + JSON.stringify(j).slice(0, 120));
      return j.data.image;
    } finally { clearTimeout(t); }
  }
  async function delImage(url) { if (url) await api('DELETE', '/admin/image', { image: url }); }
  const fixUrl = (u) => { if (!u) return null; try { return encodeURI(decodeURI(u)); } catch (e) { return encodeURI(u); } };
  const hashes = () => { try { return JSON.parse(localStorage.__r2hashes || '{}'); } catch (e) { return {}; } };
  const saveHash = (h, t) => { const o = hashes(); o[h] = t; try { localStorage.__r2hashes = JSON.stringify(o); } catch (e) {} };

  async function findBy(path, key, field, value) {
    const r = await api('GET', `${path}?page=1&limit=100&searchText=${encodeURIComponent(value)}`);
    const list = r.j?.data?.[key] || [];
    return list.filter((x) => norm(x[field]) === norm(value)).sort((a, b) => String(b.createdAt).localeCompare(String(a.createdAt)))[0] || null;
  }

  window.__P = { api, getBlob, sha, upload, delImage, norm, fixUrl, findBy, hashes };

  // spec: {key, org:{name, reuseId?, isGovernment, email, phone, website, instagram, facebook, youtube, logoUrl?},
  //        venue:{title, address, lat, lng, municipality, website, email, phone, instagram, facebook, youtube, openingHours, interestId, description, ctaLink},
  //        event:{title, description, isFree, childMinAge, recurrence, interestIds, ctaLink},
  //        img:{event, venue}}   (img urls are ready-to-fetch wsrv urls)
  window.__publishPlace = async (spec) => {
    const st = { key: spec.key, steps: [], ids: {} }; const made = [];
    const log = (s) => st.steps.push(s);
    try {
      const ev = spec.event, ve = spec.venue, og = spec.org;
      // duplicate guards
      if (await findBy('/admin/events', 'events', 'title', ev.title)) throw new Error('duplicate event title');
      if (await findBy('/admin/places', 'places', 'title', ve.title)) throw new Error('duplicate venue title');
      const munId = window.__muni[ve.municipality]; if (!munId) throw new Error('no municipality ' + ve.municipality);
      // images
      const evBlob = await getBlob(spec.img.event); const veBlob = await getBlob(spec.img.venue);
      if (evBlob.size < 5000 || veBlob.size < 5000) throw new Error('image too small');
      const evHash = await sha(evBlob); const known = hashes();
      if (known[evHash]) throw new Error('duplicate image of ' + known[evHash]);
      log('images ' + evBlob.size + '/' + veBlob.size);
      // organizer
      let orgId = og.reuseId || null;
      if (!orgId) { const ex = await findBy('/admin/organizations', 'organizations', 'name', og.name); if (ex) { orgId = ex.organizationId; log('org reused ' + og.name); } }
      if (!orgId) {
        let avatar = null;
        if (og.logoUrl) { const lb = await getBlob(og.logoUrl); if (lb.size > 1500) { avatar = await upload(lb, 'organization.jpg'); made.push(avatar); } }
        const body = { name: og.name, avatar, isPartnered: false, isGovernment: !!og.isGovernment, email: og.email || null, phoneNumber: og.phone || null,
          website: fixUrl(og.website), instagram: fixUrl(og.instagram), facebook: fixUrl(og.facebook), youtube: fixUrl(og.youtube) };
        const r = await api('POST', '/admin/organizations', body);
        if (r.s !== 200 && r.s !== 201) throw new Error('org ' + r.s + ' ' + JSON.stringify(r.j).slice(0, 160));
        const f = await findBy('/admin/organizations', 'organizations', 'name', og.name); if (!f) throw new Error('org not found after create');
        orgId = f.organizationId; made.length = 0; log('org created ' + og.name);
      }
      st.ids.org = orgId;
      // venue
      const veImg = await upload(veBlob, 'place.jpg-' + Date.now()); made.push(veImg);
      const hours = ve.openingHours ? ve.openingHours.map((h) => ({ open: { day: h.day, time: h.open }, close: { day: h.day, time: h.close } })) : null;
      const pb = { organizationId: orgId, interestId: ve.interestId, municipalityId: munId, images: [veImg], openingHours: hours, lat: ve.lat, lng: ve.lng,
        address: ve.address, website: fixUrl(ve.website), phoneNumber: ve.phone || null, title: ve.title, description: ve.description,
        ctaLink: fixUrl(ve.ctaLink || ve.website), ctaText: 'Läs mer', instagram: fixUrl(ve.instagram), facebook: fixUrl(ve.facebook), youtube: fixUrl(ve.youtube), isPublished: true };
      if (ve.email) pb.email = ve.email;
      const rp = await api('POST', '/admin/places', pb);
      if (rp.s !== 200 && rp.s !== 201) throw new Error('place ' + rp.s + ' ' + JSON.stringify(rp.j).slice(0, 160));
      const fp = await findBy('/admin/places', 'places', 'title', ve.title); if (!fp) throw new Error('place not found after create');
      st.ids.place = fp.placeId; made.length = 0; log('venue created');
      // event
      const evImg = await upload(evBlob, 'event.jpg-' + Date.now()); made.push(evImg);
      const eb = { placeId: fp.placeId, title: ev.title, description: ev.description, images: [evImg], lat: ve.lat, lng: ve.lng, address: ve.address,
        isFree: !!ev.isFree, shouldNotifyUsers: false, isRecurring: true, recurrence: ev.recurrence, parentMinAge: 18, parentMaxAge: 100,
        childMinAge: ev.childMinAge || 0, childMaxAge: 18, interestIds: ev.interestIds, ctaLink: fixUrl(ev.ctaLink), ctaText: 'Läs mer' };
      const re = await api('POST', '/admin/events', eb);
      if (re.s !== 200 && re.s !== 201) throw new Error('event ' + re.s + ' ' + JSON.stringify(re.j).slice(0, 160));
      const fe = await findBy('/admin/events', 'events', 'title', ev.title); if (!fe) throw new Error('event not found after create');
      st.ids.event = fe.eventId; made.length = 0; saveHash(evHash, ev.title); log('event created');
      st.ok = true;
    } catch (e) {
      st.err = String(e && e.message || e);
      for (const u of made) { try { await delImage(u); } catch (x) {} }
    }
    return st;
  };

  window.__bg = window.__bg || {};
  window.__queueRun = (specs, tag) => {
    window.__bg[tag] = { running: true, done: [], at: 0 };
    (async () => {
      for (const s of specs) { window.__bg[tag].at = s.key; const r = await window.__publishPlace(s); window.__bg[tag].done.push(r); await sleep(400); }
      window.__bg[tag].running = false;
    })();
    return 'queued ' + specs.length;
  };
  return 'helpers ok';
})();
