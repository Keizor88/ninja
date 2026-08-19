# ============================================================
#  WEATHER EDGE — paste ke Google Colab / Pydroid, tekan RUN.
#  Self-contained (gak perlu clone repo). Cuma stdlib.
#  Udah diisi market: "Lowest temp Hong Kong, Aug 20".
#  Ganti bagian "ISI DI SINI" buat market lain.
# ============================================================
import urllib.request, urllib.parse, json
from datetime import date

# ---------- ISI DI SINI (dari Polymarket) ----------
CITY   = "Hong Kong"
LAT, LON, TZ, AGENCY = 22.3193, 114.1694, "Asia/Hong_Kong", "HKO"
DATE   = "2026-08-20"          # tanggal resolusi market (YYYY-MM-DD)
METRIC = "min"                 # "min" = Lowest temp,  "max" = Highest temp
UNIT   = "celsius"             # "celsius" atau "fahrenheit" (kota US biasanya F)
THRESHOLD = 0.10               # edge minimum buat BET (0.10 = 10pp)
KELLY  = 0.25                  # fraksi Kelly (kecil)
BIAS   = 0.0                   # koreksi bias stasiun (°C), dari calibrate_hko.py
                               # contoh HK: +0.5 kalau stasiun HKO lebih hangat dari grid

# bucket: (label, low, high, harga_yes)  -> pakai None utk tak-terbatas
# harga = angka % besar di Polymarket / 100
BUCKETS = [
    ("<=22", None, 22.49, 0.005),
    ("23",  22.5, 23.49, 0.005),
    ("24",  23.5, 24.49, 0.01),
    ("25",  24.5, 25.49, 0.03),
    ("26",  25.5, 26.49, 0.18),
    ("27",  26.5, 27.49, 0.42),
    ("28",  27.5, 28.49, 0.27),
    ("29",  28.5, 29.49, 0.06),
    ("30",  29.5, 30.49, 0.02),
    ("31",  30.5, 31.49, 0.005),
    (">=32",31.5, None,  0.005),
]
MODELS = "gfs_seamless,ecmwf_ifs025,icon_seamless"   # GEFS + ECMWF + ICON
# ---------------------------------------------------

daily_var = "temperature_2m_min" if METRIC == "min" else "temperature_2m_max"
params = {"latitude": LAT, "longitude": LON, "daily": daily_var,
          "models": MODELS, "timezone": TZ, "forecast_days": 16,
          "temperature_unit": UNIT}
url = "https://ensemble-api.open-meteo.com/v1/ensemble?" + \
      "&".join(f"{k}={urllib.parse.quote(str(v))}" for k, v in params.items())

with urllib.request.urlopen(url, timeout=30) as r:
    data = json.loads(r.read().decode())

d = data["daily"]
series = [v for k, v in d.items() if k.startswith(daily_var) and isinstance(v, list)]
if DATE not in d["time"]:
    raise SystemExit(f"{DATE} di luar jangkauan forecast. Tersedia: {d['time'][0]}..{d['time'][-1]}")
i = d["time"].index(DATE)
vals = [float(s[i]) + BIAS for s in series if i < len(s) and s[i] is not None]

n = len(vals); sv = sorted(vals)
mean = sum(sv)/n; med = sv[n//2]; p10 = sv[int(.1*(n-1))]; p90 = sv[int(.9*(n-1))]
horizon = (date.fromisoformat(DATE) - date.today()).days

def P(lo, hi):
    return sum(1 for v in vals if (lo is None or v >= lo) and (hi is None or v <= hi))/n
def kelly(p, price):
    return 0.0 if price >= 1 or price <= 0 or p <= price else KELLY*(p-price)/(1-price)

mlbl = "MIN (Lowest temp)" if METRIC == "min" else "MAX (Highest temp)"
bias_note = f" | BIAS {BIAS:+.2f}°C" if BIAS else " | BIAS 0 (belum dikalibrasi!)"
print(f"\n=== {CITY} | resolve {DATE} | ~{horizon}d out | {mlbl} | agensi: {AGENCY}{bias_note} ===")
print(f"member: {n} | mean {mean:.1f} med {med:.1f} p10 {p10:.1f} p90 {p90:.1f} "
      f"spread {p90-p10:.1f}  ({'DIVERGE-tail nyata' if p90-p10>=2 else 'AGREE-sempit'})\n")
print(f"{'bucket':<7}{'P(model)':>9}{'P(mkt)':>8}{'edge':>8}{'sinyal':>9}{'Kelly':>8}")
print("-"*49)
tot = 0.0; bet = False
for lbl, lo, hi, price in BUCKETS:
    p = P(lo, hi); tot += p; edge = p - price
    if   edge >=  THRESHOLD: sig, bet = "BUY YES", True
    elif edge <= -THRESHOLD: sig, bet = "BUY NO",  True
    else:                    sig = "skip"
    print(f"{lbl:<7}{p*100:>8.1f}%{price*100:>7.0f}%{edge*100:>+7.1f}pp{sig:>9}{kelly(p,price):>8.3f}")
print("-"*49)
print(f"{'TOTAL':<7}{tot*100:>8.1f}%")
print("\n>> " + ("ADA SINYAL BET. Cross-check " + AGENCY +
      ", size Kelly kecil, catat ke log." if bet else
      f"Gak ada edge >{THRESHOLD*100:.0f}pp -> SKIP (disiplin: 80% waktu emang skip)."))
print("Catatan: layer koreksi bias agensi " + AGENCY + " sebelum eksekusi. Data aneh = SKIP.\n")
