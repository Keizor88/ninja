# Bias Calibrations (grid Open-Meteo → stasiun agensi)

Nilai koreksi hasil `tools/calibrate_auto.py`. Tambahin ke `BIAS` di calculator
sebelum bucketing. **Ini aset edge lo** — bias yang bot generik gak koreksi.

| Kota | Metric | Agensi/Stasiun | BIAS (°C) | Sebar (±) | n hari | Dikalibrasi | Catatan |
|---|---|---|---|---|---|---|---|
| Hong Kong | MAX | HKO HQ | **+1.43** | 0.92 | 31 | 2026-08-19 | Stasiun darat > grid pesisir. Semua 31 hari positif. Sebar besar → bias beda per regime (hujan vs cerah). |
| Hong Kong | MIN | HKO HQ | *(belum)* | — | — | — | Diduga positif (urban heat island). Jalanin calibrate_auto METRIC=min. |
| Tokyo | MAX | Weather Underground | *(tak reliabel)* | — | 1 | 2026-08-19 | Grid pusat (Otemachi) kepanasan ~1.1° (Aug 19: 33.1 vs aktual 32). n=1 doang; Meteostat basi (stop Mar 2026), WU no free API. **Sulit dikalibrasi → hindari trade.** |

## ✅ EDGE TERVALIDASI: HK MAX tail underpriced

Validasi `hko_climo.py` (61 hari aktual HKO): **≥33 = 26.2%, ≥34 = 9.8%** — cocok
dengan P model bias-corrected (~25-36%). Tail model **bukan artefak** (sempat
dikira artefak bias flat; ternyata HKO emang sering ≥33 di puncak musim panas).

Market cenderung harga bucket ekor (33/34/35) **~10% total**, padahal aktual
**~26%** → **underpriced sistematis** (bias #3: market ketat, tail murah).

**Strategi:** beli YES 33/34 yang murah di banyak tanggal (utamakan hari panas),
size kecil per bet, perlakukan sebagai **portfolio tail** (tiap bet kalah ~70%,
pemenang bayar 5-15x). Cek dulu HK resolve ke HKO (bukan WU).

**Catatan MIN:** HKO MIN 61 hari **max cuma 29.2, ≥30 = 0%** → bucket min ≥30
selalu ~0%; kalau market harga >0, itu free BUY NO.

## Pelajaran: pilih kota by kemudahan kalibrasi

- ✅ **Tradeable:** agensi punya open-data API terkini (HK/HKO). Bisa kalibrasi 30+ hari sekali jalan.
- ❌ **Hindari:** resolve ke sumber tanpa API bersih/terkini (Tokyo→Weather Underground; Meteostat basi). Mentok di n=1, bias gak bisa dipercaya.

## Cara pakai

1. Jalanin `tools/calibrate_auto.py` (set `METRIC` & koordinat kota) → dapet BIAS.
2. Masukin ke `BIAS` di `colab_paste.py` / `market_*.py`, atau `--bias` di CLI.
3. Update tabel ini.

## Peringatan

- **Sebar (std) gede = bias gak stabil.** HK-max sebar ±0.92 → koreksi mean bener,
  tapi hari tertentu bisa meleset ±1°. Idealnya kondisikan bias ke regime cuaca
  (hujan/mendung vs cerah) kalau mau presisi.
- **Kalibrasi ulang tiap musim.** Bias bisa geser antar musim.
- Bias per **kota + metric** beda-beda — jangan pukul rata.
