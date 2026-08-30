# -*- coding: utf-8 -*-
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, PageBreak, HRFlowable)

OUT = "/home/user/ninja/reports/riset-crypto-ringkasan-30agu2026.pdf"

INK   = colors.HexColor("#16181d")
MUTED = colors.HexColor("#5b6270")
LINE  = colors.HexColor("#d4d8e0")
BG    = colors.HexColor("#f2f4f8")
ACC   = colors.HexColor("#1a4f8a")
RED   = colors.HexColor("#a8202a")
GRN   = colors.HexColor("#1d6b3f")
AMB   = colors.HexColor("#8a5a00")

ss = getSampleStyleSheet()
def S(n, **kw):
    d = dict(name=n, fontName="Helvetica", fontSize=8.6, leading=12,
             textColor=INK, alignment=TA_LEFT, spaceAfter=4)
    d.update(kw); return ParagraphStyle(**d)

H1   = S("H1", fontName="Helvetica-Bold", fontSize=17, leading=20, textColor=ACC, spaceAfter=2)
SUB  = S("SUB", fontSize=9, textColor=MUTED, spaceAfter=10)
H2   = S("H2", fontName="Helvetica-Bold", fontSize=11.5, leading=14, textColor=ACC,
         spaceBefore=11, spaceAfter=5)
H3   = S("H3", fontName="Helvetica-Bold", fontSize=9.2, leading=12, spaceBefore=7, spaceAfter=3)
BODY = S("BODY")
SMALL= S("SMALL", fontSize=7.8, leading=10.5, textColor=MUTED)
CELL = S("CELL", fontSize=7.9, leading=10.2, spaceAfter=0)
CELLB= S("CELLB", fontSize=7.9, leading=10.2, fontName="Helvetica-Bold", spaceAfter=0)
KEY  = S("KEY", fontSize=9.6, leading=13, fontName="Helvetica-Bold", textColor=ACC)

def P(t, s=BODY): return Paragraph(t, s)
def bullets(items):
    return [Paragraph("&bull;&nbsp;&nbsp;" + t, ParagraphStyle("b", parent=BODY, leftIndent=9)) for t in items]

def tbl(header, rows, widths, hilite=None):
    data = [[Paragraph(h, CELLB) for h in header]]
    for r in rows:
        data.append([Paragraph(str(c), CELL) for c in r])
    t = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    st = [
        ("BACKGROUND", (0,0), (-1,0), BG),
        ("LINEBELOW", (0,0), (-1,0), 0.8, ACC),
        ("LINEBELOW", (0,1), (-1,-2), 0.3, LINE),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("TOPPADDING", (0,0), (-1,-1), 3.5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 3.5),
        ("LEFTPADDING", (0,0), (-1,-1), 5),
        ("RIGHTPADDING", (0,0), (-1,-1), 5),
    ]
    for i in (hilite or []):
        st.append(("BACKGROUND", (0,i), (-1,i), colors.HexColor("#eaf1fa")))
    t.setStyle(TableStyle(st))
    return t

def rule(): return HRFlowable(width="100%", thickness=0.6, color=LINE,
                              spaceBefore=6, spaceAfter=6)

def box(title, lines, bc=ACC):
    inner = [Paragraph(title, ParagraphStyle("bt", parent=CELLB, fontSize=9, textColor=bc))]
    inner += [Paragraph(l, CELL) for l in lines]
    t = Table([[inner]], colWidths=[172*mm], hAlign="LEFT")
    t.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1), colors.HexColor("#f7f9fc")),
        ("BOX",(0,0),(-1,-1), 0.7, bc),
        ("LEFTPADDING",(0,0),(-1,-1),8), ("RIGHTPADDING",(0,0),(-1,-1),8),
        ("TOPPADDING",(0,0),(-1,-1),6), ("BOTTOMPADDING",(0,0),(-1,-1),6),
    ]))
    return t

W = 172*mm
F = []

# ---------------- COVER / HEADER ----------------
F.append(P("Ringkasan Riset Portofolio Kripto", H1))
F.append(P("Sesi riset 27-30 Agustus 2026 &nbsp;|&nbsp; disusun 30 Agustus 2026 &nbsp;|&nbsp; repo: keizor88/ninja", SUB))
F.append(rule())

