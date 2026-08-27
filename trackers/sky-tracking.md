# SKY (eks-MakerDAO) — Deep Dive `analyzer111` + RECHECK

**Trigger:** `sky tracking update`
**Tarikan:** 27 Agu 2026 · **refresh sebelum eksekusi**

---

## ⚠️ KOREKSI FRAMING SENDIRI
Sebelumnya aku nyebut SKY "**paling stabil / cacat paling sedikit**" dan mosisiin dia sebagai penyeimbang aman. **Itu terlalu manis.**
Hasil recheck: **SKY = BANK dengan modal TIPIS, governance terpusat, rating S&P B- (spekulatif).** Risikonya bukan kecil — risikonya **BEDA JENIS** (kredit/bank), bukan risiko spekulasi-crypto.
Itu tetap bikin dia penyeimbang yang sah (faktor risiko beda = diversifikasi nyata), **tapi "beda risiko" ≠ "risiko rendah".** Dibetulin di bawah.

---

## 1. Tesis + Skor — **7/10**
**Mesin kas terbaik di basket, dengan neraca paling rapuh.** SKY satu-satunya nama yang: accrual bersih + ~99% beredar + revenue non-spekulatif + **naik pas bunga naik** (hedge alami vs skenario hawkish yang bunuh sisa porto). Tapi dibeli bareng: **buffer modal 0.4%, rating B-, satu orang efektif ngendaliin governance.** Layak masuk sebagai **anchor basket RWA + hedge makro**, bukan sebagai "aset aman".

## 2. Apa ini
Penerbit stablecoin **USDS** (eks-DAI) via CDP + RWA (T-bill/USDC). **Penerbit stablecoin #3 dunia** setelah Tether & Circle. **USDS udah nyalip USDe (Ethena), sekarang ~2x ukurannya.** Revenue = spread antara imbal hasil aset (T-bill, bunga CDP) dikurangi yang dibayar ke penabung (SSR).

## 3. Katalis
- 🟢 **Reserve $150M udah kepenuhan** (treasury $149.04M) → buyback bisa re-akselerasi
- 🟢 **Pasar kini price potensi KENAIKAN bunga akhir tahun** → revenue SKY naik
- 🟢 Q1-2026 **kuartal terkuat sepanjang sejarah**
- 🔴 *(negatif)* Fed potong bunga → revenue kompres

## 4. On-chain / Fundamental
| Metrik | Nilai |
|---|---|
| TVL | **$5.869B** (~69% USDC, ~29% WETH) |
| Fees (Ann, DeFiLlama) | $404.84M |
| Revenue (Ann, DeFiLlama) | $221.73M |
| **Holders Revenue (Ann)** | **$69.77M** ← yang beli-balik SKY |
| Incentives 1y | **$0** |
| Q1-2026 (laporan Sky) | gross **$123.79M** (ann ~$495M) · net surplus $46.04M |
| Posisi | stablecoin issuer **#3 dunia** |
⚠️ **Angka bentrok antar sumber** (definisi beda: gross vs net vs holders). **Yang relevan buat token cuma Holders Revenue $69.77M.** Jangan pakai "$419M/$495M" buat valuasi token.

## 5. Tokenomics — **kekuatan utama**
- **~99% beredar** (mcap $1.606B ≈ FDV $1.609B) → **overhang TERENDAH dari semua nama yang kita cek**
- **$0 incentives** → gak mungkin kena jebakan AERO/Canton
- Smart Burn Engine: revenue → beli SKY
- **Staked $704.16M = 43.84% mcap**, yield **~9.91%**

