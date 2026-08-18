# Weather Prediction Market Trading — Operating Manual

Panduan trading market suhu (weather) di prediction market seperti Polymarket & Kalshi.
Fokus: proses kuantitatif berbasis fisika, bukan tebak-tebakan sentimen.

> **Inti dari semuanya:** Lo tidak betting "apa yang bakal terjadi." Lo betting
> "market salah harga berapa." Edge = `P(model lo) − P(harga market)`. Bet hanya
> kalau `|edge| > 10pp`.

Dokumen lengkap ada di [`docs/`](docs/):

| Bab | Isi |
|---|---|
| [01 — Overview & Edge Thesis](docs/01-overview.md) | Apa yang di-trade, kenapa weather, prinsip edge |
| [02 — Sumber Data](docs/02-data-sources.md) | Model global, agensi nasional, akses data |
| [03 — Workflow](docs/03-workflow.md) | Langkah per market, dari struktur resolusi sampai sizing |
| [04 — Aturan Disiplin](docs/04-discipline-rules.md) | Kapan bet, kapan skip, tracking, risk |
| [05 — Bias yang Bisa Di-exploit](docs/05-biases.md) | Pola mispricing yang berulang |
| [06 — Tools](docs/06-tools.md) | Daftar tools & API |
| [07 — Reality Check](docs/07-reality-check.md) | Ekspektasi jujur soal profit & tujuan |

## Quick Start (chat/sesi baru)

1. Pilih **1 kota Asia** (misal Seoul / Shanghai / Hong Kong), **3–5 hari out**.
2. Modal receh dulu. Tujuan awal **bukan cuan** — kalibrasi apakah `P(lo)` akurat.
3. Jalanin [workflow](docs/03-workflow.md) **10–20×** sambil **track tiap bet**.
4. Kalau `P(lo)` konsisten lebih baik dari market → baru scale.

## TL;DR Prinsip

- **Weather diatur fisika**, satu-satunya kategori yang bisa dimodelin kuantitatif murni.
- **Ensemble spread = distribusi probabilitas** langsung dari model publik.
- **Bias agensi nasional** = edge persisten & terukur per kota/musim.
- **80% waktu = nggak bet.** Kesabaran gak-bet itu edge tersendiri.
- **Edge diferensiasi lo:** kota Asia + agensi regional (CMA/HKO/KMA/JMA) yang bot US lemah di situ.
