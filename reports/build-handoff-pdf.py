# -*- coding: utf-8 -*-
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, PageBreak, HRFlowable)

OUT = "/home/user/ninja/reports/handoff-riset-crypto-01sep2026.pdf"

INK=colors.HexColor("#16181d"); MUTED=colors.HexColor("#5b6270")
LINE=colors.HexColor("#d4d8e0"); BG=colors.HexColor("#f2f4f8")
ACC=colors.HexColor("#1a4f8a"); RED=colors.HexColor("#a8202a")
GRN=colors.HexColor("#1d6b3f"); AMB=colors.HexColor("#8a5a00")

def S(n,**kw):
    d=dict(name=n,fontName="Helvetica",fontSize=8.6,leading=12,textColor=INK,
           alignment=TA_LEFT,spaceAfter=4); d.update(kw); return ParagraphStyle(**d)
H1=S("H1",fontName="Helvetica-Bold",fontSize=17,leading=20,textColor=ACC,spaceAfter=2)
SUB=S("SUB",fontSize=9,textColor=MUTED,spaceAfter=10)
H2=S("H2",fontName="Helvetica-Bold",fontSize=11.5,leading=14,textColor=ACC,spaceBefore=11,spaceAfter=5)
H3=S("H3",fontName="Helvetica-Bold",fontSize=9.2,leading=12,spaceBefore=7,spaceAfter=3)
BODY=S("BODY"); SMALL=S("SMALL",fontSize=7.8,leading=10.5,textColor=MUTED)
CELL=S("CELL",fontSize=7.9,leading=10.2,spaceAfter=0)
CELLB=S("CELLB",fontSize=7.9,leading=10.2,fontName="Helvetica-Bold",spaceAfter=0)
def P(t,s=BODY): return Paragraph(t,s)
def bullets(items):
    return [Paragraph("&bull;&nbsp;&nbsp;"+t,ParagraphStyle("b",parent=BODY,leftIndent=9)) for t in items]
def tbl(header,rows,widths,hilite=None):
    data=[[Paragraph(h,CELLB) for h in header]]+[[Paragraph(str(c),CELL) for c in r] for r in rows]
    t=Table(data,colWidths=widths,repeatRows=1,hAlign="LEFT")
    st=[("BACKGROUND",(0,0),(-1,0),BG),("LINEBELOW",(0,0),(-1,0),0.8,ACC),
        ("LINEBELOW",(0,1),(-1,-2),0.3,LINE),("VALIGN",(0,0),(-1,-1),"TOP"),
        ("TOPPADDING",(0,0),(-1,-1),3.5),("BOTTOMPADDING",(0,0),(-1,-1),3.5),
        ("LEFTPADDING",(0,0),(-1,-1),5),("RIGHTPADDING",(0,0),(-1,-1),5)]
    for i in (hilite or []): st.append(("BACKGROUND",(0,i),(-1,i),colors.HexColor("#eaf1fa")))
    t.setStyle(TableStyle(st)); return t
def box(title,lines,bc=ACC):
    inner=[Paragraph(title,ParagraphStyle("bt",parent=CELLB,fontSize=9,textColor=bc))]
    inner+=[Paragraph(l,CELL) for l in lines]
    t=Table([[inner]],colWidths=[172*mm],hAlign="LEFT")
    t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),colors.HexColor("#f7f9fc")),
        ("BOX",(0,0),(-1,-1),0.7,bc),("LEFTPADDING",(0,0),(-1,-1),8),
        ("RIGHTPADDING",(0,0),(-1,-1),8),("TOPPADDING",(0,0),(-1,-1),6),
        ("BOTTOMPADDING",(0,0),(-1,-1),6)])); return t
def rule(): return HRFlowable(width="100%",thickness=0.6,color=LINE,spaceBefore=6,spaceAfter=6)

F=[]
F.append(P("Handoff Riset Portofolio Kripto",H1))
F.append(P("Status per 1 September 2026 &nbsp;|&nbsp; repo keizor88/ninja &nbsp;|&nbsp; branch claude/handoff-data-state-0d83l7",SUB))
F.append(rule())

