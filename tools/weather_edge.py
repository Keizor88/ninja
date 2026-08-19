#!/usr/bin/env python3
"""
weather_edge.py — Weather prediction-market edge calculator.

Jalanin seluruh workflow dari docs/03-workflow.md pakai data ASLI:
  1. Tarik ensemble multi-model (GEFS/ECMWF/ICON/GEM) dari Open-Meteo.
  2. Hitung daily max per member -> distribusi.
  3. P(bucket) = fraksi member yang mendarat di tiap bracket suhu.
  4. Edge = P(model) - P(market). Flag kalau |edge| > threshold.
  5. Kelly kecil (fractional) buat sizing.

Butuh: Python 3.8+, akses internet ke ensemble-api.open-meteo.com (GRATIS, no key).
Zero dependency eksternal (cuma stdlib).

Contoh:
  python3 weather_edge.py --city seoul --date 2026-08-22 \\
      --bucket "<=27:_:27" --bucket "28-29:28:29" --bucket "30-31:30:31" --bucket ">=32:32:_" \\
      --price "<=27:0.10" --price "28-29:0.30" --price "30-31:0.38" --price ">=32:0.22"

Kalau market pakai Fahrenheit (biasanya kota US), tambah:  --unit fahrenheit
"""

import argparse
import json
import sys
import urllib.request
import urllib.error
import urllib.parse
from datetime import date

ENSEMBLE_URL = "https://ensemble-api.open-meteo.com/v1/ensemble"

# Model Open-Meteo -> perkiraan jumlah member (buat info; kode ngitung member aktual).
MODELS = {
    "gfs_seamless": 31,      # NOAA GEFS
    "ecmwf_ifs025": 51,      # ECMWF (model terbaik)
    "icon_seamless": 40,     # DWD ICON
    "gem_global": 21,        # Environment Canada
}

# Kota tradeable + agensi nasional (lihat docs/02 & docs/08).
CITIES = {
    # Asia — EDGE DIFERENSIASI (bot US lemah di sini)
    "seoul":     (37.5665, 126.9780, "Asia/Seoul",      "KMA"),
    "tokyo":     (35.6762, 139.6503, "Asia/Tokyo",      "JMA"),
    "hongkong":  (22.3193, 114.1694, "Asia/Hong_Kong",  "HKO"),
    "shanghai":  (31.2304, 121.4737, "Asia/Shanghai",   "CMA"),
    "beijing":   (39.9042, 116.4074, "Asia/Shanghai",   "CMA"),
    "chengdu":   (30.5728, 104.0668, "Asia/Shanghai",   "CMA"),
    "chongqing": (29.4316, 106.9123, "Asia/Shanghai",   "CMA"),
    "wuhan":     (30.5928, 114.3055, "Asia/Shanghai",   "CMA"),
    "shenzhen":  (22.5431, 114.0579, "Asia/Shanghai",   "CMA"),
    "taipei":    (25.0330, 121.5654, "Asia/Taipei",     "CWA"),
    "singapore": (1.3521,  103.8198, "Asia/Singapore",  "MSS"),
    "jakarta":   (-6.2088, 106.8456, "Asia/Jakarta",    "BMKG"),
    "mumbai":    (19.0760, 72.8777,  "Asia/Kolkata",    "IMD"),
    "delhi":     (28.6139, 77.2090,  "Asia/Kolkata",    "IMD"),
    "lucknow":   (26.8467, 80.9462,  "Asia/Kolkata",    "IMD"),
    # Eropa / lainnya
    "london":    (51.5074, -0.1278,  "Europe/London",   "Met Office"),
    "paris":     (48.8566, 2.3522,   "Europe/Paris",    "Meteo-France"),
    "munich":    (48.1351, 11.5820,  "Europe/Berlin",   "DWD"),
    "milan":     (45.4642, 9.1900,   "Europe/Rome",     "AM"),
    "madrid":    (40.4168, -3.7038,  "Europe/Madrid",   "AEMET"),
    "warsaw":    (52.2297, 21.0122,  "Europe/Warsaw",   "IMGW"),
    "moscow":    (55.7558, 37.6173,  "Europe/Moscow",   "Roshydromet"),
    "istanbul":  (41.0082, 28.9784,  "Europe/Istanbul", "MGM"),
    "ankara":    (39.9334, 32.8597,  "Europe/Istanbul", "MGM"),
    "telaviv":   (32.0853, 34.7818,  "Asia/Jerusalem",  "IMS"),
    "auckland":  (-36.8485, 174.7633, "Pacific/Auckland", "MetService"),
}