F.append(box("PERINGATAN PENTING - BACA DULU", [
 "1. Semua data pasar berstempel <b>29 Agustus 2026</b> dan berasal dari screenshot yang ditarik pengguna. Per 30 Agustus data ini sudah basi 1 hari.",
 "2. Cutoff pengetahuan asisten: <b>Mei 2026</b>. Akses jaringan keluar diblokir. Ada blind spot ~4 bulan (Mei-Agustus 2026).",
 "3. Angka bertanda <b>(turunan)</b> adalah hasil perhitungan/estimasi, bukan data yang ditarik.",
 "4. Dokumen ini adalah catatan riset, <b>bukan nasihat keuangan</b>.",
], RED))
F.append(Spacer(1,7))

# ---------------- ATURAN ----------------
F.append(P("1. Aturan Main yang Berlaku", H2))
F.append(tbl(["Aturan","Isi","Konsekuensi praktis"],[
 ["RULE #1<br/>Value Accrual","Beli TOKEN-nya, bukan protokolnya. Harus ada pipa mekanis: buyback / burn / fee-share.",
  "Earnings = Revenue - Incentives. \"% fee ke holder\" bukan net accrual."],
 ["RULE #2<br/>Data Discipline","Tidak pernah mengarang angka. Kalau data tidak ada: berhenti, sebutkan yang hilang, minta ditarik.",
  "Beberapa kesimpulan di dokumen ini sengaja dibiarkan menggantung."],
 ["RULE #3<br/>Flow Normalization","Angka absolut dilarang jadi dasar peringkat. Selalu bagi dengan basis (mis. stablecoin chain).",
  "Lahir dari kesalahan denominator yang melebihkan basis 3.6x."],
], [26*mm, 74*mm, 72*mm]))

# ---------------- PANGGILAN UTAMA ----------------
F.append(P("2. Panggilan Utama - Target Dasar Siklus", H2))
F.append(tbl(["Aset","Harga 29 Agu","Target dasar","Titik tengah","Dari harga","Dari ATH","Waktu"],[
 ["<b>BTC</b>","77.857","48.000 - 52.000","<b>50.000</b>","<b>-36%</b>","-59,5%","Okt-Des 2026"],
 ["<b>ETH</b>","2.435","1.450 - 1.550","<b>1.500</b>","<b>-38%</b>","-69,6%","bersamaan BTC"],
], [16*mm,22*mm,30*mm,22*mm,22*mm,22*mm,38*mm], hilite=[1,2]))

F.append(P("Dasar penetapan BTC 50.000", H3))
F.extend(bullets([
 "<b>Bukan 57.000</b> (hasil tertimbang probabilitas 56.557): low sebelumnya jarang bertahan, biasanya ditembus. Kalau bertahan, bear berhenti di -53,8% - lebih dangkal dari bear BTC mana pun dalam sejarah.",
 "<b>Bukan 37.000-43.000</b> (base rate -65/-70%): drawdown mengecil tiap siklus (-86 &rarr; -84 &rarr; -77). ETF dan treasury company memberi lantai struktural.",
 "<b>Konfluensi di 50.000</b>: shelf 50.148 (digambar pengguna) + fraktal ulangan 47.894 + dasar tangga lama 46-58K. Harga biasanya menembus shelf lalu mendasar sedikit di bawahnya.",
]))
F.append(P("Fraktal: chart BTC sudah memuat satu bounce gagal (63K &rarr; 98K = +55%, gagal, low baru 57K = -41,8%). Bounce sekarang 57K &rarr; 82,3K = +44,5% cocok profil bear-market rally. Mengulang retracement yang sama: 82.344 x 0,5816 = <b>47.894</b>.", SMALL))

F.append(P("Dasar penetapan ETH 1.500 - tiga metode konvergen", H3))
F.append(tbl(["Metode","Hasil"],[
 ["Beta pada leg sisa (BTC -35,8% x 1,06-1,15)","1.433 - 1.511"],
 ["Retest wick low sebelumnya (dibaca dari chart)","~1.400 - 1.500"],
 ["-70% dari ATH (drawdown yang sudah terbukti dicetak)","1.478"],
], [110*mm, 62*mm]))
F.append(P("ETH selalu turun lebih dalam dari BTC: 2018 beta 1,12x; Mei 2021 1,15x; 2022 1,06x. Beta implisit siklus ini ~1,17-1,19x - lebih tinggi karena L2 menyedot fee dari L1 sehingga burn EIP-1559 melemah secara struktural, dan ETH net-inflasi saat pemakaian rendah.", SMALL))