F.append(box("CARA PAKAI DOKUMEN INI",[
 "Ini dokumen SERAH TERIMA. Isinya: aturan yang dipakai, keputusan yang sedang berlaku, angka terakhir, dan apa yang belum dijawab.",
 "<b>Bagian 3 (Keputusan Aktif) dan Bagian 10 (Belum Dijawab) adalah dua bagian yang harus dibaca duluan.</b> Sisanya adalah alasan di baliknya.",
 "Semua panggilan harga adalah <b>penilaian dengan keyakinan sedang</b>, bukan fakta, dan setiap satu punya pemicu pembatalan yang dinyatakan di muka.",
 "<b>Bukan nasihat keuangan.</b>",
],ACC))
F.append(Spacer(1,5))
F.append(box("BATAS DATA - PENTING",[
 "1. Harga BTC/ETH/INDEX di dokumen ini dari <b>1 September 2026</b>, ditarik lewat pencarian web. <b>Sumber berbeda memberi angka berbeda</b> (BTC $78.243-78.838, INDEX $0,0298-0,0332). Verifikasi di venue eksekusi sendiri.",
 "2. Data flow (stablecoin, TVL per chain) berstempel <b>27-29 Agustus</b> - sudah basi.",
 "3. Asisten: cutoff pengetahuan Mei 2026. <b>WebSearch berfungsi</b>; fetch langsung ke coingecko/cryptoquant/defillama <b>diblokir</b>.",
 "4. Angka bertanda <b>(turunan)</b> = hasil hitungan, bukan data tarikan.",
],RED))

F.append(P("1. Aturan Main",H2))
F.append(tbl(["Aturan","Isi"],[
 ["<b>RULE #1</b> Value Accrual","Beli TOKEN-nya, bukan protokolnya. Harus ada pipa mekanis: buyback / burn / fee-share. Earnings = Revenue &minus; Incentives. \"% fee ke holder\" bukan net accrual."],
 ["<b>RULE #2</b> Data Discipline","Tidak pernah mengarang angka. Kalau data tidak ada: berhenti, sebutkan yang hilang, minta ditarik."],
 ["<b>RULE #3</b> Flow Normalization","Angka absolut dilarang jadi dasar peringkat. Selalu bagi dengan basis yang relevan."],
], [30*mm,142*mm]))

F.append(P("2. Tiga Jebakan yang Berulang",H2))
F.append(tbl(["Jebakan","Contoh nyata","Cara lolos"],[
 ["Kolom \"Holders Revenue\" bisa berarti LP atau pemegang derivatif staking, bukan token governance","Lido, Uniswap, Aerodrome","Baca dokumen distribusi, bukan kolom agregator"],
 ["\"Buyback\" bukan pengurangan suplai","Dari 11 token yang klaim buyback, hanya ~2 yang benar-benar menyusut. CPOOL: buyback live, <b>0% dibakar</b>","Cek berapa persen DIBAKAR, bukan berapa dibeli"],
 ["\"Rekor\" tanpa denominator adalah iklan","SOL ETF inflow \"terbesar 2026\" $33,5jt = <b>0,211%</b> dari basis stablecoin Solana","Selalu bagi dengan basis"],
], [50*mm,68*mm,54*mm]))

F.append(PageBreak())
F.append(P("3. KEPUTUSAN AKTIF - baca ini dulu",H2))
F.append(box("A. AMBIL KAS DI ALTCOIN - keputusan 1 September",[
 "<b>Alasan pokok:</b> EV pegang = &minus;32% s/d &minus;40%; EV kas = 0%. Titik impas ada di P(turun) = ~50%. Taksiran kita 80%.",
 "<b>Kokohnya di sini:</b> bahkan kalau taksiran 80% ternyata cuma 60%, kas tetap menang. Keputusan tidak bergantung angka itu tepat.",
 "<b>Matematika pemulihan:</b> turun 60% butuh naik 150% cuma untuk impas. Salah dan di kas cuma perlu bayar 10-20% lebih mahal.",
 "<b>Carry tidak menolong:</b> 14,2%/thn = 4,7% selama 4 bulan, menutup 7,9% dari drawdown 60%.",
],GRN))
F.append(Spacer(1,4))
F.append(tbl(["Tier","Aset","Jual berapa","Alasan"],[
 ["<b>A</b>","Alt tanpa accrual, beta murni, meme, launch baru, token launchpad","<b>100%</b>","Tidak ada lantai, tidak ada carry"],
 ["<b>B</b>","<b>HYPE</b>","<b>70-80%</b>","LIKUIDITAS, bukan tesis. 21.941 alamat aktif vs Solana 2,71jt = 123x lebih sedikit. Tidak bisa keluar SAAT flush, hanya SEBELUM"],
 ["<b>C</b>","SYRUP, PENDLE","<b>50-60%</b>","Carry nyata, tapi tidak menutup drawdown"],
 ["<b>C+</b>","<b>SKY</b>","<b>60-70%</b>","Dipangkas LEBIH banyak walau grade accrual tertinggi. Buffer modal 0,4% = di crash risikonya SOLVENSI, bukan harga. Nama lain jatuh lalu pulih; buffer 0,4% bisa tidak pulih"],
 ["-","<b>BTC</b>","<b>PERTAHANKAN</b>","Naik 10-20% ke <b>25-30%</b>"],
 ["-","<b>ETH</b>","<b>PERTAHANKAN</b>","Z1 <b>10%</b> saja"],
], [12*mm,50*mm,22*mm,88*mm], hilite=[1,2,3,4,5,6]))
F.append(Spacer(1,3))
F.append(box("Timing eksekusi - agak berlawanan intuisi",[
 "BTC baru memantul dan Coinbase Premium baru hijau pertama kali dalam ~100 hari.",
 "<b>Itu LIKUIDITAS KELUAR untuk buku altcoin, bukan sinyal beli.</b> Kekuatan = spread sempit + ada bid. Kalau menunggu flush mulai, kamu menjual ke spread lebar di harga terburuk.",
 "Sebar <b>2-3 hari</b>, jam likuiditas AS/Eropa, <b>limit order</b> (terutama HYPE).",
 "<b>Pajak tidak dihitung</b> - variabel ini bisa membalik keputusan untuk Tier C. Cek sendiri.",
],AMB))

