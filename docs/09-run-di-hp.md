# 09 — Cara Run di HP (paling gampang)

Install Python di HP itu ribet. Cara termudah: **Google Colab** — Python di
browser, gratis, network kebuka, **tanpa install**.

## Cara A — Google Colab (RECOMMENDED)

1. Buka browser HP → **[colab.research.google.com](https://colab.research.google.com)**.
   Login pakai akun Google.
2. Tap **+ New notebook** (atau "File → New notebook").
3. Di kotak kode kosong, paste **3 baris bootstrap** ini (JANGAN paste URL-nya
   doang — harus 3 baris ini semua):

   ```python
   import urllib.request
   url = "https://raw.githubusercontent.com/Keizor88/ninja/claude/weather-prediction-market-guide-m83zaq/tools/colab_paste.py"
   exec(urllib.request.urlopen(url).read().decode())
   ```

4. Tap tombol **▶ (play)** di kiri kotak. Tunggu ~5 detik.
5. Hasilnya muncul di bawah: tabel `P(model)`, `edge`, dan **sinyal BUY/SKIP`
   tiap bucket.

> ⚠️ Kalau lo cuma paste URL-nya (tanpa `exec(...)`), Colab bakal error
> `SyntaxError: invalid syntax` — karena URL bukan kode Python. Paste ketiga
> barisnya.

### Buat market lain (edit variabel)

Bootstrap di atas jalanin versi default (market HK). Buat ganti market, paste
**seluruh isi** [`tools/colab_paste.py`](../tools/colab_paste.py) ke cell (bukan
bootstrap), lalu edit blok **"ISI DI SINI"** (kota, tanggal, metric min/max,
daftar bucket + harga), terus ▶.

Cara ambil isinya di HP: buka link `tools/colab_paste.py` di atas → tombol
**Raw** → tap-tahan → **Select all** → **Copy** → paste ke Colab.

## Cara B — Pydroid 3 (app Android, offline-friendly)

1. Install **Pydroid 3** dari Play Store.
2. New file → paste isi `tools/colab_paste.py`.
3. Tap ▶. (Butuh internet aktif buat narik data Open-Meteo.)

## Cara C — Termux (buat yang mau full repo)

```bash
pkg install python git
git clone https://github.com/Keizor88/ninja
cd ninja
python3 tools/weather_edge.py --city hongkong --date 2026-08-20 --metric min \
  --bucket "<=22:_:22.49" --bucket "23:22.5:23.49" --bucket "24:23.5:24.49" \
  --bucket "25:24.5:25.49" --bucket "26:25.5:26.49" --bucket "27:26.5:27.49" \
  --bucket "28:27.5:28.49" --bucket "29:28.5:29.49" --bucket "30:29.5:30.49" \
  --bucket "31:30.5:31.49" --bucket ">=32:31.5:_" \
  --price "<=22:0.005" --price "23:0.005" --price "24:0.01" --price "25:0.03" \
  --price "26:0.18" --price "27:0.42" --price "28:0.27" --price "29:0.06" \
  --price "30:0.02" --price "31:0.005" --price ">=32:0.005"
```

## Cara baca output

```
bucket  P(model)  P(mkt)   edge   sinyal   Kelly
27        53.3%    42%   +11.3pp  BUY YES  0.049
```

- **P(model)** = peluang dari ensemble asli (fraksi member di bucket itu).
- **edge = P(model) − P(mkt)**. Positif besar → market under-price → **BUY YES**.
  Negatif besar → over-price → **BUY NO**.
- **sinyal**: muncul cuma kalau `|edge| > 10pp`. Kalau semua "skip" → **jangan bet.**
- **Kelly** = saran fraksi size (kecil). Contoh 0.049 = ~4.9% dari bankroll trading.

## Setelah dapet sinyal — WAJIB

1. **Cross-check agensi lokal** (HKO/KMA/JMA/…) buat koreksi bias sebelum eksekusi.
2. **Cek ask di Polymarket** — lo bayar harga "Buy Yes X¢" (lebih mahal dari %).
   Edge harus tetap nutup ask, bukan cuma mid.
3. **Catat** ke [`TRADE-LOG.md`](../TRADE-LOG.md), termasuk kalau SKIP.

> Kalau output-nya aneh (mean jauh dari klimatologi kota) → **data buruk = SKIP.**
> Jangan bet di atas angka yang lo sendiri gak yakin.
