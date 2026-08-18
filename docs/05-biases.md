# 05 — Bias yang Bisa Di-exploit

Pola mispricing yang cenderung **berulang**. Ini tempat edge muncul.

## 1. Fade "Yes / default overtrading"

- Market cenderung **over-beli sisi Yes / bucket default**.
- Konsekuensinya: **sisi No sering underpriced**.
- Aksi: cari bucket di mana Yes kelewat mahal → **jual Yes / beli No** kalau
  model lo setuju harga terlalu tinggi.

## 2. Model AGREE ketat, tapi market harga LEBAR

- Ensemble member semua **berdekatan** (spread sempit) → outcome sebenernya
  cukup pasti.
- Tapi market masih ngasih harga **lebar** ke bracket ekstrem.
- Aksi: **fade the tail** → **jual bracket ekstrem yang overpriced.**

## 3. Model DIVERGE >2°, tapi market ketat

- Ensemble **menyebar** (spread lebar, model gak sepakat) → tail risk nyata.
- Tapi market ngehargain seolah outcome pasti (bracket tengah kemahalan, tail
  kemurahan).
- Aksi: **buy the tail** → **beli bracket ekstrem** yang market underprice.

## Ringkasan

| Kondisi model | Kondisi market | Aksi |
|---|---|---|
| Agree (spread sempit) | Harga tail lebar/mahal | **Jual** tail (fade) |
| Diverge (spread lebar >2°) | Harga tail ketat/murah | **Beli** tail |
| — | Yes/default overtraded | **Beli No** (fade default) |

**Catatan:** semua ini tetap tunduk ke aturan `edge > 10pp` dan "skip kalau data
gak presisi" ([04](04-discipline-rules.md)). Bias ini nunjukin *di mana* nyari,
bukan izin buat bet tanpa edge.