F.append(P("4. Panggilan Harga - BTC & ETH",H2))
F.append(tbl(["Aset","Harga 1 Sep","Target dasar","Titik tengah","Dari harga","Dari ATH","Waktu"],[
 ["<b>BTC</b>","~78.500","48.000-52.000","<b>50.000</b>","<b>&minus;36,3%</b>","&minus;59,5%","Okt-Des 2026"],
 ["<b>ETH</b>","~2.440","1.450-1.550","<b>1.500</b>","<b>&minus;38,5%</b>","&minus;69,6%","bersamaan BTC"],
], [16*mm,24*mm,30*mm,22*mm,22*mm,20*mm,38*mm], hilite=[1,2]))
F.append(P("Dasarnya",H3))
F.extend(bullets([
 "<b>BTC bukan 57.000</b> (hasil tertimbang 56.557): low sebelumnya jarang bertahan, biasanya ditembus. Kalau bertahan, bear berhenti di &minus;53,8% - lebih dangkal dari bear BTC mana pun dalam sejarah (terdangkal &minus;77%).",
 "<b>BTC bukan 37.000-43.000</b>: drawdown mengecil tiap siklus (&minus;86 &rarr; &minus;84 &rarr; &minus;77). ETF + treasury company memberi lantai.",
 "<b>Konfluensi 50.000</b>: shelf 50.148 + fraktal ulangan 47.894 + dasar tangga lama 46-58K.",
 "<b>ETH:</b> tiga metode konvergen di 1.433-1.511 (beta leg sisa, retest wick low, &minus;70% ATH). Beta ETH ke BTC selalu &gt;1 (2018: 1,12x; 2022: 1,06x; siklus ini implisit ~1,17-1,19x karena L2 menyedot fee L1).",
 "<b>Progres:</b> BTC 62% jalan menuju target, ETH 73%. <b>ETH lebih jauh, bukan tertinggal</b> - tapi leg sisa ETH masih sedikit lebih dalam (&minus;38,4% vs &minus;35,8%), jadi urutan tetap BTC dulu, jaraknya rapat.",
]))
F.append(P("Tangga",H3))
F.append(tbl(["BTC","Porsi","","ETH","Porsi"],[
 ["T1 (terpasang) 77.800","10-20% &rarr; <b>25-30%</b>","","Z1 2.100","10%"],
 ["T2 71.070","20%","","Z2 1.950","20%"],
 ["T3 67.153 <i>(Fib 78,6% = 67.140)</i>","30%","","<b>Z3 1.450-1.550</b>","<b>40%</b>"],
 ["<b>T4 48.000-52.000</b>","<b>20%</b>","","Z4 1.323","20%"],
 ["Kas","10-20%","","Kas","10%"],
], [58*mm,28*mm,6*mm,52*mm,20*mm], hilite=[4]))
F.append(P("Stress test: kalau black swan mencetak 47.894 - tangga pecah &minus;20,9% vs all-in &minus;38,5%; saat pulih ke 123.374, tangga pecah <b>+80,1%</b> vs all-in +58,5%. Tangga lebih tahan di crash DAN lebih untung di pemulihan, karena tranche terakhir mengubah crash jadi peluang. Tangga bertingkat ADALAH manajemen black swan.",SMALL))
F.append(P("Pembatal",H3))
F.append(tbl(["Aset","Terlalu dalam kalau...","Terlalu dangkal kalau..."],[
 ["BTC","Tutup MINGGUAN &gt; 82.344 &rarr; dasar naik ke 67.153","Tutup MINGGUAN &lt; 46.000 &rarr; target 37.000"],
 ["ETH","Tutup MINGGUAN &gt; 2.750 &rarr; batalkan Z1-Z2","Tutup MINGGUAN &lt; 1.323 &rarr; tambah Z5 di 1.100"],
], [16*mm,78*mm,78*mm]))

