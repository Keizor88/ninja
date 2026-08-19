# 10 — Kalibrasi Bias Stasiun (edge asli lo)

Model global baca suhu di **grid**; market resolve di **stasiun resmi agensi**
(HKO HQ, dst) yang sering beda karena urban heat island, elevasi, dekat laut.
Selisih itu **bias** — stabil & terukur. Ngukur bias ini = edge yang bot generik
gak punya.

> **Kasus nyata (HK, Aug 20):** tool ngasih "BUY YES 26 +14pp". Setelah koreksi
> bias +0.5°C, `P(26)` jatuh dari 35% → 10% → edge **nguap**. Sinyal itu palsu,
> murni artefak grid-vs-stasiun. Kalibrasi yang nyelametin lo dari bet jelek.

## Langkah kalibrasi

### 1. Kumpulin nilai ASLI agensi utk hari lampau

Sumber termudah: **Polymarket tab "Past"** — bucket yang **menang** = nilai yang
dicatat agensi (dibulatkan ke integer). Ambil 2–5 hari. Buat nilai eksak, cek
situs agensi (hko.gov.hk, dll).

### 2. Jalanin `tools/calibrate_hko.py` di Colab

Bootstrap (paste 3 baris ini, ▶):

```python
import urllib.request
url = "https://raw.githubusercontent.com/Keizor88/ninja/claude/weather-prediction-market-guide-m83zaq/tools/calibrate_hko.py"
exec(urllib.request.urlopen(url).read().decode())
```

Tapi lo **wajib edit `AGENCY_ACTUAL`** dulu (isi nilai asli tiap hari). Jadi
lebih baik: buka [`tools/calibrate_hko.py`](../tools/calibrate_hko.py) → Raw →
copy semua → paste ke Colab → ganti angka di blok "ISI DI SINI" → ▶.

Output:

```
tanggal      grid   agensi   bias(agensi-grid)
2026-08-16   27.5    28.0          +0.50
2026-08-17   27.6    28.0          +0.40
2026-08-18   26.8    27.0          +0.20
>> BIAS RATA-RATA = +0.37°C
>> KOREKSI: di colab_paste.py set  BIAS = 0.37
```

### 3. Colok bias ke calculator

Di `colab_paste.py` (atau `--bias` di CLI):

```python
BIAS = 0.37   # dari langkah 2
```

Sekarang tiap member ensemble ditambah +0.37°C sebelum bucketing → P(bucket)
lo udah dikoreksi ke stasiun resolusi. Baru itu edge-nya bisa dipercaya.

CLI: `python3 tools/weather_edge.py ... --bias 0.37`

## Catatan penting

- **Bias bisa beda per musim/kondisi.** Malam cerah-kering (radiasi kuat) →
  bias beda dari malam mendung-lembab. Idealnya kalibrasi pakai hari yang
  regime cuacanya mirip target.
- **Makin banyak hari lampau = makin stabil.** Kalau sebar (std) > 0.7°C, bias
  belum bisa dipercaya — tambah data.
- **Ini proses berulang.** Tiap market ter-resolve, tambahin ke kalibrasi →
  bias makin akurat seiring waktu. Itu compounding edge lo.
- Kalibrasi bikin per **kota + metric** (min vs max bisa beda bias-nya).
