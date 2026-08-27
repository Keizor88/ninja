# XPL (Plasma) — Deep Dive `analyzer111`

**Trigger:** `plasma update`
**Tarikan:** 27 Agu 2026 · **refresh sebelum eksekusi**

---

## 1. Tesis + Skor — **3/10 · ❌ AVOID**
**Chain yang produknya GRATIS, jadi tokennya gak bisa nangkep apa-apa — bukan gagal eksekusi, tapi by design.** Narasi paling nyambung ke tema Jackson Hole yang pernah kita liat, dan **flow-nya negatif, fee-nya nol, inflasinya jalan, unlock-nya numpuk.** Ini bukan "belum waktunya" — ini cacat struktural.

## 2. Apa ini
L1 EVM khusus stablecoin. Fitur utama: **transfer USDT TANPA BIAYA**. Didukung Bitfinex/Tether. Raise **$373M** oversubscribed, mainnet beta 25 Sep 2025, 100+ partner DeFi hari-1 (Aave, Ethena, Fluid, Euler).

## 3. 💣 MASALAH INTINYA — fee nol BY DESIGN
| Chain | Fee annualized |
|---|---|
| Solana | $324.54M |
| Tron | $317.96M |
| Base | $54.91M |
| Hyperliquid | $24.72M |
| Avalanche *(udah kita sebut "mikroskopis")* | $1.11M |
| **PLASMA** | **$0.21M** ($563.48/HARI) |

**Plasma 5.4x LEBIH KECIL dari Avalanche** — dan AVAX udah kita kasih ❌❌ karena fee-nya cuma $3,048/hari.
**Sebabnya bukan kurang pengguna. Sebabnya PRODUK UTAMANYA GRATIS.** Kalau jualannya "transfer USDT nol biaya", ya gak ada fee buat dikumpulin. **Sukses produk ≠ pendapatan protokol.**

## 4. Akrual = NEGATIF
- **Inflasi 5%/thn** (turun 0.5%/thn → baseline 3%), buat reward validator
- **Fee ke token: ~0%**
- → **NET ≈ −5%/thn BOCOR** buat holder pasif. Bukan "accrual lemah" — **accrual NEGATIF.**
- XPL cuma dipakai staking/gas non-USDT. Delegator dapet bagian reward = **bagi-bagi inflasi**, bukan bagi-bagi pendapatan.

## 5. Valuasi
| | |
|---|---|
| Harga | **$0.087128** |
| ATH | $1.68 → **−94.8%** |
| ATL | $0.07237 → cuma **+20.4%** di atas dasar |
| Debut mcap | **$2.4B** (25 Sep 2025) |
| P/Fees | **729x–2,431x** (tergantung mcap; AVAX 2,856x udah telak) |
⛔ **Mcap terkini belum ditarik** — tapi kesimpulan **kokoh di semua skenario**: $205K/thun fee gak bisa nopang mcap berapapun.

## 6. 🚨 SUPLAI — dua gelombang
- **28 Jul 2026: 1 MILIAR XPL** rilis ke pembeli US (lockup 12 bulan habis) — **UDAH KEJADIAN**, kemungkinan besar ini penjelasan outflow & harga nempel ATL
- **25 Sep 2026: cliff 1/3 token TEAM** — **BULAN DEPAN**
- Alokasi: Investor 25% · Team 25% · Ecosystem 40% · Public sale 10% → **50% ke insider**

## 7. 🔍 UJI NARASI vs FLOW — ini contoh terbaik framework kita
| Narasi | Data kita |
|---|---|
| "L1 khusus stablecoin" | stablecoin **$875.94M, 7d −5.34% = OUTFLOW** |
| "USDT zero-fee" | **fee $563/hari** = gak ada pendapatan |
| "Raise $373M oversubscribed" | harga **−94.8% dari ATH** |
| "100+ partner DeFi hari-1" | TVL Aave-on-Plasma $6.6B **tapi $0 ke XPL** |
| "Persis tema Jackson Hole" | flow keluar, insider unlock bulan depan |
**Kalau cuma denger cerita, ini pick #1 tema stablecoin. Semua lima cek ngasih jawaban kebalikan.**

## 8. Skenario
| | Isi | Prob |
|---|---|---|
| 🟢 Bull | Volume meledak + governance nyalain fee tier (belum ada rencana) + stablecoin balik inflow | **10%** |
| 🟡 Base | Tetap chain transfer murah, fee nol, inflasi jalan, XPL luruh pelan | **55%** |
| 🔴 Bear | Cliff team Sep + outflow lanjut → tembus ATL $0.0724 | **35%** |

## 9. Tripwire kalau mau dipantau (BUKAN dibeli)
| Sinyal | Arti |
|---|---|
| **Stablecoin Plasma balik INFLOW 2 refresh** | modal beneran balik |
| **Fee chain >$50K/hari** | ada model pendapatan yang jalan |
| **Governance nyalain fee/burn** | pipa ke token kebuka |
| Cliff team 25 Sep lewat tanpa dump | overhang kelar |
**Sebelum minimal 2 nyala: SKIP.**

## 🎯 PELAJARAN (lebih berharga dari tokennya)
**Model bisnis "gratis" = token gak bisa nangkep value dari produk intinya.**
Ini beda dari AVAX (fee-light karena RWA emang gak generate fee) — **Plasma milih gratis sebagai strategi.** Bagus buat adopsi, fatal buat token.
**Aturan baru: sebelum beli token chain, tanya "produk utamanya BERBAYAR gak?"** Kalau gratis, fee-nya nol, dan tokennya cuma nampung inflasi.
Ini juga **jawaban buat pertanyaan "kecipratan money flow"**: chain bisa jadi jalur uang lewat **tanpa** tokennya kecipratan sepeser pun. **Volume ≠ pendapatan ≠ akrual.**
