# 03 — Workflow (per market)

Jalankan langkah ini **berurutan** untuk tiap market yang lo pertimbangkan.

## Langkah

1. **Konfirmasi struktur resolusi dulu.**
   - `"≥X°C"` (threshold) **vs** `"bucket tepat X°C"` (rentang).
   - Ini nentuin **semua** hitungan berikutnya. Salah baca struktur = semua
     probabilitas lo salah.

2. **Ambil data ensemble.**
   - Buka **Open-Meteo** → ambil **GEFS 31-member** + **ECMWF** high temp untuk
     kota + tanggal target.

3. **Hitung `P(bucket)`.**
   - Dari 31 member ensemble, berapa yang mendarat di bucket target?
   - Contoh: `13 / 31 = 42%`.

4. **Layer agensi nasional.**
   - Ambil forecast agensi lokal kota itu (lihat [02](02-data-sources.md)) →
     koreksi bias lokal terhadap angka model global.

5. **Bandingin ke harga market.**
   - `Edge = P(lo) − P(market)`.

6. **Keputusan bet.**
   - Bet **cuma kalau `edge > 10pp`**.
   - Size pakai **Kelly kecil** (fractional Kelly, jangan full Kelly).

## Contoh hitung cepat

```
Market: "Highest temp in Seoul on 2026-08-22, bucket 30–31°C?"  Harga Yes = 28%

GEFS 31-member yang jatuh di 30–31°C : 13  → P(model) = 13/31 = 42%
Koreksi bias KMA (musim panas cenderung +0.5°C)             → P(lo) ≈ 45%

Edge = 45% − 28% = +17pp  →  > 10pp  →  BET Yes, size Kelly kecil.
```

## Sizing — Kelly kecil

- Pakai **fractional Kelly** (misal ¼ atau ½ Kelly), bukan full Kelly.
- Full Kelly terlalu agresif ketika estimasi `P(lo)` lo sendiri punya error —
  dan di weather, error model itu nyata.
- Modal awal receh: tujuannya kalibrasi, bukan maksimalin cuan (lihat
  [07 — Reality Check](07-reality-check.md)).
