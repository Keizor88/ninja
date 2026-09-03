# 🔎 LONGETF (Robinhood Chain) — CEK CEPAT
**3 September 2026** · sumber: post X @LongETF_RH + chart GMGN

## ⛔ VERDICT: **BUKAN KANDIDAT. Skala dan likuiditasnya membuat ini tidak bisa ditradingkan.**

## 📉 ANGKANYA — baca pelan-pelan
| Metrik | Nilai |
|---|---|
| **Market cap** | **$73.940** — **tujuh puluh tiga RIBU dolar**, bukan juta |
| **Pool likuiditas** | **$30.540** |
| Umur token | **1 HARI** |
| Holder | **283** |
| Top 10 | 12,54% |
| **Flag phishing (GMGN)** | **10,99%** 🔴 |
| Pajak | 1% beli / 1% jual |
| Posisi | −11,5% dari ATH $83,58K · **+151% dari low $29,43K** |
| **vs $INDEX ($32,6jt)** | **441x lebih kecil** |

## 🚫 MASALAH #1 — TIDAK BISA KELUAR
Pool cuma $30.540. Hitungan slippage (AMM, pulang-pergi + pajak 2%):
| Beli | Rugi sebelum harga bergerak sama sekali |
|---|---|
| $200 | **4,6%** |
| $500 | **8,2%** |
| $1.000 | **13,9%** |
| $2.000 | **23,8%** |
| $5.000 | **45,2%** |
> **Di ukuran posisi yang berarti, kamu rugi seperempat sampai separuh modal cuma untuk masuk dan keluar.** Ini bukan risiko harga — ini biaya struktural yang pasti terjadi.

## 🚫 MASALAH #2 — ANGKA FEE-NYA MENIPU
Total fee sejak launch: **0,41 ETH ≈ $1.000** — dikumpulkan dalam **1 hari**.
Kalau dianualisasi: $365.000/tahun pada mcap $73.940 = **yield 494%**.
> **Itu angka omong kosong.** Volume hari peluncuran tidak pernah bertahan.
> 🔁 **Ini kesalahan yang SAMA yang kubuat di INDEX** (menganualisasi data 2 bulan jadi "27% yield"), **tapi 60x lebih parah.** Data 1 hari tidak bisa dianualisasi. Titik.

## 🚨 MASALAH #3 — VERIFIKASI KONTRAK
Post X dari @LongETF_RH menyuruh orang "connect dev wallet, paste CA, verify & register".
**Aku tidak bisa memverifikasi bahwa kontrak `0xef...b1ad` di chart itu benar-benar milik akun tersebut.** Flag phishing 10,99% dari GMGN konsisten dengan kekhawatiran ini.
> **Token peniru rutin muncul dalam hitungan jam setelah proyek diumumkan.** Kalau tetap mau lihat-lihat: **ambil CA HANYA dari akun/situs resmi, jangan dari agregator atau chart.**

## ⚙️ SOAL PLATFORM-nya (beda dari tokennya)
Yang ditawarkan LongETF: otomasi **burn + distribusi ke holder** untuk token lain di Robinhood Chain. Mekanik yang dijelaskan (`deployVault`, `updateBeneficiary(poolId, vault)`) terdengar masuk akal secara teknis — pemilik fee memindahkan haknya sendiri ke vault, tidak bisa dilakukan atau dibatalkan orang lain.
**Tapi platform yang masuk akal ≠ tokennya layak dibeli.** Itu persis pelajaran XPL/Plasma: produk jalan, token tidak menangkap apa-apa. Di sini bahkan lebih awal — belum ada bukti apa pun.

## 🧭 SATU HAL YANG BERGUNA — sinyal tematik untuk INDEX
Model "fee → burn + distribusi otomatis ke holder" sekarang **mulai disalin** di Robinhood Chain.
| Baca | Untuk INDEX |
|---|---|
| 🟢 **Konfirmasi tema** | Model ini bukan keanehan satu proyek — dia menyebar. Itu memvalidasi kategori |
| 🔴 **Risiko baru: kompetisi** | INDEX bukan lagi satu-satunya. Moat-nya = first-mover + skala 441x, **bukan teknologi** |
> **Ditambahkan ke daftar risiko INDEX: kompetisi di design space yang sama sudah muncul dalam 2 bulan.**

## 📌 KESIMPULAN
**Jangan sentuh.** Bukan karena idenya jelek — tapi karena pada mcap $74rb dengan pool $31rb, **ukuran posisi apa pun yang berarti bagimu akan menggerakkan harganya sendiri**, dan kamu membayar 14-45% cuma untuk masuk-keluar.
Kalau tetap penasaran: **tunggu 30 hari.** Kalau masih hidup, punya likuiditas &gt;$500rb, dan fee-nya bertahan — baru ada yang bisa dinilai. Sekarang belum ada apa-apa untuk dinilai.

---

## 🔄 REVISI — user bilang ini uang taruhan (lottery size)

### ✅ Aku terima: keberatan utamaku RUNTUH di ukuran kecil
Argumen likuiditasku dihitung pada $1.000-5.000. **Di ukuran taruhan, friksinya wajar:**
| Beli | Pulang-pergi + pajak |
|---|---|
| $50 | **2,7%** |
| $100 | **3,3%** |
| $200 | **4,6%** |
| $300 | 5,8% |
→ **Di bawah ~$300, slippage bukan alasan untuk tidak masuk.** Itu keberatan terkuatku dan **dia bergantung pada ukuran** — jadi kalau ukurannya kecil, keberatannya gugur. Kucatat.

### 🚨 YANG TIDAK GUGUR — dan ini bukan soal ukuran
**Risiko HARGA dibatasi oleh berapa yang kamu masukkan. Risiko KONTRAK TIDAK.**
Flag phishing 10,99% berarti bahayanya bukan cuma "token jadi nol" — tapi **approve kontrak jahat lalu seluruh isi dompet ditarik.** Taruhan $100 bisa jadi kerugian $10.000 kalau dompetnya salah.
| Wajib | Kenapa |
|---|---|
| **Dompet burner** | isi cuma sebesar taruhannya, nol aset lain |
| **CA dari sumber resmi** | ambil dari situs/akun resmi, **BUKAN** dari agregator, chart, atau reply |
| **Revoke approval setelah selesai** | approval yang menganggur = pintu yang dibiarkan terbuka |
> **Ini satu-satunya bagian yang tidak boleh dikompromikan, dan dia gratis.**

### 🎲 KALAU BERTARUH, BERTARUHLAH SESUAI ATURAN KITA SENDIRI
Dari `asymmetry-filter.md` — matematika yang sudah kita hitung:
| Jumlah pick | Peluang dapat ≥1 pemenang | **Kemungkinan NOL semua** |
|---|---|---|
| **1** | **15%** | **85%** |
| 3 | 38,6% | 61,4% |
| 5 | 55,6% | 44,4% |
| **10** | **80,3%** | 19,7% |
> **Satu taruhan = 85% kemungkinan nol.** Kalau memang mau main di tier ini, **sebar ke beberapa nama**, jangan satu.
> Sizing dari aturan PURR kita: **debu, 0,5-2% porto, siap nol.** Untuk token umur 1 hari: **ujung paling bawah rentang itu.**

### 📌 POSISI FINAL
**Sebagai taruhan kecil dengan dompet burner: silakan, itu keputusanmu dan matematikanya masuk.**
**Yang kutolak bukan taruhannya — tapi (a) masuk dengan ukuran serius, dan (b) menyentuh kontrak tanpa verifikasi.** Yang pertama sudah kamu jawab. Yang kedua tetap wajib.
