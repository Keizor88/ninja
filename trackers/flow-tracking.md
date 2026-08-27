# Capital Flow Tracking

**Trigger:** `flow tracking update`
**Tujuan:** ngikutin uang SEBELUM deploy ke eco (nangkep di kaki awal, bukan pas token udah pump)

---

## 🧠 Model: urutan aliran (leading → lagging)
```
1. Stablecoin supply naik di chain X   ← LEADING (dry powder dateng)
2. Bridge net-inflow ke X              ← modal aktif pindah
3. TVL X naik                          ← modal deploy
4. DEX volume + active address naik    ← usage nyambung
5. Token L1 (X) pump                   ← lagging
6. Eco token (DeFi→meme) pump          ← PALING lagging
```
Retail masuk #5-6 (telat). Target: masuk #1-2. **Stablecoin inflow = sinyal paling awal.**

## 🛠️ Tool stack
**Tier 1 (wajib, gratis):** DeFiLlama (Stablecoins-by-chain · Bridges · Chains TVL) · Artemis (cross-chain flow) · Arkham (whale/entity)
**Tier 2:** Nansen (smart money, paid) · DeBank (multichain, lagi difarming) · Token Terminal (revenue/chain) · Dune (custom)
**Tier 3 (rotasi makro):** TradingView (BTC.D·ETH/BTC·TOTAL2/3) · CoinGecko Categories · CryptoQuant/Coinglass (exchange netflow)

## 📋 Workflow mingguan (4 step di DeFiLlama+Artemis)
1. **Stablecoins by chain:** mana supply NAIK paling kenceng? (modal dateng)
2. **Bridges:** mana net-inflow konsisten?
3. **Chains TVL %chg 7d/30d:** naik sementara token belum? (divergence = early)
4. **DEX volume + active addr:** usage nyambung?
→ Kalau 1-4 nyala TAPI token belum pump = **window masuk.** L1 dulu → DeFi bluechip → meme paling akhir.

## ⚠️ Jebakan
- **TVL ≠ flow riil** (bisa naik gara2 harga aset / insentif mercenary — Berachain $3.3B→$71M). Cross-check stablecoin + revenue.
- **Bridge inflow bisa wash** (bot/farming). Liat sustained.
- **Stablecoin = sinyal terbaik** (modal murni, bukan mark-to-market).

---

## 🌊 SNAPSHOT 26 Agu 2026
| Metrik | Nilai | Baca |
|---|---|---|
| Total stablecoin supply | **$308B (-4.5% dari peak $322.4B Mei)** | 🔴 KONTRAKSI = dry powder nyusut |
| ETH USDT/USDC | $74.81B (-4.77%) / $45.84B (-2.40%) | outflow, dikunci di DeFi |
| DeFi TVL total | -37% YTD → $71.77B (ETH 53.1%) | rotasi/keluar |
| **RWA** | **$26.01B** | 🟢 satu-satunya kategori inflow institusi |

**Baca:** stablecoin agregat KONTRAKSI = modal keluar crypto, bukan masuk. **Konfirmasi rally sempit** (retail absen + premium negatif + Strategy jual + flow nyusut = 4 kaki demand lemah). Rotasi ke: DeFi-terkunci ETH, **RWA (satu2nya tumbuh)**, emerging (Hyperliquid). **Tema flow paling sehat = RWA.**

## 🔄 KOREKSI + ROTATION MAP (user screenshot DeFiLlama, 27 Agu)
**Koreksi:** stablecoin GAK contracting — total **$303.7B, 7d +$2.816B (+0.94%)** = stabil + mild inflow (angka "-4.5%" sebelumnya dari search stale 13 Agu). Dry powder flat-to-slightly-up. ETH stablecoin dominance 48.66%. Distribusi: ETH ~48% · Solana 6.40% · BSC 6.31% · Base ~6% · Tron 5.9% · BTC 4% · Arbitrum 1.6% · Monad 1.07%.

