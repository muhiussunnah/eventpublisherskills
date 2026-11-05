"""Closure / renovation scan of every recurring place in the app.

Reads det.json (export of /admin/events/{id} for all recurring events), fetches each place's
website (and ctaLink when different), and flags pages whose text contains closure phrases.
Writes scan.json (per place: http status, matched phrases with context) and prints a summary.
"""
import json, re, sys, html, concurrent.futures as cf, time
import requests, urllib3
urllib3.disable_warnings()

AUD = r"C:\Users\User\AppData\Local\Temp\claude\793086065a500b32\4ad7473a-f7bd-4184-b47a-6ef00f11c16a\scratchpad\audit"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36",
      "Accept-Language": "sv-SE,sv;q=0.9,en;q=0.8"}

PHRASES = [
    r"stängt? för renovering", r"stängd för renovering", r"stänger för renovering", r"stängt? tills vidare",
    r"stängd tills vidare", r"tillfälligt stängt", r"tillfälligt stängd", r"stängt på obestämd tid",
    r"håller stängt", r"öppnar igen", r"återöppn", r"nyöppn", r"under renovering", r"under ombyggnad",
    r"ombyggnation", r"renoveras", r"renoveringen", r"har flyttat", r"flyttar till", r"upphört", r"lagt ner",
    r"lägger ner", r"nedlagd", r"konkurs", r"permanent stängt", r"stänger för gott", r"stängt för gott",
    r"sista öppetdag", r"har stängt", r"stängt sedan", r"stängd sedan", r"closed for renovation",
    r"temporarily closed", r"permanently closed", r"closed until", r"stängt hela", r"stängt under",
    r"öppnar (?:vi )?(?:igen )?(?:i |under |hösten |våren |sommaren )?20(?:27|28)", r"stängt 20(?:26|27)",
    r"säsongen är slut", r"säsongen är över", r"stängt för säsongen", r"vinterstängt", r"sommarstängt",
    r"i vinter är det stängt", r"öppnar till våren", r"öppnar till sommaren",
]
RX = re.compile("|".join("(?:%s)" % p for p in PHRASES), re.I)

def text_of(html_src):
    s = re.sub(r"(?is)<(script|style|noscript|svg)[^>]*>.*?</\1>", " ", html_src)
    s = re.sub(r"(?s)<[^>]+>", " ", s)
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s)

def fetch(url):
    try:
        r = requests.get(url, headers=UA, timeout=20, verify=False, allow_redirects=True)
        return r.status_code, r.url, r.text if "text" in r.headers.get("content-type", "") or "html" in r.headers.get("content-type", "") else ""
    except Exception as e:
        return -1, url, "ERR:" + type(e).__name__

def scan_one(item):
    urls = []
    for u in (item["place"].get("website"), item.get("cta")):
        if u and u.startswith("http") and u not in urls:
            urls.append(u)
    out = {"id": item["id"], "title": item["title"], "place": item["place"]["title"], "muni": item["place"].get("muni"),
           "urls": [], "hits": []}
    for u in urls[:2]:
        st, fu, body = fetch(u)
        rec = {"url": u, "status": st, "final": fu}
        if body.startswith("ERR:"):
            rec["error"] = body[4:]
        else:
            txt = text_of(body)
            for m in RX.finditer(txt):
                a, b = max(0, m.start() - 90), min(len(txt), m.end() + 90)
                out["hits"].append({"url": u, "match": m.group(0), "ctx": txt[a:b]})
                if len(out["hits"]) >= 12:
                    break
        out["urls"].append(rec)
    return out

def main():
    det = json.load(open(AUD + r"\det.json", encoding="utf-8"))
    items = list(det.values()) if isinstance(det, dict) else det
    print("places:", len(items), flush=True)
    res = []
    t0 = time.time()
    with cf.ThreadPoolExecutor(max_workers=16) as ex:
        for i, r in enumerate(ex.map(scan_one, items)):
            res.append(r)
            if (i + 1) % 100 == 0:
                print(i + 1, "done", int(time.time() - t0), "s", flush=True)
    json.dump(res, open(AUD + r"\scan.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    flagged = [r for r in res if r["hits"]]
    bad = [r for r in res if any(u["status"] != 200 for u in r["urls"]) or not r["urls"]]
    print("flagged by phrase:", len(flagged), " non-200/no url:", len(bad))

if __name__ == "__main__":
    main()
