# Superanalyst: full matchday 18 November 2026 WIB

Delapan pertandingan pada lampiran, UEFA Nations League senior putra. Seluruh kickoff **Rabu, 18 November 2026 pukul 02.45 WIB** (17 November 19.45 UTC). Batas informasi **17 November 2026, 19.16.25 WIB**. Cakupan hasil: 90 menit + injury time, tanpa extra time/penalti. Status keseluruhan **provisional**, karena XI resmi belum diumumkan dalam snapshot ini. Jadwal: [UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/).

## Cara membaca dua model

**Utama:** acuan kualitatif UNL v1, `qualitative_superanalyst_national_team_pilot_v1`, dalam paket skill v0.4.3. Lima laga, lawan, venue, skuad dan konteks dibaca bersama. Tingkat keyakinan bersifat kualitatif; tidak diubah menjadi persentase buatan.

**Beta:** `national-team-research-v1`, dilatih ulang pada 17 November dengan resep dan kalibrator asli. 1X2/BTTS memakai kekuatan serang-bertahan berbobot waktu paruh 730 hari dan latihan kompetitif; total memakai 365 hari dengan friendly sebagai kompetisi tersendiri. Jendela latih enam tahun, regularisasi tim/kompetisi 20 dan jeda tiga tanggal kalender tetap. Model 1X2 berlatih pada 3.076 laga, model total pada 4.624 laga; hasil terbaru yang masuk 14 November. Probabilitas setiap target dikalibrasi tersendiri, sehingga bukan satu distribusi skor gabungan.

Korpus lama sampai 6 Oktober ditambah **26 hasil UNL matchday 5** dari UEFA. Hasil global non-UNL setelah 6 Oktober belum diaudit lengkap. Cedera, pergantian pelatih, xG, XI dan pasar tidak menjadi fitur beta. Karena itu angka beta merupakan forecast eksperimental berbasis skor dengan batas konteks yang nyata. Rekonstruksi 848 laga UEFA 2022–2025 pada studi asli bukan bukti prospektif untuk matchday ini; tidak diklaim sebagai akurasi masa depan.

**Aturan penerbitan beta untuk sesi ini:** 1X2 baru aktif jika peluang tertinggi ≥45% dan selisih dua teratas ≥10 poin persentase. BTTS/total aktif jika peluang sisi yang dipilih ≥55%. Ambang ini hanya mengatur abstain pada laporan, belum divalidasi untuk keuntungan dan tidak mengubah probabilitas model. Angka yang tidak lolos tetap ditampilkan, tetapi `pick=null`. Keyakinan beta juga mempertimbangkan keterwakilan konteks; Austria diturunkan ke rendah karena rotasi.

**Observasi** berarti tidak ada pilihan aktif. Skor adalah skenario, bukan pilihan otomatis. Fokus dipilih sebelum hasil diketahui dan disimpan bersama status/keyakinan masing-masing target. “Cukup kuat” adalah tingkat relatif di dalam analisis, bukan probabilitas terkalibrasi.

## Model utama

| Laga | 1X2 | BTTS | Total 2,5 | Fokus | Skor* |
|---|---|---|---|---|---|
| Denmark vs Norwegia | Denmark (Rendah) | Ya (Sedang) | Over 2,5 (Sedang) | BTTS Ya | 2-1 |
| Wales vs Portugal | Portugal (Sedang) | Observasi | Observasi | 1X2 Portugal | 0-2 |
| Bosnia & Herzegovina vs Rumania | Bosnia & Herzegovina (Rendah) | Ya (Sedang) | Over 2,5 (Rendah) | BTTS Ya | 2-1 |
| Hungaria vs Irlandia Utara | Observasi | Tidak (Sedang) | Under 2,5 (Cukup kuat) | Total 2,5 Under 2,5 | 1-0 |
| Republik Irlandia vs Kosovo | Observasi | Tidak (Sedang) | Under 2,5 (Sedang) | Total 2,5 Under 2,5 | 1-0 |
| Israel vs Austria | Observasi | Observasi | Observasi | Tidak ada | 0-1 |
| Polandia vs Swedia | Swedia (Rendah) | Observasi | Over 2,5 (Rendah) | 1X2 Swedia | 1-2 |
| Ukraina vs Georgia | Observasi | Tidak (Cukup kuat) | Under 2,5 (Sedang) | BTTS Tidak | 1-0 |

*Utama: skenario editorial. Beta: modus dari Poisson **mentah** resep 1X2, bukan skor hasil kalibrasi semua target. Modus 0-0 tidak menjamin seri. Pilihan aktif/8: 1X2 4, BTTS 5, Total 2,5 6.

## Model beta

| Laga | 1X2 | BTTS | Total 2,5 | Fokus | Skor* |
|---|---|---|---|---|---|
| Denmark vs Norwegia | Observasi | Observasi | Observasi | Tidak ada | 1-1 |
| Wales vs Portugal | Portugal (Sedang) | Observasi | Observasi | 1X2 Portugal | 1-1 |
| Bosnia & Herzegovina vs Rumania | Observasi | Observasi | Observasi | Tidak ada | 1-1 |
| Hungaria vs Irlandia Utara | Observasi | Tidak (Sedang) | Under 2,5 (Sedang) | Total 2,5 Under 2,5 | 1-0 |
| Republik Irlandia vs Kosovo | Observasi | Tidak (Rendah) | Under 2,5 (Sedang) | Total 2,5 Under 2,5 | 1-0 |
| Israel vs Austria | Austria (Rendah) | Observasi | Under 2,5 (Rendah) | 1X2 Austria | 1-1 |
| Polandia vs Swedia | Observasi | Observasi | Observasi | Tidak ada | 1-1 |
| Ukraina vs Georgia | Observasi | Tidak (Rendah) | Under 2,5 (Sedang) | Total 2,5 Under 2,5 | 1-0 |

*Utama: skenario editorial. Beta: modus dari Poisson **mentah** resep 1X2, bukan skor hasil kalibrasi semua target. Modus 0-0 tidak menjamin seri. Pilihan aktif/8: 1X2 2, BTTS 3, Total 2,5 4.

## Klasemen dan motivasi yang terverifikasi

| Grup | Peringkat berdasarkan poin sebelum laga | Implikasi langsung |
|---|---|---|
| A4 | Portugal 12; Denmark 9; Norwegia 6; Wales 3 | Denmark cukup seri untuk dua besar; Norwegia harus menang. Portugal cukup seri untuk juara. |
| B2 | Irlandia Utara 11; Hungaria 10; Ukraina 4; Georgia 2 | Irlandia Utara cukup seri untuk juara; Hungaria harus menang. Ukraina cukup seri untuk posisi ketiga. |
| B3 | Austria 11; Kosovo 6; Republik Irlandia 5; Israel 3 | Austria sudah juara; Irlandia–Kosovo menentukan posisi kedua. Israel memerlukan kemenangan dan hasil lain. |
| B4 | Swedia 13; Bosnia & Herzegovina 8; Polandia 4; Rumania 3 | Swedia sudah juara dan Bosnia pasti kedua; Polandia/Rumania menentukan tempat ketiga. |

