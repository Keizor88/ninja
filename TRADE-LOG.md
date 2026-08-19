# Trade Log

Catat **tiap** bet di sini — termasuk yang di-skip (biar keliatan disiplinnya).
Tujuan utama: **kalibrasi** apakah `P(lo)` lo beneran lebih baik dari market.

> Aturan: bet cuma kalau `edge > 10pp`. 80% waktu = **SKIP**. Lihat
> [docs/04-discipline-rules.md](docs/04-discipline-rules.md).

## Kolom

| Kolom | Isi |
|---|---|
| **Tanggal** | Tanggal lo bikin keputusan (bukan tanggal resolusi) |
| **Kota** | Kota market |
| **Market/Bucket** | Bracket suhu, misal `30–31°C` atau `≥29°C` |
| **Resolve** | Tanggal resolusi market |
| **Horizon** | Berapa hari out saat bet (target: 3–5d) |
| **P(lo)** | Probabilitas model lo (ensemble + koreksi agensi) |
| **P(mkt)** | Harga market (%) saat lo lihat |
| **Edge** | `P(lo) − P(mkt)` dalam pp |
| **Sisi** | Yes / No / **SKIP** |
| **Size** | Ukuran posisi (unit/USDC) |
| **Hasil** | Win / Loss / — (belum resolve) |
| **PnL** | Untung/rugi setelah fee |
| **Catatan** | Sumber bias, agensi, alasan skip, dll |

## Log

| Tanggal | Kota | Market/Bucket | Resolve | Horizon | P(lo) | P(mkt) | Edge | Sisi | Size | Hasil | PnL | Catatan |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| _(contoh)_ 2026-08-18 | Seoul | 30–31°C | 2026-08-22 | 4d | 45% | 28% | +17pp | Yes | 1u | — | — | GEFS 13/31; KMA bias +0.5°C |
| 2026-08-19 | Hong Kong | LOW 26°C | 2026-08-20 | 1d | 32% | 18% | +14pp | **SKIP** | 0 | — | — | Tool flag BUY YES 26 (122 member, mean 26.8). DITOLAK: grid Open-Meteo baca min lebih dingin dari stasiun HKO HQ (urban, TST) → mass "26" mestinya geser ke 27; +14pp = artefak bias stasiun, bukan edge. Plus 1d out = terlalu efisien. TODO: kalibrasi bias grid-vs-HKO dari data Past. |
| 2026-08-19 | Hong Kong | MAX (29 vs 31) | 2026-08-20 | 1d | mean 29.5 | ~31 | +27pp @29 (semu) | **SKIP** | 0 | — | — | Tool flag BUY YES 28/29 + BUY NO 31/32. KALIBRASI (calibrate_auto, n=31 hari) buktiin bias MAX HKO = **+1.43°C** (semua 31 hari positif). Koreksi geser mean model 29.5→~30.9 = pas market/klimatologi 31 → edge NGUAP → PALSU. Market yg bener. Bias +1.43 disimpen buat HK-max ke depan. |
| 2026-08-19 | Tokyo | MAX (33 vs 31) | 2026-08-20 | 1d | mean 31.9 | ~31.3 | +17.8pp @33 (semu) | **SKIP** | 0 | — | — | Tool flag BUY YES 33. Kalibrasi: grid Otemachi Aug 19 = 33.1 vs aktual WU 32 → grid KEPANASAN 1.1°C → koreksi bikin edge nguap. n=1 + grid produk gak sepakat (Otemachi 33.1 vs Haneda 31.6, beda 1.5°) = noise ≈ edge. Tokyo/WU susah kalibrasi (no clean API). SKIP. |
| 2026-08-19 | Hong Kong | MAX ≥33°C | 2026-08-21 | 2d | 23.8% | 2% | +21.8pp | **PAPER / probe kecil** | 0 (atau ¼Kelly) | — | — | Sinyal pertama yg survive noise. Bias-corrected +1.43. Edge sign-robust (P≥33 = 6-24% across ±0.92, selalu >2%). TAPI tail (kalah sering walau +EV, buruk buat kalibrasi single-shot), 2d out, raw 29.8 = hari mendung → bias mungkin over-koreksi. Rekomendasi: tunggu Aug 22-24 bucket tengah. |
| 2026-08-19 | Hong Kong | MAX tail 33/34 | multi | 3-5d | ≥33: 24-36% | ≥33: ~10% | +10-16pp | **EDGE ASLI (verif HKO dulu)** | portfolio kecil | — | — | VALIDASI: HKO aktual 61 hari ≥33 = 26.2%, ≥34 = 9.8% — cocok model. Tail BUKAN artefak. Market harga tail ~10% vs aktual 26% → underpriced sistematis (bias #3). STRATEGI: beli YES 33/34 murah di banyak tanggal (hari panas), size kecil, portfolio. VERIF: pastiin HK resolve ke HKO (bukan WU). |
| 2026-08-19 | Hong Kong | MAX 33°C | 2026-08-21 | 2d | ~17% | ~6% | +11pp | **YES** | $2 @6¢ (~33 sh) | — | — | Bet sah #1. Tail portfolio. Menang → ~$33. HKO confirmed. |
| 2026-08-19 | Hong Kong | MAX 34°C | 2026-08-21 | 2d | ~5% | ~2% | +3pp | **YES** | $1 @2¢ (~50 sh) | — | — | Bet sah #2. Tail tipis. Menang → ~$50. |
| | | | | | | | | | | | | |

---

## Ringkasan kalibrasi

Isi setelah tiap ~10 bet ter-resolve:

| Metrik | Nilai | Target |
|---|---|---|
| Jumlah bet (non-skip) | — | — |
| Jumlah skip | — | ~80% |
| Win rate | — | — |
| Rata-rata edge saat entry | — | > 10pp |
| **Kalibrasi**: dari bet "P(lo) ≈ X%", apakah ~X% beneran kejadian? | — | ya |
| PnL kumulatif (setelah fee) | — | — |

**Aturan scaling:** kalau `P(lo)` **kalibrasi** (yang lo bilang 45% beneran
kejadian ~45%) → baru boleh naikin size. Kalau nggak → **benahi model, jangan
naikin size.**
