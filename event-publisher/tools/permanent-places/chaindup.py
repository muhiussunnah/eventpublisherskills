import sys, os, io, glob, hashlib, requests
from PIL import Image, ImageOps

PP = 'C:/Users/User/AppData/Local/Temp/claude/F--eventpublisherskills/4ad7473a-f7bd-4184-b47a-6ef00f11c16a/scratchpad/pp/'
CH = PP + 'chain/'
os.makedirs(CH, exist_ok=True)
UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'}


def dhash(im, n=8):
    g = ImageOps.fit(im.convert('L'), (n + 1, n))
    px = list(g.getdata())
    return sum(1 << i for i in range(n * n) if px[(i // n) * (n + 1) + i % n] > px[(i // n) * (n + 1) + i % n + 1])


def ham(a, b):
    return bin(a ^ b).count('1')


urls = open(PP + 'chain_urls.txt', encoding='utf-8').read().split()
ref = {}
for u in urls:
    p = CH + hashlib.md5(u.encode()).hexdigest() + '.img'
    if not os.path.exists(p):
        try:
            r = requests.get(u, headers=UA, timeout=40)
            if r.status_code == 200: open(p, 'wb').write(r.content)
        except Exception:
            pass
    if os.path.exists(p):
        try:
            ref[u] = dhash(Image.open(p))
        except Exception:
            pass
print('reference images', len(ref))
for pat in sys.argv[1:]:
    for f in sorted(glob.glob(PP + 'img/' + pat)):
        h = dhash(Image.open(f))
        best = min(((ham(h, v), u) for u, v in ref.items()), default=(99, ''))
        flag = 'DUP?' if best[0] <= 10 else 'ok'
        print(os.path.basename(f), flag, best[0], best[1][-60:])
