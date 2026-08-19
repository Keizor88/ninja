# ============================================================
#  TES SENSITIVITAS LOKASI — Tokyo MAX Aug 20.
#  Jalanin ensemble di beberapa titik (pusat kota vs Haneda pesisir),
#  bandingin ke market. Kalau hasil beda jauh antar-titik -> "edge"
#  rapuh (artefak lokasi), bukan edge asli. Cuma butuh Open-Meteo.
#  Bootstrap:
#    import urllib.request
#    u="https://raw.githubusercontent.com/Keizor88/ninja/claude/weather-prediction-market-guide-m83zaq/tools/tokyo_location_test.py"
#    exec(urllib.request.urlopen(u).read().decode())
# ============================================================
import urllib.request, urllib.parse, json

DATE = "2026-08-20"; TZ = "Asia/Tokyo"
MODELS = "gfs_seamless,ecmwf_ifs025,icon_seamless"
POINTS = [
    ("Pusat kota (Otemachi)", 35.6906, 139.7514),
    ("Haneda (bandara/pesisir)", 35.5533, 139.7811),
    ("Nerima (inland NW)", 35.7357, 139.6517),
]
# market P(mkt) utk tiap bucket
MKT = {"30": .11, "31": .48, "32": .34, "33": .06, "34": .02}
BUCKETS = [("30",29.5,30.49),("31",30.5,31.49),("32",31.5,32.49),
           ("33",32.5,33.49),("34",33.5,34.49)]

def members(lat, lon):
    p = {"latitude": lat, "longitude": lon, "daily": "temperature_2m_max",
         "models": MODELS, "timezone": TZ, "forecast_days": 16,
         "temperature_unit": "celsius"}
    u = "https://ensemble-api.open-meteo.com/v1/ensemble?" + \
        "&".join(f"{k}={urllib.parse.quote(str(v))}" for k, v in p.items())
    d = json.loads(urllib.request.urlopen(u, timeout=30).read().decode())["daily"]
    i = d["time"].index(DATE)
    s = [v for k, v in d.items() if k.startswith("temperature_2m_max") and isinstance(v, list)]
    return [float(x[i]) for x in s if i < len(x) and x[i] is not None]

def P(vals, lo, hi): return sum(1 for v in vals if lo <= v <= hi)/len(vals)

print(f"\n=== TOKYO MAX {DATE} — sensitivitas lokasi (grid Open-Meteo) ===")
print(f"{'lokasi':<26}{'mean':>6}   " + "".join(f"{b:>6}" for b,_,_ in BUCKETS))
print("-"*66)
print(f"{'MARKET':<26}{'~31.3':>6}   " + "".join(f"{int(MKT[b]*100):>5}%" for b,_,_ in BUCKETS))
print("-"*66)
for name, lat, lon in POINTS:
    try:
        v = members(lat, lon)
    except Exception as e:
        print(f"{name:<26} gagal: {e}"); continue
    mean = sum(v)/len(v)
    print(f"{name:<26}{mean:>6.1f}   " + "".join(f"{P(v,lo,hi)*100:>5.0f}%" for _,lo,hi in BUCKETS))
print("-"*66)
print("\n>> Kalau mean & distribusi GESER banyak antar-lokasi (mis. pusat 31.9 vs")
print("   Haneda ~31) -> 'edge panas' tadi rapuh/artefak lokasi -> SKIP.")
print(">> Kalau SEMUA lokasi tetap jauh lebih panas dari market -> mungkin edge asli.")
print(">> Bucket resolusi = titik yg Weather Underground pakai (cek stasiun WU).\n")
