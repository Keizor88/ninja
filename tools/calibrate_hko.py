# ============================================================
#  KALIBRASI BIAS STASIUN — paste ke Google Colab, tekan RUN.
#  Bandingin grid Open-Meteo vs nilai ASLI yang dicatat agensi
#  (HKO/KMA/JMA/...) buat hari lampau -> hitung bias koreksi.
#  Self-contained, stdlib only.
# ============================================================
import urllib.request, urllib.parse, json

# ---------- ISI DI SINI ----------
CITY = "Hong Kong"
LAT, LON, TZ = 22.3193, 114.1694, "Asia/Hong_Kong"
METRIC = "min"          # "min" (Lowest temp) atau "max" (Highest temp)
UNIT   = "celsius"

# Nilai ASLI yg dicatat agensi utk tiap hari lampau (2-5 hari).
# Sumber termudah: Polymarket tab "Past" -> bucket yang MENANG = nilai
# (dibulatkan ke integer). Atau situs agensi utk nilai eksak.
# Makin banyak hari & makin eksak -> kalibrasi makin bagus.
AGENCY_ACTUAL = {
    "2026-08-16": 28.0,   # <- GANTI dgn data asli
    "2026-08-17": 28.0,   # <- GANTI
    "2026-08-18": 27.0,   # <- GANTI
}
# ---------------------------------

var = "temperature_2m_min" if METRIC == "min" else "temperature_2m_max"
params = {"latitude": LAT, "longitude": LON, "daily": var, "timezone": TZ,
          "past_days": 31, "forecast_days": 1, "temperature_unit": UNIT,
          "models": "best_match"}
url = "https://api.open-meteo.com/v1/forecast?" + \
      "&".join(f"{k}={urllib.parse.quote(str(v))}" for k, v in params.items())
d = json.loads(urllib.request.urlopen(url, timeout=30).read().decode())["daily"]
grid = dict(zip(d["time"], d[var]))

print(f"\n=== KALIBRASI BIAS: {CITY} — grid Open-Meteo vs agensi ({METRIC}) ===")
print(f"{'tanggal':<12}{'grid':>8}{'agensi':>9}{'bias(agensi-grid)':>19}")
print("-" * 48)
biases = []
for dt in sorted(AGENCY_ACTUAL):
    g = grid.get(dt)
    a = AGENCY_ACTUAL[dt]
    if g is None:
        print(f"{dt:<12}{'—':>8}{a:>9.1f}   (grid tak tersedia utk tgl ini)")
        continue
    b = a - g
    biases.append(b)
    print(f"{dt:<12}{g:>8.1f}{a:>9.1f}{b:>+19.2f}")
print("-" * 48)
if biases:
    mb = sum(biases) / len(biases)
    sd = (sum((x - mb) ** 2 for x in biases) / len(biases)) ** 0.5
    print(f"\n>> BIAS RATA-RATA = {mb:+.2f}°C   (n={len(biases)}, sebar ±{sd:.2f})")
    arah = "lebih HANGAT" if mb > 0 else "lebih DINGIN"
    print(f">> Stasiun {CITY} {arah} dari grid ~{abs(mb):.2f}°C.")
    print(f">> KOREKSI: di colab_paste.py set  BIAS = {mb:.2f}")
    print(f"   (tiap member ensemble ditambah {mb:+.2f}°C sebelum bucketing)")
    if sd > 0.7:
        print(f">> ⚠️ sebar besar (±{sd:.2f}) -> bias gak stabil, "
              f"tambah lebih banyak hari lampau biar yakin.")
else:
    print("\nGak ada hari yang cocok. Cek format tanggal & isi AGENCY_ACTUAL.")
print()
