# ============================================================
#  KALIBRASI via METEOSTAT — grid Open-Meteo vs stasiun observasi asli.
#  Buat kota yg resolve pakai stasiun bandara/WU (mis. Tokyo=Weather
#  Underground). Bandingin beberapa kandidat stasiun sekaligus.
#  Stdlib only (urllib + gzip). Bootstrap:
#    import urllib.request
#    u="https://raw.githubusercontent.com/Keizor88/ninja/claude/weather-prediction-market-guide-m83zaq/tools/calibrate_meteostat.py"
#    exec(urllib.request.urlopen(u).read().decode())
# ============================================================
import urllib.request, urllib.parse, json, gzip
from datetime import date

# ---------- ISI DI SINI ----------
METRIC = "max"          # "max" atau "min"
TZ = "Asia/Tokyo"
# kandidat stasiun: (nama, meteostat_id, lat, lon)
#   47662 = Tokyo (JMA, pusat/Otemachi) ; 47671 = Tokyo/Haneda (bandara, pesisir)
STATIONS = [
    ("Tokyo-central(47662)", "47662", 35.6906, 139.7514),
    ("Haneda-airport(47671)", "47671", 35.5533, 139.7811),
]
# ---------------------------------

col = 2 if METRIC == "min" else 3   # meteostat daily: 0=date,1=tavg,2=tmin,3=tmax
gvar = "temperature_2m_min" if METRIC == "min" else "temperature_2m_max"

def fetch(url, binary=False):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    r = urllib.request.urlopen(req, timeout=40).read()
    return r if binary else r.decode("utf-8", "ignore")

def grid_at(lat, lon):
    gp = {"latitude": lat, "longitude": lon, "daily": gvar, "timezone": TZ,
          "past_days": 90, "forecast_days": 1, "temperature_unit": "celsius",
          "models": "best_match"}
    u = "https://api.open-meteo.com/v1/forecast?" + \
        "&".join(f"{k}={urllib.parse.quote(str(v))}" for k, v in gp.items())
    gd = json.loads(fetch(u))["daily"]
    return {t: v for t, v in zip(gd["time"], gd[gvar]) if v is not None}

def meteostat(station):
    u = f"https://bulk.meteostat.net/v2/daily/{station}.csv.gz"
    raw = gzip.decompress(fetch(u, binary=True)).decode("utf-8", "ignore")
    out = {}
    for line in raw.splitlines():
        f = line.split(",")
        if len(f) > col and len(f[0]) == 10 and f[0][4] == "-":
            try: out[f[0]] = float(f[col])
            except ValueError: pass
    return out

today = date.today()
mlbl = "MIN" if METRIC == "min" else "MAX"
print(f"\n=== KALIBRASI METEOSTAT ({mlbl}) — grid vs stasiun observasi ===")
for name, sid, lat, lon in STATIONS:
    try:
        grid = grid_at(lat, lon)
        obs = meteostat(sid)
    except Exception as e:
        print(f"\n[{name}] gagal: {e}"); continue
    common = sorted(d for d in grid if d in obs and date.fromisoformat(d) < today)
    if not common:
        rng = f"(grid {len(grid)}d, obs {len(obs)}d"
        if obs: rng += f", obs terakhir {max(obs)}"
        print(f"\n[{name}] gak ada overlap {rng}) — mungkin Meteostat belum update Agustus 2026.")
        continue
    recent = common[-30:]                       # 30 hari terakhir yg overlap
    b = [obs[d] - grid[d] for d in recent]
    mb = sum(b)/len(b); sd = (sum((x-mb)**2 for x in b)/len(b))**0.5
    print(f"\n[{name}]  overlap {recent[0]}..{recent[-1]} (n={len(recent)})")
    print(f"   BIAS (obs-grid) = {mb:+.2f}°C   sebar ±{sd:.2f}")
    print(f"   obs rata2 {sum(obs[d] for d in recent)/len(recent):.1f} | "
          f"grid rata2 {sum(grid[d] for d in recent)/len(recent):.1f}")
print("\n>> Pilih stasiun yg Weather Underground pakai buat 'Tokyo' (cek di WU).")
print(">> Pakai BIAS stasiun itu + koordinatnya buat run market ulang.")
print(">> Kalau dua-duanya beda jauh, lokasi salah bisa jadi sumber 'edge' semu.\n")
