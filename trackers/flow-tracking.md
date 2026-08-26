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

## 🚨 DATA GAP (egress DeFiLlama ke-block — user pull)
1. Stablecoin supply **change per-chain** → defillama.com/stablecoins/chains (kolom 7d/30d)
2. Bridge **net-flow per chain** → defillama.com/bridges
3. Chains **TVL %change** → defillama.com/chains
Belum dapet "chain mana narik modal paling kenceng" (leading #1). Butuh screenshot 3 di atas.