F.append(box("PROGRES DRAWDOWN - temuan yang membalik urutan", [
 "BTC di -36,9% dari ATH = <b>62% jalan</b> menuju target. ETH di -50,6% dari ATH = <b>73% jalan</b>.",
 "<b>ETH lebih jauh jalannya, bukan tertinggal.</b> Aturan \"BTC dulu\" tetap berlaku tapi jaraknya rapat: leg sisa BTC -35,8% vs ETH -38,4%, selisih hanya 2,6 poin.",
 "Praktis: isi ETH satu tranche setelah BTC T4 terkonfirmasi, bukan menunggu berbulan-bulan.",
], GRN))

# ---------------- TANGGA ----------------
F.append(P("3. Tangga Eksekusi", H2))
F.append(P("BTC - 5 tranche", H3))
F.append(tbl(["Tranche","Zona","Porsi","Catatan"],[
 ["T1 (terpasang)","77.800","10-20%","Starter. Jangan dijual - asuransi terhadap skenario \"benar arah, tak pernah terisi\"."],
 ["T2","71.070","20%","Support hitam, Fib ~61,8%"],
 ["T3","67.153","30%","Konfluensi: Fib 78,6% (67.140, selisih 13 dolar) + struktur horizontal"],
 ["<b>T4</b>","<b>48.000-52.000</b>","<b>20%</b>","<b>Target sesungguhnya</b>"],
 ["Kas","-","10-20%","Opsionalitas"],
], [22*mm,32*mm,18*mm,100*mm], hilite=[4]))

F.append(P("ETH - 4 zona (Fib retracement bounce 1.500 &rarr; 2.750)", H3))
F.append(tbl(["Zona","Harga","Porsi","Dari 2.435","Dari ATH","Dasar"],[
 ["Z1","2.100","10%","-13,8%","-57,4%","Fib 50% (2.125)"],
 ["Z2","1.950","20%","-19,9%","-60,4%","Fib 61,8% (1.978) + horizontal"],
 ["<b>Z3</b>","<b>1.450-1.550</b>","<b>40%</b>","<b>-38,4%</b>","-69,6%","<b>Target utama</b>"],
 ["Z4","1.323","20%","-45,7%","-73,1%","Garis hitam pengguna"],
 ["Kas","-","10%","-","-","Opsionalitas"],
], [16*mm,28*mm,16*mm,24*mm,22*mm,66*mm], hilite=[3]))
F.append(P("Avg entry ETH = <b>1.584</b> (-67,8% dari ATH). 60% bobot ada di atau di bawah 1.550 - sengaja, untuk menghindari front-load di atas target.", SMALL))

F.append(P("Stress test tangga - kalau black swan mencetak 47.894 (BTC)", H3))
F.append(tbl(["Pendekatan","Avg entry","Saat crash 47.894","Saat pulih 123.374"],[
 ["<b>Tangga pecah</b> (T1-T4 + 15% kas)","63.509","<b>-20,9%</b>","<b>+80,1%</b>"],
 ["All-in sekarang","77.857","-38,5%","+58,5%"],
], [66*mm,28*mm,38*mm,40*mm], hilite=[1]))
F.append(box("Kenapa ini penting", [
 "Tangga pecah lebih tahan di crash <b>DAN</b> lebih untung di pemulihan. Biasanya proteksi dibayar dengan upside; di sini tidak - karena tranche terakhir yang menembak di dasar mengubah crash dari kerugian menjadi peluang.",
 "Ini barbell Taleb dalam bentuk aritmetika. <b>Tangga bertingkat ADALAH manajemen black swan.</b>",
], GRN))

