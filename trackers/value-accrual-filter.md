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
| **RAY** (Raydium, Solana) | **12% SELURUH trading fee → beli RAY → BAKAR** (bukan muter ke staker). Rekam jejak 4 thn: **$216M / 90.8M RAY dibakar, ~4,991 event sejak 2022.** Emisi cuma 1.9M RAY/thn. Mcap $205.6M (#166), rev Jul $18.33M (+137% MoM) | 🟢 **NET DEFLASI ASLI −3.7% s/d −8.2% suplai/thn** (1 dari ~2 token buyback yg suplainya beneran nyusut). Intensitas 4.4-8.9% mcap = **sekelas/di atas HYPE**, tapi mcap 87x lebih kecil & BELUM crowded. ⚠️ Revenue nempel siklus MEME (LaunchLab) — Solana REV −43% QoQ = risiko; kompetisi DEX Solana brutal (Jupiter/Pump/Meteora) |
| **LIT** (Lighter, perp DEX) | **Suplai FIXED 1B, NOL emisi berjalan.** Buyback → **BAKAR** (diubah awal Jul-26, burn pertama ~15.5M LIT). Holders rev $355,981/hr = **$130M/thn = 15.6% mcap** (tertinggi bersih di board) / **3.9% FDV**. Revenue TERDIVERSIFIKASI: **Circle USDC revshare ~$40M/thn (31%, pendapatan BUNGA stabil kayak SKY)** + tier premium MM/HFT + fee likuidasi. **Retail bayar NOL fee.** Mcap $831M (#60), TVL $607.67M | 🟢 **KUAT — mekanik paling bersih strukturnya** (gak ada emisi = gak bisa kena jebakan AERO/Canton). ⚠️ TAPI **cuma 25% circ, FDV 4x mcap** = overhang berat (sekelas KNTQ/HYPE). Tier-3 durabilitas (token baru 2026, belum kena bear). Saingan langsung Hyperliquid (perps $8.86B/24h) |
| **CANTON (CC)** | **burn-mint: fee (denominasi USD) dibayar dgn BAKAR CC.** Fee 30d $60.2M (chain #1, ngalahin Tron $27.6M & ETH $11.3M), holders rev $1.91M/hr = **$697M/thn = 14.7% mcap BRUTO (tertinggi di board)**. Mcap $4.73B, circ 39.42B, **no hard cap** | 🟡→❌ **JEBAKAN AERO SKALA $4.7B.** Per DeFiLlama: **token incentives HARIAN > fees HARIAN → NET BELUM DEFLASI.** 14.7% itu bruto, net-nya negatif. + 3 bendera merah: (a) **DRW dikabarkan BAYARIN partner buat pakai network** = usage disubsidi/sirkular, (b) sentralisasi ekstrem (SV = institusi, dikritik "bukan blockchain"), (c) **anomali data DeFiLlama: fees thn $7.8K vs revenue $668M** (ini yg bikin ikon ⚠️). Mint 100% ke App 50.87%/SV 34%/Validator 15.13% — **holder pasif NOL, cuma ke-dilusi** |
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

---

# 🪤 JEBAKAN KOLOM "HOLDERS REVENUE" (temuan live 27 Agu, screenshot user)
**"Holders Revenue" di DeFiLlama BUKAN berarti duitnya ke TOKEN GOVERNANCE.** Dari top-8 live, **3 adalah jebakan:**
| # | Protokol | Holders Rev 24h | Duitnya ke SIAPA |
|---|---|---|---|
| 5 | **Lido** | $775,187 | **stETH holder — LDO dapet NOL** (scorecard kita udah ❌) |
| 7 | **Uniswap** | $350,669 | **LP — UNI dapet NOL** (fee $892M → rev $12M = 1.4% capture) |
| 8 | **Aerodrome** | $245,127 | veAERO TAPI **net −$14M** abis emisi |
→ **Aturan: abis liat Holders Revenue, WAJIB tanya "holder yang MANA?"** Kalau jawabannya LP / staking-derivative / bukan token yg kamu beli → **NOL buat kamu.** Ranking mentah kolom ini menyesatkan.

## 📊 KONSENTRASI (live, total $7.76M/24h · $121.71M/30d · weekly +78.97%)
| # | Protokol | 24h | Share |
|---|---|---|---|
| 1 | **Hyperliquid** | $3.42M | **44.1%** |
| 2 | **Canton** | $1.91M | 24.6% |
| 3 | **Pump** | $1.12M | 14.4% |
**TOP-3 = 83.1%** (data stale bilang 71% → aslinya LEBIH pekat). Sisanya: Tron $871K · Lido $775K · Lighter $356K · Uniswap $351K · Aerodrome $245K · Aster $185K · Jupiter $145K · **Sky $132K** · Railgun $111K · PancakeSwap $105K.

## 🆕 NAMA BARU dari leaderboard live (belum dicek)
- **CANTON** — **#2, $1.91M/hari ≈ $697M/thn.** Chain institusi/privacy (Digital Asset). Fee chain #1 juga. **Prioritas cek berikutnya.**
- **LIGHTER** ($356K/hr, 2 chain) & **ASTER** ($185K/hr, 2 chain) — dua-duanya perp DEX = **sektor crowding kita.** Antre cek.
- **RAILGUN** ($111K/hr) — privacy.
**Catatan RAY:** gak muncul di top-13 (< $105K/hari) — **konsisten** sama estimasi buyback ~$50K/hari. Kecil di ABSOLUT, tinggi di INTENSITAS krn mcap cuma $205M. Justru itu poin "masuk sebelum crowded".


---

# 🪤 CANTON — studi kasus "angka bruto tercantik, net negatif"
Canton nyaris lolos karena **headline-nya paling cantik yang pernah kita liat**: chain fee #1 sedunia ($60.2M/30d, ngalahin Tron+ETH digabung), holders revenue $697M/thn, intensitas bruto **14.7% mcap** (di atas RAY 8.9% & HYPE 7%), P/S cuma 7.1x, tema RWA/institusi (Goldman, DTCC, 80+ peserta).
**Yang nyelametin kita: cek NET.** DeFiLlama nunjukin **token incentives harian > fees harian** → suplai belum nyusut. Sama persis AERO (fee $110M vs emisi $124M), tapi mcap 30x lebih gede.
**Plus jebakan yang AERO gak punya:** usage-nya dikabarkan **disubsidi DRW** (bayarin partner buat transaksi). Kalau bener, "fee" itu bukan permintaan eksternal — itu **duit muter di lingkaran sendiri**. Metrik fee jadi gak bermakna.
**Pelajaran ke-3 (gabung sama AERO & buyback-meta):** makin cantik angka brutonya, makin wajib cek net + asal-usul usage. **Chain fee #1 sedunia pun bisa gagal filter.**
**Yang bikin flip ke 🟢:** incentives turun di bawah fees (net deflasi) + bukti usage organik non-subsidi + anomali data DeFiLlama diklarifikasi. Sampai itu: **WATCH, jangan beli.**


---

# 🎯 LIT (Lighter) — kenapa ini beda dari Canton/AERO
**Struktur, bukan sekadar angka.** Canton & AERO gagal karena **emisi > burn**. LIT **gak punya emisi sama sekali** (fixed 1B, sekali mint) → jebakan itu **mustahil secara desain**. Buyback-nya juga dibakar, bukan ditahan/muter ke staker.
**Revenue-nya campuran sehat:** 31% dari **Circle USDC revshare (~$40M/thn)** = pendapatan bunga stabil (karakter SKY), 69% fee trading (siklikal). Jauh lebih tahan siklus dibanding RAY yang 100% nempel meme.
**Sambungan ke tesis crowding kita:** Lighter jalanin perps **di dalam Robinhood Wallet (revenue split 50/50, live 1 Jul-26)**. Ini **jawaban** buat catatan sebelumnya "sektor tokenized-equity/brokerage lagi crowding TAPI gak ada tokennya" — **ada: LIT.** Cocok sama data velocity kita: **Robinhood Chain velocity 1.10x, stablecoin +10.48% 7d.**

## ⚠️ Yang nahan skornya
| Risiko | Detail |
|---|---|
| **Overhang 4x** | cuma 250M/1B beredar. FDV $3.32B vs mcap $831M. Intensitas jujur = **3.9% FDV**, bukan 15.6% |
| **Belum teruji** | token baru 2026, belum kena bear = Tier-3 |
| **Saingan Hyperliquid** | HL perps $8.86B/24h, jauh lebih gede. LIT TVL $607M |
| **Ketergantungan suku bunga** | Circle revshare (31% revenue) nyusut kalau Fed potong bunga |
| **Model zero-fee** | revenue gak dari retail volume — kalau tier MM/HFT pindah, revenue rontok |
| **Snapshot 1 hari** | $355,981 itu holders-rev SEHARI, belum dicek konsistensinya |

## 📊 PAPAN INTENSITAS (vs mcap) — hasil semua cek
| Token | Intensitas | Catatan |
|---|---|---|
| **LIT** | **15.6%** (3.9% FDV) | 🟢 bersih, tapi overhang 4x |
| CANTON | 14.7% BRUTO | 🟡→❌ net negatif (emisi > fee) |
| **RAY** | 8.9% | 🟢 bersih, tapi bisnis −20.6% QoQ |
| **HYPE** | 7.0% | 🟢 tapi udah crowded (ATH+unlock) |
| **SKY** | 4.3% | 🟢 paling stabil, ~99% circ |
| SYRUP | 0.6% | 🟢 tipis, momentum TVL terbaik |
**Pola:** intensitas tinggi SELALU dateng bareng satu cacat (overhang / siklikalitas / crowding / emisi). **SKY intensitasnya paling rendah TAPI cacatnya paling sedikit** — itu kenapa dia anchor basket.
