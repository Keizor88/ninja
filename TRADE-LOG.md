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
| 2026-08-19 | Hong Kong | MAX (29 vs 31) | 2026-08-20 | 1d | mean 29.5 | ~31 | +27pp @29 / −25pp @32 | **HOLD (kalibrasi)** | 0 | — | — | Tool flag BUY YES 28/29 + BUY NO 31/32 (gede). Model mean 29.5 = 1.5°C di bawah market & klimatologi (~31) → dugaan cool-bias grid coastal vs stasiun HKO darat. WAJIB kalibrasi MAX: grid≈HKO → edge ASLI & besar (eksekusi); grid ~1.5° dingin → palsu (skip). Nunggu data Past max Aug 18/19. |
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