# ---------------- DATA SNAPSHOT ----------------
F.append(P("4. Snapshot Data - 29 Agustus 2026", H2))
F.append(tbl(["Indikator","Nilai","Ambang kita","Status"],[
 ["BTC daily close","~77.835 (merah)","struktur 76.000","Di bawah 78.000; masih +2,36% di atas 76.000"],
 ["Coinbase Premium","<b>0 (provisional)</b>","hijau 2 hari berturut","STALL - streak 3-naik putus. Nilai final belum pernah terlihat"],
 ["Stablecoin total","303,981 miliar USD","-","Dominasi USDT 60,3%"],
 ["Stablecoin 7d","<b>+0,59%</b>","&gt;+1,5% cross-check / &gt;+2% regime","GAGAL keduanya. Melambat 19-37% dari 27 Agu"],
 ["US30Y","5,213%","&lt;5,3%","HIJAU. Turun dari puncak 5,33% (tertinggi 19 tahun)"],
 ["Tripwire nyala","<b>0 dari 3</b>","3 dari 3","Premium stall + stablecoin melambat + BTC.D belum ditarik"],
], [30*mm,32*mm,40*mm,70*mm]))

F.append(P("Urutan Coinbase Premium", H3))
F.append(tbl(["23 Agu","24 Agu","26 Agu","28 Agu","29 Agu"],
        [["-0,0266","SOL ETF inflow \"rekor\" 33,5jt","0,00","<b>+0,03</b>","<b>0 (stall)</b>"]],
        [30*mm,50*mm,26*mm,30*mm,36*mm]))
F.append(P("Catatan kalibrasi: premium tidak kembali ke -0,05/-0,10 seperti Mei-Agustus. Penjual tidak mendorong - tapi pembeli juga berhenti. Rentang hijau normal historis 0,10-0,25, jadi angka 0,03 sudah ujung paling bawah.", SMALL))

F.append(PageBreak())

# ---------------- FLOW ----------------
F.append(P("5. Money Flow Tracking", H2))
F.append(P("Model berlapis: stablecoin supply (leading) &rarr; bridge net-flow &rarr; TVL &rarr; DEX volume / active address &rarr; token L1 &rarr; token ekosistem (meme terakhir).", BODY))

F.append(P("Temuan terbesar yang masih terbuka", H3))
F.append(box("Aritmetik komposisi stablecoin tidak ketemu", [
 "Total tumbuh <b>+1.792 juta USD</b> dalam 7 hari. Dari lima koin yang datanya ada, yang bisa dijelaskan hanya <b>~+60 juta</b> - dan itu setelah USDT (-0,03%) dan USDC (-0,05%) menariknya ke bawah.",
 "Artinya <b>lebih dari 95% pertumbuhan mingguan datang dari penerbit yang tidak ada di data kita</b> (~1,73 miliar USD).",
 "<b>Pertanyaan penentu:</b> sisa itu fiat atau leverage? Kalau <b>USDe (Ethena)</b> - sintetis, tumbuh dari funding-rate arb - maka itu BUKAN dry powder, melainkan permintaan leverage yang unwind saat funding negatif (mekanisme refleksif tipe LUNA). Kalau <b>PYUSD / USD1 / FDUSD</b> - fiat-backed - maka itu dry powder asli.",
 "<b>Selama belum dijawab, angka +0,59% tidak bisa dipakai sebagai konfirmasi maupun bantahan.</b>",
], AMB))

F.append(P("Papan stablecoin per chain (stempel 27 Agu - sudah basi)", H3))
F.append(tbl(["Chain","Basis","7d %","Grade"],[
 ["Hyperliquid L1","6,751 mia","+5,15%","Inflow terkuat antar mayor"],
 ["XRPL","1,073 mia","+5,34%","Kecil"],
 ["Arbitrum","3,501 mia","+2,65%","Sedang"],
 ["Tron","93,398 mia","+1,17%","Absolut terbesar (+1,09 mia)"],
 ["Solana","15,905 mia","+1,06%","Sedang"],
 ["Ethereum","147,934 mia","+0,41%","Noise"],
 ["Base","5,018 mia","+0,06%","FLAT - tesis \"Base juara flow\" dicabut"],
 ["Avalanche","1,393 mia","-5,07%","OUTFLOW"],
], [34*mm,26*mm,22*mm,90*mm]))

