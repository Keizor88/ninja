# ============================================================
#  HKO CLIMO / TAIL VALIDATOR — histogram max/min ASLI HKO
#  beberapa bulan terakhir. Cek: seberapa sering HKO beneran
#  tembus 33? (validasi apakah tail model kena artefak bias flat)
#  Bootstrap:
#    import urllib.request
#    u="https://raw.githubusercontent.com/Keizor88/ninja/claude/weather-prediction-market-guide-m83zaq/tools/hko_climo.py"
#    exec(urllib.request.urlopen(u).read().decode())
# ============================================================
import urllib.request, urllib.parse, json
from datetime import date

METRIC = globals().get("HK_METRIC", "max")   # "max" / "min"
dtype = "CLMMINT" if METRIC == "min" else "CLMMAXT"
gvar  = "temperature_2m_min" if METRIC == "min" else "temperature_2m_max"
LAT, LON, TZ = 22.3193, 114.1694, "Asia/Hong_Kong"

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    return urllib.request.urlopen(req, timeout=40).read().decode("utf-8", "ignore")

# HKO aktual, 3 bulan terakhir
today = date.today(); hko = {}
months = set()
y, m = today.year, today.month
for _ in range(3):
    months.add((y, m)); m -= 1
    if m == 0: m = 12; y -= 1
for (yy, mm) in months:
    try: txt = fetch(f"https://data.weather.gov.hk/weatherAPI/opendata/opendata.php"
                     f"?dataType={dtype}&rformat=csv&station=HKO&year={yy}&month={mm}")
    except Exception: continue
    for line in txt.splitlines():
        f=[x.strip() for x in line.split(",")]
        if len(f)>=4 and f[0].isdigit() and f[1].isdigit() and f[2].isdigit():
            try: hko[f"{int(f[0]):04d}-{int(f[1]):02d}-{int(f[2]):02d}"]=float(f[3])
            except ValueError: pass

vals = [v for d, v in hko.items() if date.fromisoformat(d) < today]
mlbl = "MIN" if METRIC=="min" else "MAX"
if not vals:
    raise SystemExit("HKO data gagal ditarik.")
vals.sort(); n=len(vals)
mean=sum(vals)/n; mn=vals[0]; mx=vals[-1]
print(f"\n=== HKO {mlbl} AKTUAL — {n} hari terakhir (s/d kemarin) ===")
print(f"mean {mean:.1f} | min {mn:.1f} | max {mx:.1f}\n")
# histogram integer
lo, hi = int(mn), int(mx)+1
print("suhu   #hari   %    bar")
for t in range(lo, hi+1):
    c = sum(1 for v in vals if t-0.5 <= v < t+0.5)
    if c: print(f"{t:>4}   {c:>4}  {c/n*100:>4.0f}%  {'#'*c}")
print()
for th in ([33,34,35] if METRIC=="max" else [30,31,32]):
    c = sum(1 for v in vals if v >= th)
    print(f">> HKO {mlbl} >= {th}: {c}/{n} hari = {c/n*100:.1f}% (aktual musim ini)")
print("\n>> Bandingin ke P(>=33) model (~25-36%). Kalau AKTUAL jauh lebih kecil,")
print("   berarti bias flat OVER-inflate tail -> sinyal >=33 PALSU -> jgn beli tail.")
print("   Kalau AKTUAL mirip model -> tail nyata -> >=33 murah = edge beneran.\n")
