# ⚡ SCALP / DAY TRADE — kerangka (BEDA TOTAL dari sistem flow)

**Trigger:** `scalp playbook`
**Dibuat:** 27 Agu 2026

---

## ⚠️ PENGAKUAN DULU
**Semua yang dibangun sebelum ini SALAH ALAT buat scalping.**
Flow tracking = mingguan. Accrual filter = tahunan. Di chart 5-menit, keduanya **nol gunanya.**
Yang nentuin di timeframe ini: **biaya · likuiditas · volatilitas · disiplin risiko.** Bukan fundamental.

---

## 💀 MATEMATIKA BIAYA — baca ini sebelum apa-apa
Biaya sekali putar (buka+tutup) **TAKER**: fee 0.05%×2 + slip 0.02%×2 = **0.14%**

| Target | Biaya jadi % target | **Win rate min (BEP)** |
|---|---|---|
| 0.2% | **70%** | **85.0%** ← mustahil |
| 0.3% | 47% | **73.3%** |
| 0.5% | 28% | **64.0%** |
| 1.0% | 14% | **57.0%** |
| 2.0% | 7% | **53.5%** |

### 🚨 Contoh nyata
**100 trade/bulan · target 0.3% · win rate 55%** (win rate yang bagus!) → **−11% modal/bulan.**
Bahkan **win rate 65%** → masih **−5%/bulan.**
**Bukan soal skill. Biaya tetap MEMAKAN target kecil.** Makin kecil target, makin mustahil matematikanya.

---

## 🔑 TUAS TERBESAR: MAKER, bukan TAKER
Biaya sekali putar **MAKER** (limit order): fee 0.015%×2 + slip 0.005%×2 = **0.04%** (3.5x lebih murah)

| Target | Win rate min TAKER | **Win rate min MAKER** | Selisih |
|---|---|---|---|
| 0.3% | 73.3% | **56.7%** | **16.7 poin** |
| 0.5% | 64.0% | **54.0%** | 10.0 poin |
| 1.0% | 57.0% | **52.0%** | 5.0 poin |

### Contoh: 100 trade/bln, target 0.5%, win rate 58% (SAMA)
- **TAKER: −6.0%/bulan** (rugi)
- **MAKER: +4.0%/bulan** (untung)
**Win rate identik. Yang beda cuma biaya. Ini bukan detail — ini penentu.**

> **ATURAN #1: PAKAI LIMIT ORDER. Jangan market order kecuali darurat keluar.**
> Ini satu perubahan yang dampaknya lebih besar dari semua analisa teknikal digabung.

---

## 📏 KONSEKUENSI: DAY TRADE > SCALP
Matematika di atas bilang jelas: **target 0.2-0.3% itu perangkap struktural.**
**Rekomendasi: target minimal 0.8-1.5%** (day trade), bukan 0.2-0.3% (scalp ketat).
Lebih sedikit trade, target lebih besar, biaya jadi porsi kecil. **Frekuensi tinggi = musuh, bukan keunggulan.**

---

## 🎯 PILIH INSTRUMEN — di sini kerja kita KEPAKE
**Metrik VELOCITY kita berbalik arti di timeframe ini:**
| | Buat POSISI (hold) | **Buat SCALP** |
|---|---|---|
| Velocity tinggi | ❌ crowded, kamu jadi exit liquidity | ✅ **churn tinggi = banyak gerakan + likuiditas** |

| Instrumen | Velocity / Volume | Cocok buat scalp? |
|---|---|---|
| **HYPE / perp Hyperliquid** | velocity **1.371x**, perps **$8.86B/24h** | 🟢 **paling likuid & paling churn** |
| **BTC perp** | OI $58B | 🟢 spread tertipis, paling dalam |
| **SOL** | DEX $2.43B/24h, velocity 0.153x | 🟢 volatil + likuid |
| ETH | velocity 0.008x | 🟡 likuid tapi paling adem = range sempit |
| **LINK** | vol $452M | 🟡 oke |
| ONDO | vol $118M | 🔴 tipis buat scalp |
| CFG · QNT · XPL | <$30M | ❌ **spread bakal makan kamu hidup-hidup** |

**Aturan: scalp HANYA di 3-5 instrumen paling likuid. Titik.** Alt tipis = spread + slippage bikin matematika mustahil.

---

## ⏰ WAKTU (WITA)
| Sesi | Jam WITA | Karakter |
|---|---|---|
| Asia | 07:00-15:00 | range, volume rendah — **paling buruk** |
| **Eropa** | **15:00-21:00** | volume naik, tren mulai |
| **US open** | **20:30-23:00** | 🔥 **volatilitas + likuiditas terbaik** |
| US late | 23:00-04:00 | tren lanjut, mulai tipis |
**Kalau cuma bisa 2 jam sehari: ambil 20:30-22:30 WITA.**
**Hari yang dihindari/diwaspadai:** rilis data makro (PCE/CPI/FOMC), dan **event kayak Warsh besok ~22:00 WITA** — volatilitas melonjak, stop kena wick, spread melebar.

---

## 🛡️ ATURAN RISIKO (ini edge-nya, bukan setup)
1. **Risiko per trade: 0.5-1% modal.** Size dihitung MUNDUR dari jarak stop.
2. **Stop loss WAJIB, dipasang bareng entry.** Bukan "mental stop".
3. **Batas rugi harian: −3%.** Kena → tutup laptop. Tanpa pengecualian.
4. **Batas rugi mingguan: −6%.** Kena → libur sampai minggu depan.
5. **Maks 3-5 trade/hari.** Lebih dari itu = overtrading, biaya numpuk.
6. **Jangan pernah tambah posisi rugi (averaging down).**
7. **Leverage maks 3-5x.** Leverage tinggi = likuidasi kena wick, bukan kena tesis.

## 📓 JURNAL (wajib, non-negotiable)
Catat tiap trade: **jam · instrumen · alasan masuk · entry/stop/target · maker atau taker · hasil · emosi.**
Tanpa jurnal, kamu gak akan tau apakah punya edge atau cuma beruntung. **Review mingguan: win rate, rata-rata R, biaya total.**

## ⚖️ EKSPEKTASI JUJUR
- **Bulan 1-3: target BREAK-EVEN**, bukan profit. Belajar eksekusi & biaya dulu.
- Kalau setelah 100 trade jurnal nunjukin **ekspektasi negatif → berhenti, jangan gedein size.**
- Mayoritas yang rugi di scalping bukan karena analisa jelek — karena **biaya + overtrading + gak ada stop.**

## 🔗 SATU-SATUNYA JEMBATAN KE SISTEM LAMA
**Kalender event** tetap kepake: **Warsh 28 Agu ~21:00 · HYPE unlock 29 Agu · XPL cliff 25 Sep · ASTER Sep.**
Buat scalper, ini bukan tesis — ini **jam volatilitas**: siap-siap spread melebar & wick panjang. Kecilin size atau libur.

## ⛔ YANG BELUM AKU TAU (mempengaruhi angka di atas)
1. **Bursa/venue apa?** (fee tier beda-beda — HL, Binance, Bybit, dsb)
2. **Modal trading berapa?** (nentuin size minimum & apakah fee tier bagus kejangkau)
3. **Spot atau perp/futures?**
Kasih tiga itu, aku hitung ulang biaya + size presisi buat kondisimu.
