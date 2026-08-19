# ============================================================
#  MARKET: "Highest temperature in Tokyo on August 20"
#  RESOLUSI: Weather Underground 'Daily Observations' (BUKAN JMA).
#  Self-contained. Bootstrap:
#    import urllib.request
#    u="https://raw.githubusercontent.com/Keizor88/ninja/claude/weather-prediction-market-guide-m83zaq/tools/market_tokyo_max_aug20.py"
#    exec(urllib.request.urlopen(u).read().decode())
# ============================================================
import urllib.request, urllib.parse, json
from datetime import date

CITY = "Tokyo"; AGENCY = "Weather Underground (cek stasiun!)"
LAT, LON, TZ = 35.6906, 139.7514, "Asia/Tokyo"   # area Otemachi/Kitanomaru
DATE   = "2026-08-20"
METRIC = "max"
UNIT   = "celsius"
THRESHOLD = 0.10
KELLY  = 0.25
BIAS   = 0.0                   # BELUM dikalibrasi. Cek model mentah dulu.
MODELS = "gfs_seamless,ecmwf_ifs025,icon_seamless"

BUCKETS = [
    ("<=26", None, 26.49, 0.003),
    ("27",  26.5, 27.49, 0.01),
    ("28",  27.5, 28.49, 0.02),
    ("29",  28.5, 29.49, 0.04),
    ("30",  29.5, 30.49, 0.11),
    ("31",  30.5, 31.49, 0.48),
    ("32",  31.5, 32.49, 0.34),
    ("33",  32.5, 33.49, 0.06),
    ("34",  33.5, 34.49, 0.02),
    ("35",  34.5, 35.49, 0.01),
    (">=36",35.5, None,  0.004),
]

var = "temperature_2m_min" if METRIC == "min" else "temperature_2m_max"
params = {"latitude": LAT, "longitude": LON, "daily": var, "models": MODELS,
          "timezone": TZ, "forecast_days": 16, "temperature_unit": UNIT}
url = "https://ensemble-api.open-meteo.com/v1/ensemble?" + \
      "&".join(f"{k}={urllib.parse.quote(str(v))}" for k, v in params.items())
d = json.loads(urllib.request.urlopen(url, timeout=30).read().decode())["daily"]
series = [v for k, v in d.items() if k.startswith(var) and isinstance(v, list)]
if DATE not in d["time"]:
    raise SystemExit(f"{DATE} di luar jangkauan. Tersedia {d['time'][0]}..{d['time'][-1]}")
i = d["time"].index(DATE)
vals = [float(s[i]) + BIAS for s in series if i < len(s) and s[i] is not None]

n = len(vals); sv = sorted(vals)
mean = sum(sv)/n; med = sv[n//2]; p10 = sv[int(.1*(n-1))]; p90 = sv[int(.9*(n-1))]
horizon = (date.fromisoformat(DATE) - date.today()).days

def P(lo, hi): return sum(1 for v in vals if (lo is None or v >= lo) and (hi is None or v <= hi))/n
def kelly(p, price): return 0.0 if price >= 1 or price <= 0 or p <= price else KELLY*(p-price)/(1-price)

bnote = f"BIAS {BIAS:+.2f}" if BIAS else "BIAS 0 (mentah, belum dikalibrasi)"
print(f"\n=== {CITY} | resolve {DATE} | ~{horizon}d out | MAX | {AGENCY} | {bnote} ===")
print(f"member: {n} | mean {mean:.1f} med {med:.1f} p10 {p10:.1f} p90 {p90:.1f} "
      f"spread {p90-p10:.1f} ({'DIVERGE' if p90-p10>=2 else 'AGREE'})\n")
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
print(f"\n>> mean model {mean:.1f} vs puncak market 31.")
print("   Kalau mean ≈ 31 & semua skip -> SKIP (gak perlu kalibrasi).")
print("   Kalau mean beda jauh (spt HK) -> KALIBRASI dulu (bias WU), jangan langsung bet.")
print("   INGAT: resolusi Weather Underground, bukan JMA. Kalibrasi ke stasiun WU.\n")
