# 🎯 PLAYBOOK TRADING IKUT FLOW (konfirmasi, bukan prediksi)

**Trigger:** `flow trading`
**Dibuat:** 27 Agu 2026

---

## 🧭 PRINSIP INTI
**Jangan tebak kemana uang AKAN pergi. Masuk setelah uang TERBUKTI dateng, tapi SEBELUM harganya lari.**
Jendelanya sempit dan nyata: **antara "modal masuk" (Layer 1-2) dan "token pump" (Layer 5).** Itu doang edge-nya.
**Beli pas velocity RENDAH, jual pas velocity TINGGI.** Satu kalimat itu inti seluruh sistem.

---

## 🚪 5 GERBANG — semua harus hijau baru eksekusi

### GERBANG 1 — REGIME (boleh main long atau nggak)
**Syarat: Coinbase Premium FLIP POSITIF.**
Selama negatif = cuma institusi yang beli lewat pipa ETF, retail absen → **rally rapuh, breakout gampang gagal.**
- 🔴 Merah → **dilarang long directional pakai size.** Boleh: fade rally, size mini, atau diem.
- 🟢 Hijau → boleh cari setup long.
*Ini gerbang paling penting. Melanggar ini = sumber kerugian terbesar.*

### GERBANG 2 — CHAIN (dimana uangnya)
**Syarat: stablecoin chain 7d > +2%** (bukan bridge absolut — itu gampang nipu).
Kalau di bawah +1% = noise, bukan sinyal.

### GERBANG 3 — TOKEN (mana yang belum lari)
**Syarat: Divergence ≥ +4.**
`Divergence = FlowScore − (TokenMove30d × 2)` · TokenMove: <+10%→0 · +10-30%→1 · >+30%→2
**Flow tinggi + harga BELUM naik = ini yang dicari.** Flow tinggi + harga UDAH naik = telat, itu distribusi.

### GERBANG 4 — TIMING (belum rame + gak ada jebakan suplai)
**Syarat A: Velocity < 0.5x** (`volume 24h ÷ basis stablecoin`). Di atas 0.5 = udah rame = kamu jadi exit liquidity.
**Syarat B: TIDAK ada unlock/cliff dalam 30 hari.** Ini satu-satunya risiko yang bisa kamu tau **sebelum** kejadian — gak ada alasan kena.

### GERBANG 5 — EKSEKUSI
- **Risiko per trade: maks 1-2% modal trading.** Ukuran posisi dihitung MUNDUR dari jarak stop, bukan dari "gue yakin".
- **Stop = INVALIDASI FLOW, bukan angka harga.** Keluar kalau: stablecoin chain balik negatif 2 refresh · velocity nembus >0.5x tanpa posisimu untung · unlock diumumkan mendadak.
- **Target = velocity, bukan harga.** Mulai distribusi pas velocity **>0.5x**. Habisin pas **>1.0x**.
- **Time stop:** kalau 3-4 minggu gak gerak padahal flow masih masuk → tesis gagal, keluar. Modal nganggur itu biaya.

---

## 📊 STATUS SEKARANG (27 Agu 2026)
| Gerbang | Syarat | Status | Detail |
|---|---|---|---|
| **1. REGIME** | premium flip positif | 🔴 **MERAH** | masih −0.0264, belum ditarik hari ini |
| **2. CHAIN** | stablecoin 7d >+2% | 🟢 **LOLOS** | **Hyperliquid +5.15%** · XRPL +5.34% · Arbitrum +2.65% |
| **3. TOKEN** | divergence ≥+4 | 🟡 sebagian | HYPE: flow masuk TAPI harga **+38%** → divergence **NEGATIF** |
| **4. TIMING** | velocity <0.5x, no unlock | 🔴 **MERAH** | HYPE velocity **1.371x** + **unlock 29 Agu** |
| **5. EKSEKUSI** | — | ⬜ | nunggu 1-4 |

### 🎯 Apa yang sistem BILANG sekarang
> **"Uang beneran dateng ke Hyperliquid (+5.15%, inflow terkuat antar mayor). TAPI pintu masuknya (HYPE) udah rame (velocity 1.371x, ATH, unlock lusa)."**

Itu **BUKAN sinyal beli HYPE.** Itu sinyal buat **cari yang BELUM rame di chain yang sama** — persis pola tangga rotasi kita (L1 duluan, eco token belakangan).
**Kandidat yang ditunjuk sistem: KNTQ** (infra HL, harga belum lari kayak HYPE).
⚠️ **Tapi Gerbang 1 masih MERAH + Gerbang 4 kena** (KNTQ: airdrop 1 Okt = dump-watch, 28% circ). → **Belum eksekusi. Catat, tunggu.**

---

## 🚫 KESALAHAN YANG MEMBUNUH
1. **Masuk pas Gerbang 1 merah** karena "setup-nya bagus". Regime ngalahin setup. Selalu.
2. **Ngejar velocity tinggi.** Kalau udah 1.371x, orang yang untung adalah yang masuk pas 0.2x. Kamu jadi likuiditasnya.
3. **Pakai angka absolut.** "+$1.84B ke Base" keliatan juara sampai dinormalisasi. Selalu bagi ke basis chain.
4. **Long menjelang unlock.** XPL 25 Sep · ASTER Sep · HYPE 29 Agu. Ini di kalender, bukan kejutan.
5. **Nyampur akun trading & hold.** Trade nyangkut yang "dipromosiin" jadi investasi = cara paling umum rugi besar.
6. **Percaya narasi tanpa cek flow.** Plasma: cerita sempurna, stablecoin −5.34%, fee $563/hari.

## ⏱️ EKSPEKTASI JUJUR
Sistem ini **LAMBAT.** Konfirmasi flow makan waktu mingguan. Mungkin cuma dapet **4-8 setup setahun**.
Itu bukan cacat — itu harganya kalau mau masuk sebelum rame. **Kalau maunya trading harian, sistem ini salah alat.**

## 🔁 RITUAL MINGGUAN (15 menit)
1. Coinbase premium → **Gerbang 1 buka/tutup?**
2. DeFiLlama stablecoin by chain → **ada yang >+2%?**
3. Chain yang lolos → cek TVL + DEX volume (Layer 3-4 nyambung?)
4. Hitung **velocity** token di chain itu → masih <0.5x?
5. Cek kalender unlock 30 hari ke depan
6. Semua hijau → hitung size dari stop → eksekusi. Ada satu merah → **tunggu.**
