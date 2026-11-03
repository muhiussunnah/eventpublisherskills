import json, sys, os, urllib.parse, concurrent.futures as cf
import requests
from PIL import Image, ImageDraw, ImageOps

PP = 'C:/Users/User/AppData/Local/Temp/claude/F--eventpublisherskills/4ad7473a-f7bd-4184-b47a-6ef00f11c16a/scratchpad/pp/'
IMG = PP + 'img/'
os.makedirs(IMG, exist_ok=True)
UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'}


def wsrv(url, logo=False, extra=''):
    e = urllib.parse.quote(url, safe='')
    if logo:
        return f'https://wsrv.nl/?url={e}&w=512&h=512&fit=contain&cbg=white&bg=white&output=jpg&q=90'
    return f'https://wsrv.nl/?url={e}&w=1080&h=1080&fit=cover&output=jpg&q=88{extra}'


def fetch(job):
    path, url = job
    if os.path.exists(path) and os.path.getsize(path) > 5000:
        return path, 'cached'
    try:
        r = requests.get(url, headers=UA, timeout=45)
        if r.status_code != 200 or not r.headers.get('content-type', '').startswith('image'):
            return path, f'http {r.status_code}'
        open(path, 'wb').write(r.content)
        return path, f'ok {len(r.content)}'
    except Exception as ex:
        return path, 'err ' + str(ex)[:60]


def main(groups):
    places = []
    for g in groups:
        f = PP + f'res_{g}.json'
        if not os.path.exists(f):
            print('missing', g); continue
        for x in json.load(open(f, encoding='utf-8')):
            x['_g'] = g
            places.append(x)
    jobs = []
    for x in places:
        if x.get('skip'):
            continue
        for k, u in enumerate((x.get('images') or [])[:4]):
            jobs.append((IMG + f"{x['i']}_{k}.jpg", wsrv(u)))
        lg = (x.get('org') or {}).get('logo')
        if lg:
            jobs.append((IMG + f"{x['i']}_logo.jpg", wsrv(lg, logo=True)))
    status = {}
    with cf.ThreadPoolExecutor(8) as ex:
        for p, s in ex.map(fetch, jobs):
            status[os.path.basename(p)] = s
    bad = {k: v for k, v in status.items() if not (v.startswith('ok') or v == 'cached')}
    print('images', len(jobs), 'bad', len(bad))
    for k, v in sorted(bad.items()):
        print('  BAD', k, v)
    # contact sheets: 6 places per sheet, 5 tiles per row (4 photos + logo)
    T, PAD, LAB = 230, 6, 18
    todo = [x for x in places if not x.get('skip')]
    for s in range(0, len(todo), 6):
        chunk = todo[s:s + 6]
        W = 5 * (T + PAD) + PAD
        Hh = len(chunk) * (T + LAB + PAD) + PAD
        sheet = Image.new('RGB', (W, Hh), 'white')
        d = ImageDraw.Draw(sheet)
        for r, x in enumerate(chunk):
            y = PAD + r * (T + LAB + PAD)
            d.text((PAD, y), f"#{x['i']} {x['name'][:60]}", fill='black')
            for c, tag in enumerate(['0', '1', '2', '3', 'logo']):
                p = IMG + f"{x['i']}_{tag}.jpg"
                if os.path.exists(p):
                    try:
                        im = Image.open(p).convert('RGB')
                        im = ImageOps.fit(im, (T, T))
                        sheet.paste(im, (PAD + c * (T + PAD), y + LAB))
                        d.text((PAD + c * (T + PAD) + 3, y + LAB + 3), tag, fill='yellow')
                    except Exception:
                        pass
        name = PP + f"sheet_{'_'.join(groups)}_{s // 6}.jpg"
        sheet.save(name, quality=85)
        print('sheet', name)


if __name__ == '__main__':
    main(sys.argv[1:])