F.append(P("5. Data Terakhir - 1 September 2026",H2))
F.append(tbl(["Indikator","Nilai","Status"],[
 ["<b>BTC</b>","~$78.500 (sumber 78.243-78.838)","Tutup mingguan DAN bulanan 31 Agu <b>di bawah ~$80.000</b>. Super Trend mingguan tetap MERAH"],
 ["Low pra-close","$77.024","Cuma <b>+1,3%</b> di atas level struktur 76.000 - nyaris kena"],
 ["Likuidasi","&gt;$400jt","Saat tembus $78.000"],
 ["<b>Tripwire 82.344</b>","<b>TIDAK TEMBUS</b> (&minus;4,7%)","Panggilan $50.000 <b>bertahan</b>"],
 ["<b>Coinbase Premium</b>","<b>POSITIF</b>","Flip akhir Agustus setelah rekor <b>102-103 hari negatif</b>. Nilai numerik BELUM didapat"],
 ["Stablecoin total","$303,98 miliar, <b>+0,59%/7d</b> <i>(29 Agu)</i>","GAGAL ambang &gt;+1,5% (cross-check) dan &gt;+2% (regime). Melambat 19-37%"],
 ["US30Y","5,213%","HIJAU (&lt;5,3%). Turun dari puncak 5,33% - tertinggi 19 tahun"],
 ["<b>ETH</b>","~$2.440","200W EMA aktual <b>$2.456</b> (harga 0,65% DI BAWAH); 50W EMA $2.375 (di atas). Terlalu tipis untuk sinyal"],
 ["<b>Tripwire nyala</b>","<b>1 dari 3</b>","Premium hijau. Stablecoin merah. BTC.D belum pernah ditarik"],
], [30*mm,44*mm,98*mm], hilite=[4,5,9]))
F.append(P("Odds: <b>P(Q4 turun/bottom) = 80%</b> (turun dari 85% karena premium hijau). Distribusi: chop 67-82K 30% | tembus 67.153 ke 50.148 30% | fraktal penuh 47.894 20% | base-rate historis &lt;43.000 5% | rally keluar 15%.",SMALL))

F.append(P("6. Money Flow - keadaan dan lubangnya",H2))
F.append(P("Model berlapis: stablecoin supply (leading) &rarr; bridge net-flow &rarr; TVL &rarr; DEX volume / active address &rarr; token L1 &rarr; token ekosistem (meme terakhir).",BODY))
F.append(box("LUBANG TERBESAR YANG MASIH TERBUKA - komposisi stablecoin",[
 "Total stablecoin tumbuh <b>+$1.792 juta</b> dalam 7 hari. Dari lima koin yang datanya ada, cuma <b>~+$60 juta</b> yang bisa dijelaskan - dan itu setelah USDT (&minus;0,03%) dan USDC (&minus;0,05%) menariknya ke bawah.",
 "Artinya <b>&gt;95% pertumbuhan (~$1,73 miliar) datang dari penerbit yang tidak ada di data kita.</b>",
 "<b>Pertanyaan penentu: fiat atau leverage?</b> Kalau <b>USDe (Ethena)</b> - sintetis, tumbuh dari funding-rate arb - itu BUKAN dry powder, melainkan leverage yang unwind saat funding negatif (mekanisme refleksif tipe LUNA). Kalau <b>PYUSD/USD1/FDUSD</b> - fiat-backed - itu dry powder asli.",
 "<b>Selama belum dijawab, angka +0,59% tidak bisa dipakai sebagai konfirmasi maupun bantahan.</b> Tarik: defillama.com/stablecoins, koin peringkat 5-15.",
],AMB))
F.append(P("Kebutuhan bahan bakar untuk skenario bullish (BTC 145.000 pada Januari 2027)",H3))
F.append(P("Asumsi terbuka: leg BTC yang menggandakan harga historisnya disertai ekspansi stablecoin ~20% = ~+$60,8 miliar.",SMALL))
F.append(tbl(["Leg naik mulai","Sisa minggu","Butuh harga","Butuh stablecoin","vs +0,59% sekarang"],[
 ["1 Oktober","17,4","+4,5%/mg","+1,15%/mg","~2x"],
 ["1 November","13,0","+6,1%/mg","+1,54%/mg","~2,6x"],
 ["1 Desember","9,0","+8,9%/mg","+2,22%/mg","~3,8x"],
], [30*mm,24*mm,28*mm,32*mm,34*mm]))
F.append(P("<b>Dua angka kunci:</b> (1) bar yang dibutuhkan (1,15-1,54%/mg) ada DI BAWAH ambang regime-change kita (&gt;2%/mg) - jadi kalau tripwire stablecoin nyala, target 145K terbiayai penuh. (2) <b>Batas ~22 November</b>: setelah itu kebutuhan menembus 2%/mg dan target berubah dari cerita flow jadi butuh mania.",BODY))

