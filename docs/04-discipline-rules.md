# 04 — Aturan Disiplin

Ini yang misahin menang dari kalah. Data bagus percuma kalau disiplinnya bocor.

## ⚠️ Reality: edge itu tipis

- Cuma **~7.6% wallet Polymarket** yang profit. **Edge itu WAJIB, bukan opsional.**
- Overall market **well-calibrated** (error rata-rata ~2.1pp) → lo **gak bisa
  menang** cuma dengan "nebak lebih baik" sedikit. Butuh gap yang jelas.

## Aturan

1. **Edge terbesar di 3–5 HARI out.**
   - Di horizon itu ketidakpastian di-harga lebar → gap lebih sering muncul.
   - **1-hari-out = terlalu efisien**, hindari. Market udah nge-konvergen.

2. **JANGAN bet kalau data lo gak cukup presisi.**
   - **Pelajaran Munich:** satu forecast salah baca 34°C vs market 26°C →
     keliatan "edge palsu 8°C" → itu **jebakan**, bukan edge.
   - Data buruk / sinyal aneh = **skip**. Jangan dipaksa.

3. **80% waktu = NGGAK bet.**
   - Nunggu edge jelas. **Kesabaran gak-bet = edge itu sendiri.**

4. **Track tiap bet.**
   - Catat `P(lo)`, `P(market)`, dan **hasil**. Ini buat **kalibrasi diri**:
     apakah `P(lo)` lo beneran lebih baik dari market secara konsisten?

5. **Satu wallet, no wash-trade (Sybil).**
   - Jangan multi-wallet buat manipulasi/nge-farm. Risiko banned + bukan edge.

## Template tracking (contoh)

> File siap-pakai: [`../TRADE-LOG.md`](../TRADE-LOG.md) dan
> [`../trade-log.csv`](../trade-log.csv).

Simpan tiap bet dalam tabel biar bisa dievaluasi:

| Tanggal | Kota | Market/Bucket | Horizon | P(lo) | P(market) | Edge | Sisi | Size | Hasil | Catatan |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-08-18 | Seoul | 30–31°C | 4d | 45% | 28% | +17pp | Yes | 1u | — | KMA +0.5 bias |

Setelah 10–20 bet, cek: kalau rata-rata `P(lo)` lo **kalibrasi** (yang lo bilang
45% beneran kejadian ~45%), berarti proses lo real. Kalau nggak → benahi model,
jangan naikin size.