F.append(P("Kebutuhan bahan bakar untuk skenario bullish (BTC 145.000 pada Januari 2027)", H3))
F.append(P("Asumsi model dinyatakan terbuka: leg BTC yang menggandakan harga historisnya disertai ekspansi suplai stablecoin ~20%, yaitu ~+60,8 miliar USD dari basis sekarang.", SMALL))
F.append(tbl(["Leg naik mulai","Sisa minggu","Butuh harga","Butuh stablecoin","vs +0,59% sekarang"],[
 ["1 Oktober","17,4","+4,5%/mg","+1,15%/mg","perlu ~2x"],
 ["1 November","13,0","+6,1%/mg","+1,54%/mg","perlu ~2,6x"],
 ["1 Desember","9,0","+8,9%/mg","+2,22%/mg","perlu ~3,8x"],
], [30*mm,24*mm,28*mm,32*mm,34*mm]))
F.append(box("Dua angka yang menyatukan semuanya", [
 "1. Bar yang dibutuhkan (1,15-1,54%/mg) ada <b>DI BAWAH</b> ambang regime-change kita (&gt;2%/mg). Kalau tripwire stablecoin nyala, target 145K terbiayai penuh - rencana bullish adalah <b>hilir dari sinyal yang sudah kita lacak</b>.",
 "2. <b>Batas ~22 November.</b> Setelah itu kebutuhan menembus 2%/mg: target berhenti jadi cerita flow dan berubah jadi butuh mania. Per 30 Agustus: tersisa <b>84 hari</b>.",
]))

F.append(PageBreak())

# ---------------- ACCRUAL ----------------
F.append(P("6. Filter Value Accrual - Hasil Skrining", H2))
F.append(P("Temuan struktural: accrual bersih itu langka. Tiga protokol teratas menguasai 83,1% dari seluruh holders revenue DeFi.", BODY))

F.append(tbl(["Aset","Grade","Alasan"],[
 ["<b>SKY</b>","LOLOS","Mesin kas terbaik di basket. Accrual bersih, ~99% beredar, revenue non-spekulatif, naik saat bunga naik (hedge makro alami). <b>TAPI</b>: S&amp;P B-, buffer modal 0,4%, Rune kendalikan governance dengan ~9% token, usulan freeze USDS."],
 ["<b>SYRUP</b>","LOLOS","Dikoreksi naik setelah pengecekan ulang. Risiko: bisnisnya kredit tanpa jaminan penuh - risiko kredit by design."],
 ["<b>PENDLE</b>","LOLOS (watch)","Paling align tema flow. Diturunkan ke watch karena peringatan TVL (1,19 mia)."],
 ["<b>RAY</b>","LOLOS","Deep dive 6/10. Revenue Q1-2026 5,79 juta, <b>-20,6% QoQ</b> - menurun, bukan akselerasi."],
 ["<b>LIT</b>","LOLOS","-"],
 ["<b>ETH</b>","WATCH","Pipa ada (EIP-1559 live bertahun-tahun). Net-inflasi sekarang. <b>Bar break-even 4,4x lebih rendah dari SOL</b> (issuance ~0,8% vs 3,55%). Kandidat L1 terkuat."],
 ["<b>SOL</b>","WATCH","Naik dari GAGAL setelah SGP-0002 (disinflasi -15% &rarr; -30%) dan SGP-0003 (resource fee 100% dibakar). Tapi SGP-0003 masih <b>mandat</b>, bukan kode terkirim."],
 ["<b>ASTER</b>","WATCH","-"],
 ["<b>CPOOL</b>","WATCH","Buyback LIVE sejak 20 Okt 2025, tapi <b>0% dibakar</b> - 50% rewards recirculate, 50% reserve."],
 ["<b>TRX</b>","WATCH","Mekanisme nyata tapi net ~0."],
 ["<b>CANTON</b>","GAGAL","-"],
 ["<b>CFG</b>","GAGAL","Optionalitas CP172 dicatat terpisah."],
 ["<b>XPL</b> (Plasma)","GAGAL","3/10. TVL Aave 6,6 miliar lewat chain-nya, <b>XPL tidak menangkap apa pun</b>."],
 ["<b>AVAX</b>","GAGAL","Outflow stablecoin -5,07% + fee mikroskopis."],
], [24*mm,20*mm,128*mm], hilite=[1,2,3,4,5]))

F.append(P("Tiga jebakan yang berulang - catat ini", H3))
F.append(tbl(["Jebakan","Contoh","Cara lolos"],[
 ["Kolom \"Holders Revenue\" bisa berarti LP atau pemegang derivatif staking, bukan token governance",
  "Lido, Uniswap, Aerodrome - semuanya jebakan di top 8 live","Baca dokumen distribusi, bukan kolom agregator"],
 ["\"Buyback\" bukan pengurangan suplai","Dari 11 token yang mengklaim buyback, hanya ~2 yang benar-benar menyusut","Cek berapa persen DIBAKAR, bukan berapa dibeli"],
 ["\"Rekor\" tanpa denominator adalah iklan","SOL ETF inflow \"terbesar 2026\" 33,5jt = <b>0,211%</b> dari basis stablecoin Solana sendiri","Selalu bagi dengan basis yang relevan"],
], [52*mm,66*mm,54*mm]))

