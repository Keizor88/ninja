# 01 — Overview & Edge Thesis

## Apa yang di-trade

Market suhu (temperature markets) di prediction market:

- **Polymarket** — pilih ini untuk weather: **0 taker fee** di kategori weather.
- **Kalshi** — biaya **2% of profit**.

Format market:

> **"Highest temperature in [Kota] on [Tanggal]?"**

Tiap market punya **bracket suhu** (bucket), dan tiap bracket ditradekan sebagai
Yes/No. Contoh bracket: `≤24°C`, `25–26°C`, `27–28°C`, `≥29°C`.

## Kenapa weather (edge thesis)

Weather adalah satu-satunya kategori prediction market yang bisa dimodelin
**kuantitatif murni**, karena:

1. **Diatur FISIKA, bukan sentimen.** Beda dari politik/crypto/sports yang
   digerakin narasi + manipulasi.
2. **Model ensemble publik kasih probabilitas LANGSUNG.** Spread antar-member =
   distribusi peluang, jadi lo dapet `P(outcome)` gratis dari data.
3. **Bias agensi nasional = edge persisten & terukur** (per kota, per musim, per
   tipe suhu — misal bias di suhu ekstrem beda dari suhu normal).
4. **Kompetisi lebih rendah** dibanding election markets.
5. **Resolusi objektif.** Suhu diukur di stasiun resmi → zero ambiguitas
   settlement. Gak ada debat "siapa yang menang."

## Prinsip Edge (inti dari segalanya)

```
Edge = P(model lo) − P(harga market)
```

- Lo **TIDAK** betting "apa yang bakal terjadi."
- Lo betting **"market salah harga berapa."**
- Menang = nemu **gap** antara probabilitas data lo vs harga pasar.
- **Bet CUMA kalau `|edge| > 10pp`** (untuk nutup fee + error model).

Ambang 10pp itu bukan angka keramat, tapi buffer minimum: model lo punya error,
market punya fee/slippage, dan lo butuh margin biar edge bertahan setelah semua
gesekan itu.
