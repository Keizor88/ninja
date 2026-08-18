# 02 — Sumber Data

Dua lapis data: **model global** (probabilitas dasar) + **agensi nasional**
(koreksi bias lokal).

## Model Global (probabilitas dasar)

| Model | Asal | Catatan |
|---|---|---|
| **GFS / GEFS** (31-member) | NOAA 🇺🇸 | Gratis. Ensemble spread = probabilitas langsung. |
| **ECMWF** | Eropa 🇪🇺 | Model terbaik, akurasi tertinggi. |
| **ICON** | DWD 🇩🇪 | Bagus sebagai pembanding. |

**Akses:**

- **[Open-Meteo](https://open-meteo.com/)** — gratis, ada API ensemble. **Ini inti.**
- **[Windy](https://www.windy.com/)** — visualisasi multi-model.
- **[Pivotal Weather](https://www.pivotalweather.com/)** — peta model detail.

Gunakan **ensemble** (GEFS 31-member) supaya dapet distribusi, bukan cuma satu
angka. Dari 31 member, hitung berapa yang mendarat di bracket target →
itu `P(bracket)`.

## Agensi Nasional (koreksi bias lokal)

Tiap kota tradeable punya agensi lokal yang lebih paham iklim mikro kota itu.
Pakai ini untuk **koreksi bias** di atas model global.

| Kota | Agensi | Singkatan |
|---|---|---|
| Kota-kota US | National Weather Service | **NWS** |
| London | UK Met Office | **Met Office** |
| Paris | Météo-France | **Météo-France** |
| Munich / Berlin | Deutscher Wetterdienst | **DWD** |
| Hong Kong | Hong Kong Observatory | **HKO** |
| Shanghai | China Meteorological Administration | **CMA** |
| Seoul | Korea Meteorological Administration | **KMA** |
| Tokyo | Japan Meteorological Agency | **JMA** |
| Istanbul / Ankara | Meteoroloji Genel Müdürlüğü | **MGM** |
| Tel Aviv | Israel Meteorological Service | **IMS** |
| Jakarta *(belum ada market)* | Badan Meteorologi, Klimatologi, dan Geofisika | **BMKG** |

## 🎯 Edge Diferensiasi Lo

**Main di kota ASIA** (Hong Kong / Shanghai / Seoul) pakai **CMA / HKO / KMA**
+ pengetahuan regional.

Alasannya: bot US fokus ke NWS + model generik dan **lemah di Asia** (masalah
timezone, dan gak ngikutin agensi Asia). Di situ akses + konteks regional lo =
keunggulan yang bot US **gak punya**.
