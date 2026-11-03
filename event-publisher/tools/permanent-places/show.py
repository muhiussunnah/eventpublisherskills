import json, sys
PP = 'C:/Users/User/AppData/Local/Temp/claude/F--eventpublisherskills/4ad7473a-f7bd-4184-b47a-6ef00f11c16a/scratchpad/pp/'
D = 'SMTWTFS'
for g in sys.argv[1:]:
    for x in json.load(open(PP + f'res_{g}.json', encoding='utf-8')):
        if x.get('skip'):
            print(f"#{x['i']} SKIP {x['name']}: {x['skip'][:160]}"); continue
        o, v, e = x['org'], x['venue'], x['event']; r = e['recurrence']
        oh = v.get('openingHours')
        ohs = 'always' if not oh else ' '.join(f"{D[h['day']]}{h['open']}-{h['close']}" for h in oh)
        print(f"#{x['i']} {e['title']}")
        print(f"   org: {o['name']} | reuse={o.get('reuse')} gov={o.get('isGovernment')} | {o.get('email')} | {o.get('phone')} | logo={'y' if o.get('logo') else 'n'}")
        print(f"   venue: {v['title']} | {v['address']} | {v['municipality']} | {v['lat']},{v['lng']} | int {v.get('venueInterestId')}")
        print(f"   hours: {ohs}")
        print(f"   rec: {''.join(D[d] for d in r['days'])} {r['startTime']} +{r['durationMinutes']}m {r['startDate']}→{r['endDate']} | free={e['isFree']} min={e['childMinAge']} int={e['interestIds']} | desc {len(e['description'])}")
        print(f"   cta: {e['ctaLink']} | flags: {x.get('flags')} | note: {(x.get('note') or '')[:220]}")
