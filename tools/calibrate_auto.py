# ============================================================
#  KALIBRASI OTOMATIS — grid Open-Meteo vs data resmi HKO.
#  Narik dua-duanya sendiri (Colab network bebas). No manual input.
#  Bootstrap:
#    import urllib.request
#    u="https://raw.githubusercontent.com/Keizor88/ninja/claude/weather-prediction-market-guide-m83zaq/tools/calibrate_auto.py"
#    exec(urllib.request.urlopen(u).read().decode())
# ============================================================
import urllib.request, urllib.parse, json
from datetime import date

# ---------- ISI DI SINI ----------
LAT, LON, TZ = 22.3193, 114.1694, "Asia/Hong_Kong"
METRIC = "max"          # "max" (Highest temp) atau "min" (Lowest temp)
HKO_STATION = "HKO"     # stasiun HKO HQ (yg resolve market)
# ---------------------------------

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    return urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "ignore")

# --- 1. GRID (Open-Meteo, analisis hari lampau) ---
gvar = "temperature_2m_min" if METRIC == "min" else "temperature_2m_max"
gp = {"latitude": LAT, "longitude": LON, "daily": gvar, "timezone": TZ,
      "past_days": 60, "forecast_days": 1, "temperature_unit": "celsius",
      "models": "best_match"}
gurl = "https://api.open-meteo.com/v1/forecast?" + \
       "&".join(f"{k}={urllib.parse.quote(str(v))}" for k, v in gp.items())
gd = json.loads(fetch(gurl))["daily"]
grid = {t: v for t, v in zip(gd["time"], gd[gvar]) if v is not None}

# --- 2. AKTUAL (HKO open data, CLMMAXT/CLMMINT) ---
dtype = "CLMMINT" if METRIC == "min" else "CLMMAXT"
today = date.today()
months = {(today.year, today.month)}
pm = today.month - 1 or 12
py = today.year if today.month > 1 else today.year - 1
months.add((py, pm))

hko = {}
for (yy, mm) in months:
    hurl = (f"https://data.weather.gov.hk/weatherAPI/opendata/opendata.php"
            f"?dataType={dtype}&rformat=csv&station={HKO_STATION}&year={yy}&month={mm}")
    try:
        txt = fetch(hurl)
    except Exception as e:
        print(f"(HKO {yy}-{mm} gagal: {e})"); continue
    for line in txt.splitlines():
        f = [x.strip() for x in line.split(",")]
        if len(f) >= 4 and f[0].isdigit() and f[1].isdigit() and f[2].isdigit():
            try:
                hko[f"{int(f[0]):04d}-{int(f[1]):02d}-{int(f[2]):02d}"] = float(f[3])
            except ValueError:
                pass

# --- 3. BANDINGIN ---
common = sorted(d for d in grid if d in hko and date.fromisoformat(d) < today)
mlbl = "MIN" if METRIC == "min" else "MAX"
print(f"\n=== KALIBRASI OTOMATIS: HK {mlbl} — grid Open-Meteo vs HKO ({HKO_STATION}) ===")
if not common:
    print("Gak ada tanggal yang cocok. Cek: HKO API kebuka? METRIC bener? "
          f"(grid punya {len(grid)} hari, HKO {len(hko)} hari)")
else:
    biases = []
    print(f"{'tanggal':<12}{'grid':>8}{'HKO':>8}{'bias(HKO-grid)':>16}")
    print("-" * 44)
    for d in common[-21:]:                       # tampilin s/d 21 hari terakhir
        b = hko[d] - grid[d]; biases.append(b)
        print(f"{d:<12}{grid[d]:>8.1f}{hko[d]:>8.1f}{b:>+16.2f}")
    # pakai SEMUA hari yg cocok utk statistik (bukan cuma yg ditampilin)
    allb = [hko[d] - grid[d] for d in common]
    mb = sum(allb) / len(allb)
    sd = (sum((x - mb) ** 2 for x in allb) / len(allb)) ** 0.5
    print("-" * 44)
    print(f"\n>> BIAS RATA-RATA = {mb:+.2f}°C   (n={len(allb)} hari, sebar ±{sd:.2f})")
    arah = "lebih HANGAT" if mb > 0 else "lebih DINGIN"
    print(f">> Stasiun HKO {arah} dari grid ~{abs(mb):.2f}°C ({mlbl}).")
    print(f">> KOREKSI: set  BIAS = {mb:.2f}  di calculator (colab_paste / market_*.py / --bias).")
    if sd > 0.9:
        print(f">> ⚠️ sebar besar (±{sd:.2f}) — bias kurang stabil (mungkin campur "
              f"hari hujan & cerah). Pakai hati-hati.")
    print(f"\n>> ARTINYA BUAT MARKET AUG 20:")
    print(f"   Tambah {mb:+.2f}°C ke tiap member ensemble. Kalau ini geser mean "
          f"model ke ~market/klimatologi → 'edge' tadi PALSU (bias). Jalanin ulang "
          f"market_hk_max_aug20.py dgn BIAS={mb:.2f} buat cek sinyal aslinya.")
print()
