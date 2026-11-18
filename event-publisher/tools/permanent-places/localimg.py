"""Prepare local 1080x1080 crops (and a 512 logo) for places whose host the image proxy cannot reach.
usage: python -I -X utf8 localimg.py <G> <i> [more i ...]
Writes pp3/local/<i>_event.jpg, <i>_venue.jpg, <i>_logo.jpg and a spec file pp3/local_<i>.json whose img urls are
'local:<file>' (the page helper looks them up in window.__localBlobs).
"""
import json, sys, os, io
import requests
from PIL import Image, ImageOps
PP = '<scratchpad>/pp/'  # point at the current session's scratchpad folder
UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'}
os.makedirs(PP + 'local', exist_ok=True)
g = sys.argv[1]
want = set(sys.argv[2:])
choice = json.load(open(PP + 'choice.json', encoding='utf-8'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def get(u):
    r = requests.get(u, headers=UA, timeout=60)
    r.raise_for_status()
    return Image.open(io.BytesIO(r.content))


for x in json.load(open(PP + f'res_{g}.json', encoding='utf-8')):
    i = str(x['i'])
    if i not in want:
        continue
    c = choice[i]
    imgs = x['images']
    for tag, k in (('event', c['event']), ('venue', c.get('venue', c['event']))):
        im = ImageOps.exif_transpose(get(imgs[k])).convert('RGB')
        im = ImageOps.fit(im, (1080, 1080), Image.LANCZOS)
        im.save(PP + f'local/{i}_{tag}.jpg', 'JPEG', quality=88)
    logo = None
    if x['org'].get('logo') and c.get('logo', True):
        lg = get(x['org']['logo']).convert('RGBA')
        bg = Image.new('RGBA', (512, 512), (29, 53, 87, 255) if c.get('logoDark') else (255, 255, 255, 255))
        lg = ImageOps.contain(lg, (432, 432), Image.LANCZOS)  # also scales small logos up, keeps a margin
        bg.paste(lg, ((512 - lg.width) // 2, (512 - lg.height) // 2), lg)
        bg.convert('RGB').save(PP + f'local/{i}_logo.jpg', 'JPEG', quality=90)
        logo = f'local:{i}_logo.jpg'
    og, v, e = x['org'], x['venue'], x['event']
    spec = {'key': f'{g}-{i}',
            'org': {'name': og['name'], 'reuseId': None, 'isGovernment': bool(og.get('isGovernment')), 'email': og.get('email'),
                    'phone': og.get('phone'), 'website': og.get('website'), 'instagram': og.get('instagram'),
                    'facebook': og.get('facebook'), 'youtube': og.get('youtube'), 'logoUrl': logo},
            'venue': {**{k: v.get(k) for k in ('title', 'address', 'lat', 'lng', 'municipality', 'website', 'email', 'phone', 'instagram',
                                               'facebook', 'youtube', 'openingHours')},
                      'interestId': v['venueInterestId'], 'description': e['description'], 'ctaLink': e['ctaLink']},
            'event': {k: e[k] for k in ('title', 'description', 'isFree', 'childMinAge', 'recurrence', 'interestIds', 'ctaLink')},
            'img': {'event': f'local:{i}_event.jpg', 'venue': f'local:{i}_venue.jpg'}}
    for k, val in (c.get('rec') or {}).items(): spec['event']['recurrence'][k] = val
    for k, val in (c.get('ev') or {}).items(): spec['event'][k] = val
    for k, val in (c.get('ve') or {}).items(): spec['venue'][k] = val
    for k, val in (c.get('og') or {}).items(): spec['org'][k] = val
    json.dump([spec], open(PP + f'local_{i}.json', 'w', encoding='utf-8'), ensure_ascii=True)
    print('ok', i, spec['event']['title'][:50], os.path.getsize(PP + f'local/{i}_event.jpg'))