F.append(PageBreak())

# ---------------- RISIKO ----------------
F.append(P("7. Peta Risiko Ekor", H2))
F.append(P("Probabilitas - tiga pertanyaan berbeda", H3))
F.append(tbl(["Pertanyaan","Jawaban","Bisa dikendalikan?"],[
 ["P(peristiwa ekor parah dalam 5 bulan)","<b>~40%</b> (rentang 28-44%)","Tidak sama sekali"],
 ["P(kena drawdown | peristiwa terjadi)","~80% - korelasi menuju 1 saat krisis","Hampir tidak"],
 ["P(kehancuran permanen | peristiwa)","Ditentukan struktur portofolio","<b>Ya, hampir seluruhnya</b>"],
 ["P(black swan sejati / unknown-unknown)","<b>Tidak bisa diketahui</b>","-"],
], [58*mm,66*mm,48*mm], hilite=[1,4]))
F.append(P("Base rate: 17 peristiwa sistemik / 15 tahun (2011-2026) &rarr; lambda 1,13 per tahun &rarr; P(&ge;1 dalam setahun) 67,8%; dalam kuartal 24,7%; dalam 5 bulan 37,6%. <b>Crypto memproduksi peristiwa ekor kira-kira sekali setahun - itu properti kelas asetnya, bukan anomali.</b>", SMALL))
F.append(P("Penyesuaian: blowup crypto menggerombol 6-14 bulan setelah puncak siklus (2021: LUNA 6 bln, 3AC 7, Celsius 8, FTX 12). Puncak siklus ini ~pertengahan 2025, jadi sekarang ~14 bulan - <b>ujung belakang jendela, bukan awalnya</b>. Peringatan: bulan 12-14 jatuh di Mei-Agustus 2026, persis blind spot asisten.", SMALL))

F.append(P("Titik paling rapuh - berdasarkan angka yang sudah ada", H3))
F.append(box("RISIKO #1 - ada di portofolio sendiri: buffer modal SKY 0,4%", [
 "Rating S&amp;P <b>B-</b> (spekulatif). Buffer ~<b>23 juta USD di atas TVL 5,87 miliar</b>.",
 "Artinya mekanis: <b>kerugian 0,4% di sisi aset menghabiskan modalnya</b>. Bank komersial jalan di tier-1 8-15% - SKY <b>20-37x lebih tipis dari bank</b>.",
 "Ini bukan alasan menjual - SKY tetap mesin kas terbaik di basket. Tapi aturan sizing yang mengikuti: <b>cap SKY di porsi yang sanggup dilihat jadi nol</b>.",
], RED))
F.append(Spacer(1,4))
F.append(tbl(["Arketipe kehancuran","Contoh","Paparan"],[
 ["Fraud kustodian","FTX, Celsius, Mt.Gox","<b>Tergantung di mana disimpan.</b> Satu-satunya risiko besar yang bisa dihapus hari ini, gratis: self-custody untuk core, exchange hanya untuk modal scalping."],
 ["Peg patah","UST, USDC-SVB","USDS (SKY)"],
 ["Guncangan makro","Mar 2020, Mar 2023","US30Y tertinggi 19 tahun + intervensi Treasury gagal. <b>Guncangan makro tidak peduli filter accrual - semua turun bersamaan. Diversifikasi antar-token bukan diversifikasi.</b>"],
 ["Unwind leverage","3AC, LUNA","Isu USDe (lihat bagian 5)"],
 ["Contagion kredit","Genesis, BlockFi","SYRUP/Maple - kredit by design"],
 ["Konsentrasi likuiditas","-","HYPE: 21.941 alamat aktif vs Solana 2,71 juta = <b>123x lebih sedikit</b>. Sedikit whale keluar = tidak ada bid."],
], [34*mm,32*mm,106*mm]))