F.append(PageBreak())
F.append(P("7. $INDEX (The Index) - Robinhood Chain - kandidat baru",H2))
F.append(box("PERINGATAN: ADA DUA TOKEN BERNAMA \"INDEX\"",[
 "<b>Index Cooperative (INDEX)</b> di Ethereum (penerbit DPI) adalah <b>aset yang sama sekali berbeda</b>.",
 "Yang dibahas di sini: <b>The Index / @TheIndexFi, di Robinhood Chain.</b> <b>Cocokkan alamat kontrak sebelum transaksi apa pun.</b>",
],RED))
F.append(Spacer(1,4))
F.append(P("Cara kerjanya satu kalimat",H3))
F.append(P("<b>Fee trading di Robinhood Chain dikumpulkan &rarr; dipakai membeli saham tokenized (NVDA, GOOG, AAPL) &rarr; dibagikan ke pemegang $INDEX.</b> Protokol TIDAK menerbitkan token baru untuk imbalan - dia membeli aset eksternal.",BODY))
F.append(tbl(["Metrik","Nilai"],[
 ["Harga / Market cap","<b>$0,033</b> / <b>$32,6 juta</b> (rank #613)"],
 ["Suplai","980,54jt beredar / 1 miliar maks = <b>98,05% BEREDAR</b>. FDV/mcap = 1,009x"],
 ["Revenue 30 hari","$290.792 (dari fee $456.509 - take rate 63,7%)"],
 ["Revenue run-rate","<b>$3,54 juta/tahun</b>"],
 ["<b>Yield / P/S</b>","<b>10,9% / 9,2x</b> - dan yield ini BATAS ATAS (dokumen bilang \"sebagian\" revenue)"],
 ["ATH","<b>$0,035 pada 30 Agustus</b> - harga sekarang &minus;5,7% dari situ"],
 ["Momentum","<b>+361% dalam 7 hari</b>, +244% dalam 30 hari. Mcap $7jt &rarr; $32jt dalam seminggu"],
 ["Turnover 24h","16,9% (volume $5,5jt)"],
], [38*mm,134*mm], hilite=[5,6,7]))
F.append(P("Chain-nya: Robinhood Chain (L2 Arbitrum Orbit, live 1 Juli 2026). TVL Juni $4jt &rarr; akhir Agustus <b>$1,4-1,46 miliar</b>. Rekor volume DEX <b>$989 juta sehari</b>. Chain tercepat tumbuh dari semua yang lahir 2026. 426rb pemegang saham tokenized.",BODY))

