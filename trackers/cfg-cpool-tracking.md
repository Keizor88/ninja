# CFG (Centrifuge) & CPOOL (Clearpool) — Deep Dive

**Trigger:** `cfg cpool update`
**Tarikan:** 27 Agu 2026 · **refresh sebelum eksekusi**

---

## ⚠️ KOREKSI: aku salah soal CPOOL
Pesan sebelumnya aku bilang buyback CPOOL "**BARU AKAN diumumkan, belum live**". **Salah.**
**Buyback CPOOL SUDAH JALAN sejak 20 Okt 2025** ("resumption of its CPOOL buyback program", didanai revenue seluruh ekosistem: Dynamic Pools, Prime, Credit Vaults, USDX T-Pool).
Tapi begitu dibuka mekaniknya, **tetap gak lolos** — alasannya beda, dijelasin di bawah.

---

# 🔶 CPOOL (Clearpool) — mcap $19.43M

## Apa ini
Marketplace kredit terdesentralisasi: peminjam institusi akses pinjaman **tanpa jaminan penuh**. Produk: Dynamic Pools, Prime, Credit Vaults, USDX T-Pool. **Ozean** = blockchain RWA-yield bareng **Hex Trust** (custodian institusi teregulasi), didukung Optimism.

## Angka
| Metrik | Nilai |
|---|---|
| Mcap | **$19.43M** (paling murah dari semua kandidat) |
| Suplai | **fixed 1B, genesis Apr-2021 — nol inflasi** ✅ |
| Loans originated | >$650M kumulatif |
| USDX T-Pool | $41M (Flare) |
| **Revenue** | ⛔ **BELUM ADA ANGKA** |

## 🚨 Kenapa tetap gak lolos: buyback-nya RESIRKULASI, bukan burn
Alokasi token hasil buyback:
- **50% → Clearpool Rewards** (dibagi lagi ke user = **muter balik ke peredaran**)
- **50% → Clearpool Reserve** (ditahan, **tidak dibakar**)
- **0% DIBAKAR**

→ Ini **persis temuan riset buyback-meta**: *"fee buybacks just recirculate tokens to stakers"* — 9 dari 11 token buyback gagal ngurangin suplai karena ini. Buyback CPOOL **gak ngurangin suplai beredar secara bersih.**
→ **Grade: 🟡** — mekanik ada & live, tapi efeknya ke holder pasif tipis. Bukan ❌ (revenue-nya nyata & nol inflasi), tapi bukan 🟢.

## ⛔ Data gap kritis
**Revenue-nya berapa?** Tanpa itu **intensitas buyback gak bisa dihitung sama sekali.** Di mcap $19M, revenue $1M aja udah 5% — tapi bisa juga $100K. **Gak bisa dinilai.**
→ Tarik: https://defillama.com/protocol/clearpool (Fees/Revenue/Holders Revenue Ann)

---

# 🔷 CFG (Centrifuge) — mcap $52.9M

## Apa ini
Infrastruktur tokenisasi RWA (kredit terstruktur, trade finance). Klien besar: **Janus Henderson JAAA** (CLO AAA-rated), **Grove $250M**, produk **JTRSY** (T-bill tokenized) & **SPXA** (S&P 500). Integrasi dalam ke Sky.

## Angka — murahnya nyata
| Metrik | Nilai |
|---|---|
| Mcap | **$52.9M** (circ 380M, harga ~$0.139) |
| **TVL** | **$1.61B** |
| **mcap/TVL** | **0.033** vs SKY 0.274 → **CFG 8.3x lebih murah per TVL** |
| Revenue proyeksi 2026 | ~$15M → **P/S ~3.5x** |
| **Katalis** | **Coinbase tunjuk "Preferred Tokenization Infrastructure" + investasi strategis** |

## ❌ Tapi accrual SEKARANG = NOL
- **Inflasi 3%/thn → masuk DAO TREASURY** (bukan holder) = **POLA ARB PERSIS**
- Fee transaksi → **validator & nominator** (yang stake amanin chain), bukan holder pasif
- **Holder pasif: ke-dilusi 3%/thn, dapet NOL**
→ **Grade sekarang: ❌** (fundamental bagus, gak nyampe token — persis kasus ARB/ONDO)

## 🎲 TAPI ADA OPSIONALITAS BESAR: **CP172**
Proposal governance **CP172** (RFC, 14 hari): **CFG holder yang eligible bisa TUKAR token jadi SAHAM EKUITAS di Centrifuge Inc., rasio 1:1.**
**Kalau lolos, ini nyelesain masalah struktural RWA yang kita temuin:** selama ini value RWA lari ke *operating company*, bukan token. CP172 **mengubah token JADI operating company.** Bukan nambal accrual — melompati masalahnya.
**Risiko proposal:** (a) bisa gak lolos; (b) **"eligible"** kemungkinan butuh akreditasi → mayoritas retail bisa gak kebagian; (c) ekuitas swasta = **ILIKUID**, gak bisa dijual bebas; (d) syarat konversi bisa gak menguntungkan; (e) implikasi sekuritas/regulasi.

---

# ⚖️ VERDICT DUA-DUANYA
| | CPOOL | CFG |
|---|---|---|
| Mcap | $19.43M | $52.9M |
| Inflasi | **nol** ✅ | **3%/thn ke treasury** ❌ |
| Buyback | live tapi **0% burn** (resirkulasi) | tidak ada |
| Accrual ke holder pasif | tipis | **NOL** |
| Grade | 🟡 | ❌ (dgn opsionality) |
| Data gap | **revenue gak ada** | — |
| Pemicu masuk | buyback diubah ke **BURN** + revenue terverifikasi | **CP172 LOLOS + eligible mencakup retail** |

## 🎯 SIKAP
**Dua-duanya WATCHLIST, bukan beli.** Alasannya bukan "bisnisnya jelek" — bisnis dua-duanya nyata (CFG TVL $1.61B + backing Coinbase; CPOOL nol inflasi + Ozean/Hex Trust). Alasannya: **pipanya belum nyampe ke holder pasif.**
**CFG lebih menarik dari CPOOL** — TVL 8.3x lebih murah dari SKY, katalis Coinbase nyata, dan CP172 = opsionality yang bisa re-rate tajam di mcap $52.9M. **Tapi jangan beli sebelum CP172 jelas** (lolos? siapa yang eligible?). Beli sekarang = beli janji, persis kesalahan ONDO.
**Ukuran kalau nekat:** posisi lottery kecil, sadar bahwa yang dibeli adalah **opsi atas keputusan governance**, bukan cashflow.