Aturan transisi 2028/29: posisi ketiga League B tetap di B, sedangkan posisi keempat masuk play-off B/C. Posisi kedua B masuk play-off A/B. Jangan memakai aturan degradasi dari edisi lama. [Aturan UEFA terkini](https://www.uefa.com/uefanationsleague/news/0298-1d6ef1acfaef-b54fcf1da859-1000--2026-27-uefa-nations-league-all-you-need-to-know/).

## Mutu data sebelum membaca tiap laga

Semua tim mempunyai lima laga kompetitif grup, dari 24/25 September sampai 14 November; usia laga tertua 53–54 hari saat cutoff. Empat laga September/Oktober dan laga November dibaca terpisah agar satu hasil terbaru tidak menutupi pola. Persahabatan tidak menggantikan lima laga kompetitif. Seluruh tim terakhir bermain 14 November waktu Eropa; tidak dihitung jumlah jam pemulihan persis karena seluruh timestamp kickoff historis belum diselaraskan.

Skor/hasil lima laga lengkap 5/5. Tembakan dan SoT berasal dari laporan UEFA dengan denominator pada setiap ringkasan. xG memakai **Opta melalui FotMob**, tersedia 1/5 untuk 14 tim dan 0/5 untuk Kosovo/Israel. xG/90 yang tersedia dari satu pertandingan bukan rata-rata form lima laga. Tidak ada pengisian nol untuk data hilang. Nilai xG tersebut adalah peluang historis, berbeda dari laju gol Poisson beta. Definisi rinci/versi model xG provider tidak dipublikasikan dalam tangkapan ini.

UEFA dan Opta berbeda dalam beberapa hitungan tembakan/penguasaan bola. Tabel mempertahankan tembakan UEFA dan memisahkan xG Opta; keduanya tidak dirata-ratakan. Tidak ada data lengkap serangan sayap, set piece, lokasi tembakan atau xG menit 76–90+ yang konsisten untuk lima laga. Pembacaan taktik di bawah berlabel hipotesis/inferensi. Tabel H2H memakai sampai lima pertemuan sejak 2014 dari korpus, dengan pertandingan terbaru 2026 dicocokkan ke UEFA; cakupan korpus tidak membuktikan semua pertemuan sepanjang sejarah tercakup.

## 1. Denmark vs Norwegia

Grup **A4**. Venue: **Parken, Kopenhagen**. [Identitas laga UEFA](https://www.uefa.com/uefanationsleague/match/2047919--denmark-vs-norway/matchinfo/). Semua waktu pada tabel riwayat berikut adalah **tanggal lokal pertandingan**, bukan tanggal WIB; H/A/N berarti kandang/tandang/netral. Skor ditulis dari perspektif tim pada judul tabel.

### Data: lima pertandingan kompetitif

**Denmark**

| Tanggal lokal | Lawan | Venue | Skor | Hasil | xG/xGA Opta | Shots/SoT UEFA | Penguasaan UEFA | Sumber |
|---|---|---|---|---|---|---|---|
| 2026-09-24 | Norwegia | A | 2-3 | L | N/A | 13/7 | 48% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2048005_FR.pdf) |
| 2026-09-27 | Wales | H | 2-0 | W | N/A | 20/3 | 60% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2047977_FR.pdf) |
| 2026-10-01 | Portugal | H | 2-4 | L | N/A | N/A | N/A | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/) |
| 2026-10-04 | Wales | A | 1-0 | W | N/A | 13/4 | 44% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2047930_FR.pdf) |
| 2026-11-14 | Portugal | A | 4-1 | W | 2.23/1.20 | 17/5 | 46% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2047892_FR.pdf); [xG](https://www.fotmob.com/en-GB/matches/denmark-vs-portugal/2a13rx) |

Ringkasan: **3W-0D-2L**, 1.80 poin/laga; GF 11, GA 8 (1.60/laga). Clean sheet 2/5; gagal mencetak gol 0/5; BTTS 3/5; Over 2,5 3/5. Shots 15.75 (4/5); SoT 4.75 (4/5). xG/xGA pada laga yang tersedia: 2.23 (1/5) / 1.20 (1/5). xGD berpasangan: +1.03 (1/5).

Pemisahan venue pada fase ini: H 2 laga, GF-GA 4-4; A 3 laga, GF-GA 7-4. Pembanding jangka panjang terukur tidak diterbitkan di acuan utama; model beta memakai jendela enam tahun sebagai sumber kekuatan terpisah.

**Norwegia**

| Tanggal lokal | Lawan | Venue | Skor | Hasil | xG/xGA Opta | Shots/SoT UEFA | Penguasaan UEFA | Sumber |
|---|---|---|---|---|---|---|---|
| 2026-09-24 | Denmark | H | 3-2 | W | N/A | 13/7 | 52% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2048005_FR.pdf) |
| 2026-09-27 | Portugal | H | 1-2 | L | N/A | 20/6 | 59% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2047978_FR.pdf) |
| 2026-10-01 | Wales | A | 1-2 | L | N/A | 12/4 | 52% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2047950_FR.pdf) |
| 2026-10-04 | Portugal | A | 1-2 | L | N/A | 9/3 | 42% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2047924_FR.pdf) |
| 2026-11-14 | Wales | H | 3-1 | W | 2.45/0.95 | 15/5 | 58% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2047893_FR.pdf); [xG](https://www.fotmob.com/en-GB/matches/wales-vs-norway/1oqabn) |

Ringkasan: **2W-0D-3L**, 1.20 poin/laga; GF 9, GA 9 (1.80/laga). Clean sheet 0/5; gagal mencetak gol 0/5; BTTS 5/5; Over 2,5 5/5. Shots 13.80 (5/5); SoT 5.00 (5/5). xG/xGA pada laga yang tersedia: 2.45 (1/5) / 0.95 (1/5). xGD berpasangan: +1.50 (1/5).

Pemisahan venue pada fase ini: H 3 laga, GF-GA 7-5; A 2 laga, GF-GA 2-4. Pembanding jangka panjang terukur tidak diterbitkan di acuan utama; model beta memakai jendela enam tahun sebagai sumber kekuatan terpisah.


### Data: H2H dan skuad

| Tanggal | Pertandingan dan skor 90 menit | Kompetisi | BTTS |
|---|---|---|---|
| 2024-06-08 | Denmark 3-1 Norwegia | Friendly | Ya |
| 2026-09-24 | Norwegia 3-2 Denmark | UEFA Nations League | Ya |

H2H lama dan friendly memiliki relevansi lebih rendah setelah pergantian skuad/pelatih. Penguasaan bola H2H di luar lima laga tidak tersedia; tidak diberi bobot numerik buatan.

**Fakta konteks:** Denmark memiliki 9 poin dan cukup menghindari kekalahan untuk menjaga posisi dua besar. Norwegia, 6 poin, harus menang; kemenangan juga memberi mereka keunggulan H2H atas Denmark. Portugal sudah mengumpulkan 12 poin. Kebutuhan Norwegia menyerang merupakan alasan skenario terbuka, bukan bukti bahwa mereka pasti mencetak gol.

**XI dan ketersediaan:** Perkiraan: Højlund ditopang Isaksen, Damsgaard dan Skov Olsen; Hjulmand–Højbjerg menjaga tengah. Norwegia diperkirakan tetap mengandalkan Haaland, Nusa dan Ødegaard. Ødegaard bermain setelah sakit sebelum laga Wales; kebugaran penuh untuk malam ini belum terkonfirmasi. Sports Mole memperkirakan Hermansen; Kristensen, Andersen, Nelsson, Mæhle; Højbjerg, Hjulmand; Isaksen, Damsgaard, Skov Olsen; Højlund. Norwegia: Selvik; Ryerson, Ajer, Heggem, Wolfe; Berg, Berge; Bobb, Ødegaard, Nusa; Haaland. Semua masih perkiraan; laporan absensi Denmark yang beredar belum seluruhnya terkonfirmasi melalui federasi.

Sumber skuad/konteks: [Sports Mole, perkiraan DEN–NOR](https://www.sportsmole.co.uk/football/denmark/preview/denmark-vs-norway-prediction-team-news-lineups_609154.html), [DBU, jadwal resmi](https://www.dbu.dk/landshold/herrelandshold/a-landsholdet/program/). Tanggal publikasi yang tepat tidak seluruhnya tersedia; waktu pengambilan dan status ketersediaan sumber dicatat dalam snapshot.

Perjalanan: seluruh tim berasal dari rangkaian laga 14 November. Lokasi laga sebelumnya tercatat di laporan pertandingan, tetapi rute aktual, waktu kedatangan, durasi penerbangan dan menit pemulihan klub belum terverifikasi. Tidak ditambahkan penalti kelelahan berbasis jarak tebakan.

### Pola: hasil, peluang dan BTTS

Norwegia mencetak gol dan kebobolan pada seluruh lima pertandingan grup. Dua clean sheet Denmark sama-sama datang melawan Wales sehingga tidak cukup untuk menyimpulkan pertahanannya aman menghadapi Haaland. Kemenangan 4-1 di Portugal didukung xG Opta 2,23 berbanding 1,20, tetapi empat gol aktual tetap lebih besar daripada kualitas peluang pada satu laga itu. Norway–Wales menghasilkan xG 2,45–0,95. Hipotesis: Norwegia yang wajib menang membuka ruang transisi untuk Højlund. Data kejadian untuk mengukur pressing, crossing dan set piece selama lima laga belum lengkap.

**Menit 76–90+:** Pada laga terakhir Norwegia, Brooks mencetak gol menit 79 dan Haaland menit 88. Ini bukti dua kejadian pada satu laga, bukan pola intensitas menit akhir selama lima pertandingan.

Clean sheet historis adalah frekuensi pada tabel. Sebagai diagnostik terpisah, Poisson **mentah** resep 1X2 menghasilkan P(clean sheet Denmark)=24,1% dan P(clean sheet Norwegia)=17,2%, dari laju gol 1.762 dan 1.421. Angka ini belum dikalibrasi sebagai clean sheet dan tidak boleh digabung dengan BTTS yang dikalibrasi terpisah untuk membentuk satu distribusi gabungan.

### Keputusan dua model

| Target | Utama | Keyakinan/status | Beta | Keyakinan/status |
|---|---|---|---|---|
| 1X2 | Denmark | Rendah / provisional | Observasi | N/A / observasi |
| BTTS | Ya | Sedang / provisional | Observasi | N/A / observasi |
| Total 2,5 | Over 2,5 | Sedang / provisional | Observasi | N/A / observasi |

**Probabilitas beta:** 1 36,3%, X 24,8%, 2 38,9% (pembulatan dijaga berjumlah 100,0%). BTTS Ya 52,1%; BTTS Tidak 47,9%. Over 2,5 54,3%; Under 45,7%. Probabilitas yang tipis tetap terlihat walau tidak menjadi pilihan aktif.

Fokus utama: **BTTS Ya**. Fokus beta: **tidak ada**. Skenario utama 2-1, alternatif 2-2.

**Skenario pembalik dan alasan observasi:** Denmark boleh bermain untuk seri; Norwegia memenangkan pertemuan pertama 3-2. Kelayakan BTTS berkurang jika salah satu penyerang utama tidak menjadi starter atau Denmark menurunkan blok yang sangat konservatif.

Pemeriksaan pasar: kutipan tiga operator melalui satu agregator ada pada lampiran; verifikasi independen langsung 0/3. Spread, kedalaman dan pembacaan T-30 belum tersedia. Tidak ada klaim anomali atau informasi internal. Kualitas data laga: skor kuat; statistik peluang/kejadian parsial; berita pemain bervariasi; XI belum resmi.

## 2. Wales vs Portugal

Grup **A4**. Venue: **Cardiff City Stadium, Cardiff**. [Identitas laga UEFA](https://www.uefa.com/uefanationsleague/match/2047920--wales-vs-portugal/matchinfo/). Semua waktu pada tabel riwayat berikut adalah **tanggal lokal pertandingan**, bukan tanggal WIB; H/A/N berarti kandang/tandang/netral. Skor ditulis dari perspektif tim pada judul tabel.

### Data: lima pertandingan kompetitif

**Wales**

| Tanggal lokal | Lawan | Venue | Skor | Hasil | xG/xGA Opta | Shots/SoT UEFA | Penguasaan UEFA | Sumber |
|---|---|---|---|---|---|---|---|
| 2026-09-24 | Portugal | A | 0-1 | L | N/A | 5/0 | 42% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2048002_FR.pdf) |
| 2026-09-27 | Denmark | A | 0-2 | L | N/A | 10/3 | 40% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2047977_FR.pdf) |
| 2026-10-01 | Norwegia | H | 2-1 | W | N/A | 12/6 | 48% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2047950_FR.pdf) |
| 2026-10-04 | Denmark | H | 0-1 | L | N/A | 5/1 | 56% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2047930_FR.pdf) |
| 2026-11-14 | Norwegia | A | 1-3 | L | 0.95/2.45 | 13/5 | 42% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2047893_FR.pdf); [xG](https://www.fotmob.com/en-GB/matches/wales-vs-norway/1oqabn) |

Ringkasan: **1W-0D-4L**, 0.60 poin/laga; GF 3, GA 8 (1.60/laga). Clean sheet 0/5; gagal mencetak gol 3/5; BTTS 2/5; Over 2,5 2/5. Shots 9.00 (5/5); SoT 3.00 (5/5). xG/xGA pada laga yang tersedia: 0.95 (1/5) / 2.45 (1/5). xGD berpasangan: -1.50 (1/5).

Pemisahan venue pada fase ini: H 2 laga, GF-GA 2-2; A 3 laga, GF-GA 1-6. Pembanding jangka panjang terukur tidak diterbitkan di acuan utama; model beta memakai jendela enam tahun sebagai sumber kekuatan terpisah.

**Portugal**

| Tanggal lokal | Lawan | Venue | Skor | Hasil | xG/xGA Opta | Shots/SoT UEFA | Penguasaan UEFA | Sumber |
|---|---|---|---|---|---|---|---|
| 2026-09-24 | Wales | H | 1-0 | W | N/A | 23/5 | 58% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2048002_FR.pdf) |
| 2026-09-27 | Norwegia | A | 2-1 | W | N/A | 11/4 | 41% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2047978_FR.pdf) |
| 2026-10-01 | Denmark | A | 4-2 | W | N/A | N/A | N/A | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/) |
| 2026-10-04 | Norwegia | H | 2-1 | W | N/A | 19/7 | 58% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2047924_FR.pdf) |
| 2026-11-14 | Denmark | H | 1-4 | L | 1.20/2.23 | 15/8 | 54% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2047892_FR.pdf); [xG](https://www.fotmob.com/en-GB/matches/denmark-vs-portugal/2a13rx) |

Ringkasan: **4W-0D-1L**, 2.40 poin/laga; GF 10, GA 8 (1.60/laga). Clean sheet 1/5; gagal mencetak gol 0/5; BTTS 4/5; Over 2,5 4/5. Shots 17.00 (4/5); SoT 6.00 (4/5). xG/xGA pada laga yang tersedia: 1.20 (1/5) / 2.23 (1/5). xGD berpasangan: -1.03 (1/5).

Pemisahan venue pada fase ini: H 3 laga, GF-GA 4-5; A 2 laga, GF-GA 6-3. Pembanding jangka panjang terukur tidak diterbitkan di acuan utama; model beta memakai jendela enam tahun sebagai sumber kekuatan terpisah.


### Data: H2H dan skuad

| Tanggal | Pertandingan dan skor 90 menit | Kompetisi | BTTS |
|---|---|---|---|
| 2016-07-06 | Portugal 2-0 Wales | UEFA Euro | Tidak |
| 2026-09-24 | Portugal 1-0 Wales | UEFA Nations League | Tidak |

H2H lama dan friendly memiliki relevansi lebih rendah setelah pergantian skuad/pelatih. Penguasaan bola H2H di luar lima laga tidak tersedia; tidak diberi bobot numerik buatan.

**Fakta konteks:** Portugal sudah lolos ke perempat final, tetapi hasil seri memastikan posisi pertama tanpa bergantung pada Denmark. Wales berada di posisi keempat dengan 3 poin dan tidak dapat mengejar dua besar. Mereka masih berkepentingan terhadap peringkat akhir dan hasil penutup di kandang, bukan sedang memperebutkan tiket perempat final.

**XI dan ketersediaan:** Wales: Ethan Ampadu terkena skorsing; Neco Williams dilaporkan cedera, dengan Roberts dan Sheehan sebagai opsi pengganti. Perkiraan: Darlow; Roberts, Rodon, Davies, Dasilva; Cullen, Sheehan; Johnson, Brooks, Wilson; Koumas. Portugal: Rúben Dias dan João Palhinha diskors; Bernardo Silva dinyatakan tidak fit dan dilepas dari pemusatan latihan menurut RTP yang mengutip FPF. António Silva dan João Neves merupakan opsi pengisi peran. Konflik sumber: perkiraan Sports Mole masih memasukkan Bernardo sebagai starter. Perkiraan itu tidak dipakai sebagai XI valid; pengganti di sektor serang Portugal belum ditetapkan dalam analisis ini.

Sumber skuad/konteks: [RTP, pelepasan Dias/Palhinha/Bernardo (15 November)](https://www.rtp.pt/noticias/selecao-nacional/dias-palhinha-e-bernardo-dispensados-do-estagio-de-portugal_d1779333), [FAW, skuad November](https://faw.cymru/news/cymru-squad-announced-for-norway-and-portugal/), [Sports Mole, perkiraan WAL–POR yang mengandung konflik Bernardo](https://www.sportsmole.co.uk/football/portugal/uefa-nations-league/preview/wales-vs-portugal-prediction-team-news-lineups_609143.html). Tanggal publikasi yang tepat tidak seluruhnya tersedia; waktu pengambilan dan status ketersediaan sumber dicatat dalam snapshot.

Perjalanan: seluruh tim berasal dari rangkaian laga 14 November. Lokasi laga sebelumnya tercatat di laporan pertandingan, tetapi rute aktual, waktu kedatangan, durasi penerbangan dan menit pemulihan klub belum terverifikasi. Tidak ditambahkan penalti kelelahan berbasis jarak tebakan.

### Pola: hasil, peluang dan BTTS

Portugal menang empat kali sebelum kalah 1-4 dari Denmark. Wales kalah empat dari lima laga grup dan hanya mencetak tiga gol. Hasil buruk Portugal tidak langsung membatalkan keunggulan kualitasnya, tetapi absensi di poros pertahanan dan gelandang serta kebutuhan hanya satu poin membuat target gol kurang jelas. Opta mencatat xG Portugal 1,20 saat kalah dari Denmark dan Wales 0,95 saat kalah di Norwegia. Arah Portugal masih didukung, sedangkan BTTS dan total ditahan sampai susunan serta pendekatan pertandingan lebih jelas.

**Menit 76–90+:** Gol Bernardo pada 90+3 saat melawan Denmark merupakan satu kejadian terakhir. Pemain itu absen sekarang; kejadian tersebut tidak dipindahkan menjadi proyeksi ancaman menit akhir yang sama.

Clean sheet historis adalah frekuensi pada tabel. Sebagai diagnostik terpisah, Poisson **mentah** resep 1X2 menghasilkan P(clean sheet Wales)=21,8% dan P(clean sheet Portugal)=32,2%, dari laju gol 1.134 dan 1.523. Angka ini belum dikalibrasi sebagai clean sheet dan tidak boleh digabung dengan BTTS yang dikalibrasi terpisah untuk membentuk satu distribusi gabungan.

### Keputusan dua model

| Target | Utama | Keyakinan/status | Beta | Keyakinan/status |
|---|---|---|---|---|
| 1X2 | Portugal | Sedang / provisional | Portugal | Sedang / provisional |
| BTTS | Observasi | N/A / observasi | Observasi | N/A / observasi |
| Total 2,5 | Observasi | N/A / observasi | Observasi | N/A / observasi |

**Probabilitas beta:** 1 10,7%, X 23,3%, 2 66,0% (pembulatan dijaga berjumlah 100,0%). BTTS Ya 46,9%; BTTS Tidak 53,1%. Over 2,5 45,5%; Under 54,5%. Probabilitas yang tipis tetap terlihat walau tidak menjadi pilihan aktif.

Fokus utama: **1X2 Portugal**. Fokus beta: **1X2 Portugal**. Skenario utama 0-2, alternatif 1-2.

**Skenario pembalik dan alasan observasi:** Rotasi Portugal, hilangnya Dias/Palhinha dan kemampuan Harry Wilson menciptakan peluang dapat mengubah skenario clean sheet. Konfirmasi Bernardo absen adalah koreksi terhadap sumber perkiraan, bukan alasan membuat probabilitas baru tanpa model.

Pemeriksaan pasar: kutipan tiga operator melalui satu agregator ada pada lampiran; verifikasi independen langsung 0/3. Spread, kedalaman dan pembacaan T-30 belum tersedia. Tidak ada klaim anomali atau informasi internal. Kualitas data laga: skor kuat; statistik peluang/kejadian parsial; berita pemain bervariasi; XI belum resmi.

## 3. Bosnia & Herzegovina vs Rumania

Grup **B4**. Venue: **Bilino Polje, Zenica**. [Identitas laga UEFA](https://www.uefa.com/uefanationsleague/match/2047917--bosnia-and-herzegovina-vs-romania/matchinfo/). Semua waktu pada tabel riwayat berikut adalah **tanggal lokal pertandingan**, bukan tanggal WIB; H/A/N berarti kandang/tandang/netral. Skor ditulis dari perspektif tim pada judul tabel.

### Data: lima pertandingan kompetitif

**Bosnia & Herzegovina**

| Tanggal lokal | Lawan | Venue | Skor | Hasil | xG/xGA Opta | Shots/SoT UEFA | Penguasaan UEFA | Sumber |
|---|---|---|---|---|---|---|---|
| 2026-09-25 | Polandia | A | 0-0 | D | N/A | N/A | N/A | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/) |
| 2026-09-28 | Rumania | A | 4-2 | W | N/A | 15/7 | 47% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2047984_FR.pdf) |
| 2026-10-02 | Swedia | H | 1-1 | D | N/A | N/A | N/A | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/) |
| 2026-10-05 | Polandia | H | 1-0 | W | N/A | 9/1 | 48% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2047939_FR.pdf) |
| 2026-11-14 | Swedia | A | 2-3 | L | 1.19/2.27 | 17/7 | 56% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2047890_FR.pdf); [xG](https://www.fotmob.com/matches/sweden-vs-bosnia-herzegovina/2vabe3) |

Ringkasan: **2W-2D-1L**, 1.60 poin/laga; GF 8, GA 6 (1.20/laga). Clean sheet 2/5; gagal mencetak gol 1/5; BTTS 3/5; Over 2,5 2/5. Shots 13.67 (3/5); SoT 5.00 (3/5). xG/xGA pada laga yang tersedia: 1.19 (1/5) / 2.27 (1/5). xGD berpasangan: -1.08 (1/5).

Pemisahan venue pada fase ini: H 2 laga, GF-GA 2-1; A 3 laga, GF-GA 6-5. Pembanding jangka panjang terukur tidak diterbitkan di acuan utama; model beta memakai jendela enam tahun sebagai sumber kekuatan terpisah.

**Rumania**

| Tanggal lokal | Lawan | Venue | Skor | Hasil | xG/xGA Opta | Shots/SoT UEFA | Penguasaan UEFA | Sumber |
|---|---|---|---|---|---|---|---|
| 2026-09-25 | Swedia | A | 1-2 | L | N/A | 10/1 | 43% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2048015_FR.pdf) |
| 2026-09-28 | Bosnia & Herzegovina | H | 2-4 | L | N/A | 13/4 | 53% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2047984_FR.pdf) |
| 2026-10-02 | Polandia | A | 0-6 | L | N/A | 10/3 | 37% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2047963_FR.pdf) |
| 2026-10-05 | Swedia | H | 0-1 | L | N/A | N/A | N/A | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/) |
| 2026-11-14 | Polandia | H | 2-1 | W | 0.99/1.56 | N/A | N/A | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [xG](https://www.fotmob.com/matches/poland-vs-romania/2rojpt) |

Ringkasan: **1W-0D-4L**, 0.60 poin/laga; GF 5, GA 14 (2.80/laga). Clean sheet 0/5; gagal mencetak gol 2/5; BTTS 3/5; Over 2,5 4/5. Shots 11.00 (3/5); SoT 2.67 (3/5). xG/xGA pada laga yang tersedia: 0.99 (1/5) / 1.56 (1/5). xGD berpasangan: -0.57 (1/5).

Pemisahan venue pada fase ini: H 3 laga, GF-GA 4-6; A 2 laga, GF-GA 1-8. Pembanding jangka panjang terukur tidak diterbitkan di acuan utama; model beta memakai jendela enam tahun sebagai sumber kekuatan terpisah.


### Data: H2H dan skuad

| Tanggal | Pertandingan dan skor 90 menit | Kompetisi | BTTS |
|---|---|---|---|
| 2022-06-07 | Bosnia & Herzegovina 1-0 Rumania | UEFA Nations League | Tidak |
| 2022-09-26 | Rumania 4-1 Bosnia & Herzegovina | UEFA Nations League | Ya |
| 2025-03-21 | Rumania 0-1 Bosnia & Herzegovina | FIFA World Cup qualification | Tidak |
| 2025-11-15 | Bosnia & Herzegovina 3-1 Rumania | FIFA World Cup qualification | Ya |
| 2026-09-28 | Rumania 2-4 Bosnia & Herzegovina | UEFA Nations League | Ya |

H2H lama dan friendly memiliki relevansi lebih rendah setelah pergantian skuad/pelatih. Penguasaan bola H2H di luar lima laga tidak tersedia; tidak diberi bobot numerik buatan.

**Fakta konteks:** Swedia 13 poin, Bosnia 8, Polandia 4 dan Rumania 3. Bosnia sudah memastikan posisi kedua dan tidak dapat mengejar Swedia; intensitas serta rotasi perlu diperhatikan. Rumania membutuhkan hasil lebih baik untuk melewati Polandia dan menghindari posisi terakhir. Posisi keempat League B masuk play-off B/C, bukan otomatis turun langsung pada format transisi ini.

**XI dan ketersediaan:** Federasi Bosnia mengonfirmasi persiapan terakhir untuk laga di Zenica. Demirović dan Alajbegović merupakan titik serang yang perlu diperiksa di XI. FRF menyatakan Nicolae Stanciu dan Valentin Mihăilă tidak tersedia karena masalah otot; Rareș Ilie dipanggil sebagai pengganti. Laporan sekunder menyebut keraguan Tabaković dan skorsing Băluță, tetapi verifikasi primer untuk kedua status itu belum lengkap. Karena itu XI penuh tidak diterbitkan sebagai susunan pasti.

Sumber skuad/konteks: [NFSBiH, persiapan resmi](https://www.nfsbih.ba/en/news/football-m/a-national-team-m/dragons-ready-for-match-against-romania/), [FRF, skuad dan absensi](https://www.frf.ro/nationale/masculin/echipa-nationala/lotul-romaniei-pentru-meciurile-cu-polonia-si-bosnia-hertegovina/), [NFSBiH, venue dan kickoff](https://www.nfsbih.ba/en/news/football-m/a-national-team-m/ticket-information-for-match-against-romania/). Tanggal publikasi yang tepat tidak seluruhnya tersedia; waktu pengambilan dan status ketersediaan sumber dicatat dalam snapshot.

Perjalanan: seluruh tim berasal dari rangkaian laga 14 November. Lokasi laga sebelumnya tercatat di laporan pertandingan, tetapi rute aktual, waktu kedatangan, durasi penerbangan dan menit pemulihan klub belum terverifikasi. Tidak ditambahkan penalti kelelahan berbasis jarak tebakan.

### Pola: hasil, peluang dan BTTS

Pertemuan pertama menghasilkan kemenangan Bosnia 4-2. Bosnia juga mencetak dua gol saat kalah 2-3 di Swedia, meski xG Opta hanya 1,19 melawan 2,27. Pertahanan Bosnia belum aman, sementara Rumania harus mencari gol. Keuntungan kandang dan form grup mendukung Bosnia secara tipis; motivasi serta risiko rotasi menahan keyakinan 1X2. BTTS lebih didukung daripada memilih pemenang dengan keyakinan tinggi. Skor 4-2 H2H tidak menjadi jaminan enam gol kembali terjadi.

**Menit 76–90+:** Rumania mencetak gol menit 68 dan 72 melawan Polandia, lalu kebobolan menit 82. Tidak ada gol sesudah menit 75 pada laga Swedia–Bosnia terakhir. Cakupan kejadian ini hanya laga terakhir masing-masing.

Clean sheet historis adalah frekuensi pada tabel. Sebagai diagnostik terpisah, Poisson **mentah** resep 1X2 menghasilkan P(clean sheet Bosnia & Herzegovina)=32,0% dan P(clean sheet Rumania)=24,2%, dari laju gol 1.421 dan 1.140. Angka ini belum dikalibrasi sebagai clean sheet dan tidak boleh digabung dengan BTTS yang dikalibrasi terpisah untuk membentuk satu distribusi gabungan.

### Keputusan dua model

| Target | Utama | Keyakinan/status | Beta | Keyakinan/status |
|---|---|---|---|---|
| 1X2 | Bosnia & Herzegovina | Rendah / provisional | Observasi | N/A / observasi |
| BTTS | Ya | Sedang / provisional | Observasi | N/A / observasi |
| Total 2,5 | Over 2,5 | Rendah / provisional | Observasi | N/A / observasi |

**Probabilitas beta:** 1 32,3%, X 31,6%, 2 36,1% (pembulatan dijaga berjumlah 100,0%). BTTS Ya 46,2%; BTTS Tidak 53,8%. Over 2,5 46,9%; Under 53,1%. Probabilitas yang tipis tetap terlihat walau tidak menjadi pilihan aktif.

Fokus utama: **BTTS Ya**. Fokus beta: **tidak ada**. Skenario utama 2-1, alternatif 1-1.

**Skenario pembalik dan alasan observasi:** Rotasi besar Bosnia atau absennya penyerang utama dapat menurunkan dukungan BTTS dan Over. Rumania memiliki hasil terkini yang lebih baik daripada empat kekalahan sebelumnya, sehingga arah kandang tetap berkeyakinan rendah.

Pemeriksaan pasar: kutipan tiga operator melalui satu agregator ada pada lampiran; verifikasi independen langsung 0/3. Spread, kedalaman dan pembacaan T-30 belum tersedia. Tidak ada klaim anomali atau informasi internal. Kualitas data laga: skor kuat; statistik peluang/kejadian parsial; berita pemain bervariasi; XI belum resmi.

## 4. Hungaria vs Irlandia Utara

Grup **B2**. Venue: **Puskás Aréna, Budapest**. [Identitas laga UEFA](https://www.uefa.com/uefanationsleague/match/2047921--hungary-vs-northern-ireland/matchinfo/). Semua waktu pada tabel riwayat berikut adalah **tanggal lokal pertandingan**, bukan tanggal WIB; H/A/N berarti kandang/tandang/netral. Skor ditulis dari perspektif tim pada judul tabel.

### Data: lima pertandingan kompetitif

**Hungaria**

| Tanggal lokal | Lawan | Venue | Skor | Hasil | xG/xGA Opta | Shots/SoT UEFA | Penguasaan UEFA | Sumber |
|---|---|---|---|---|---|---|---|
| 2026-09-25 | Ukraina | H | 0-1 | L | N/A | 14/4 | 54% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2048012_FR.pdf) |
| 2026-09-28 | Irlandia Utara | A | 0-0 | D | N/A | N/A | N/A | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/) |
| 2026-10-02 | Georgia | H | 1-0 | W | N/A | N/A | N/A | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/) |
| 2026-10-05 | Ukraina | N | 2-1 | W | N/A | 10/4 | 48% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2047932_FR.pdf) |
| 2026-11-14 | Georgia | A | 2-0 | W | 1.89/0.67 | 11/5 | 47% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2047895_FR.pdf); [xG](https://www.fotmob.com/matches/georgia-vs-hungary/2ccy6u) |

Ringkasan: **3W-1D-1L**, 2.00 poin/laga; GF 5, GA 2 (0.40/laga). Clean sheet 3/5; gagal mencetak gol 2/5; BTTS 1/5; Over 2,5 1/5. Shots 11.67 (3/5); SoT 4.33 (3/5). xG/xGA pada laga yang tersedia: 1.89 (1/5) / 0.67 (1/5). xGD berpasangan: +1.22 (1/5).

Pemisahan venue pada fase ini: H 2 laga, GF-GA 1-1; A 2 laga, GF-GA 2-0; N 1 laga, GF-GA 2-1. Pembanding jangka panjang terukur tidak diterbitkan di acuan utama; model beta memakai jendela enam tahun sebagai sumber kekuatan terpisah.

**Irlandia Utara**

| Tanggal lokal | Lawan | Venue | Skor | Hasil | xG/xGA Opta | Shots/SoT UEFA | Penguasaan UEFA | Sumber |
|---|---|---|---|---|---|---|---|
| 2026-09-25 | Georgia | A | 1-0 | W | N/A | 12/5 | 39% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2048014_FR.pdf) |
| 2026-09-28 | Hungaria | H | 0-0 | D | N/A | N/A | N/A | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/) |
| 2026-10-02 | Ukraina | N | 3-0 | W | N/A | 11/3 | 35% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2047959_FR.pdf) |
| 2026-10-05 | Georgia | H | 0-0 | D | N/A | N/A | N/A | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/) |
| 2026-11-14 | Ukraina | H | 1-0 | W | 1.59/0.75 | 14/5 | 38% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2047897_FR.pdf); [xG](https://www.fotmob.com/en-GB/matches/ukraine-vs-northern-ireland/2dt35j) |

Ringkasan: **3W-2D-0L**, 2.20 poin/laga; GF 5, GA 0 (0.00/laga). Clean sheet 5/5; gagal mencetak gol 2/5; BTTS 0/5; Over 2,5 1/5. Shots 12.33 (3/5); SoT 4.33 (3/5). xG/xGA pada laga yang tersedia: 1.59 (1/5) / 0.75 (1/5). xGD berpasangan: +0.84 (1/5).

Pemisahan venue pada fase ini: H 3 laga, GF-GA 1-0; A 1 laga, GF-GA 1-0; N 1 laga, GF-GA 3-0. Pembanding jangka panjang terukur tidak diterbitkan di acuan utama; model beta memakai jendela enam tahun sebagai sumber kekuatan terpisah.


### Data: H2H dan skuad

| Tanggal | Pertandingan dan skor 90 menit | Kompetisi | BTTS |
|---|---|---|---|
| 2014-09-07 | Hungaria 1-2 Irlandia Utara | UEFA Euro qualification | Ya |
| 2015-09-07 | Irlandia Utara 1-1 Hungaria | UEFA Euro qualification | Ya |
| 2022-03-29 | Irlandia Utara 0-1 Hungaria | Friendly | Tidak |
| 2026-09-28 | Irlandia Utara 0-0 Hungaria | UEFA Nations League | Tidak |

H2H lama dan friendly memiliki relevansi lebih rendah setelah pergantian skuad/pelatih. Penguasaan bola H2H di luar lima laga tidak tersedia; tidak diberi bobot numerik buatan.

**Fakta konteks:** Irlandia Utara memimpin dengan 11 poin, Hungaria 10. Tim tamu cukup seri untuk promosi otomatis; Hungaria harus menang untuk menjadi juara grup. Skenario ini memberi alasan untuk permainan terukur dari tim tamu. Keperluan menang Hungaria tidak otomatis menghapus ketahanan lawan.

**XI dan ketersediaan:** Irish FA mengonfirmasi Jamie Donley diskors dan Michael O’Neill menjalani larangan mendampingi dari tepi lapangan; staf tetap menyiapkan taktik. Seluruh pemain lain dalam skuad yang tersisa dinyatakan tersedia oleh pelatih. Magennis merupakan opsi pengganti Donley. Sports Mole melaporkan skorsing Willi Orbán dan Milan Vitalis pada Hungaria serta kondisi Szoboszlai yang masih perlu dicermati. Varga sudah kembali dan mencetak gol di Georgia. Perkiraan Hungaria: B. Tóth; Osváth, Szalai, Csinger, Kerkez; R. Tóth, Schäfer; Sallai, Szoboszlai, Nagy; Varga. Semua perkiraan belum resmi.

Sumber skuad/konteks: [Irish FA, konferensi prapertandingan (16 November)](https://www.irishfa.com/news/2026/november/o-neill-wants-players-to-show-spirit-and-conviction-against-hungary), [Sports Mole, status Hungaria](https://www.sportsmole.co.uk/football/hungary/nations-league-predictions/preview/hungary-vs-n-ireland-prediction-team-news-lineups_609115.html). Tanggal publikasi yang tepat tidak seluruhnya tersedia; waktu pengambilan dan status ketersediaan sumber dicatat dalam snapshot.

Perjalanan: seluruh tim berasal dari rangkaian laga 14 November. Lokasi laga sebelumnya tercatat di laporan pertandingan, tetapi rute aktual, waktu kedatangan, durasi penerbangan dan menit pemulihan klub belum terverifikasi. Tidak ditambahkan penalti kelelahan berbasis jarak tebakan.

### Pola: hasil, peluang dan BTTS

Irlandia Utara menjaga clean sheet dalam kelima pertandingan grup. Hungaria dan Irlandia Utara masing-masing memiliki empat Under 2,5 dari lima laga; kemenangan Irlandia Utara 3-0 atas Ukraina tetap termasuk Over. Pertemuan bersama 0-0 adalah observasi yang tumpang tindih, bukan dua bukti independen. Varga menambah ancaman Hungaria, tetapi Donley absen dan tim tamu tidak harus mengejar kemenangan. Pemenang ditahan. Fokus utama Under 2,5, dengan BTTS Tidak sebagai target terpisah.

**Menit 76–90+:** Varga mencetak gol menit 85 di Georgia, sedangkan gol kemenangan Irlandia Utara atas Ukraina terjadi menit 68. Gol akhir Hungaria menunjukkan risiko Under tetap ada apabila mereka terlambat memperoleh keunggulan.

Clean sheet historis adalah frekuensi pada tabel. Sebagai diagnostik terpisah, Poisson **mentah** resep 1X2 menghasilkan P(clean sheet Hungaria)=42,6% dan P(clean sheet Irlandia Utara)=31,8%, dari laju gol 1.147 dan 0.853. Angka ini belum dikalibrasi sebagai clean sheet dan tidak boleh digabung dengan BTTS yang dikalibrasi terpisah untuk membentuk satu distribusi gabungan.

### Keputusan dua model

| Target | Utama | Keyakinan/status | Beta | Keyakinan/status |
|---|---|---|---|---|
| 1X2 | Observasi | N/A / observasi | Observasi | N/A / observasi |
| BTTS | Tidak | Sedang / provisional | Tidak | Sedang / provisional |
| Total 2,5 | Under 2,5 | Cukup kuat / provisional | Under 2,5 | Sedang / provisional |

**Probabilitas beta:** 1 30,2%, X 41,3%, 2 28,5% (pembulatan dijaga berjumlah 100,0%). BTTS Ya 39,8%; BTTS Tidak 60,2%. Over 2,5 35,6%; Under 64,4%. Probabilitas yang tipis tetap terlihat walau tidak menjadi pilihan aktif.

Fokus utama: **Total 2,5 Under 2,5**. Fokus beta: **Total 2,5 Under 2,5**. Skenario utama 1-0, alternatif 0-0.

**Skenario pembalik dan alasan observasi:** Gol cepat, kartu merah, atau Hungaria yang tertinggal dapat mengubah ritme. Orbán absen melemahkan argumen clean sheet Hungaria, sehingga BTTS Tidak tidak diberi tingkat keyakinan yang sama dengan Under.

Pemeriksaan pasar: kutipan tiga operator melalui satu agregator ada pada lampiran; verifikasi independen langsung 0/3. Spread, kedalaman dan pembacaan T-30 belum tersedia. Tidak ada klaim anomali atau informasi internal. Kualitas data laga: skor kuat; statistik peluang/kejadian parsial; berita pemain bervariasi; XI belum resmi.

## 5. Republik Irlandia vs Kosovo

Grup **B3**. Venue: **Aviva Stadium, Dublin**. [Identitas laga UEFA](https://www.uefa.com/uefanationsleague/match/2047923--republic-of-ireland-vs-kosovo/matchinfo/). Semua waktu pada tabel riwayat berikut adalah **tanggal lokal pertandingan**, bukan tanggal WIB; H/A/N berarti kandang/tandang/netral. Skor ditulis dari perspektif tim pada judul tabel.

### Data: lima pertandingan kompetitif

**Republik Irlandia**

| Tanggal lokal | Lawan | Venue | Skor | Hasil | xG/xGA Opta | Shots/SoT UEFA | Penguasaan UEFA | Sumber |
|---|---|---|---|---|---|---|---|
| 2026-09-24 | Kosovo | A | 0-1 | L | N/A | 3/1 | 47% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2048007_FR.pdf) |
| 2026-09-27 | Israel | N | 3-0 | W | N/A | N/A | N/A | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/) |
| 2026-10-01 | Austria | H | 2-2 | D | N/A | N/A | N/A | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/) |
| 2026-10-04 | Israel | N | 1-1 | D | N/A | 15/4 | 55% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2047929_FR.pdf) |
| 2026-11-14 | Austria | A | 0-1 | L | 1.09/2.15 | N/A | N/A | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [xG](https://www.fotmob.com/en-GB/matches/ireland-vs-austria/1mqmsw) |

Ringkasan: **1W-2D-2L**, 1.00 poin/laga; GF 6, GA 5 (1.00/laga). Clean sheet 1/5; gagal mencetak gol 2/5; BTTS 2/5; Over 2,5 2/5. Shots 9.00 (2/5); SoT 2.50 (2/5). xG/xGA pada laga yang tersedia: 1.09 (1/5) / 2.15 (1/5). xGD berpasangan: -1.06 (1/5).

Pemisahan venue pada fase ini: H 1 laga, GF-GA 2-2; A 2 laga, GF-GA 0-2; N 2 laga, GF-GA 4-1. Pembanding jangka panjang terukur tidak diterbitkan di acuan utama; model beta memakai jendela enam tahun sebagai sumber kekuatan terpisah.

**Kosovo**

| Tanggal lokal | Lawan | Venue | Skor | Hasil | xG/xGA Opta | Shots/SoT UEFA | Penguasaan UEFA | Sumber |
|---|---|---|---|---|---|---|---|
| 2026-09-24 | Republik Irlandia | H | 1-0 | W | N/A | 22/6 | 53% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2048007_FR.pdf) |
| 2026-09-27 | Austria | A | 1-3 | L | N/A | N/A | N/A | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/) |
| 2026-10-01 | Israel | N | 0-0 | D | N/A | 18/3 | 53% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2047952_FR.pdf) |
| 2026-10-04 | Austria | H | 1-1 | D | N/A | N/A | N/A | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/) |
| 2026-11-14 | Israel | H | 0-0 | D | N/A | 16/3 | 47% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2047896_FR.pdf) |