F.append(P("Yang bagus",H3))
F.extend(bullets([
 "<b>Pipanya bersih dan otomatis</b> - tidak perlu voting, tidak perlu keputusan tim.",
 "<b>Tidak mencetak token baru untuk imbalan</b> - jadi Earnings = Revenue, biaya insentif ~nol.",
 "<b>Suplai 98% beredar</b> - praktis tidak ada overhang unlock. Struktur terbaik dari semua nama yang pernah dinilai.",
 "<b>Imbalannya di luar crypto (NVDA/AAPL).</b> Ini menjawab langsung temuan risiko ekor kita: guncangan makro membuat semua token turun bersamaan, jadi diversifikasi antar-token bukan diversifikasi. INDEX satu-satunya yang keluar dari korelasi itu.",
 "<b>Satu-satunya nama yang mengenai ketiga kriteria user sekaligus</b>: money flow + RWA + accrual.",
 "<b>Multiple mengempis cepat kalau volume bertahan:</b> revenue 2x &rarr; P/S 4,6x, yield 21,7%; revenue 3x &rarr; P/S 3,1x, yield 32,6%.",
]))
F.append(P("Yang jelek",H3))
F.extend(bullets([
 "<b>Harganya di puncak</b> - ATH dua hari lalu, +361% seminggu.",
 "<b>Divergence Score kita sendiri: &minus;478</b> (ambang +4). Gagal telak - ini jendela AKHIR, bukan awal.",
 "<b>Umur 2 bulan.</b> Belum pernah kena bear market, belum pernah diuji drawdown.",
 "<b>Tidak jelas berapa persen revenue yang dibagi.</b> Kalau ternyata 30%, yield jadi <b>3,3%</b> dan seluruh alasan beli hilang.",
 "<b>Tergantung satu chain milik perusahaan.</b> Robinhood bisa ubah struktur fee kapan saja.",
 "<b>Bentuk regulasi:</b> membagikan imbal hasil ekuitas ke pemegang token secara struktural mirip sekuritas pembayar dividen.",
]))
F.append(box("RENCANA - didanai dari hasil penjualan Tier A/B, bukan dari kas cadangan",[
 "<b>Total jatah: 2% portofolio (maks 3%).</b> Di 2%, salah total = porto turun 2%; naik 3x = porto naik 4%. Ukuran yang benar untuk aset umur 2 bulan.",
 "<b>Starter 25% sekarang (~$0,030-0,033)</b> - asuransi terhadap \"benar tapi tidak pernah terisi\", logika sama dengan starter BTC.",
 "<b>Inti 40% di $0,0211</b> (Fib 50%, yield naik ke 17,1%) &nbsp;|&nbsp; <b>Tambahan 35% di $0,0179</b> (Fib 61,8%, yield 20,2%).",
 "<b>Upside terhitung</b> (re-rate ke yield 10%): entry $0,0211 + revenue 2x = <b>+242%</b>; + revenue 3x = <b>+413%</b>.",
 "<b>Pembatal:</b> revenue 30d Oktober &lt; $290rb &rarr; jual, batal total. Volume DEX chain &lt; ~$300jt/hari &rarr; potong sizing separuh. Tembus $0,035 dan bertahan &rarr; starter ikut, JANGAN chase sisanya. Berita regulasi &rarr; keluar duluan.",
],GRN))

F.append(PageBreak())
F.append(P("8. Hasil Skrining Value Accrual",H2))
F.append(P("Temuan struktural: accrual bersih itu langka - tiga protokol teratas menguasai <b>83,1%</b> dari seluruh holders revenue DeFi.",BODY))
F.append(tbl(["Aset","Grade","Catatan"],[
 ["<b>INDEX</b>","<b>7/10 WATCH-TINGGI</b>","Pipa terbersih yang ditemukan. Lihat bagian 7. Aset bagus, entry buruk"],
 ["<b>SKY</b>","LOLOS","Mesin kas terbaik. TAPI S&amp;P B&minus;, buffer modal 0,4% (~$23jt di atas TVL $5,87mia), Rune kendalikan governance dgn ~9% token, usulan freeze USDS. <b>Risiko BEDA JENIS, bukan risiko rendah</b>"],
 ["<b>SYRUP</b>","LOLOS","Dikoreksi naik. Risiko: bisnisnya kredit tanpa jaminan penuh - risiko kredit by design"],
 ["<b>PENDLE</b>","LOLOS (watch)","Paling align tema flow. Diturunkan ke watch karena peringatan TVL ($1,19mia)"],
 ["<b>RAY</b>","LOLOS","6/10. Revenue Q1-2026 $5,79jt, <b>&minus;20,6% QoQ</b> - menurun"],
 ["<b>LIT</b>","LOLOS","-"],
 ["<b>ETH</b>","WATCH","Pipa ada (EIP-1559). Net-inflasi sekarang. <b>Bar break-even 4,4x lebih rendah dari SOL</b> (issuance ~0,8% vs 3,55%). Kandidat L1 terkuat"],
 ["<b>SOL</b>","WATCH","Naik dari GAGAL setelah SGP-0002 (disinflasi &minus;15% ke &minus;30%) dan SGP-0003 (resource fee 100% dibakar). Tapi SGP-0003 masih <b>mandat</b>, bukan kode terkirim. Break-even butuh $1,4-2,8mia fee/thn dibakar"],
 ["<b>ASTER, CPOOL, TRX</b>","WATCH","CPOOL: buyback live sejak 20 Okt 2025 tapi 0% dibakar. TRX: mekanisme nyata tapi net ~0"],
 ["<b>CANTON, CFG, XPL, AVAX</b>","GAGAL","XPL: TVL Aave $6,6mia lewat chain-nya, XPL tidak menangkap apa pun. AVAX: outflow &minus;5,07% + fee mikroskopis"],
], [30*mm,26*mm,116*mm], hilite=[1,2]))