## 6. Valuasi
| | |
|---|---|
| Mcap | $1.606B (#45) · Harga $0.069 · +23.21% 30d |
| **Buyback intensity** | **4.34% mcap/thn** |
| Holders rev / revenue | 31% (sisanya ke surplus/buffer) |
Bukan termurah, bukan termahal. **Intensitas 4.34% = menengah** (LIT 15.6%, RAY 8.9%, HYPE 7%, SYRUP 0.6%).

## 7. Struktur pasar
Mcap $1.6B = mid-cap, likuiditas layak. Korelasi ke beta crypto **lebih rendah** dari nama lain di scorecard karena revenue-nya dari bunga, bukan volume trading.

## 8. Narasi vs Value
**Narasi mati, value hidup.** Nyaris gak ada yang ngomongin SKY (kalah rame sama Ethena/Ondo/HYPE) padahal dia **issuer #3 dunia dengan revenue nyata**. Kebalikan ONDO (narasi juara, token nol).

## 9. 🚨 SISI GELAP (hasil recheck — ini yang bikin skor cuma 7)
| Risiko | Detail |
|---|---|
| **Rating S&P B-** | **spekulatif/junk.** Dibatasi: konsentrasi deposan, governance terpusat, kapitalisasi lemah |
| **Buffer modal 0.4%** | ~**$23M** buffer di atas TVL $5.87B. Kerugian >0.4% aset langsung makan modal. **TIPIS BANGET** |
| **Rune efektif kuasai governance** | cuma pegang **9% token**, tapi partisipasi voting rendah → kendali de-facto. **Key-man risk** |
| **Drama governance** | Rune dorong perubahan darurat karena klaim "serangan governance" & "malapetaka tak terbalikkan" → debat transparansi/proses |
| **Fungsi FREEZE di USDS** | diusulkan — buat stablecoin "terdesentralisasi" ini pelanggaran filosofis + risiko sensor |
| **Konsentrasi deposan** | sedikit deposan besar → **risiko rush/bank-run** |
| **35% aset di RWA** | T-bill + USDC = counterparty + risiko regulasi |
| **Sensitivitas bunga** | SSR **3.75%** sekarang, dari **>8% (2024)** = turun 53%. Bunga turun → revenue kompres |

## 10. 💡 KENAPA TETAP MASUK — 4 alasan yang gak dimiliki nama lain
1. **HEDGE MAKRO ALAMI.** Pasar kini price potensi **kenaikan** bunga akhir tahun (Warsh hawkish). Skenario itu **bunuh sisa porto crypto TAPI NAIKIN revenue SKY.** Satu-satunya posisi di book yang begini.
2. **OVERHANG TERENDAH.** ~99% beredar. HYPE 25%, LIT 25%, KNTQ 28%, ASTER 33%. Gak ada unlock cliff yang lawan buyback.
3. **REVENUE NON-SPEKULATIF.** Gak butuh retail balik, gak butuh volume meme, gak butuh siklus perp. Satu-satunya di basket yang begitu.
4. **TERUJI BEAR.** Eks-Maker — lolos 2018, 2020 (Black Thursday), 2022 (Luna/FTX). Semua nama lain di scorecard Tier-2/3 belum kena bear.

## 11. Skenario
| | Isi | Prob |
|---|---|---|
| 🟢 **Bull** | Bunga naik/tinggi-lama + reserve penuh → buyback re-akselerasi, USDS terus rebut share, re-rate **2-3x** | **35%** |
| 🟡 **Base** | Bunga flat, revenue stabil, buyback 4-5%, **1-1.5x** + yield ~10% | **45%** |
| 🔴 **Bear** | Fed potong agresif (revenue kompres) ATAU insiden governance/depeg/run → **−40-60%** | **20%** |

## 12. Entry + Exit + Tripwire
**Entry:** anchor basket RWA (bobot terbesar). Akum di flush; boleh starter sekarang krn overhang rendah = risiko dilusi kecil. Stake buat ~9.9% yield sambil nunggu.
**Exit:** kalau buyback intensity turun <2% mcap sustained, atau tesis hedge-bunga patah (Fed potong dalam & lama).
**TRIPWIRE — jual/kurangi kalau:**
| Sinyal | Arti |
|---|---|
| **USDS depeg / rush deposan** | risiko modal 0.4% kejadian |
| **Fungsi freeze DIAKTIFKAN** | risiko sensor jadi nyata |
| **S&P turunin rating di bawah B-** | kredit memburuk |
| **Fed potong >100bps** | mesin revenue kompres |
| **Holders revenue turun 2 kuartal** | accrual layu |
| **Rune keluar / krisis governance** | key-man risk kejadian |

## ⛔ DATA GAP
- **Holders Revenue per kuartal** (trennya naik/turun?) — cuma punya angka annualized 1 titik
- **Rasio modal terkini** (S&P per akhir Juli — perlu update)
- **Konsentrasi deposan presisi** (berapa % dipegang top-10?)
- Sumber: https://defillama.com/protocol/sky · laporan kuartalan Sky

## 🎯 KESIMPULAN RECHECK
**SKY TETAP MASUK — tapi alasannya bukan "aman".** Alasannya: **satu-satunya hedge makro di porto** (naik pas bunga naik), overhang terendah, revenue non-spekulatif, dan sudah teruji bear.
**Yang berubah:** dia **bukan** "aset paling aman di basket". Dia bank tipis modal dengan governance terpusat dan rating junk. **Sizing harus mencerminkan itu** — anchor basket RWA, ya; tapi jangan diperlakukan seperti stablecoin atau tabungan.
