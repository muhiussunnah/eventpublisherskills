import json, sys, os, re, urllib.parse

PP = 'C:/Users/User/AppData/Local/Temp/claude/F--eventpublisherskills/4ad7473a-f7bd-4184-b47a-6ef00f11c16a/scratchpad/pp/'
TODAY = '2026-11-03'
VALID_INT = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
REUSE = {'medley': '259197707078370566'}
MUNIS = {'Kungsbacka', 'Varberg', 'Falkenberg', 'Halmstad', 'Hylte', 'Laholm', 'Karlstad', 'Hammarö', 'Forshaga', 'Kil',
         'Kristinehamn', 'Storfors', 'Filipstad', 'Grums', 'Säffle', 'Arvika', 'Eda', 'Årjäng', 'Sunne', 'Torsby', 'Hagfors', 'Munkfors'}


def wsrv(url, logo=False, extra=''):
    e = urllib.parse.quote(url, safe='')
    if logo:
        return f'https://wsrv.nl/?url={e}&w=512&h=512&fit=contain&cbg=white&bg=white&output=jpg&q=90'
    return f'https://wsrv.nl/?url={e}&w=1080&h=1080&fit=cover&output=jpg&q=88{extra}'


def tmin(s):
    h, m = s.split(':')[:2]
    return int(h) * 60 + int(m)


def check(x):
    p = []
    ev, ve, og = x['event'], x['venue'], x['org']
    if not (300 <= len(ev['description']) <= 650): p.append(f"desc {len(ev['description'])}")
    if len(ev['title']) > 110: p.append(f"title {len(ev['title'])}")
    if ' – ' not in ev['title']: p.append('title format')
    if re.search(r'[\n*#•]|\d{1,2}[.:]\d{2}\s*[–-]', ev['description']): p.append('desc has list/hours')
    ii = ev.get('interestIds') or []
    if len(ii) != 2 or not set(ii) <= VALID_INT: p.append(f'interests {ii}')
    if ve.get('venueInterestId') not in VALID_INT: p.append('venueInterest')
    if ve.get('municipality') not in MUNIS: p.append(f"muni {ve.get('municipality')}")
    if not (55 < float(ve['lat']) < 61.5 and 11 < float(ve['lng']) < 15.5): p.append('coords')
    rc = ev['recurrence']
    if not re.fullmatch(r'\d\d:\d\d:\d\d', rc['startTime']): p.append('startTime')
    if not (0 < rc['durationMinutes'] <= 1439): p.append('duration')
    if rc['endDate'] < TODAY: p.append('ends in past')
    if rc['startDate'] > rc['endDate']: p.append('start>end')
    if not rc['days'] or any(d not in range(7) for d in rc['days']): p.append('days')
    st, en = tmin(rc['startTime']), tmin(rc['startTime']) + rc['durationMinutes']
    oh = ve.get('openingHours')
    if oh:
        for d in rc['days']:
            rows = [h for h in oh if h['day'] == d]
            if not any(tmin(h['open']) <= st and en <= tmin(h['close']) for h in rows):
                p.append(f'window not open day {d}'); break
    elif rc['durationMinutes'] != 1439:
        p.append('no hours but not always-open')
    for k in ('email',):
        for v in (og.get(k), ve.get(k)):
            if v and re.match(r'^[a-zåäö]+\.[a-zåäö]+@', v, re.I): p.append(f'personal email? {v}')
    for v in (og.get('phone'), ve.get('phone')):
        if v and re.sub(r'\D', '', v).startswith(('07', '467')): p.append(f'mobile? {v}')
    if not x.get('images'): p.append('no images')
    return p


def main():
    choice = json.load(open(PP + 'choice.json', encoding='utf-8')) if os.path.exists(PP + 'choice.json') else {}
    groups = sys.argv[1:]
    specs, report = [], []
    for g in groups:
        for x in json.load(open(PP + f'res_{g}.json', encoding='utf-8')):
            i = str(x['i'])
            c = choice.get(i, {})
            if x.get('skip') or c.get('skip'):
                report.append(f"#{i} {x['name']}: SKIP {c.get('skip') or x.get('skip')}")
                continue
            probs = check(x)
            report.append(f"#{i} {x['event']['title'][:70]} | {', '.join(probs) or 'ok'}")
            if probs and not c.get('accept'):
                continue
            if 'event' not in c:
                continue
            imgs = x['images']
            og = x['org']
            reuse = og.get('reuse')
            spec = {
                'key': f"{g}-{i}",
                'org': {'name': og['name'], 'reuseId': REUSE.get((reuse or '').lower()) or REUSE.get(og['name'].lower()),
                        'isGovernment': bool(og.get('isGovernment')), 'email': og.get('email'), 'phone': og.get('phone'),
                        'website': og.get('website'), 'instagram': og.get('instagram'), 'facebook': og.get('facebook'),
                        'youtube': og.get('youtube'),
                        'logoUrl': wsrv(og['logo'], logo=True, ) if og.get('logo') and c.get('logo', True) else None},
                'venue': {**{k: x['venue'].get(k) for k in ('title', 'address', 'lat', 'lng', 'municipality', 'website', 'email', 'phone',
                                                             'instagram', 'facebook', 'youtube', 'openingHours')},
                          'interestId': x['venue']['venueInterestId'], 'description': x['event']['description'],
                          'ctaLink': x['event']['ctaLink']},
                'event': {k: x['event'][k] for k in ('title', 'description', 'isFree', 'childMinAge', 'recurrence', 'interestIds', 'ctaLink')},
                'img': {'event': wsrv(imgs[c['event']], extra=c.get('crop', '')),
                        'venue': wsrv(imgs[c.get('venue', c['event'])], extra=c.get('vcrop', c.get('crop', '')))},
            }
            if c.get('title'): spec['event']['title'] = c['title']
            if c.get('cta'): spec['event']['ctaLink'] = c['cta']; spec['venue']['ctaLink'] = c['cta']
            for k, v in (c.get('rec') or {}).items(): spec['event']['recurrence'][k] = v
            for k, v in (c.get('ev') or {}).items(): spec['event'][k] = v
            for k, v in (c.get('ve') or {}).items(): spec['venue'][k] = v
            for k, v in (c.get('og') or {}).items(): spec['org'][k] = v
            if c.get('orgName'): spec['org']['name'] = c['orgName']
            specs.append(spec)
    out = PP + f"specs_{'_'.join(groups)}.json"
    json.dump(specs, open(out, 'w', encoding='utf-8'), ensure_ascii=True, separators=(',', ':'))
    print('\n'.join(report))
    print('specs', len(specs), out, os.path.getsize(out))


if __name__ == '__main__':
    main()
