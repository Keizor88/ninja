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