F.append(P("9. Risiko Ekor",H2))
F.append(tbl(["Pertanyaan","Jawaban","Bisa dikendalikan?"],[
 ["P(peristiwa ekor parah dalam 5 bulan)","<b>~40%</b> (rentang 28-44%)","Tidak sama sekali"],
 ["P(kena drawdown | peristiwa terjadi)","~80% - korelasi menuju 1 saat krisis","Hampir tidak"],
 ["P(kehancuran permanen | peristiwa)","Ditentukan struktur portofolio","<b>Ya, hampir seluruhnya</b>"],
 ["P(black swan sejati)","<b>Tidak bisa diketahui</b>","-"],
], [58*mm,66*mm,48*mm], hilite=[1,4]))
F.append(P("Base rate: 17 peristiwa sistemik / 15 tahun (2011-2026) &rarr; lambda 1,13/thn. Crypto memproduksi peristiwa ekor kira-kira sekali setahun - itu properti kelas asetnya. Blowup menggerombol 6-14 bulan setelah puncak siklus (2021: LUNA 6bln, 3AC 7, Celsius 8, FTX 12); puncak siklus ini ~pertengahan 2025 jadi sekarang ~14 bulan = ujung belakang jendela. Peringatan: bulan 12-14 jatuh di Mei-Agustus 2026, persis blind spot asisten.",SMALL))
F.append(box("Titik paling rapuh, urut",[
 "<b>1. Buffer modal SKY 0,4%.</b> Kerugian 0,4% di sisi aset menghabiskan modalnya. Bank komersial jalan di tier-1 8-15% - SKY <b>20-37x lebih tipis dari bank</b>. Aturan: cap SKY di porsi yang sanggup dilihat jadi nol.",
 "<b>2. Di mana disimpan.</b> Pelajaran FTX: fraudnya off-chain, data on-chain tidak menunjukkan apa pun. <b>Satu-satunya risiko besar yang bisa dihapus hari ini, gratis: self-custody untuk core, exchange hanya untuk modal scalping.</b>",
 "<b>3. Konsentrasi HYPE.</b> 21.941 alamat aktif vs Solana 2,71jt = 123x lebih sedikit. Sedikit whale keluar = tidak ada bid.",
 "<b>4. Makro.</b> US30Y tertinggi 19 tahun + intervensi Treasury gagal. Guncangan makro tidak peduli filter accrual - semua turun bersamaan.",
 "<b>Risiko terbesar sesungguhnya (bukan black swan):</b> BENAR soal dip dan tetap hancur karenanya. Kalau 60% terpasang di 67.153 lalu black swan mencetak 47K - analisisnya benar, amunisi habis di dasar. Ini alasan struktural T4 harus dijaga.",
],RED))

F.append(PageBreak())
F.append(P("10. BELUM DIJAWAB - baca ini kedua",H2))
F.append(tbl(["#","Data","Kenapa penting","Sumber"],[
 ["<b>1</b>","<b>Nilai NUMERIK Coinbase Premium</b> (bukan cuma \"positif\")","Penentu apakah sizing BTC naik ke 35-45%. Positif 0,01 dan 0,15 dua dunia berbeda (rentang hijau normal 0,10-0,25)","cryptoquant.com/asset/btc/chart/market-data/coinbase-premium-index"],
 ["<b>2</b>","<b>Komposisi stablecoin peringkat 5-15</b> (USDe, PYUSD, USD1, FDUSD, USDG)","Menutup lubang $1,73 miliar: fiat (bullish) atau leverage (refleksif, berbahaya)","defillama.com/stablecoins"],
 ["<b>3</b>","<b>Berapa % revenue INDEX yang dibagikan</b>","Kalau 100% yield 10,9% dan tesis utuh. Kalau 30% yield 3,3% dan tesis runtuh. <b>Cari sebelum tranche kedua</b>","docs resmi The Index / X @TheIndexFi"],
 ["4","Stablecoin total 7d terkini","Masih +0,59% atau sudah &gt;+1,5%?","defillama.com/stablecoins"],
 ["5","BTC.D (dominance)","Tripwire ketiga, belum pernah ditarik sama sekali","TradingView"],
 ["6","Revenue INDEX 30d bulan Oktober","Satu-satunya angka yang menentukan nasib posisi INDEX","defillama.com/protocol/the-index"],
 ["7","Fee revenue tahunan Solana + split SIMD-0553","Uji break-even RULE #1 untuk SOL","defillama.com/chain/Solana"],
 ["8","Mcap PENDLE, revenue CPOOL, revenue RAY Q2-2026","Melengkapi kartu skor accrual","DeFiLlama / CoinGecko"],
], [10*mm,42*mm,58*mm,62*mm], hilite=[1,2,3]))