F.append(box("Risiko terbesar yang sebenarnya - dan ini bukan black swan", [
 "<b>Bukan crash-nya. Tapi BENAR soal dip dan tetap hancur karenanya.</b>",
 "Kalau 60% terpasang di 67.153 lalu black swan mencetak 47K - analisisnya benar, tapi amunisi habis di dasar. Ini alasan struktural (bukan kehati-hatian kosong) kenapa T4 di 46-52K harus tetap dijaga.",
 "Ekor atas juga nyata: posisi yang menunggu dip dengan starter 10-20% <b>rentan terhadap kejutan NAIK</b> - kalau muncul pembeli besar atau pivot mendadak, 80% posisi ketinggalan. Itu sebabnya starter tidak boleh dijual.",
], RED))

F.append(PageBreak())

# ---------------- KOREKSI ----------------
F.append(P("8. Log Koreksi - kesalahan yang tercatat dan diperbaiki", H2))
F.append(P("Bagian ini sengaja disertakan. Riset yang tidak mencatat kesalahannya sendiri tidak bisa dipercaya.", SMALL))
F.append(tbl(["Klaim awal (salah)","Perbaikan"],[
 ["Base adalah juara flow (dari persentase pie Chain-Rankings by TVL)",
  "<b>Denominator salah</b> - basis dilebihkan 3,6x (18,22 mia vs 5,018 mia aktual). Semua angka intensitas v2 dicabut. Base ternyata FLAT (+0,06%). Melahirkan RULE #3."],
 ["Hyperliquid: bridge outflow = distribusi","Salah. HL justru inflow stablecoin TERKUAT (+5,15%). Diganti dengan bukti konsentrasi."],
 ["CPOOL: buyback belum live","Salah - live sejak 20 Okt 2025. Gagal karena alasan berbeda: <b>0% dibakar</b>."],
 ["SOL: L1 tanpa pipa mekanis","Salah - Solana bakar 50% base fee sejak awal. Gagal karena <b>net accrual</b>, bukan ketiadaan mekanisme. (Pola yang sama dengan CPOOL - dua kali menyimpulkan benar lewat premis salah.)"],
 ["RAY revenue 18,33 juta Juli, +137% MoM = akselerasi","Angka itu hampir pasti Juli <b>2025</b>. Data segar: Q1-2026 5,79 juta, <b>-20,6% QoQ</b> - menurun."],
 ["SKY paling stabil, cacat paling sedikit","Recheck menemukan S&amp;P B-, buffer 0,4%, governance terpusat. Dikoreksi jadi <b>\"risiko BEDA JENIS, bukan risiko rendah\"</b>."],
 ["Premium negatif = pembeli absen = rally rapuh","Ki Young Ju membaca sebaliknya: penjual kehabisan tenaga. Urutan -0,0266 &rarr; 0,00 &rarr; +0,03 mendukung <b>bacaannya</b>, bukan bacaanku."],
 ["Stablecoin melambat 37%","Baseline 27 Agu tidak konsisten antar file (0,73% vs 0,94%). Yang benar: <b>melambat 19-37%</b>. Arah pasti, besaran tidak."],
 ["USDT/USDC negatif = redistribusi, bukan uang baru","Tidak didukung aritmetik - total naik 1,79 miliar. <b>Suplai baru memang dicetak</b>, hanya bukan oleh USDT/USDC."],
 ["ETH mendasar di -65% dari ATH","<b>Sudah terbantah sebelum diucapkan</b> - ETH sudah wick ke -70/-72%. Beta 1,10x kurang agresif; implisitnya ~1,19x. (Alasan strukturalnya benar, angkanya kurang berani.)"],
 ["ETH mendasar belakangan dari BTC","Diperhalus: ETH <b>73% jalan</b> vs BTC <b>62%</b>. ETH lebih jauh, bukan tertinggal."],
 ["Zona 46-58K mungkin tidak akan pernah terisi","Direhabilitasi - di skenario \"pola lama berulang\" zona itu justru tepat sasaran. Alasan tangga harus <b>dipecah</b>, bukan digeser."],
 ["Waktu Warsh ~21:00 WITA","Salah. 10:00 ET = 14:00 UTC = <b>22:00 WITA</b>. 21:00 itu WIB."],
], [58*mm,114*mm]))

