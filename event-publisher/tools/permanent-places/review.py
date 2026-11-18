"""Compact review of research groups + default choices.
usage: python -I -X utf8 review.py <G...>     (prints one block per place; creates default choice entries)
"""
import json, sys, os, re
PP = '<scratchpad>/pp/'  # point at the current session's scratchpad folder
D = 'SMTWTFS'
cf = PP + 'choice.json'
choice = json.load(open(cf, encoding='utf-8')) if os.path.exists(cf) else {}


def tmin(s):
    h, m = s.split(':')[:2]
    return int(h) * 60 + int(m)


for g in sys.argv[1:]:
    f = PP + f'res_{g}.json'
    if not os.path.exists(f):
        print('missing', g); continue
    data = json.load(open(f, encoding='utf-8'))
    grp = {p['i'] for p in json.load(open(PP + f'group_{g}.json', encoding='utf-8'))}
    got = {x['i'] for x in data}
    if grp != got:
        print(f'!! group {g}: missing {sorted(grp - got)} extra {sorted(got - grp)}')
    for x in data:
        i = str(x['i'])
        if x.get('skip'):
            print(f"#{i} SKIP {x['name']}: {x['skip'][:150]}")
            continue
        o, v, e = x['org'], x['venue'], x['event']
        r = e['recurrence']
        oh = v.get('openingHours')
        ohs = 'always' if not oh else ' '.join(f"{D[h['day']]}{h['open']}-{h['close']}" for h in oh)
        end = tmin(r['startTime']) + r['durationMinutes']
        nimg = len(x.get('images') or [])
        ev = x.get('evidence') or []
        evk = ''.join(sorted({(q.get('fact') or '?')[0] for q in ev}))
        print(f"#{i} {e['title']}")
        print(f"   org {o['name']} | gov={int(bool(o.get('isGovernment')))} | {o.get('email')} | {o.get('phone')} | logo={'y' if o.get('logo') else 'n'} || venue {v['title']} | {v['address']} | {v['municipality']} | {v.get('email')} | {v.get('phone')}")
        print(f"   hours {ohs}")
        print(f"   rec {''.join(D[d] for d in r['days'])} {r['startTime'][:5]}-{end // 60:02d}:{end % 60:02d} {r['startDate']}>{r['endDate']} | free={int(bool(e['isFree']))} min={e.get('childMinAge')} int={e['interestIds']} | img {nimg} | ev {evk} | flags {x.get('flags')}")
        print(f"   note {(x.get('note') or '')[:330]}")
        if i not in choice:
            choice[i] = {'event': 0, 'venue': 1 if nimg > 1 else 0}
json.dump(choice, open(cf, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