def fetch_members(lat, lon, tz, models, unit, daily_var="temperature_2m_max"):
    """Return dict {date_str: [daily value per member]} pooling all members across models.

    daily_var: 'temperature_2m_max' (market 'Highest temp') atau
               'temperature_2m_min' (market 'Lowest temp').
    """
    params = {
        "latitude": lat,
        "longitude": lon,
        "daily": daily_var,
        "models": ",".join(models),
        "timezone": tz,
        "forecast_days": 16,
        "temperature_unit": unit,
    }
    q = "&".join(f"{k}={urllib.parse.quote(str(v))}" for k, v in params.items())
    url = f"{ENSEMBLE_URL}?{q}"
    try:
        with urllib.request.urlopen(url, timeout=30) as r:
            data = json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        sys.exit(f"HTTP {e.code} dari Open-Meteo: {e.read().decode()[:300]}")
    except Exception as e:
        sys.exit(f"Gagal fetch: {e}\nURL: {url}")

    daily = data.get("daily") or {}
    times = daily.get("time")
    if not times:
        sys.exit(f"Respons tak terduga (no daily.time). Raw: {json.dumps(data)[:400]}")

    # Kumpulin SEMUA seri yang namanya diawali daily_var
    # (base + member01..memberNN, dari semua model yang di-pool).
    member_series = [v for k, v in daily.items()
                     if k.startswith(daily_var) and isinstance(v, list)]

    by_date = {}
    for di, d in enumerate(times):
        vals = []
        for series in member_series:
            if di < len(series) and series[di] is not None:
                vals.append(float(series[di]))
        by_date[d] = vals
    return by_date, data.get("daily_units", {}).get(daily_var, unit[:1].upper())


def bucket_prob(vals, low, high):
    """Fraksi member di [low, high]. low/high None = tak terbatas di sisi itu."""
    if not vals:
        return 0.0
    n = 0
    for v in vals:
        if (low is None or v >= low) and (high is None or v <= high):
            n += 1
    return n / len(vals)


def kelly_fraction(p, price, frac=0.25):
    """Fractional Kelly buat kontrak binary Yes @ price (payout 1). f* = (p - price)/(1 - price)."""
    if price >= 1 or price <= 0:
        return 0.0
    edge = p - price
    if edge <= 0:
        return 0.0
    return frac * edge / (1 - price)


def parse_bucket(s):
    # "label:low:high"  -> pakai "_" utk unbounded. Contoh "<=27:_:27", ">=32:32:_"
    label, lo, hi = s.split(":")
    lo = None if lo in ("_", "", "-inf") else float(lo)
    hi = None if hi in ("_", "", "inf") else float(hi)
    return label, lo, hi