# ---------------- GAP ----------------
F.append(P("9. Lubang Data yang Masih Menganga", H2))
F.append(tbl(["Prioritas","Data","Kenapa penting","Sumber"],[
 ["<b>1</b>","Coinbase Premium - nilai FINAL 29 Agu + sekarang","Satu-satunya kaki yang tersisa. 2 hijau berturut = naikkan sizing ke 35-45%","cryptoquant.com/asset/btc/chart/market-data/coinbase-premium-index"],
 ["<b>2</b>","Komposisi stablecoin peringkat 5-15 (USDe, PYUSD, USD1, FDUSD, USDG)","Menutup lubang 1,73 miliar: fiat atau leverage","defillama.com/stablecoins"],
 ["<b>3</b>","BTC daily close 29 Agu + harga sekarang","Apakah 76.000 sudah disentuh","TradingView"],
 ["4","Fee revenue tahunan Solana","Uji break-even RULE #1 (butuh &gt;1,4 mia)","defillama.com/chain/Solana"],
 ["5","Split inclusion vs resource fee (SIMD-0553)","Menentukan besar burn SOL sesungguhnya","github.com/solana-foundation/solana-improvement-documents"],
 ["6","Mcap PENDLE, revenue CPOOL, revenue RAY Q2-2026","Melengkapi kartu skor accrual","DeFiLlama / CoinGecko"],
 ["7","BTC.D (dominance)","Tripwire ketiga, belum pernah ditarik","TradingView"],
], [16*mm,44*mm,46*mm,66*mm], hilite=[1,2,3]))

# ---------------- AGENDA ----------------
F.append(PageBreak())
F.append(P("10. Agenda Terdekat", H2))
F.append(box("Senin 31 Agustus - hari terpenting minggu ini", [
 "<b>Dua tutup mingguan resolve serentak:</b>",
 "&nbsp;&nbsp;&bull; <b>BTC vs 82.344</b> - tutup di atas = bounce bukan bear rally, panggilan 50K batal, dasar naik ke 67.153",
 "&nbsp;&nbsp;&bull; <b>ETH vs MA 200W (~2.400)</b> - harga 2.435 hanya &lt;1,5% di atasnya. Tutup di bawah = tangga ETH aktif",
 "Kalau hanya sempat cek sekali minggu ini, cek setelah lilin mingguan tutup.",
], ACC))
F.append(Spacer(1,5))
F.append(P("Pembatal panggilan - dinyatakan di depan", H3))
F.append(tbl(["Aset","Terlalu dalam kalau...","Terlalu dangkal kalau..."],[
 ["BTC","Tutup MINGGUAN &gt; 82.344 &rarr; dasar naik ke 67.153","Tutup MINGGUAN &lt; 46.000 &rarr; target berikut 37.000 (-70% ATH)"],
 ["ETH","Tutup MINGGUAN &gt; 2.750 &rarr; batalkan Z1-Z2","Tutup MINGGUAN &lt; 1.323 &rarr; tambah Z5 di 1.100 (-78% ATH)"],
], [16*mm,78*mm,78*mm]))
F.append(Spacer(1,7))
F.append(rule())
F.append(P("Dokumen ini dihasilkan dari catatan riset di repo keizor88/ninja, branch claude/handoff-data-state-0d83l7. "
           "Semua panggilan adalah penilaian dengan keyakinan sedang, bukan fakta, dan disertai pemicu pembatalan yang dinyatakan di muka. "
           "Bukan nasihat keuangan.", SMALL))

def footer(canv, doc):
    canv.saveState()
    canv.setFont("Helvetica", 7)
    canv.setFillColor(MUTED)
    canv.drawString(19*mm, 11*mm, "Ringkasan Riset Kripto - 30 Agustus 2026 - data berstempel 29 Agu 2026")
    canv.drawRightString(196*mm, 11*mm, "Hal. %d" % doc.page)
    canv.setStrokeColor(LINE); canv.setLineWidth(0.4)
    canv.line(19*mm, 14*mm, 196*mm, 14*mm)
    canv.restoreState()

doc = SimpleDocTemplate(OUT, pagesize=A4,
                        leftMargin=19*mm, rightMargin=19*mm,
                        topMargin=15*mm, bottomMargin=18*mm,
                        title="Ringkasan Riset Portofolio Kripto - 30 Agustus 2026",
                        author="Catatan riset sesi")
doc.build(F, onFirstPage=footer, onLaterPages=footer)
print("OK ->", OUT)
