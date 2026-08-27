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
- **Solana +$220M** = masih narik modal → dukung SOL second-core.
- **Arbitrum -$410M** (outflow terbesar) = konfirmasi ARB avoid (value-trap, modal kabur).
- **RH Chain -$87M / Monad -$139M** = meme frenzy cooling / post-launch cooldown.

**Rotasi:** modal → Base + Solana + Avalanche (quality/RWA), kabur dari app-chain froth (Hyperliquid) + L2 lama (Arbitrum).

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

## 💡 SINTESIS: flow universal = YIELD-SEEKING = defensif (konfirmasi ke-7 chop)
Di DUA pemenang flow (Base + Solana), uang sama2 → **LENDING/YIELD** (Morpho / Kamino+Jupiter). Bahkan trading Solana cooling. → **Modal yang gerak = cari yield aman, di mana-mana. BUKAN risk-on beta.** Speculation/DEX/meme flow balik HANYA pas risk-on kembali (retail + premium flip). = konfirmasi terkuat regime chop/risk-off dari perilaku modal langsung.
