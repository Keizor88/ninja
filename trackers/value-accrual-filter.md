# Value Accrual Filter (gate wajib tiap analyzer111)

**Trigger:** `accrual check`
**Rule inti:** BELI TOKEN-nya, bukan protokolnya.

---

## Prinsip
Protokol bisa jadi bisnis hebat sambil token-nya cuma **stiker governance kosong**. Sebelum beli token infra/DeFi apapun, jawab:

> **"Kalau protokol ini 10x revenue, token gue naik gak — lewat mekanisme APA?"**

Kalau jawabannya cuma "sentimen / governance / narasi" → **SKIP.**
Harus ada pipa mekanis: **buyback · burn · fee-share · revenue-share · stake-yield.**

## Grade level
- 🟢 **Kuat** — revenue mekanis & langsung ke token (buyback/burn/fee-share ke holder)
- 🟡 **Moderat** — ada mekanik tapi diskresi/terbatas/kecil
- ⚠️ **Mechanism-yes-effect-no** — desain bener, tapi flow riil masih negligible → WATCH, jangan beli sampai bermakna
- ❌ **Gagal** — revenue ke treasury/DAO/pihak lain, bukan token → AVOID (walau fundamental protokol bagus)

---

## Scorecard (per 25 Agu 2026)
| Token | Mekanik | Grade |
|---|---|---|
| **HYPE** | **97% fees → buyback→burn (AF): ~$1.26B/thn = ~7% mcap/thn** (TERKUAT di scorecard) | 🟢 #1 (TAPI ~75% locked = unlock lawan buyback; fee siklikal perp) |
| **KNTQ** | **buyback: holder rev $2.75M = ~58% revenue (CONFIRMED), staker yield ~14%, ZERO incentives, P/E ~12x** | 🟢 (murah+yield tinggi; TAPI 28% circ overhang berat, ¼ skala PENDLE) |
| **PENDLE** | **sPENDLE: 80% revenue → staker (CONFIRMED $16.14M/$19.97M = 80.8%), earnings +$12.36M (net incentives $7.61M)** | 🟢 accrual TAPI ⚠️ **TVL $1.193B, ~-68% dari puncak $3.7B (Des-25)** = basis aset rontok, revenue nyusul kalau gak balik. **Turun jadi posisi-3 basket.** Jangan nambah sblm TVL naik 2 refresh berturut |
| **SYRUP** | **MIP-021 live: buyback ~10% rev (tier floor) ~$1.44M/thn = ~0.6% mcap. v3 27-Agu: TVL $3.053B NAIK (udah > PENDLE), fees ann $110.9M, rev ann $14.42M** | 🟢 accrual tipis TAPI **momentum TVL terbaik di basket** → naik jadi posisi-2. Operating leverage: >$2M/bln rev → tier 30% = buyback 3x |
| **SKY** (eks-Maker) | **Holders Rev $69.77M = ~4.3% mcap/thn buyback, staker yield ~9.9% ($704M staked/43.84%), earnings +$221.73M dgn $0 incentives, ~99% circ (overhang terendah)** | 🟢 KUAT — RWA-accrual SAH (yang ONDO/AVAX/MORPHO gagal jadi). Sekelas KNTQ/PENDLE, di atas SYRUP. Mcap $1.606B (#45), TVL $5.87B (~69% USDC/29% WETH). Katalis: reserve $150M udah kepenuhan (treasury $149M) → buyback bisa re-akselerasi. Caveat: governance kompleks (CDP/risk-curator), upside moderat (mature) |
| **ZRO** | fee-switch burn ADA, tapi fee ~$20K/hari | ⚠️ effect-no-yet → WATCH |
| **ARB** | fees → **DAO treasury, bukan token** | ❌ AVOID sampai loop nutup |
| **LDO** | governance only, reward → stETH holder; buyback baru | ❌ weak |
| **BIO** | dana → BioDAOs, bukan BIO | ❌ weak |
| **SYN** | token secure pool, accrual gak jelas | ❌ weak |
| **MORPHO** | **fee switch OFF, holder $0, Association disinsentif nyalain** (protokol A+ $5.8B TVL/$170M fees tapi token nol) | ❌ (optionality: Apollo bet fee-switch flip, spekulatif) |
| **ONDO** | RWA #1 (AUM $3.43B, BlackRock/Mastercard) TAPI **revenue → operating company, $0 ke token**, governance-only, priced 3-4x peer | ❌ (optionality: fee-switch H2'26 + Ondo Chain, belum live) |
| **AVAX** | RWA winner TAPI net-inflasi (RWA fee-light, burn gak cukup). **v3 27-Agu: chain fees $3,048/HARI (~$1.11M/thn) → P/Fees ~2,856x; stablecoin -5.07% 7d (OUTFLOW); DeFi TVL cuma $480M** | ❌❌ dikonfirmasi ULANG, lebih telak. Bukti terkeras "RWA = fee-light" |

## 🚨 POLA "RWA TOKEN TRAP" (STRUKTURAL)
4 token RWA/flow-winner berturut GAGAL accrual: **AVAX ❌ · MORPHO ❌ · AERO 🟡 · ONDO ❌.** Sebab STRUKTURAL: RWA = bisnis institusi/regulated → value ke **operating company (equity) / depositor (yield)**, BUKAN token governance. **"Flow → RWA → beli token RWA" = JEBAKAN** (token nangkep $0, harga premium, + flow-nya DEFENSIF bukan moon-fuel — modal keluar RWA pas risk-on balik).
**Cara main RWA bener:** **PENDLE 🟢** (satu-satunya RWA/yield token accrual-bersih, bisnisnya yield-tokenization) + **jadi depositor** (earn USDY/OUSG/USDC yield) + ETH rail. SKIP token RWA governance.

| **AERO** (Aerodrome, Base) | 100% fee → veAERO ($110M) TAPI **emisi $124M > fee → earnings NET -$14M** | 🟡 ve(3,3) trap: % tertinggi tapi value net BOCOR. Holder pasif ke-dilusi. Cuma buat lock-and-farm aktif |

**N/A (lottery, bukan main fundamental):** PURR, CASHCAT — bet atensi/reflexivity, rule ini gak berlaku.

## ⚠️ PELAJARAN: % fee ≠ accrual (net-in emisi!)
AERO = % fee TERTINGGI (100%) TAPI **satu-satunya earnings NEGATIF** (-$14M) karena emisi ($124M) > fee ($110M). **Selalu cek Earnings (Annualized) = Revenue − Incentives**, bukan cuma "% ke holder". Contoh net-positif: PENDLE +$12.21M, KNTQ +$4.77M, HYPE + (burn, $0 incentive). Net-negatif = value bocor walau % tinggi.
**Equity (klaim langsung):** COIN, HOOD — earnings ke shareholder by nature.

## Koreksi tercatat
- **ARB:** turun dari 6.5 → ~4/10 di bawah rule ini (fundamental bagus, gak ngaruh ke token).
- **KNTQ vs ARB:** persis kenapa KNTQ layak (buyback langsung) & ARB nggak (treasury).

---

# 🔎 SCREEN LINTAS-CHAIN (27 Agu 2026) — hasil + 3 temuan struktural

## 🚨 Temuan 1 — accrual bersih itu LANGKA (bukan opini, angka)
Holders-revenue DeFi (30d, data Mei-26): **Top 3 = 71% dari SELURUH holders revenue. Top 10 = 87%.**
| # | Protokol | Holders Rev 30d | Share |
|---|---|---|---|
| 1 | **Hyperliquid** | $53.5M | **38.4%** |
| 2 | edgeX | $23.3M | 16.7% |
| 3 | Pump.fun | $22.9M | 16.4% |
→ **Validasi filter kita.** Ribuan token, yang beneran ngalirin duit ke holder < 10 nama. Kalau list kita pendek, itu bener — bukan kurang riset.

## 🚨 Temuan 2 — "BUYBACK" ≠ SUPLAI TURUN (jebakan AERO skala industri)
Riset buyback meta $19B (2025-26): **dari 11 token buyback besar, cuma ~2 yang suplainya BENERAN nyusut.**
Sebab: (a) buyback fee cuma **muter balik ke staker**, bukan dibakar; (b) yang dibakar kalah sama emisi baru.
→ **Aturan tambahan: cek NET SUPPLY (token dibakar − token baru), jangan berhenti di kata "buyback".**
→ Contoh lolos (per sumber): **RAY (Raydium)** — emisi cuma ~1.9jt/thn, jauh di bawah laju buyback = **net deflasi asli.**

## 🚨 Temuan 3 — REVENUE ≠ HARGA (koreksi buat framework kita sendiri)
2026: **6 protokol besar hasilin $7.42B revenue, harga token tetap TURUN.** Ada riset judulnya literal "The Broken Link between Protocol Revenues and Token Performance".
→ **Accrual itu SYARAT PERLU, bukan syarat CUKUP.** Filter kita nyaring yang gagal, tapi gak jamin naik. Yang nentuin harga tetap: **harga masuk (flush) + siklus likuiditas + float/unlock.** Jangan over-trust accrual doang.

## 📋 KANDIDAT BARU dari screen (BELUM diverifikasi — butuh mcap buat hitung intensitas)
| Token | Chain | Mekanik | Catatan |
|---|---|---|---|
| **RAY** | Solana | buyback + **net deflasi asli** (emisi ~1.9jt/thn) | ⭐ paling menarik — 1 dari ~2 yg suplainya nyusut beneran |
| **AAVE** | multi | **Aavenomics 3.0 (live 27-Jun-26): buyback OTOMATIS non-diskresi**, ~$117.5M rev/thn | ke ecosystem reserve, BUKAN burn. Fee capture cuma 13% ($951M fee → $127M rev) |
| **DYDX** | dYdX chain | **75% net protocol fee → buyback** (naik dari 25%, Nov-25), 100% di-stake | perp sector |
| **PUMP** | Solana | holders rev $22.9M (#3) | launchpad meme — siklikal ekstrem |
| **EDGE** | edgeX | buyback+burn harian | ⚠️ **JANGGAL: rev 30d $1.74M vs "annualized" $225.62M** = aktivitas kemungkinan ANJLOK ~90%. Jangan sentuh sblm diklarifikasi |
| **JUP** | Solana | 50% rev → buyback + rencana burn 3B JUP | ⚠️ konflik: catatan lama kita "buyback wavering (CTO mungkin distop)" |

## ❌ Dikonfirmasi GAGAL dari screen
**UNI (Uniswap):** fee $892M → revenue **$12M = 1.4% capture**. Volume juara, token nyaris nol. Trap klasik.
**AAVE catatan:** fee $951M → rev $127M = 13% capture (jauh di bawah HYPE 90%).

## ⛔ DATA GAP — belum bisa ranking presisi
Belum ada **mcap** buat RAY · AAVE · DYDX · PUMP · EDGE → **intensitas buyback (% mcap/thn) belum kehitung**, padahal itu metrik penentu. Ranking Holders-Revenue di atas juga **data Mei-26 (3 bln stale)**.
**Butuh ditarik:** mcap + Holders Revenue (Ann) + Incentives 1y tiap nama → https://defillama.com/holders-revenue