Ringkasan: **1W-3D-1L**, 1.20 poin/laga; GF 3, GA 4 (0.80/laga). Clean sheet 3/5; gagal mencetak gol 2/5; BTTS 2/5; Over 2,5 1/5. Shots 18.67 (3/5); SoT 4.00 (3/5). xG/xGA pada laga yang tersedia: N/A (0/5) / N/A (0/5). xGD berpasangan: N/A.

Pemisahan venue pada fase ini: H 3 laga, GF-GA 2-1; A 1 laga, GF-GA 1-3; N 1 laga, GF-GA 0-0. Pembanding jangka panjang terukur tidak diterbitkan di acuan utama; model beta memakai jendela enam tahun sebagai sumber kekuatan terpisah.


### Data: H2H dan skuad

| Tanggal | Pertandingan dan skor 90 menit | Kompetisi | BTTS |
|---|---|---|---|
| 2026-09-24 | Kosovo 1-0 Republik Irlandia | UEFA Nations League | Tidak |

H2H lama dan friendly memiliki relevansi lebih rendah setelah pergantian skuad/pelatih. Penguasaan bola H2H di luar lima laga tidak tersedia; tidak diberi bobot numerik buatan.

**Fakta konteks:** Kosovo 6 poin dan Republik Irlandia 5. Irlandia harus menang untuk merebut posisi kedua; seri mempertahankan Kosovo di atasnya. Irlandia tidak boleh diasumsikan nyaman dengan hasil seri hanya karena distribusi skor mendukung pertandingan sedikit gol.

