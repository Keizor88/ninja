# 08 — Pilih Kota & Cara Kalkulasi

## Prinsip pemilihan kota

Edge muncul di kota yang: **(a)** agensi regionalnya kuat & bot US lemah, dan
**(b)** ada **ketidakpastian** di horizon 3–5 hari (spread ensemble lebar =
market harga lebar = ruang edge). Kota yang cuacanya "terkunci" = market efisien
= susah dapet 10pp.

| Kota | Agensi | Kenapa menarik / hati-hati |
|---|---|---|
| **Seoul** | KMA | ⭐ Coastal, ada variabilitas monsoon/typhoon fringe di Agustus. Starter bagus. |
| **Tokyo** | JMA | ⭐ Sama, plus JMA sangat presisi → koreksi bias enak. |
| **Hong Kong** | HKO | ⭐ Typhoon season → spread lebar, tail sering underpriced. |
| **Shanghai** | CMA | ⭐ Coastal, transisi sistem cuaca. |
| Chengdu/Chongqing/Wuhan | CMA | Panas ekstrem stabil → **sering low-variance** = market efisien. Skip buat pemula. |
| Singapore | MSS | Tropis, variance **sangat kecil** → bucket ketat, 10pp langka. Hindari dulu. |
| Auckland | MetService | Southern Hemisphere (winter Agustus) — beda regime, boleh kalau lo paham. |
| Munich/Milan/Madrid/Paris | DWD/AM/AEMET/Météo-France | Kompetisi bot lebih tinggi (agensi Eropa well-covered). |

**Rekomendasi start:** **Seoul** atau **Tokyo** atau **Hong Kong**, horizon
**3–5 hari**, modal receh. Coastal Asia = spread cukup buat edge, agensi
regional = keunggulan lo.

> Kota panas-kontinental (Wuhan 35°, Chongqing 32°) kelihatan "gampang" karena
> pasti panas — tapi justru itu masalahnya: **semua orang tau**, jadi market
> ketat dan edge tipis. Edge ada di **ketidakpastian**, bukan kepastian.

## Cara kalkulasi — pakai `tools/weather_edge.py`

⚠️ **Environment remote ini blokir Open-Meteo (egress policy).** Jalanin script
di **HP/laptop lo sendiri** yang network-nya bebas. Open-Meteo gratis, tanpa API key.

### Langkah

1. **Baca bracket + harga dari Polymarket** untuk kota + tanggal target.
   Contoh market Seoul resolve 2026-08-22 punya bucket & harga Yes:
   `≤27 = 10%`, `28–29 = 30%`, `30–31 = 38%`, `≥32 = 22%`.

2. **Jalanin:**

   ```bash
   python3 tools/weather_edge.py --city seoul --date 2026-08-22 \
     --bucket "<=27:_:27" --bucket "28-29:28:29" \
     --bucket "30-31:30:31" --bucket ">=32:32:_" \
     --price "<=27:0.10" --price "28-29:0.30" \
     --price "30-31:0.38" --price ">=32:0.22"
   ```

   Format bucket = `"label:low:high"`, pakai `_` untuk sisi tak-terbatas.
   Market US pakai °F → tambah `--unit fahrenheit`.

3. **Baca output:** tiap bucket dapet `P(model)`, `edge = P−harga`, sinyal
   (BET/skip), dan `Kelly f*`. Plus statistik spread (AGREE vs DIVERGE).

4. **Layer agensi lokal** (KMA/JMA/HKO/…) → koreksi bias sebelum bet.

5. **Bet cuma kalau ada sinyal BET** (edge > 10pp). Catat ke
   [`TRADE-LOG.md`](../TRADE-LOG.md).

### Apa yang dihitung script

- Pool **multi-model ensemble** (GEFS + ECMWF + ICON default) → tiap member =
  satu skenario daily-max.
- `P(bucket)` = fraksi member yang jatuh di bracket itu (= probabilitas empiris).
- `spread p10–p90` → indikator model AGREE (sempit) vs DIVERGE (lebar), buat
  strategi tail di [bab 05](05-biases.md).
- Fractional Kelly `f* = frac · (p − price)/(1 − price)`.

### Yang TIDAK dilakukan (batas jujur)

- Koreksi bias agensi **belum otomatis** — itu judgment lo (layer manual).
- Pooling member equal-weight = penyederhanaan; ECMWF sebetulnya lebih akurat
  dari GEFS. Kalau mau, jalanin `--models ecmwf_ifs025` sendiri buat banding.
- Script **gak** mutusin buat lo. Sinyal "BET" = kandidat, bukan perintah.