### Bridge NET FLOW (leading #1) — ranking
| 🟢 INFLOW | 🔴 OUTFLOW |
|---|---|
| **Base +$1.84B** (juara) | Arbitrum -$410M |
| Avalanche +$325M | **Hyperliquid -$173M** ⚠️ |
| **Solana +$220M** | Monad -$139M |
| Morph +$51M · Ink +$26M | Robinhood Chain -$87M |

### 💣 Implikasi
- **HYPE OUTFLOW -$173M padahal ATH $83** = distribusi/froth, BUKAN akumulasi. **Kelemahan ke-5** (retail absen + premium neg + Strategy jual + stablecoin flat + HYPE bridge-outflow). HYPE ATH = jual, jangan chase. + unlock $1.2B Jumat.
- **Base = juara flow** (RWA/Coinbase/tokenization) = kemana modal ngalir. Nyambung tema RWA-sehat.
- ~~**Solana +$220M** = masih narik modal → dukung SOL second-core.~~ **⚠️ DIKOREKSI v2:** ternyata cuma **+1.1% intensitas = NOISE**, bukan flow-winner. SOL tetep second-core krn L1/durabilitas, BUKAN krn flow. (lihat Mesin Presisi di bawah)
- **Arbitrum -$410M** (outflow terbesar) = konfirmasi ARB avoid (value-trap, modal kabur).
- **RH Chain -$87M / Monad -$139M** = meme frenzy cooling / post-launch cooldown.

**Rotasi:** modal → **Base (satu-satunya inflow bermakna, +10.1%)** + Avalanche (basis blm ditarik), kabur dari app-chain froth (Hyperliquid **-8.7%**) + L2 lama (Arbitrum **-8.4%**). Solana ≈ netral. *(angka intensitas = v2)*

## 🔵 KEMANA UANG DI DALAM BASE (destinasi flow)
- **~85% USDC** ("one-currency economy") → deploy ke **lending/yield vault**.
- **Morpho $3.3B TVL di Base** (curated USDC vault $1.62B, 22.5% global) = destinasi #1. Aerodrome DEX (USDC/WETH/CBBTC). Aave sekunder.
- **Insight: Base = stablecoin-YIELD economy, modal KONSERVATIF** (parkir stable, cari yield — institusi/RWA/retail-onramp), BUKAN spekulasi.
- → **Konfirmasi ke-6 regime defensif/chop:** bahkan chain pemenang flow narik modal DEFENSIF (cari yield aman), bukan risk-on beta.
- **⚠️ Token trap:** 2 protokol Base terbesar FAIL accrual — **AERO 🟡 (net -$14M), MORPHO ❌ (fee switch off, $0 holder).** Flow riil TAPI gak ada token bersih buat nangkep.
- **Play Base bener:** JADI depositor (USDC di Morpho vault, earn yield) ATAU ETH (indirect). **Jangan beli token Base buat accrual.**

