# ============================================================
#  HK ANALYZER (generik) — auto-kalibrasi bias HKO + hitung edge.
#  Lo cukup ganti: DATE, METRIC, dan BUCKETS (label,low,high,harga).
#  Bias dihitung OTOMATIS dari HKO tiap run (gak perlu colok manual).
#  Bootstrap:
#    import urllib.request
#    u="https://raw.githubusercontent.com/Keizor88/ninja/claude/weather-prediction-market-guide-m83zaq/tools/market_hk.py"
#    exec(urllib.request.urlopen(u).read().decode())
# ============================================================
import urllib.request, urllib.parse, json
from datetime import date

# ================= ISI DI SINI =================
# Bisa di-override dari bootstrap: definisiin HK_DATE / HK_METRIC / HK_BUCKETS
# SEBELUM exec(...) — kalau gak, pakai default di bawah.
DATE   = globals().get("HK_DATE", "2026-08-22")     # tanggal resolusi (idealnya 3-5d out)
METRIC = globals().get("HK_METRIC", "max")          # "max" / "min"
# bucket: (label, low, high, harga_yes)  None = tak-terbatas. harga = %/100.
BUCKETS = globals().get("HK_BUCKETS", [
    ("<=29", None, 29.49, 0.05),
    ("30",  29.5, 30.49, 0.20),
    ("31",  30.5, 31.49, 0.35),
    ("32",  31.5, 32.49, 0.28),
    (">=33",32.5, None,  0.12),
])
# ===============================================
THRESHOLD = 0.10
KELLY  = 0.25
LAT, LON, TZ = 22.3193, 114.1694, "Asia/Hong_Kong"
MODELS = "gfs_seamless,ecmwf_ifs025,icon_seamless"

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    return urllib.request.urlopen(req, timeout=40).read().decode("utf-8", "ignore")

var = "temperature_2m_min" if METRIC == "min" else "temperature_2m_max"

# ---- 1. AUTO-KALIBRASI bias HKO (grid analisis vs HKO resmi, ~30 hari) ----
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
                     (today.year if today.month > 1 else today.year-1,
                      today.month-1 or 12)}:
        try:
            txt = fetch(f"https://data.weather.gov.hk/weatherAPI/opendata/opendata.php"
                        f"?dataType={dtype}&rformat=csv&station=HKO&year={yy}&month={mm}")
        except Exception:
            continue
        for line in txt.splitlines():
            f = [x.strip() for x in line.split(",")]
            if len(f) >= 4 and f[0].isdigit() and f[1].isdigit() and f[2].isdigit():
                try: hko[f"{int(f[0]):04d}-{int(f[1]):02d}-{int(f[2]):02d}"] = float(f[3])
                except ValueError: pass
    common = [d for d in grid if d in hko and date.fromisoformat(d) < today]
    if not common:
        return None, 0, 0
    b = [hko[d] - grid[d] for d in common]
    mb = sum(b)/len(b); sd = (sum((x-mb)**2 for x in b)/len(b))**0.5
    return mb, sd, len(b)

# ---- 2. ENSEMBLE utk tanggal target ----
def ensemble():
    p = {"latitude": LAT, "longitude": LON, "daily": var, "models": MODELS,
         "timezone": TZ, "forecast_days": 16, "temperature_unit": "celsius"}
    d = json.loads(fetch("https://ensemble-api.open-meteo.com/v1/ensemble?" +
        "&".join(f"{k}={urllib.parse.quote(str(v))}" for k, v in p.items())))["daily"]
    if DATE not in d["time"]:
        raise SystemExit(f"{DATE} di luar jangkauan ({d['time'][0]}..{d['time'][-1]})")
    i = d["time"].index(DATE)
    s = [v for k, v in d.items() if k.startswith(var) and isinstance(v, list)]
    return [float(x[i]) for x in s if i < len(x) and x[i] is not None]

bias, sd, nb = auto_bias()
raw = ensemble()
if bias is None:
    print(">> ⚠️ Kalibrasi HKO gagal (API?). Pakai BIAS=0 — hati-hati.")
    bias, sd, nb = 0.0, 0, 0
vals = [v + bias for v in raw]

n = len(vals); sv = sorted(vals)
mean = sum(sv)/n; med = sv[n//2]; p10 = sv[int(.1*(n-1))]; p90 = sv[int(.9*(n-1))]
horizon = (date.fromisoformat(DATE) - date.today()).days
def P(lo, hi): return sum(1 for v in vals if (lo is None or v >= lo) and (hi is None or v <= hi))/n
def kelly(p, price): return 0.0 if price>=1 or price<=0 or p<=price else KELLY*(p-price)/(1-price)

mlbl = "MIN" if METRIC == "min" else "MAX"
print(f"\n=== HONG KONG {mlbl} | resolve {DATE} | ~{horizon}d out ===")
print(f"BIAS auto (HKO−grid) = {bias:+.2f}°C  (n={nb} hari, sebar ±{sd:.2f})  [udah dipasang]")
print(f"member: {n} | mean {mean:.1f} (raw {sum(raw)/len(raw):.1f}) med {med:.1f} "
      f"p10 {p10:.1f} p90 {p90:.1f} spread {p90-p10:.1f}\n")
print(f"{'bucket':<7}{'P(model)':>9}{'P(mkt)':>8}{'edge':>8}{'sinyal':>9}{'Kelly':>8}")
print("-"*49)
tot=0.0; bet=False
for lbl, lo, hi, price in BUCKETS:
    p = P(lo, hi); tot += p; edge = p - price
    if   edge >=  THRESHOLD: sig, bet = "BUY YES", True
    elif edge <= -THRESHOLD: sig, bet = "BUY NO",  True
    else:                    sig = "skip"
    print(f"{lbl:<7}{p*100:>8.1f}%{price*100:>7.0f}%{edge*100:>+7.1f}pp{sig:>9}{kelly(p,price):>8.3f}")
print("-"*49)
print(f"{'TOTAL':<7}{tot*100:>8.1f}%")
print("\n>> " + ("ADA SINYAL. Cek: horizon 3-5d? edge > sebar bias? ask di Polymarket?"
      if bet else f"Gak ada edge >{THRESHOLD*100:.0f}pp -> SKIP."))
if horizon <= 2:
    print(">> ⚠️ horizon <=2 hari = terlalu efisien. Idealnya 3-5d.")
if sd > 0.7:
    print(f">> ⚠️ sebar bias gede (±{sd:.2f}°C) = bias gak stabil (campur hari hujan/cerah). "
          f"Sinyal <~{sd*20:.0f}pp mungkin masih dalam noise -> hati-hati.")
print(">> Catat keputusan ke TRADE-LOG.md (termasuk kalau SKIP).\n")