def main():
    ap = argparse.ArgumentParser(description="Weather prediction-market edge calculator")
    ap.add_argument("--city", required=True, help="nama kota (lihat CITIES) atau 'lat,lon,tz'")
    ap.add_argument("--date", required=True, help="tanggal resolusi market YYYY-MM-DD")
    ap.add_argument("--bucket", action="append", default=[], required=True,
                    help='"label:low:high", pakai _ utk tak-terbatas. Boleh berkali-kali.')
    ap.add_argument("--price", action="append", default=[],
                    help='"label:harga_yes" (0..1). Kalau kosong, cuma nampilin P(model).')
    ap.add_argument("--models", default="gfs_seamless,ecmwf_ifs025,icon_seamless",
                    help="model Open-Meteo dipisah koma (default: GEFS+ECMWF+ICON)")
    ap.add_argument("--unit", default="celsius", choices=["celsius", "fahrenheit"])
    ap.add_argument("--metric", default="max", choices=["max", "min"],
                    help="max = market 'Highest temp'; min = market 'Lowest temp'")
    ap.add_argument("--bias", type=float, default=0.0,
                    help="koreksi bias stasiun (°C) dari kalibrasi; ditambah ke tiap member")
    ap.add_argument("--threshold", type=float, default=0.10, help="min |edge| utk BET (default 0.10 = 10pp)")
    ap.add_argument("--kelly", type=float, default=0.25, help="fraksi Kelly (default 0.25)")
    args = ap.parse_args()

    if "," in args.city:
        lat, lon, tz = args.city.split(",")[:3]
        lat, lon = float(lat), float(lon)
        agency = "?"
    else:
        key = args.city.lower().replace(" ", "")
        if key not in CITIES:
            sys.exit(f"Kota '{args.city}' gak ada. Pilihan: {', '.join(sorted(CITIES))}")
        lat, lon, tz, agency = CITIES[key]

    models = [m.strip() for m in args.models.split(",") if m.strip()]
    daily_var = "temperature_2m_min" if args.metric == "min" else "temperature_2m_max"
    by_date, unit_sym = fetch_members(lat, lon, tz, models, args.unit, daily_var)

    if args.date not in by_date:
        avail = ", ".join(sorted(by_date))
        sys.exit(f"Tanggal {args.date} di luar jangkauan forecast.\nTersedia: {avail}")

    vals = by_date[args.date]
    if not vals:
        sys.exit("Gak ada member valid utk tanggal itu.")
    if args.bias:
        vals = [v + args.bias for v in vals]

    prices = {}
    for p in args.price:
        lbl, pr = p.rsplit(":", 1)
        prices[lbl] = float(pr)

    buckets = [parse_bucket(b) for b in args.bucket]

    # Statistik distribusi
    svals = sorted(vals)
    n = len(svals)
    mean = sum(svals) / n
    median = svals[n // 2]
    p10 = svals[int(0.10 * (n - 1))]
    p90 = svals[int(0.90 * (n - 1))]
    spread = p90 - p10

    horizon = (date.fromisoformat(args.date) - date.today()).days

    metric_lbl = "daily-MIN (Lowest temp)" if args.metric == "min" else "daily-MAX (Highest temp)"
    print(f"\n=== {args.city.upper()}  |  resolve {args.date}  |  ~{horizon}d out  |  agensi lokal: {agency} ===")
    print(f"Metric: {metric_lbl}   |  Model: {', '.join(models)}   |  member valid: {n}   |  unit: {unit_sym}")
    print(f"Distribusi {metric_lbl}:  mean {mean:.1f}  median {median:.1f}  "
          f"p10 {p10:.1f}  p90 {p90:.1f}  spread(p10-p90) {spread:.1f}{unit_sym}")
    print(f"  -> spread lebar = model DIVERGE (tail risk nyata); spread sempit = model AGREE.\n")

    print(f"{'bucket':<12}{'P(model)':>10}{'P(market)':>11}{'edge':>9}{'sinyal':>10}{'Kelly f*':>10}")
    print("-" * 62)
    total_p = 0.0
    any_bet = False
    for label, lo, hi in buckets:
        p = bucket_prob(vals, lo, hi)
        total_p += p
        if label in prices:
            price = prices[label]
            edge = p - price
            f = kelly_fraction(p, price, args.kelly)
            if edge >= args.threshold:
                sig, any_bet = "BET Yes", True
            elif edge <= -args.threshold:
                sig, any_bet = "BET No", True
            else:
                sig = "skip"
            print(f"{label:<12}{p*100:>9.1f}%{price*100:>10.1f}%{edge*100:>+8.1f}pp{sig:>10}{f:>10.3f}")
        else:
            print(f"{label:<12}{p*100:>9.1f}%{'—':>11}{'—':>9}{'—':>10}{'—':>10}")

    print("-" * 62)
    print(f"{'TOTAL P':<12}{total_p*100:>9.1f}%   (idealnya ~100% kalau bucket nutup semua ruang)")

    if prices and not any_bet:
        print(f"\n>> Gak ada edge > {args.threshold*100:.0f}pp. Sesuai disiplin: SKIP. "
              f"(80% waktu emang gak bet.)")
    elif prices:
        print(f"\n>> Ada sinyal BET. Cross-check agensi {agency} dulu, size Kelly kecil, "
              f"catat ke TRADE-LOG.md.")
    print("\nCatatan: P(model) mentah dari pooled ensemble. LAYER koreksi bias agensi "
          f"({agency}) sebelum bet (docs/03 langkah 4). Data buruk/aneh = SKIP.\n")


if __name__ == "__main__":
    main()