## 🟣 KEMANA UANG DI DALAM SOLANA (+$220M)
- Destinasi: **Lending (Kamino + Jupiter Lend, 2 teratas)** + **DEX trading** (Solana venue trading #1, $2.84B/hari, share 33%) + stablecoin $14.85B.
- **Karakter: trading+yield (lebih risk-on dari Base)**, TAPI **spekulasi COOLING** (REV -43% QoQ, meme unwind) → lagi transisi ke yield-retention kayak Base.
- **Token accrual mixed:** JUP buyback WAVERING (CTO "mungkin distop"), Kamino/Jito/Raydium cek net masing2. SOL = L1 (inflasi 3.8%, stake wajib).
- **Play bersih:** SOL (second-core) atau depositor Kamino/Jupiter Lend. Skip eco token sampe net diverifikasi.

## 🔺 KEMANA UANG DI AVALANCHE (+$325M) — RWA/INSTITUSI murni
- RWA tokenized **$2.1B (8x YoY)**, RWA TVL $1.3B, Securitize anchor. **BlackRock BUIDL $500M**, Galaxy/Grove. Stablecoin settlement $69B/30d. 50+ compliance-L1s.
- Sumber: "shift ke regulated high-value settlement, BUKAN speculative flow." = pemenang flow paling institusi/RWA.

## 💡 SINTESIS FINAL — trio flow winner semua → YIELD/RWA/INSTITUSI
| Chain | Kemana | Karakter |
|---|---|---|
| Base | USDC yield (Morpho) | defensif |
| Solana | lending + trading cooling | risk-on luruh |
| Avalanche | **RWA/institusi (BlackRock/Securitize)** | paling regulated |

**Ketiganya NOL ke spekulasi murni = modal defensif rotasi ke YIELD + RWA (konfirmasi ke-8 chop).** TAPI ngasih arah positif: **RWA/yield = satu-satunya tema dgn inflow institusi riil** (ETH RWA $14.9B, AVAX $2.1B, Base USDC vault, BlackRock BUIDL, RH tokenized stocks).

## 🔑 TOKEN paling align tema flow (accrual bersih): PENDLE 🟢
Bisnis PENDLE = LITERAL stablecoin-yield tokenization = persis yang lagi ngalir. 80% fee ke holder, earnings +$12M (terbukti). **Jembatan sempurna: tema flow (yield/RWA) + accrual bersih.** Paling align sama kemana uang pergi.
Kandidat lain: ONDO (RWA #1 — CEK accrual dulu, jangan ulang MORPHO/AERO), AVAX/ETH (L1 rail), atau jadi depositor RWA/yield vault. Speculation/meme/token-beta flow balik HANYA pas risk-on kembali (retail + premium flip).

## 🏆 RWA BASKET yang LOLOS filter (3 clean-accrual) — INI yang di-consider
| Token | RWA angle | Accrual |
|---|---|---|
| **PENDLE** | yield tokenization | 🟢 80% fee, +$12M |
| **SYRUP** | institutional credit | 🟢 buyback MIP-021 |
| **SKY** (eks-Maker) | stablecoin + T-bills | 🟢 KUAT — Holders Rev $69.77M (~4.3% mcap), staker ~9.9%, earnings +$221.73M / $0 incentives, ~99% circ |
**Dua udah di book (PENDLE+SYRUP), SKY = tambahan KUAT (confirmed, sekelas KNTQ/PENDLE, overhang terendah).** Akumulasi di flush.
**❌ RWA TRAP (skip):** ONDO, AVAX, MORPHO — A+ bisnis, $0 ke token. Jangan tuker basket bersih ke trap hype.
**Alt exposure:** jadi depositor (USDY/OUSG/USDC yield) · ETH rail · COIN equity.

---

# 🎯 MESIN PRESISI (v2 — 27 Agu 2026)

> Sebelum v2, flow tracking pakai **angka absolut tanpa normalisasi** → ranking bisa salah.
> v2 = semua flow **dinormalisasi ke basis chain** + ada threshold + divergence score.

## Aturan #1 — SELALU normalisasi (jangan pernah baca angka absolut)
```
INTENSITAS = Bridge net flow ÷ Stablecoin base chain itu × 100%
```
Kenapa: +$220M ke chain $19B = noise. +$325M ke chain $3B = banjir. **Angka absolut nipu.**

### Threshold intensitas (30d)
| Nilai | Grade | Arti |
|---|---|---|
| **>+5%** | 🟢 | modal beneran pindah kesini |
| +1% s/d +5% | 🟡 | mild, belum konklusif |
| -1% s/d +1% | ⚪ | **NOISE — jangan dibaca sbg sinyal** |
| <-5% | 🔴 | modal kabur |

## Aturan #2 — SELALU stamp periode + tanggal tarik
Tiap angka wajib: `nilai (periode, tgl-tarik)`. Contoh: `+$1.84B (30d, 27-Agu)`.
Tanpa stamp = **gak bisa dibandingin next refresh** = data mati.

## Aturan #3 — DIVERGENCE SCORE (ini alpha-nya)
Flow bagus doang gak cukup — yang dicari: **flow udah masuk TAPI harga belum naik.**
```
FlowScore  = L1 stable + L2 bridge + L3 TVL + L4 usage   (tiap layer: 🔴0 / 🟡1 / 🟢2 → max 8)
TokenMove  = %chg 30d token L1:  <+10% → 0 · +10-30% → 1 · >+30% → 2
DIVERGENCE = FlowScore − (TokenMove × 2)
```
| Divergence | Verdict |
|---|---|
| **≥ +4** | 🟢 **EARLY WINDOW** — duit udah masuk, harga belum. INI yang dicari |
| +1 s/d +3 | 🟡 fair value, gak ada edge |
| **≤ 0** | 🔴 **LATE / DISTRIBUSI** — harga lari duluan tanpa flow. JANGAN CHASE |

## 📊 Papan skor (per 27 Agu 2026)
| Chain | Bridge (abs) | **Intensitas** | Token 30d | Divergence | Verdict |
|---|---|---|---|---|---|
| **Base** | +$1.84B | **+10.1%** 🟢 | *no token* | n/a | flow juara TAPI **gak ada token buat dibeli** → main jadi depositor / ETH |
| **Solana** | +$220M | **+1.1%** 🟡 | ~flat | ~netral | ⚠️ **KOREKSI: bukan flow-winner.** Nyaris noise. SOL layak second-core krn L1/durabilitas, BUKAN krn flow |
| **Avalanche** | +$325M | ⛔ *basis blm ditarik* | lemah | ? | RWA institusi riil, tapi token ❌ accrual |
| **Hyperliquid** | -$173M | **~-8.7%** 🔴 | **+38%** (2) | **🔴 SANGAT NEGATIF** | **distribusi telak** — outflow setara Arbitrum tapi harga +38%. Jangan chase |
| **Arbitrum** | -$410M | **-8.4%** 🔴 | lemah | 🔴 | modal kabur + token ❌ = mati dua-duanya |
| Monad | -$139M | -4.3% 🔴 | — | 🔴 | post-launch cooldown |

**Koreksi tercatat v2:** (a) "Solana masih narik modal" = **over-claim**, aslinya +1.1% ≈ noise. (b) Outflow Hyperliquid **jauh lebih parah** dari kesan absolut — divergence paling negatif di board.

## 🎯 Aturan #4 — TRACK PROTOKOL, bukan cuma chain (buat posisi RWA)
Chain menang flow ≠ protokol yang kita pegang kebagian. Yang dipantau tiap refresh:
| Holding | Metrik yang dipantau | Sinyal SEHAT | Sinyal RUSAK |
|---|---|---|---|
| **SKY** | TVL $5.87B · Holders Rev $69.77M · treasury $149M | TVL naik + buyback re-akselerasi (reserve udah penuh) | TVL turun · buyback dipotong lagi |
| **PENDLE** | TVL · Revenue ann $20M · 80% ke staker | TVL naik = yield-tokenization dipake | TVL stall (isu lama) |
| **SYRUP** | Revenue/bln (tier buyback) | **>$2M/bln → tier naik 10%→30% = buyback 3x** | rev stagnan = buyback tetep tipis |
**Baseline 27 Agu di atas. Tiap refresh: banding, catat %chg.**

## ⛔ DATA GAP — minta user tarik (Rule #2 Data Discipline)
Ini yang bikin papan skor belum penuh. Urut prioritas:
| # | Data | Dimana | Kenapa perlu |
|---|---|---|---|
| 1 | **Stablecoin base Avalanche + Hyperliquid ($)** | DeFiLlama → Stablecoins → Chains | 2 sel intensitas masih kosong |
| 2 | **Stablecoin %chg 30d per chain** | kolom sama | Layer-1 (dry powder) belum keisi sama sekali |
| 3 | **Chain TVL %chg 30d** (Base/SOL/AVAX/HL) | DeFiLlama → Chains | Layer-3 kosong |
| 4 | **DEX vol 30d %chg per chain** | DeFiLlama → DEXs → Chains | Layer-4 kosong |
| 5 | **Periode bridge flow** (7d/30d/all-time?) | DeFiLlama → Bridges | angka lama gak ke-stamp = gak comparable |
| 6 | **Token %chg 30d: SOL, AVAX, ETH** | CMC | buat divergence |
| 7 | **TVL 30d: SKY, PENDLE, SYRUP** | DeFiLlama protokol | flow ke posisi kita sendiri |
**Tanpa 1-4, FlowScore gak bisa dihitung penuh — papan skor sekarang = bridge-only (1 dari 4 layer).**