**XI dan ketersediaan:** FAI mengonfirmasi Nathan Collins kembali ke klub untuk pemeriksaan dan pemulihan setelah cedera melawan Austria. Jimmy Dunne menggantikannya di skuad pertandingan; Abankwah pulih dari kram. Peran Collins di udara dan pengorganisasian pertahanan perlu dibaca terhadap ancaman Vedat Muriqi. Hodža menerima kartu merah pada laga Kosovo–Israel dan menjadi isu skorsing untuk susunan Kosovo. Pilihan pengganti di lini tengah dan susunan sebelas lengkap belum diverifikasi sebagai XI resmi.

Sumber skuad/konteks: [FAI, preview dan pembaruan cedera](https://www.fai.ie/latest/match-preview-mnt-republic-ireland-v-kosovo/), [UEFA, kartu merah Kosovo–Israel](https://www.uefa.com/newsfiles/UNL/2027/2047896_FR.pdf). Tanggal publikasi yang tepat tidak seluruhnya tersedia; waktu pengambilan dan status ketersediaan sumber dicatat dalam snapshot.

Perjalanan: seluruh tim berasal dari rangkaian laga 14 November. Lokasi laga sebelumnya tercatat di laporan pertandingan, tetapi rute aktual, waktu kedatangan, durasi penerbangan dan menit pemulihan klub belum terverifikasi. Tidak ditambahkan penalti kelelahan berbasis jarak tebakan.

### Pola: hasil, peluang dan BTTS

Kosovo hanya mencetak tiga gol dalam lima laga grup dan tiga laga terakhir mereka menghasilkan 0-0, 1-1 dan 0-0. Dalam laga terakhir mereka melepaskan 16 tembakan tetapi hanya tiga tepat sasaran menurut UEFA; tekanan itu tidak sama dengan kualitas peluang tinggi. Irlandia mencatat xG Opta 1,09 di Austria tanpa mencetak gol. Under dan BTTS Tidak memiliki dukungan, tetapi absennya Collins membuat peluang gol Kosovo tidak boleh diabaikan. Keunggulan kandang Irlandia belum cukup untuk menerbitkan pilihan 1X2.

**Menit 76–90+:** Gol penentu Austria melawan Irlandia tercatat menit 79 pada FotMob. Kosovo–Israel berakhir tanpa gol; kartu merah Hodža terjadi pada paruh kedua. Ini mendukung pemeriksaan susunan, bukan klaim tren late goal universal.

Clean sheet historis adalah frekuensi pada tabel. Sebagai diagnostik terpisah, Poisson **mentah** resep 1X2 menghasilkan P(clean sheet Republik Irlandia)=40,5% dan P(clean sheet Kosovo)=31,2%, dari laju gol 1.164 dan 0.904. Angka ini belum dikalibrasi sebagai clean sheet dan tidak boleh digabung dengan BTTS yang dikalibrasi terpisah untuk membentuk satu distribusi gabungan.

### Keputusan dua model

| Target | Utama | Keyakinan/status | Beta | Keyakinan/status |
|---|---|---|---|---|
| 1X2 | Observasi | N/A / observasi | Observasi | N/A / observasi |
| BTTS | Tidak | Sedang / provisional | Tidak | Rendah / provisional |
| Total 2,5 | Under 2,5 | Sedang / provisional | Under 2,5 | Sedang / provisional |

**Probabilitas beta:** 1 29,1%, X 39,9%, 2 31,0% (pembulatan dijaga berjumlah 100,0%). BTTS Ya 40,7%; BTTS Tidak 59,3%. Over 2,5 38,7%; Under 61,3%. Probabilitas yang tipis tetap terlihat walau tidak menjadi pilihan aktif.

Fokus utama: **Total 2,5 Under 2,5**. Fokus beta: **Total 2,5 Under 2,5**. Skenario utama 1-0, alternatif 0-0.

**Skenario pembalik dan alasan observasi:** Gol awal Kosovo memaksa Irlandia membuka permainan. Pengganti Collins dan kualitas duel udara terhadap Muriqi merupakan pemicu utama untuk menilai ulang BTTS/Under.

Pemeriksaan pasar: kutipan tiga operator melalui satu agregator ada pada lampiran; verifikasi independen langsung 0/3. Spread, kedalaman dan pembacaan T-30 belum tersedia. Tidak ada klaim anomali atau informasi internal. Kualitas data laga: skor kuat; statistik peluang/kejadian parsial; berita pemain bervariasi; XI belum resmi.

## 6. Israel vs Austria

Grup **B3**. Venue: **Nagyerdei Stadion, Debrecen (netral)**. [Identitas laga UEFA](https://www.uefa.com/uefanationsleague/match/2047916--israel-vs-austria/matchinfo/). Semua waktu pada tabel riwayat berikut adalah **tanggal lokal pertandingan**, bukan tanggal WIB; H/A/N berarti kandang/tandang/netral. Skor ditulis dari perspektif tim pada judul tabel.

### Data: lima pertandingan kompetitif

**Israel**

| Tanggal lokal | Lawan | Venue | Skor | Hasil | xG/xGA Opta | Shots/SoT UEFA | Penguasaan UEFA | Sumber |
|---|---|---|---|---|---|---|---|
| 2026-09-24 | Austria | A | 1-3 | L | N/A | 5/1 | 54% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2048006_FR.pdf) |
| 2026-09-27 | Republik Irlandia | N | 0-3 | L | N/A | N/A | N/A | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/) |
| 2026-10-01 | Kosovo | N | 0-0 | D | N/A | 10/3 | 47% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2047952_FR.pdf) |
| 2026-10-04 | Republik Irlandia | N | 1-1 | D | N/A | 10/2 | 45% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2047929_FR.pdf) |
| 2026-11-14 | Kosovo | A | 0-0 | D | N/A | 6/3 | 53% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2047896_FR.pdf) |

