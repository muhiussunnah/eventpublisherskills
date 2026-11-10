import json, sys, urllib.parse, re
src, out = sys.argv[1], sys.argv[2]
S = json.load(open(src, encoding='utf-8'))
WS = 'https://wsrv.nl/?url='
def raw(u):
    assert u.startswith(WS), u
    q = u[len(WS):]
    enc, rest = (q.split('&', 1) + [''])[:2]
    return urllib.parse.unquote(enc), '&' + rest
C = []
for s in S:
    o, v, e, im = s['org'], s['venue'], s['event'], s['img']
    lg = o.get('logoUrl')
    if lg:
        lr, lx = raw(lg)
        lg = [lr, 0 if lx == '&w=512&h=512&fit=contain&cbg=white&bg=white&output=jpg&q=90' else lx]
    er, ex = raw(im['event']); vr, vx = raw(im['venue'])
    std = '&w=1080&h=1080&fit=cover&output=jpg&q=88'
    hrs = None if not v.get('openingHours') else ' '.join(f"{h['day']}{h['open'].replace(':','')}{h['close'].replace(':','')}" for h in v['openingHours'])
    r = e['recurrence']
    rec = [''.join(str(d) for d in r['days']), r['startTime'][:5], r['durationMinutes'], r['startDate'], r['endDate']]
    C.append([s['key'],
              [o['name'], o.get('reuseId'), 1 if o.get('isGovernment') else 0, o.get('email'), o.get('phone'), o.get('website'), o.get('instagram'), o.get('facebook'), o.get('youtube'), lg],
              [v['title'], v['address'], v['lat'], v['lng'], v['municipality'], v.get('website'), v.get('email'), v.get('phone'), v.get('instagram'), v.get('facebook'), v.get('youtube'), hrs, v['interestId'], v.get('ctaLink')],
              [e['title'], e['description'], 1 if e['isFree'] else 0, e.get('childMinAge') or 0, rec, e['interestIds'], e.get('ctaLink')],
              [er, 0 if ex == std else ex, vr, 0 if vx == std else vx]])
txt = json.dumps(C, ensure_ascii=False, separators=(',', ':'))
open(out, 'w', encoding='utf-8').write(txt)
print(len(C), len(txt.encode('utf-8')), len(txt))
