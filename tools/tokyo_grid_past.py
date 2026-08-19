# ============================================================
#  GRID PAST — cetak max grid Open-Meteo Tokyo utk hari lampau,
#  buat dibandingin manual sama max ASLI (Weather Underground /
#  hasil resolved market) -> hitung bias grid-vs-WU.
#  Bootstrap:
#    import urllib.request
#    u="https://raw.githubusercontent.com/Keizor88/ninja/claude/weather-prediction-market-guide-m83zaq/tools/tokyo_grid_past.py"
#    exec(urllib.request.urlopen(u).read().decode())
# ============================================================
import urllib.request, urllib.parse, json
from datetime import date

TZ = "Asia/Tokyo"
POINTS = [
    ("Pusat(Otemachi)", 35.6906, 139.7514),
    ("Haneda", 35.5533, 139.7811),
]

# OPSIONAL: isi max ASLI dari WU 'Daily Observations' / bucket resolved market.
# Kalau diisi, script langsung hitung bias-nya. Kalau kosong, cuma cetak grid.
ACTUAL = {
    # "2026-08-17": 32,
    # "2026-08-18": 33,
    # "2026-08-19": 33,
}

def grid(lat, lon):
    p = {"latitude": lat, "longitude": lon, "daily": "temperature_2m_max",
         "timezone": TZ, "past_days": 10, "forecast_days": 1,
         "temperature_unit": "celsius", "models": "best_match"}
    u = "https://api.open-meteo.com/v1/forecast?" + \
        "&".join(f"{k}={urllib.parse.quote(str(v))}" for k, v in p.items())
    d = json.loads(urllib.request.urlopen(u, timeout=30).read().decode())["daily"]
    return dict(zip(d["time"], d["temperature_2m_max"]))

cols = {name: grid(lat, lon) for name, lat, lon in POINTS}
today = date.today()
dates = [d for d in sorted(next(iter(cols.values()))) if date.fromisoformat(d) < today]

print("\n=== GRID MAX Tokyo (hari lampau) — buat kalibrasi vs WU ===")
head = f"{'tanggal':<12}" + "".join(f"{n:>18}" for n in cols)
if ACTUAL: head += f"{'WU aktual':>11}"
print(head); print("-"*len(head))
for d in dates[-10:]:
    row = f"{d:<12}" + "".join(f"{cols[n].get(d, float('nan')):>18.1f}" for n in cols)
    if d in ACTUAL: row += f"{ACTUAL[d]:>11.1f}"
    print(row)

if ACTUAL:
    print("\n--- BIAS (WU aktual − grid) ---")
    for name in cols:
        b = [ACTUAL[d] - cols[name][d] for d in ACTUAL if d in cols[name]]
        if b:
            mb = sum(b)/len(b)
            print(f"  vs {name:<16}: {mb:+.2f}°C  (n={len(b)})")
    print(">> Pakai bias stasiun yg dipakai WU. Set BIAS itu di market_tokyo, run ulang.")
else:
    print("\n>> Isi dict ACTUAL dgn max asli WU (atau bucket resolved market) utk")
    print("   tanggal2 di atas, run lagi -> keluar bias-nya.")
print()