Ringkasan: **0W-3D-2L**, 0.60 poin/laga; GF 2, GA 7 (1.40/laga). Clean sheet 2/5; gagal mencetak gol 3/5; BTTS 2/5; Over 2,5 2/5. Shots 7.75 (4/5); SoT 2.25 (4/5). xG/xGA pada laga yang tersedia: N/A (0/5) / N/A (0/5). xGD berpasangan: N/A.

Pemisahan venue pada fase ini: A 2 laga, GF-GA 1-3; N 3 laga, GF-GA 1-4. Pembanding jangka panjang terukur tidak diterbitkan di acuan utama; model beta memakai jendela enam tahun sebagai sumber kekuatan terpisah.

**Austria**

| Tanggal lokal | Lawan | Venue | Skor | Hasil | xG/xGA Opta | Shots/SoT UEFA | Penguasaan UEFA | Sumber |
|---|---|---|---|---|---|---|---|
| 2026-09-24 | Israel | H | 3-1 | W | N/A | 18/9 | 46% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2048006_FR.pdf) |
| 2026-09-27 | Kosovo | H | 3-1 | W | N/A | N/A | N/A | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/) |
| 2026-10-01 | Republik Irlandia | A | 2-2 | D | N/A | N/A | N/A | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/) |
| 2026-10-04 | Kosovo | A | 1-1 | D | N/A | N/A | N/A | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/) |
| 2026-11-14 | Republik Irlandia | H | 1-0 | W | 2.15/1.09 | N/A | N/A | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [xG](https://www.fotmob.com/en-GB/matches/ireland-vs-austria/1mqmsw) |

Ringkasan: **3W-2D-0L**, 2.20 poin/laga; GF 10, GA 5 (1.00/laga). Clean sheet 1/5; gagal mencetak gol 0/5; BTTS 4/5; Over 2,5 3/5. Shots 18.00 (1/5); SoT 9.00 (1/5). xG/xGA pada laga yang tersedia: 2.15 (1/5) / 1.09 (1/5). xGD berpasangan: +1.06 (1/5).

Pemisahan venue pada fase ini: H 3 laga, GF-GA 7-2; A 2 laga, GF-GA 3-3. Pembanding jangka panjang terukur tidak diterbitkan di acuan utama; model beta memakai jendela enam tahun sebagai sumber kekuatan terpisah.


### Data: H2H dan skuad

| Tanggal | Pertandingan dan skor 90 menit | Kompetisi | BTTS |
|---|---|---|---|
| 2019-03-24 | Israel 4-2 Austria | UEFA Euro qualification | Ya |
| 2019-10-10 | Austria 3-1 Israel | UEFA Euro qualification | Ya |
| 2021-09-04 | Israel 5-2 Austria | FIFA World Cup qualification | Ya |
| 2021-11-12 | Austria 4-2 Israel | FIFA World Cup qualification | Ya |
| 2026-09-24 | Austria 3-1 Israel | UEFA Nations League | Ya |

H2H lama dan friendly memiliki relevansi lebih rendah setelah pergantian skuad/pelatih. Penguasaan bola H2H di luar lima laga tidak tersedia; tidak diberi bobot numerik buatan.

**Fakta konteks:** Austria sudah memastikan juara grup dengan 11 poin; Kosovo maksimal hanya dapat mencapai 9. Israel memiliki 3 poin dan membutuhkan kemenangan serta hasil lain yang sesuai untuk keluar dari posisi terakhir. Laga dimainkan di Debrecen, Hungaria, sehingga tidak diberi efek kandang Israel dalam perhitungan beta.

**XI dan ketersediaan:** Rangnick, dalam laporan LAOLA1 yang mengutip konferensi pers, menyebut debut Lukas Jungwirth dan peluang bermain Weinhandl serta Spalt. Alexander Prass, Xaver Schlager, Yusuf Demir dan Romano Schmid sudah meninggalkan pemusatan latihan dengan alasan yang dilaporkan berbeda. Laporan ini lebih baru dan spesifik daripada perkiraan daring yang masih memasukkan Demir. Rincian XI Israel belum terverifikasi secara memadai. Perkiraan sebelas Austria tidak diperlakukan sebagai susunan pasti.

Sumber skuad/konteks: [ÖFB, lokasi pertandingan dan skuad](https://www.oefb.at/oefb/Mediainfo/Teamchef-Ralf-Rangnick-nominiert-Kader-fuer-Nations-League-Endspurt), [LAOLA1, keterangan Rangnick (16 November)](https://www.laola1.at/de/red/fussball/oefb-nationalteam/a-team/news/oefb-verletzungsflut--mindestens-zwei-debuets-gegen-israel/). Tanggal publikasi yang tepat tidak seluruhnya tersedia; waktu pengambilan dan status ketersediaan sumber dicatat dalam snapshot.

Perjalanan: seluruh tim berasal dari rangkaian laga 14 November. Lokasi laga sebelumnya tercatat di laporan pertandingan, tetapi rute aktual, waktu kedatangan, durasi penerbangan dan menit pemulihan klub belum terverifikasi. Tidak ditambahkan penalti kelelahan berbasis jarak tebakan.

### Pola: hasil, peluang dan BTTS

Austria tidak kalah dalam lima pertandingan grup, sementara Israel hanya mencetak dua gol. Namun kekuatan historis tim utama dan ketersediaan XI malam ini adalah dua hal berbeda. Model beta masih memberi Austria peluang tinggi karena tidak mempunyai fitur pemain atau rotasi. Acuan kualitatif menahan seluruh target: tim favorit tetap Austria secara deskriptif, tetapi arah itu tidak diterbitkan sebagai pilihan aktif sebelum XI. Dua hasil 0-0 Israel melawan Kosovo tidak cukup untuk mengunci Under melawan susunan Austria yang berubah.

**Menit 76–90+:** Kemenangan terakhir Austria atas Irlandia ditentukan pada menit 79 menurut FotMob. Data kejadian lima pertandingan untuk pemain cadangan yang berpotensi tampil malam ini tidak memadai.

Clean sheet historis adalah frekuensi pada tabel. Sebagai diagnostik terpisah, Poisson **mentah** resep 1X2 menghasilkan P(clean sheet Israel)=20,6% dan P(clean sheet Austria)=35,6%, dari laju gol 1.033 dan 1.581. Angka ini belum dikalibrasi sebagai clean sheet dan tidak boleh digabung dengan BTTS yang dikalibrasi terpisah untuk membentuk satu distribusi gabungan.

### Keputusan dua model

| Target | Utama | Keyakinan/status | Beta | Keyakinan/status |
|---|---|---|---|---|
| 1X2 | Observasi | N/A / observasi | Austria | Rendah / provisional |
| BTTS | Observasi | N/A / observasi | Observasi | N/A / observasi |
| Total 2,5 | Observasi | N/A / observasi | Under 2,5 | Rendah / provisional |

**Probabilitas beta:** 1 7,6%, X 20,9%, 2 71,5% (pembulatan dijaga berjumlah 100,0%). BTTS Ya 45,9%; BTTS Tidak 54,1%. Over 2,5 42,5%; Under 57,5%. Probabilitas yang tipis tetap terlihat walau tidak menjadi pilihan aktif.

Fokus utama: **tidak ada**. Fokus beta: **1X2 Austria**. Skenario utama 0-1, alternatif 1-1.

**Skenario pembalik dan alasan observasi:** Debut kiper, perubahan poros tengah dan jumlah starter baru dapat mengubah 1X2 maupun BTTS. Susunan resmi yang menunjukkan rotasi jauh lebih kecil menjadi alasan sah untuk membuka kembali penilaian; diperlukan snapshot baru.

Pemeriksaan pasar: kutipan tiga operator melalui satu agregator ada pada lampiran; verifikasi independen langsung 0/3. Spread, kedalaman dan pembacaan T-30 belum tersedia. Tidak ada klaim anomali atau informasi internal. Kualitas data laga: skor kuat; statistik peluang/kejadian parsial; berita pemain bervariasi; XI belum resmi.

## 7. Polandia vs Swedia

Grup **B4**. Venue: **Tarczyński Arena, Wrocław**. [Identitas laga UEFA](https://www.uefa.com/uefanationsleague/match/2047922--poland-vs-sweden/matchinfo/). Semua waktu pada tabel riwayat berikut adalah **tanggal lokal pertandingan**, bukan tanggal WIB; H/A/N berarti kandang/tandang/netral. Skor ditulis dari perspektif tim pada judul tabel.

### Data: lima pertandingan kompetitif

**Polandia**

| Tanggal lokal | Lawan | Venue | Skor | Hasil | xG/xGA Opta | Shots/SoT UEFA | Penguasaan UEFA | Sumber |
|---|---|---|---|---|---|---|---|
| 2026-09-25 | Bosnia & Herzegovina | H | 0-0 | D | N/A | N/A | N/A | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/) |
| 2026-09-28 | Swedia | A | 1-3 | L | N/A | N/A | N/A | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/) |
| 2026-10-02 | Rumania | H | 6-0 | W | N/A | 24/10 | 63% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2047963_FR.pdf) |
| 2026-10-05 | Bosnia & Herzegovina | A | 0-1 | L | N/A | 18/3 | 52% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2047939_FR.pdf) |
| 2026-11-14 | Rumania | A | 1-2 | L | 1.56/0.99 | N/A | N/A | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [xG](https://www.fotmob.com/matches/poland-vs-romania/2rojpt) |

Ringkasan: **1W-1D-3L**, 0.80 poin/laga; GF 8, GA 6 (1.20/laga). Clean sheet 2/5; gagal mencetak gol 2/5; BTTS 2/5; Over 2,5 3/5. Shots 21.00 (2/5); SoT 6.50 (2/5). xG/xGA pada laga yang tersedia: 1.56 (1/5) / 0.99 (1/5). xGD berpasangan: +0.57 (1/5).

Pemisahan venue pada fase ini: H 2 laga, GF-GA 6-0; A 3 laga, GF-GA 2-6. Pembanding jangka panjang terukur tidak diterbitkan di acuan utama; model beta memakai jendela enam tahun sebagai sumber kekuatan terpisah.

**Swedia**

| Tanggal lokal | Lawan | Venue | Skor | Hasil | xG/xGA Opta | Shots/SoT UEFA | Penguasaan UEFA | Sumber |
|---|---|---|---|---|---|---|---|
| 2026-09-25 | Rumania | H | 2-1 | W | N/A | 11/4 | 57% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2048015_FR.pdf) |
| 2026-09-28 | Polandia | H | 3-1 | W | N/A | N/A | N/A | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/) |
| 2026-10-02 | Bosnia & Herzegovina | A | 1-1 | D | N/A | N/A | N/A | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/) |
| 2026-10-05 | Rumania | A | 1-0 | W | N/A | N/A | N/A | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/) |
| 2026-11-14 | Bosnia & Herzegovina | H | 3-2 | W | 2.27/1.19 | 13/7 | 44% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2047890_FR.pdf); [xG](https://www.fotmob.com/matches/sweden-vs-bosnia-herzegovina/2vabe3) |

Ringkasan: **4W-1D-0L**, 2.60 poin/laga; GF 10, GA 5 (1.00/laga). Clean sheet 1/5; gagal mencetak gol 0/5; BTTS 4/5; Over 2,5 3/5. Shots 12.00 (2/5); SoT 5.50 (2/5). xG/xGA pada laga yang tersedia: 2.27 (1/5) / 1.19 (1/5). xGD berpasangan: +1.08 (1/5).

Pemisahan venue pada fase ini: H 3 laga, GF-GA 8-4; A 2 laga, GF-GA 2-1. Pembanding jangka panjang terukur tidak diterbitkan di acuan utama; model beta memakai jendela enam tahun sebagai sumber kekuatan terpisah.


### Data: H2H dan skuad

| Tanggal | Pertandingan dan skor 90 menit | Kompetisi | BTTS |
|---|---|---|---|
| 2021-06-23 | Swedia 3-2 Polandia | UEFA Euro | Ya |
| 2022-03-29 | Polandia 2-0 Swedia | FIFA World Cup qualification | Tidak |
| 2026-03-31 | Swedia 3-2 Polandia | FIFA World Cup qualification | Ya |
| 2026-09-28 | Swedia 3-1 Polandia | UEFA Nations League | Ya |

H2H lama dan friendly memiliki relevansi lebih rendah setelah pergantian skuad/pelatih. Penguasaan bola H2H di luar lima laga tidak tersedia; tidak diberi bobot numerik buatan.

**Fakta konteks:** Swedia sudah memastikan juara grup dan promosi dengan 13 poin; Bosnia pasti kedua dengan 8. Polandia 4 dan Rumania 3 memperebutkan posisi ketiga untuk menghindari play-off B/C. Kebutuhan poin Polandia lebih besar, tetapi hal itu bukan ukuran kekuatan serang.

**XI dan ketersediaan:** Sports Mole melaporkan Kiwior diskors, Zieliński sakit, Cash diragukan dan Grabara cedera. Swedia dilaporkan tidak memiliki Bergvall dan Wålemark. Perkiraan Polandia: Drągowski; Pyrka, Potulski, Kędziora, Kubiak; Reguła, Szymański, Nowak, Zalewski; Świderski, Lewandowski. Perkiraan Swedia: Johansson; Svensson, Lagerbielke, Lindelöf, Gudmundsson; Elanga, Larsson, Ayari, Nanasi; Gyökeres, Isak. Nama-nama starter dan kadar rotasi Potter belum resmi.

Sumber skuad/konteks: [SvFF, Swedia memastikan juara grup](https://www.svenskfotboll.se/nyheter/landslag/2026/11/unl-swe-bih/), [Sports Mole, skuad dan perkiraan](https://www.sportsmole.co.uk/football/poland/uefa-nations-league/preview/poland-vs-sweden-prediction-team-news-lineups_609183.html), [TVP, venue Wrocław](https://sport.tvp.pl/96413041/plan-zgrupowania-reprezentacji-polski-w-listopadzie-2026-kiedy-mecze-konferencje-i-treningi-kadry-terminarz). Tanggal publikasi yang tepat tidak seluruhnya tersedia; waktu pengambilan dan status ketersediaan sumber dicatat dalam snapshot.

Perjalanan: seluruh tim berasal dari rangkaian laga 14 November. Lokasi laga sebelumnya tercatat di laporan pertandingan, tetapi rute aktual, waktu kedatangan, durasi penerbangan dan menit pemulihan klub belum terverifikasi. Tidak ditambahkan penalti kelelahan berbasis jarak tebakan.

### Pola: hasil, peluang dan BTTS

Swedia menang empat dan seri sekali. Sebanyak enam dari delapan gol Polandia berasal dari satu kemenangan atas Rumania; rerata serang Polandia karena itu mudah tampak lebih baik daripada konsistensinya. Saat kalah 1-2 di Rumania, Polandia justru memiliki xG Opta 1,56 melawan 0,99, sehingga hasil terakhir tidak sepenuhnya mencerminkan kualitas peluangnya. Swedia menang 3-2 atas Bosnia dengan dua penalti; bukan semua produktivitasnya datang dari peluang terbuka. Arah Swedia hanya berkeyakinan rendah, dan BTTS ditahan karena kehilangan kreativitas Polandia serta rotasi Swedia.

**Menit 76–90+:** Reguła mencetak gol menit 82 di Rumania. Tidak ada gol Swedia sesudah 45+2 saat melawan Bosnia; dua gol balasan Bosnia terjadi sebelum menit 76. Tidak ditarik klaim intensitas akhir dari skor 3-2 saja.

Clean sheet historis adalah frekuensi pada tabel. Sebagai diagnostik terpisah, Poisson **mentah** resep 1X2 menghasilkan P(clean sheet Polandia)=26,8% dan P(clean sheet Swedia)=18,7%, dari laju gol 1.677 dan 1.316. Angka ini belum dikalibrasi sebagai clean sheet dan tidak boleh digabung dengan BTTS yang dikalibrasi terpisah untuk membentuk satu distribusi gabungan.

### Keputusan dua model

| Target | Utama | Keyakinan/status | Beta | Keyakinan/status |
|---|---|---|---|---|
| 1X2 | Swedia | Rendah / provisional | Observasi | N/A / observasi |
| BTTS | Observasi | N/A / observasi | Observasi | N/A / observasi |
| Total 2,5 | Over 2,5 | Rendah / provisional | Observasi | N/A / observasi |

**Probabilitas beta:** 1 36,8%, X 26,6%, 2 36,6% (pembulatan dijaga berjumlah 100,0%). BTTS Ya 50,3%; BTTS Tidak 49,7%. Over 2,5 52,3%; Under 47,7%. Probabilitas yang tipis tetap terlihat walau tidak menjadi pilihan aktif.

Fokus utama: **1X2 Swedia**. Fokus beta: **tidak ada**. Skenario utama 1-2, alternatif 1-1.

**Skenario pembalik dan alasan observasi:** Jika Swedia melakukan rotasi besar, dukungan kemenangan tandang dan Over melemah. Kembalinya Cash atau perubahan kondisi Zieliński juga menuntut penilaian ulang yang bersumber.

Pemeriksaan pasar: kutipan tiga operator melalui satu agregator ada pada lampiran; verifikasi independen langsung 0/3. Spread, kedalaman dan pembacaan T-30 belum tersedia. Tidak ada klaim anomali atau informasi internal. Kualitas data laga: skor kuat; statistik peluang/kejadian parsial; berita pemain bervariasi; XI belum resmi.

## 8. Ukraina vs Georgia

Grup **B2**. Venue: **Košice Football Arena, Košice (netral)**. [Identitas laga UEFA](https://www.uefa.com/uefanationsleague/match/2047918--ukraine-vs-georgia/matchinfo/). Semua waktu pada tabel riwayat berikut adalah **tanggal lokal pertandingan**, bukan tanggal WIB; H/A/N berarti kandang/tandang/netral. Skor ditulis dari perspektif tim pada judul tabel.

### Data: lima pertandingan kompetitif

**Ukraina**

| Tanggal lokal | Lawan | Venue | Skor | Hasil | xG/xGA Opta | Shots/SoT UEFA | Penguasaan UEFA | Sumber |
|---|---|---|---|---|---|---|---|
| 2026-09-25 | Hungaria | A | 1-0 | W | N/A | 9/3 | 46% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2048012_FR.pdf) |
| 2026-09-28 | Georgia | A | 0-0 | D | N/A | 7/2 | 52% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2047991_FR.pdf) |
| 2026-10-02 | Irlandia Utara | N | 0-3 | L | N/A | 11/2 | 65% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2047959_FR.pdf) |
| 2026-10-05 | Hungaria | N | 1-2 | L | N/A | 18/3 | 52% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2047932_FR.pdf) |
| 2026-11-14 | Irlandia Utara | A | 0-1 | L | 0.75/1.59 | 6/2 | 62% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2047897_FR.pdf); [xG](https://www.fotmob.com/en-GB/matches/ukraine-vs-northern-ireland/2dt35j) |

Ringkasan: **1W-1D-3L**, 0.80 poin/laga; GF 2, GA 6 (1.20/laga). Clean sheet 2/5; gagal mencetak gol 3/5; BTTS 1/5; Over 2,5 2/5. Shots 10.20 (5/5); SoT 2.40 (5/5). xG/xGA pada laga yang tersedia: 0.75 (1/5) / 1.59 (1/5). xGD berpasangan: -0.84 (1/5).

Pemisahan venue pada fase ini: A 3 laga, GF-GA 1-1; N 2 laga, GF-GA 1-5. Pembanding jangka panjang terukur tidak diterbitkan di acuan utama; model beta memakai jendela enam tahun sebagai sumber kekuatan terpisah.

**Georgia**

| Tanggal lokal | Lawan | Venue | Skor | Hasil | xG/xGA Opta | Shots/SoT UEFA | Penguasaan UEFA | Sumber |
|---|---|---|---|---|---|---|---|
| 2026-09-25 | Irlandia Utara | H | 0-1 | L | N/A | 11/4 | 61% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2048014_FR.pdf) |
| 2026-09-28 | Ukraina | H | 0-0 | D | N/A | 14/5 | 48% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2047991_FR.pdf) |
| 2026-10-02 | Hungaria | A | 0-1 | L | N/A | N/A | N/A | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/) |
| 2026-10-05 | Irlandia Utara | A | 0-0 | D | N/A | N/A | N/A | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/) |
| 2026-11-14 | Hungaria | H | 0-2 | L | 0.67/1.89 | 7/1 | 53% | [hasil UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/); [statistik UEFA](https://www.uefa.com/newsfiles/UNL/2027/2047895_FR.pdf); [xG](https://www.fotmob.com/matches/georgia-vs-hungary/2ccy6u) |

Ringkasan: **0W-2D-3L**, 0.40 poin/laga; GF 0, GA 4 (0.80/laga). Clean sheet 2/5; gagal mencetak gol 5/5; BTTS 0/5; Over 2,5 0/5. Shots 10.67 (3/5); SoT 3.33 (3/5). xG/xGA pada laga yang tersedia: 0.67 (1/5) / 1.89 (1/5). xGD berpasangan: -1.22 (1/5).

Pemisahan venue pada fase ini: H 3 laga, GF-GA 0-3; A 2 laga, GF-GA 0-1. Pembanding jangka panjang terukur tidak diterbitkan di acuan utama; model beta memakai jendela enam tahun sebagai sumber kekuatan terpisah.


### Data: H2H dan skuad

| Tanggal | Pertandingan dan skor 90 menit | Kompetisi | BTTS |
|---|---|---|---|
| 2015-06-09 | Georgia 1-2 Ukraina | Friendly | Ya |
| 2024-10-11 | Ukraina 1-0 Georgia | UEFA Nations League | Tidak |
| 2024-11-16 | Georgia 1-1 Ukraina | UEFA Nations League | Ya |
| 2026-09-28 | Georgia 0-0 Ukraina | UEFA Nations League | Tidak |

H2H lama dan friendly memiliki relevansi lebih rendah setelah pergantian skuad/pelatih. Penguasaan bola H2H di luar lima laga tidak tersedia; tidak diberi bobot numerik buatan.

**Fakta konteks:** Ukraina memiliki 4 poin dan Georgia 2. Ukraina cukup seri untuk mempertahankan tempat ketiga; Georgia harus menang. Nominal kandang Ukraina sebenarnya dimainkan di Košice, Slovakia. Model beta memakai venue netral dan tidak menambahkan bonus kandang biasa.

**XI dan ketersediaan:** Dalam konferensi yang dimuat UAF, Andrea Maldera mengakui absennya Zubkov dan Tsyhankov serta menyebut lawan kehilangan Kvaratskhelia. UAF juga menerbitkan penggantian Ponomarenko oleh Dovbyk. Tanpa menciptakan koefisien cedera baru, informasi ini memperlemah proyeksi serangan kedua tim. Susunan penuh Ukraina/Georgia belum terverifikasi sebagai XI resmi. Laporan daring yang menyatakan kedua tim tanpa absensi bertentangan dengan federasi dan tidak dipakai.

Sumber skuad/konteks: [UAF, konferensi Maldera](https://uaf.ua/news/andrea-maldera-peredusim-my-khochemo-zrobyty-nashykh-vbolivalnykiv-shchaslyvymy), [UAF, Dovbyk menggantikan Ponomarenko](https://uaf.ua/en/news/change-in-the-ukraine-national-team-lineup-dovbik-instead-of-ponomarenko), [UAF, venue Košice](https://uaf.ua/en/news/vip-hospitality-at-the-ukraine-georgia-match). Tanggal publikasi yang tepat tidak seluruhnya tersedia; waktu pengambilan dan status ketersediaan sumber dicatat dalam snapshot.

Perjalanan: seluruh tim berasal dari rangkaian laga 14 November. Lokasi laga sebelumnya tercatat di laporan pertandingan, tetapi rute aktual, waktu kedatangan, durasi penerbangan dan menit pemulihan klub belum terverifikasi. Tidak ditambahkan penalti kelelahan berbasis jarak tebakan.

### Pola: hasil, peluang dan BTTS

Georgia belum mencetak gol dalam lima laga grup; Ukraina hanya mencetak dua. Kedua tim terakhir kali bertemu dengan hasil 0-0. Opta mencatat xG Ukraina 0,75 di Belfast dan Georgia 0,67 saat menjamu Hungaria, mendukung kekhawatiran kreativitas terkini. H2H lama dan model kekuatan jangka panjang tidak menghapus masalah tersebut. BTTS Tidak menjadi fokus utama; pemenang ditahan karena Ukraina sendiri juga sulit mencetak gol. Skenario 1-0 tidak otomatis menjadi pilihan kemenangan Ukraina.

**Menit 76–90+:** Hungaria mencetak gol menit 85 pada laga terakhir Georgia. Kemungkinan Georgia yang wajib menang membuka ruang menjelang akhir adalah inferensi konteks; data xG menit 76–90+ yang konsisten belum tersedia.

Clean sheet historis adalah frekuensi pada tabel. Sebagai diagnostik terpisah, Poisson **mentah** resep 1X2 menghasilkan P(clean sheet Ukraina)=37,4% dan P(clean sheet Georgia)=32,5%, dari laju gol 1.123 dan 0.984. Angka ini belum dikalibrasi sebagai clean sheet dan tidak boleh digabung dengan BTTS yang dikalibrasi terpisah untuk membentuk satu distribusi gabungan.

### Keputusan dua model

| Target | Utama | Keyakinan/status | Beta | Keyakinan/status |
|---|---|---|---|---|
| 1X2 | Observasi | N/A / observasi | Observasi | N/A / observasi |
| BTTS | Tidak | Cukup kuat / provisional | Tidak | Rendah / provisional |
| Total 2,5 | Under 2,5 | Sedang / provisional | Under 2,5 | Sedang / provisional |

**Probabilitas beta:** 1 24,3%, X 38,5%, 2 37,2% (pembulatan dijaga berjumlah 100,0%). BTTS Ya 41,4%; BTTS Tidak 58,6%. Over 2,5 34,8%; Under 65,2%. Probabilitas yang tipis tetap terlihat walau tidak menjadi pilihan aktif.

Fokus utama: **BTTS Tidak**. Fokus beta: **Total 2,5 Under 2,5**. Skenario utama 1-0, alternatif 0-0.

**Skenario pembalik dan alasan observasi:** Gol pertama yang cepat atau munculnya dua penyerang Ukraina dapat membuat Georgia bermain lebih terbuka. XI harus diperiksa untuk memastikan pengganti kreator yang absen, bukan sekadar menghitung jumlah penyerang.

Pemeriksaan pasar: kutipan tiga operator melalui satu agregator ada pada lampiran; verifikasi independen langsung 0/3. Spread, kedalaman dan pembacaan T-30 belum tersedia. Tidak ada klaim anomali atau informasi internal. Kualitas data laga: skor kuat; statistik peluang/kejadian parsial; berita pemain bervariasi; XI belum resmi.

## Pasar: kutipan indikatif, bukan sinyal anomali

Urutan odds setiap sel: 1/X/2, desimal. Halaman mencantumkan pembaruan 17 November 09.01 UTC. Tiga operator berikut berasal dari **satu agregator**, bukan tiga konfirmasi langsung yang independen. [WBookie](https://www.wbookie.com/en/odds?date=2026-11-17).

| Laga | Bet365 | 1xBet | Pinnacle |
|---|---|---|---|
| Denmark vs Norwegia | 2.25/4.00/2.75 | 2.38/4.00/2.77 | 2.29/4.22/2.79 |
| Wales vs Portugal | 6.50/5.00/1.44 | 7.29/5.14/1.43 | 7.01/5.31/1.42 |
| Bosnia & Herzegovina vs Rumania | 2.00/3.75/3.40 | 2.05/3.76/3.59 | 2.10/3.71/3.44 |
| Hungaria vs Irlandia Utara | 1.95/3.30/4.10 | 1.94/3.46/4.40 | 1.95/3.38/4.35 |
| Republik Irlandia vs Kosovo | 2.10/3.20/3.70 | 2.18/3.24/3.80 | 2.11/3.24/3.92 |
| Israel vs Austria | 3.80/3.80/1.83 | 4.20/3.92/1.86 | 4.09/3.93/1.85 |
| Polandia vs Swedia | 2.20/3.70/2.90 | 2.28/3.76/3.05 | 2.23/3.91/3.02 |
| Ukraina vs Georgia | 2.10/3.20/3.70 | 2.23/3.38/3.49 | 2.14/3.36/3.67 |

Kontrak diperlakukan sebagai indikasi 1X2 waktu normal; aturan penyelesaian langsung tiap operator belum diperiksa. Likuiditas/spread tidak diketahui. Perbedaan dengan model belum membuktikan value atau keuntungan. Pemeriksaan sekitar T-30 masih berada di masa depan saat cutoff.

## Catatan sebelum susunan resmi

Periksa XI sekitar satu jam sebelum kickoff, terutama rotasi Austria/Swedia, pengganti Collins, poros Portugal, Szoboszlai/Orbán dan kreator Ukraina/Georgia. Pembaruan harus menyebut pemain/peran yang berubah serta dampaknya pada target, lalu disimpan sebagai snapshot baru. Laporan ini tidak mengaktifkan pemantauan otomatis.

## Arsip dan verifikasi

Utama: ID `4c1eb50062b44b4191b42c01d78acb6b`, dicatat `2026-11-17T12:16:25.429745+00:00`. SHA-256 jurnal `9f73a2765d78cc972548eb93ef66cf4a8e86b7c382ff4b3a20a9d7895bd98fcb`.

Beta: ID `5effc53438aa42ebb800cb3501d0a8d1`, dicatat `2026-11-17T12:16:25.505747+00:00`. SHA-256 jurnal `77be40749e796d1d3b2c10877d24ac79fccd86f18345988ac2a78350e0f4f92b`.

Waktu pencatatan merupakan waktu file aktual, terverifikasi sebelum kickoff terjadwal 17 November 19.45 UTC. Hash lokal membuktikan konsistensi berkas, bukan stempel waktu publik dari pihak ketiga. Semua pilihan, observasi, fokus dan skor pada poster diambil dari snapshot yang sama. Evaluasi setelah laga harus memakai hasil 90 menit terpisah; tidak memilih ulang versi yang paling benar.

Analisis ini menjadi bahan pertimbangan, bukan hasil mutlak.
