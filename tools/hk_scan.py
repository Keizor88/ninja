# ============================================================
#  HK HORIZON SCAN — distribusi model (bias-corrected) buat
#  beberapa hari ke depan. Nyari tanggal yg "menarik" (spread
#  lebar / tail gede) = tempat edge paling mungkin. Cuma butuh
#  Open-Meteo + HKO. Bootstrap:
#    import urllib.request
#    u="https://raw.githubusercontent.com/Keizor88/ninja/claude/weather-prediction-market-guide-m83zaq/tools/hk_scan.py"
#    exec(urllib.request.urlopen(u).read().decode())
# ============================================================
import urllib.request, urllib.parse, json
from datetime import date

METRIC = globals().get("HK_METRIC", "max")   # "max" / "min"
LAT, LON, TZ = 22.3193, 114.1694, "Asia/Hong_Kong"
MODELS = "gfs_seamless,ecmwf_ifs025,icon_seamless"
var = "temperature_2m_min" if METRIC == "min" else "temperature_2m_max"

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    return urllib.request.urlopen(req, timeout=40).read().decode("utf-8", "ignore")

# --- auto-bias HKO ---
def auto_bias():
    gp = {"latitude": LAT, "longitude": LON, "daily": var, "timezone": TZ,
          "past_days": 60, "forecast_days": 1, "temperature_unit": "celsius",
          "models": "best_match"}
    gd = json.loads(fetch("https://api.open-meteo.com/v1/forecast?" +
        "&".join(f"{k}={urllib.parse.quote(str(v))}" for k, v in gp.items())))["daily"]
    grid = {t: v for t, v in zip(gd["time"], gd[var]) if v is not None}
    dtype = "CLMMINT" if METRIC == "min" else "CLMMAXT"
    today = date.today(); hko = {}
    for (yy, mm) in {(today.year, today.month),
                     (today.year if today.month > 1 else today.year-1, today.month-1 or 12)}:
        try: txt = fetch(f"https://data.weather.gov.hk/weatherAPI/opendata/opendata.php"
                         f"?dataType={dtype}&rformat=csv&station=HKO&year={yy}&month={mm}")
        except Exception: continue
        for line in txt.splitlines():
            f=[x.strip() for x in line.split(",")]
            if len(f)>=4 and f[0].isdigit() and f[1].isdigit() and f[2].isdigit():
                try: hko[f"{int(f[0]):04d}-{int(f[1]):02d}-{int(f[2]):02d}"]=float(f[3])
                except ValueError: pass
    c=[d for d in grid if d in hko and date.fromisoformat(d)<today]
    if not c: return 0.0, 0
    b=[hko[d]-grid[d] for d in c]; return sum(b)/len(b), len(b)

bias, nb = auto_bias()

# --- ensemble semua tanggal ---
p = {"latitude": LAT, "longitude": LON, "daily": var, "models": MODELS,
     "timezone": TZ, "forecast_days": 16, "temperature_unit": "celsius"}
d = json.loads(fetch("https://ensemble-api.open-meteo.com/v1/ensemble?" +
    "&".join(f"{k}={urllib.parse.quote(str(v))}" for k, v in p.items())))["daily"]
series = [v for k, v in d.items() if k.startswith(var) and isinstance(v, list)]
today = date.today()

mlbl = "MIN" if METRIC=="min" else "MAX"
print(f"\n=== HK {mlbl} HORIZON SCAN — bias {bias:+.2f}°C (n={nb}) dipasang ===")
print(f"{'tanggal':<12}{'d+':>4}{'mean':>7}{'p10':>7}{'p90':>7}{'spread':>8}   distribusi (integer bucket)")
print("-"*78)
for di, dt in enumerate(d["time"]):
    h = (date.fromisoformat(dt) - today).days
    if h < 0 or h > 9: continue
    vals = [float(s[di]) + bias for s in series if di < len(s) and s[di] is not None]
    if not vals: continue
    sv = sorted(vals); nn = len(sv)
    mean = sum(sv)/nn; p10 = sv[int(.1*(nn-1))]; p90 = sv[int(.9*(nn-1))]
    spread = p90 - p10
    # histogram ringkas: dari floor(p10) sampai ceil(p90)
    lo, hi = int(p10), int(p90)+1
    cells = []
    for t in range(lo, hi+1):
        frac = sum(1 for v in vals if t-0.5 <= v < t+0.5)/nn
        if frac >= 0.10: cells.append(f"{t}:{frac*100:.0f}%")
    flag = "  <== spread lebar" if spread >= 4 else ("  <== sempit" if spread <= 2 else "")
    print(f"{dt:<12}{h:>4}{mean:>7.1f}{p10:>7.1f}{p90:>7.1f}{spread:>8.1f}   {' '.join(cells)}{flag}")
print("-"*78)
print("\n>> Incer tanggal 3-5 hari out dgn SPREAD LEBAR (>=4) & bucket 'menonjol'")
print("   yg beda dari intuisi market. Screenshot market tanggal itu -> run market_hk.py.")
print(">> Ganti ke MIN: taruh  HK_METRIC='min'  sebelum exec.\n")