F.append(P("11. Log Koreksi - kesalahan yang tercatat",H2))
F.append(P("Bagian ini sengaja disertakan. Riset yang tidak mencatat kesalahannya sendiri tidak bisa dipercaya.",SMALL))
F.append(tbl(["Klaim awal (salah)","Perbaikan"],[
 ["Base adalah juara flow","<b>Denominator salah</b> - basis dilebihkan 3,6x ($18,22mia vs $5,018mia aktual). Semua angka intensitas v2 dicabut. Base ternyata FLAT (+0,06%). <b>Melahirkan RULE #3</b>"],
 ["Hyperliquid: bridge outflow = distribusi","Salah. HL justru inflow stablecoin TERKUAT (+5,15%)"],
 ["CPOOL: buyback belum live","Salah - live sejak 20 Okt 2025. Gagal karena alasan berbeda: 0% dibakar"],
 ["SOL: L1 tanpa pipa mekanis","Salah - Solana bakar 50% base fee sejak awal. Gagal karena <b>net accrual</b>. (Pola sama dengan CPOOL - dua kali menyimpulkan benar lewat premis salah)"],
 ["RAY revenue +137% MoM = akselerasi","Angka itu Juli <b>2025</b>. Data segar: Q1-2026 &minus;20,6% QoQ - menurun"],
 ["SKY paling stabil, cacat paling sedikit","Recheck: S&amp;P B&minus;, buffer 0,4%, governance terpusat. Jadi \"risiko BEDA JENIS, bukan risiko rendah\""],
 ["Premium negatif = pembeli absen = rally rapuh","Ki Young Ju membaca sebaliknya: penjual kehabisan tenaga. Urutan data mendukung <b>bacaannya</b>"],
 ["Stablecoin melambat 37%","Baseline 27 Agu tidak konsisten antar file (0,73% vs 0,94%). Yang benar: melambat <b>19-37%</b>"],
 ["USDT/USDC negatif = redistribusi","Tidak didukung aritmetik - total naik $1,79mia. Suplai baru memang dicetak, hanya bukan oleh USDT/USDC"],
 ["ETH mendasar di &minus;65% dari ATH","Sudah terbantah sebelum diucapkan - ETH sudah wick ke &minus;70/&minus;72%. Beta 1,10x kurang agresif; implisitnya ~1,19x"],
 ["ETH mendasar belakangan dari BTC","Diperhalus: ETH 73% jalan vs BTC 62%. ETH lebih jauh, bukan tertinggal"],
 ["Zona 46-58K mungkin tidak akan pernah terisi","Direhabilitasi - di skenario \"pola lama berulang\" zona itu tepat sasaran. Alasan tangga harus <b>dipecah</b>, bukan digeser"],
 ["INDEX: pendapatan runtuh &minus;61%","<b>Kemungkinan besar salah</b> - dibangun di atas asumsi anualisasi yang tidak diverifikasi. Data chain membantah: TVL $4jt &rarr; $1,4mia, rekor DEX $989jt/hari"],
 ["\"Egress diblokir, tidak bisa menarik data\"","<b>Separuh benar.</b> WebSearch BEKERJA; hanya fetch langsung ke coingecko/cryptoquant/defillama yang diblokir. Papan sempat basi 2 hari tanpa alasan sah"],
 ["Waktu Warsh ~21:00 WITA","Salah. 10:00 ET = 14:00 UTC = <b>22:00 WITA</b>. 21:00 itu WIB"],
], [56*mm,116*mm]))

F.append(P("Sumber lengkap: repo keizor88/ninja, branch claude/handoff-data-state-0d83l7, folder trackers/. Bukan nasihat keuangan.",SMALL))

def footer(canv,doc):
    canv.saveState(); canv.setFont("Helvetica",7); canv.setFillColor(MUTED)
    canv.drawString(19*mm,11*mm,"Handoff Riset Kripto - status 1 September 2026")
    canv.drawRightString(196*mm,11*mm,"Hal. %d"%doc.page)
    canv.setStrokeColor(LINE); canv.setLineWidth(0.4); canv.line(19*mm,14*mm,196*mm,14*mm)
    canv.restoreState()

doc=SimpleDocTemplate(OUT,pagesize=A4,leftMargin=19*mm,rightMargin=19*mm,
    topMargin=15*mm,bottomMargin=18*mm,
    title="Handoff Riset Portofolio Kripto - 1 September 2026",author="Catatan riset sesi")
doc.build(F,onFirstPage=footer,onLaterPages=footer)
print("OK ->",OUT)
