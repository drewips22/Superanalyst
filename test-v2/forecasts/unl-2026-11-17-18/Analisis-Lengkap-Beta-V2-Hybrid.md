# Superanalyst — Beta V2 dan Hybrid | UNL 17–18 November 2026

Delapan laga dimulai **18 November 2026 pukul 02.45 WIB** (17 November 19.45 UTC). Batas informasi bersama: **17 Nov 2026 20.21.27 WIB**. Rekaman utama: 17 Nov 2026 20.21.27 WIB; eksperimen: 17 Nov 2026 20.21.27 WIB. Semuanya dibuat sebelum kickoff. Hasil aktual masih kosong.

Metode utama tetap UNL v1, data → pola → keputusan. Penilaian baru utama dibekukan sebelum inferensi Beta dan hanya menjadi masukan baca-saja bagi Hybrid. Tidak ada perubahan metode utama atau keputusan lama. Semua pilihan berstatus **eksperimental/provisional** karena XI belum resmi.

## Hasil ringkas yang dibekukan

| Laga | Fokus utama, kualitatif | Fokus Beta V2 | Fokus Hybrid |
|---|---|---|---|
| Denmark–Norwegia | BTTS Ya · Sedang | Observasi | Observasi |
| Wales–Portugal | Portugal menang · Rendah | Portugal menang · 66,0% | Portugal menang · 66,0% |
| Bosnia & Herzegovina–Rumania | Bosnia & Herzegovina menang · Sedang | Observasi | Observasi |
| Hungaria–Irlandia Utara | Under 2,5 · Relatif kuat | Under 2,5 · 64,4% | Under 2,5 · 64,4% |
| Irlandia–Kosovo | Under 2,5 · Sedang | Under 2,5 · 61,3% | Under 2,5 · 61,3% |
| Israel–Austria | Austria menang · Rendah | Austria menang · 71,5% | Austria menang · 71,5% |
| Polandia–Swedia | BTTS Ya · Sedang | Observasi | Observasi |
| Ukraina–Georgia | Under 2,5 · Relatif kuat | Under 2,5 · 65,2% | Under 2,5 · 65,2% |

Beta aktif **9/24 target, fokus 5/8 laga**; Hybrid **7/24 target, fokus 5/8 laga**; utama **15/24 target, fokus 8/8 laga**. Observasi bukan pilihan seri dan tidak dimasukkan sebagai prediksi kalah/benar. Fokus bukan rekomendasi menggabungkan lima laga.

Persentase di kolom Hybrid adalah dukungan numerik Beta terhadap pilihan utama, **bukan probabilitas gabungan baru**. Fokus kedua eksperimen sama malam ini, tetapi BTTS Tidak Irlandia–Kosovo dan Under Israel–Austria hanya diterbitkan Beta. Hybrid mempertahankan observasi utama untuk dua target tersebut.

## Probabilitas Beta V2 dan aturan keputusan

| Laga | Kandang | Seri | Tandang | BTTS Ya | BTTS Tidak | Over 2,5 | Under 2,5 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Denmark–Norwegia | 36,3% | 24,9% | 38,9% | 52,1% | 47,9% | 54,3% | 45,7% |
| Wales–Portugal | 10,7% | 23,3% | 66,0% | 46,9% | 53,1% | 45,5% | 54,5% |
| Bosnia & Herzegovina–Rumania | 32,3% | 31,6% | 36,1% | 46,2% | 53,8% | 46,9% | 53,1% |
| Hungaria–Irlandia Utara | 30,2% | 41,3% | 28,5% | 39,8% | 60,2% | 35,6% | 64,4% |
| Irlandia–Kosovo | 29,1% | 39,9% | 31,0% | 40,7% | 59,3% | 38,7% | 61,3% |
| Israel–Austria | 7,6% | 20,9% | 71,5% | 45,9% | 54,1% | 42,5% | 57,5% |
| Polandia–Swedia | 36,8% | 26,6% | 36,5% | 50,3% | 49,7% | 52,3% | 47,7% |
| Ukraina–Georgia | 24,3% | 38,5% | 37,2% | 41,4% | 58,6% | 34,8% | 65,2% |

Angka adalah peluang model, bukan akurasi yang sudah tercapai. Angka dibulatkan; jumlah 1X2 dapat berbeda 0,1 poin persentase dari 100%. Pilihan aktif harus searah dengan peluang tertinggi dan memenuhi ambang tetap **55%**. Arah diagnostik di bawah ambang tidak diterbitkan sebagai pilihan. Fokus Beta mengambil peluang aktif terbesar. Aturan lintas-target ini masih dapat lebih sering memilih pasar biner; tidak diubah setelah melihat hasil malam ini.

Versi: `superanalyst-beta-v2.0.0-experimental`; Hybrid `superanalyst-hybrid-beta-v1.0.0-experimental`. 1X2 dan BTTS memakai `strength_h730`; total memakai `strength_h365_plus_friendlies`. Rating serang/bertahan menyesuaikan kekuatan lawan, venue dan kompetisi dalam jendela enam tahun; peluruhan 730/365 hari dan regularisasi tetap dari protokol. Laga uji coba hanya masuk resep total dengan kategori kompetisi terpisah. Tidak ada koefisien cedera atau motivasi baru.

Fit terbaru bertanggal **17 November**, skor latihan terakhir **14 November**, mengikuti penyangga tiga hari yang sudah dibekukan. Dari 44 pembaruan UNL yang diverifikasi, 26 boleh digunakan dan 18 tanggal 15–16 November tidak masuk latihan. Korpus global setelah awal Oktober belum dijamin lengkap di luar pembaruan tersebut; kelengkapan lima laga tim-tim malam ini diperiksa terpisah. Ukuran fit: strength_h730 3076 laga; strength_h365_plus_friendlies 4624 laga. Kedua optimisasi berhasil.

Kalibrasi merupakan resep historis 2020–2021 yang tetap, belum dibuktikan terkalibrasi untuk matchday ini. Karena tiap marginal memakai resep/kalibrator sendiri, tabel di atas **bukan satu distribusi skor gabungan**. Simulasi 10.000 sampel per resep di bagian diagnostik memakai distribusi Poisson mentah; tidak menggantikan probabilitas terkalibrasi atau menentukan pilihan.

## Ringkasan lima laga setiap tim

Seluruh jendela adalah lima pertandingan kompetitif UEFA Nations League 90 menit, September–14 November 2026. W-D-L dan bentuk dibaca dari paling lama ke terbaru. Cakupan tembakan/SoT 5/5 per tim. xG/xGA **N/A, 0/5 per tim**; selisih xG juga N/A. Penguasaan bola dan SoT tidak disebut sebagai kualitas xG.

| Tim | W-D-L | GF–GA | GF/laga | GA/laga | PPG | CS | Gagal gol | BTTS | Over | Tembakan / SoT | PPG awal 2 → akhir 3 |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| Denmark | 3-0-2 | 11–8 | 2,2 | 1,6 | 1,8 | 2/5 | 0/5 | 3/5 | 3/5 | 15 / 4,8 | 1,5 → 2 |
| Norway | 2-0-3 | 9–9 | 1,8 | 1,8 | 1,2 | 0/5 | 0/5 | 5/5 | 5/5 | 14,2 / 5,2 | 1,5 → 1 |
| Wales | 1-0-4 | 3–8 | 0,6 | 1,6 | 0,6 | 0/5 | 3/5 | 2/5 | 2/5 | 9 / 3,2 | 0 → 1 |
| Portugal | 4-0-1 | 10–8 | 2 | 1,6 | 2,4 | 1/5 | 0/5 | 4/5 | 4/5 | 17,8 / 6,8 | 3 → 2 |
| Bosnia and Herzegovina | 2-2-1 | 8–6 | 1,6 | 1,2 | 1,6 | 2/5 | 1/5 | 3/5 | 2/5 | 10,6 / 3,6 | 2 → 1,33 |
| Romania | 1-0-4 | 5–14 | 1 | 2,8 | 0,6 | 0/5 | 2/5 | 3/5 | 4/5 | 11,4 / 3,2 | 0 → 1 |
| Hungary | 3-1-1 | 5–2 | 1 | 0,4 | 2 | 3/5 | 2/5 | 1/5 | 1/5 | 15,6 / 4,6 | 0,5 → 3 |
| Northern Ireland | 3-2-0 | 5–0 | 1 | 0 | 2,2 | 5/5 | 2/5 | 0/5 | 1/5 | 12,4 / 4,2 | 2 → 2,33 |
| Republic of Ireland | 1-2-2 | 6–5 | 1,2 | 1 | 1 | 1/5 | 2/5 | 2/5 | 2/5 | 10,8 / 3,6 | 1,5 → 0,67 |
| Kosovo | 1-3-1 | 3–4 | 0,6 | 0,8 | 1,2 | 3/5 | 2/5 | 2/5 | 1/5 | 14,4 / 4 | 1,5 → 1 |
| Israel | 0-3-2 | 2–7 | 0,4 | 1,4 | 0,6 | 2/5 | 3/5 | 2/5 | 2/5 | 7,8 / 2,6 | 0 → 1 |
| Austria | 3-2-0 | 10–5 | 2 | 1 | 2,2 | 1/5 | 0/5 | 4/5 | 3/5 | 16 / 6,8 | 3 → 1,67 |
| Poland | 1-1-3 | 8–6 | 1,6 | 1,2 | 0,8 | 2/5 | 2/5 | 2/5 | 3/5 | 17,8 / 5,4 | 0,5 → 1 |
| Sweden | 4-1-0 | 10–5 | 2 | 1 | 2,6 | 1/5 | 0/5 | 4/5 | 3/5 | 11,2 / 4,6 | 3 → 2,33 |
| Ukraine | 1-1-3 | 2–6 | 0,4 | 1,2 | 0,8 | 2/5 | 3/5 | 1/5 | 2/5 | 10,4 / 2,2 | 2 → 0 |
| Georgia | 0-2-3 | 0–4 | 0 | 0,8 | 0,4 | 2/5 | 5/5 | 0/5 | 0/5 | 9,4 / 3,2 | 0,5 → 0,33 |

PPG adalah poin per laga, CS clean sheet historis. Pergeseran dua versus tiga laga hanya deskriptif. Pembanding periode lebih panjang berasal dari rating model enam tahun; data xG musim/timnas lebih panjang yang sebanding tidak tersedia.

## 1. Denmark vs Norwegia — A4

**Jadwal/venue terverifikasi:** 18 November 02.45 WIB; Parken Stadium, Copenhagen, Denmark; kandang fisik. [UEFA](https://www.uefa.com/uefanationsleague/match/2047919--denmark-vs-norway/)

**Motivasi:** Denmark 9 poin perlu minimal seri untuk perempat final; Norwegia 6 harus menang. Kemenangan Norwegia berapa pun cukup berdasarkan H2H, bukan wajib selisih tiga gol. [UEFA: keadaan grup dan aturan](https://www.uefa.com/uefanationsleague/news/02ab-2209792f2fda-6a523d4500bb-1000--nations-league-latest-on-quarter-final-qualification-prom/)

### Denmark: lima laga lengkap

| Tanggal | Lawan | H/A/N | GF–GA (90m) | Hasil | xG/xGA | Tembakan | SoT | Bola % | Sumber |
|---|---|---|---|---|---|---:|---:|---:|---|
| 2026-09-24 | Norway | A | 2–3 | L | N/A / N/A | 13 | 7 | 51,3 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861046) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861046) |
| 2026-09-27 | Wales | H | 2–0 | W | N/A / N/A | 20 | 4 | 61,6 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861070) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861070) |
| 2026-10-01 | Portugal | H | 2–4 | L | N/A / N/A | 12 | 3 | 53,7 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861096) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861096) |
| 2026-10-04 | Wales | A | 1–0 | W | N/A / N/A | 13 | 4 | 44 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861125) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861125) |
| 2026-11-14 | Portugal | A | 4–1 | W | N/A / N/A | 17 | 6 | 48,5 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861167) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861167) |

Bentuk **L-W-L-W-W**; penguasaan rata-rata 51,82% (n=5), kartu merah total 0. Venue: home: n=2, GF–GA 4–4, menang 1; away: n=3, GF–GA 7–4, menang 2. Jeda antar-kickoff 72 jam, bukan pengukuran pemulihan individual.

Gol menit 76–90+: GF 0 / GA 2, cakupan 5/5. Hanya hitungan event yang cocok dengan skor akhir; tidak dipakai sebagai tambahan koefisien model.

### Norway: lima laga lengkap

| Tanggal | Lawan | H/A/N | GF–GA (90m) | Hasil | xG/xGA | Tembakan | SoT | Bola % | Sumber |
|---|---|---|---|---|---|---:|---:|---:|---|
| 2026-09-24 | Denmark | H | 3–2 | W | N/A / N/A | 13 | 7 | 48,7 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861046) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861046) |
| 2026-09-27 | Portugal | H | 1–2 | L | N/A / N/A | 22 | 6 | 62 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861073) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861073) |
| 2026-10-01 | Wales | A | 1–2 | L | N/A / N/A | 12 | 4 | 49,6 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861100) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861100) |
| 2026-10-04 | Portugal | A | 1–2 | L | N/A / N/A | 9 | 3 | 41,4 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861126) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861126) |
| 2026-11-14 | Wales | H | 3–1 | W | N/A / N/A | 15 | 6 | 55 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861165) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861165) |

Bentuk **W-L-L-L-W**; penguasaan rata-rata 51,34% (n=5), kartu merah total 2.0. Venue: home: n=3, GF–GA 7–5, menang 2; away: n=2, GF–GA 2–4, menang 0. Jeda antar-kickoff 74,75 jam, bukan pengukuran pemulihan individual.

Gol menit 76–90+: GF 1 / GA 2, cakupan 5/5. Hanya hitungan event yang cocok dengan skor akhir; tidak dipakai sebagai tambahan koefisien model.

### H2H dan relevansi

| Tanggal | Pertemuan | Skor 90m | Kompetisi | Sumber |
|---|---|---|---|---|
| 2011-03-26 | Norway–Denmark | 1–1 | UEFA Euro qualification | [Arsip](https://github.com/martj42/international_results/blob/b0948cb558c927c357db4067eac5b37b96d0e4bb/results.csv#L34654) |
| 2011-09-06 | Denmark–Norway | 2–0 | UEFA Euro qualification | [Arsip](https://github.com/martj42/international_results/blob/b0948cb558c927c357db4067eac5b37b96d0e4bb/results.csv#L35202) |
| 2013-11-15 | Denmark–Norway | 2–1 | Friendly | [Arsip](https://github.com/martj42/international_results/blob/b0948cb558c927c357db4067eac5b37b96d0e4bb/results.csv#L37451) |
| 2024-06-08 | Denmark–Norway | 3–1 | Friendly | [Arsip](https://github.com/martj42/international_results/blob/b0948cb558c927c357db4067eac5b37b96d0e4bb/results.csv#L47322) |
| 2026-09-24 | Norway–Denmark | 3–2 | UEFA Nations League | [Arsip](https://www.espn.com/soccer/match/_/gameId/401861046) |

Pertemuan grup 2026 paling relevan. Laga lama/uji coba ditampilkan sebagai konteks; kesinambungan semua pelatih dan susunan historis tidak terverifikasi, sehingga tidak diperlakukan sebagai kekuatan tim saat ini. Penguasaan/xG H2H lintas periode yang sebanding N/A; pertandingan grup yang sama sudah ada dalam lima laga dan tidak dihitung sebagai bukti independen tambahan.

### Pemain dan XI perkiraan

| Tim | Pemain/peran | Status sumber | Pengaruh yang dinilai | Sumber |
|---|---|---|---|---|
| Denmark | Joachim Andersen / Bek tengah | doubtful | Keluhan ligamen setelah laga Portugal; Nelsson alternatif, konfirmasi XI diperlukan. | [Berita](https://www.tntsports.co.uk/betting/tips/denmark-vs-norway-prediction-tips-and-odds-17-11-26/) |
| Denmark | Patrick Dorgu / Kasper Dolberg / Andreas Christensen / Sisi kiri / striker / bek | out_reported | Absensi yang sudah ada pada jendela ini, bukan pengurang peluang baru otomatis. | [Berita](https://www.tntsports.co.uk/betting/tips/denmark-vs-norway-prediction-tips-and-odds-17-11-26/) |
| Norway | Fredrik Aursnes / Gelandang | withdrawn | NFF mencatat penarikan 8 November; Hugo Vetlesen masuk skuad. | [Berita](https://www.fotball.no/landslag/norge-a-herrer/2026/herrelandslagets-tropp-til-nations-league-kamper/) |
| Norway | Martin Odegaard / Kreator | available_projected | Sudah memulai laga Wales setelah gangguan kondisi; bukan jaminan 90 menit. | [Berita](https://www.sportsmole.co.uk/football/denmark/preview/denmark-vs-norway-prediction-team-news-lineups_609154.html) |

**XI Denmark (perkiraan):** Hermansen; Kristensen, Andersen, Nelsson, Maehle; Hojbjerg, Hjulmand; Isaksen, Damsgaard, Skov Olsen; Hojlund.

**XI Norwegia (perkiraan):** Selvik; Ryerson, Ajer, Heggem, Wolfe; Berg, Berge; Bobb, Odegaard, Nusa; Haaland.

Proyeksi Sports Mole; status Andersen ditandai belum pasti, bukan susunan resmi. [Sumber den-nor-preview](https://www.sportsmole.co.uk/football/denmark/preview/denmark-vs-norway-prediction-team-news-lineups_609154.html) · [Sumber den-nor-teamnews](https://www.tntsports.co.uk/betting/tips/denmark-vs-norway-prediction-tips-and-odds-17-11-26/) · [Sumber nff-squad](https://www.fotball.no/landslag/norge-a-herrer/2026/herrelandslagets-tropp-til-nations-league-kamper/) · [Sumber nff-program](https://www.fotball.no/tema/medieservice/2026/herrelandslagets-program-til-kampene-mot-wales-og-danmark/)

**Pola data:** Lima BTTS Norwegia mencakup dua kartu merah di jendela tersebut sehingga kebobolan tidak dibaca sebagai takdir. Kedua tim tetap memiliki output SoT yang layak; Denmark cukup seri dapat membuat tempo awal lebih hati-hati.

**Taktik/konteks:** Inferensi: kebutuhan Norwegia menang dapat membuka transisi; belum ada data event yang membuktikan pola pressing atau xG serangan sisi. NFF mengonfirmasi aktivitas Oslo kemudian Parken; rute penerbangan, durasi dan pemulihan aktual tidak tersedia. Tidak tersedia data event lengkap untuk mengukur pressing, transisi, kualitas crossing atau set piece. Tidak dibuat bonus persen dari narasi ini.

### Keputusan per target, seluruhnya dari snapshot yang sama

| Target | Utama (kualitatif) | Beta V2 aktif | Hybrid aktif | Alasan filter Hybrid |
|---|---|---|---|---|
| 1X2 | Observasi | Observasi | Observasi | Observasi utama dipertahankan |
| BTTS | BTTS Ya · Sedang | Observasi | Observasi | Dukungan di bawah ambang 55% |
| Total 2,5 | Over 2,5 · Sedang | Observasi | Observasi | Dukungan di bawah ambang 55% |

**Fokus Beta:** Observasi. **Fokus Hybrid:** Observasi.

**Alasan dan kontra utama yang dibekukan:**

- 1X2: Denmark menang dua laga terakhir; Norwegia membutuhkan kemenangan. Kontra/batas: Kualitas serang berimbang; Denmark cukup seri; XI dan Andersen belum pasti.
- BTTS: Norwegia mencetak dan kebobolan dalam 5/5; Denmark mencetak dalam 5/5.; Rata-rata SoT Denmark 4,8 dan Norwegia 5,2; laga pertama 3–2. Kontra/batas: Dua clean sheet Denmark terjadi melawan Wales; Denmark dapat memperlambat permainan untuk mengejar seri.
- Total 2,5: Kelima laga Norwegia dan tiga laga Denmark melewati 2,5. Kontra/batas: Bukan xG; dua laga kandang Denmark memberi hasil sangat berbeda.

**Skenario utama, bukan exact-score pick:** 2–2. **Pemicu penilaian ulang:** Jika Haaland/Odegaard atau dua penyerang Denmark tidak memulai, dukungan BTTS/Over melemah. Gol awal dapat memperbesar peluang transisi.

**Clean sheet model mentah:** Denmark 24,1%, Norwegia 17,2%, dari resep mentah strength_h730. Ini estimasi Poisson mentah tanpa kalibrasi khusus clean sheet; berbeda dari frekuensi CS historis dan bukan konsekuensi tunggal tabel marginal terkalibrasi.

**Sensitivitas lima laga lama (diagnostik):** menghilangkan satu dari 9 pertandingan unik secara bergantian menghasilkan perubahan arah 1X2/BTTS/total sebanyak 0/0/0. Ini diagnostik rumus lima laga mentah, bukan uji sensitivitas rating Beta V2 atau interval keyakinan; hasil ekstrem tidak dibuang dari model.

| Resep mentah | Laju gol H/A | Skor MC teratas | Frekuensi sampel |
|---|---|---|---|
| strength_h730 | 1,76/1,42 | 1–1 | 10,5% |
| strength_h365_plus_friendlies | 1,74/1,35 | 1–1 | 10,6% |

MC: 10.000 sampel **per resep** dengan seed tetap. Skor paling sering tetap hanya satu skenario; tidak otomatis menjadi pilihan 1X2/BTTS/total terkalibrasi.

**Pembanding pasar:** DraftKings via ESPN, diambil 17 Nov 2026 19.55.25 WIB, waktu quote asli N/A. Harga Amerika H/D/A 145/285.0/140; peluang tanpa margin secara proporsional 37,6%/23,9%/38,4% (margin mentah 8,5%). Line gol **3,5**, Over/Under 105.0/-135.0. Line 3,5 tidak dibandingkan langsung dengan probabilitas target 2,5. [Feed](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861194)

Jumlah provider independen terverifikasi **1/3**. Spread bid/ask, kedalaman, BTTS quote dan perubahan 30 menit sebelum kickoff N/A. Belum cukup untuk menyebut anomali terkonfirmasi, informasi internal, keunggulan harga atau keuntungan yang dapat dieksekusi.

## 2. Wales vs Portugal — A4

**Jadwal/venue terverifikasi:** 18 November 02.45 WIB; Cardiff City Stadium, Cardiff, Wales; kandang fisik. [UEFA](https://www.uefa.com/uefanationsleague/match/2047920--wales-vs-portugal/)

**Motivasi:** Portugal 12 poin sudah lolos, tetapi perlu minimal seri untuk mengunci pertama. Wales 3 sudah pasti keempat dan play-off A/B menurut UEFA terbaru. [UEFA: keadaan grup dan aturan](https://www.uefa.com/uefanationsleague/news/02ab-2209792f2fda-6a523d4500bb-1000--nations-league-latest-on-quarter-final-qualification-prom/)

### Wales: lima laga lengkap

| Tanggal | Lawan | H/A/N | GF–GA (90m) | Hasil | xG/xGA | Tembakan | SoT | Bola % | Sumber |
|---|---|---|---|---|---|---:|---:|---:|---|
| 2026-09-24 | Portugal | A | 0–1 | L | N/A / N/A | 5 | 1 | 38,6 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861044) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861044) |
| 2026-09-27 | Denmark | A | 0–2 | L | N/A / N/A | 10 | 3 | 38,4 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861070) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861070) |
| 2026-10-01 | Norway | H | 2–1 | W | N/A / N/A | 12 | 6 | 50,4 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861100) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861100) |
| 2026-10-04 | Denmark | H | 0–1 | L | N/A / N/A | 6 | 1 | 56 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861125) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861125) |
| 2026-11-14 | Norway | A | 1–3 | L | N/A / N/A | 12 | 5 | 45 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861165) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861165) |

Bentuk **L-L-W-L-L**; penguasaan rata-rata 45,68% (n=5), kartu merah total 0. Venue: home: n=2, GF–GA 2–2, menang 1; away: n=3, GF–GA 1–6, menang 0. Jeda antar-kickoff 74,75 jam, bukan pengukuran pemulihan individual.

Gol menit 76–90+: GF 1 / GA 1, cakupan 5/5. Hanya hitungan event yang cocok dengan skor akhir; tidak dipakai sebagai tambahan koefisien model.

### Portugal: lima laga lengkap

| Tanggal | Lawan | H/A/N | GF–GA (90m) | Hasil | xG/xGA | Tembakan | SoT | Bola % | Sumber |
|---|---|---|---|---|---|---:|---:|---:|---|
| 2026-09-24 | Wales | H | 1–0 | W | N/A / N/A | 23 | 5 | 61,4 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861044) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861044) |
| 2026-09-27 | Norway | A | 2–1 | W | N/A / N/A | 12 | 4 | 38 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861073) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861073) |
| 2026-10-01 | Denmark | A | 4–2 | W | N/A / N/A | 19 | 10 | 46,3 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861096) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861096) |
| 2026-10-04 | Norway | H | 2–1 | W | N/A / N/A | 20 | 7 | 58,6 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861126) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861126) |
| 2026-11-14 | Denmark | H | 1–4 | L | N/A / N/A | 15 | 8 | 51,5 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861167) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861167) |

Bentuk **W-W-W-W-L**; penguasaan rata-rata 51,16% (n=5), kartu merah total 1.0. Venue: home: n=3, GF–GA 4–5, menang 2; away: n=2, GF–GA 6–3, menang 2. Jeda antar-kickoff 72 jam, bukan pengukuran pemulihan individual.

Gol menit 76–90+: GF 3 / GA 0, cakupan 5/5. Hanya hitungan event yang cocok dengan skor akhir; tidak dipakai sebagai tambahan koefisien model.

### H2H dan relevansi

| Tanggal | Pertemuan | Skor 90m | Kompetisi | Sumber |
|---|---|---|---|---|
| 2000-06-02 | Portugal–Wales | 3–0 | Friendly | [Arsip](https://github.com/martj42/international_results/blob/b0948cb558c927c357db4067eac5b37b96d0e4bb/results.csv#L24562) |
| 2016-07-06 | Portugal–Wales | 2–0 | UEFA Euro | [Arsip](https://github.com/martj42/international_results/blob/b0948cb558c927c357db4067eac5b37b96d0e4bb/results.csv#L39967) |
| 2026-09-24 | Portugal–Wales | 1–0 | UEFA Nations League | [Arsip](https://www.espn.com/soccer/match/_/gameId/401861044) |

Pertemuan grup 2026 paling relevan. Laga lama/uji coba ditampilkan sebagai konteks; kesinambungan semua pelatih dan susunan historis tidak terverifikasi, sehingga tidak diperlakukan sebagai kekuatan tim saat ini. Penguasaan/xG H2H lintas periode yang sebanding N/A; pertandingan grup yang sama sudah ada dalam lima laga dan tidak dihitung sebagai bukti independen tambahan.

### Pemain dan XI perkiraan

| Tim | Pemain/peran | Status sumber | Pengaruh yang dinilai | Sumber |
|---|---|---|---|---|
| Wales | Ethan Ampadu / Gelandang bertahan | suspended | Sheehan/gelandang lain mengisi; mengurangi kesinambungan perlindungan bek. | [Berita](https://www.sportsmole.co.uk/football/portugal/uefa-nations-league/preview/wales-vs-portugal-prediction-team-news-lineups_609143.html) |
| Wales | Neco Williams / Bek sayap | injured_reported | Connor Roberts diproyeksikan menggantikan; status terakhir perlu XI resmi. | [Berita](https://www.tntsports.co.uk/betting/tips/wales-vs-portugal-prediction-tips-and-odds-nations-league-17-11-26/) |
| Portugal | Ruben Dias / Joao Palhinha / Bek tengah / gelandang bertahan | suspended | Antonio Silva dan Joao Neves merupakan opsi, tanpa potongan persen buatan. | [Berita](https://as.com/futbol/internacional/bernardo-silva-tocado-vuelve-a-madrid-f202611-n/) |
| Portugal | Bernardo Silva / Kreator | withdrawn | Dokter FPF menjelaskan tidak layak untuk laga Wales; dicoret dari proyeksi yang masih memuatnya. | [Berita](https://www.abola.pt/noticias/medico-da-selecao-explica-dispensa-de-bernardo-silva-a-posicao-foi-correta-2026111617005371230) |

**XI Wales (perkiraan):** Darlow; Roberts, Rodon, Davies, Dasilva; Cullen, Sheehan; Johnson, Brooks, Wilson; Koumas.

**XI Portugal (perkiraan):** Diogo Costa; Alberto Costa, Antonio Silva, Renato Veiga, Dalot; Joao Neves, Vitinha; Pedro Neto, Joao Felix, Bruno Fernandes; Ramos.

Proyeksi sekunder diperbarui secara eksplisit: Bernardo tidak dimasukkan, Neto menjadi opsi di tiga pemain belakang striker. Ini inferensi susunan, bukan XI resmi. [Sumber wal-por-preview](https://www.sportsmole.co.uk/football/portugal/uefa-nations-league/preview/wales-vs-portugal-prediction-team-news-lineups_609143.html) · [Sumber wal-por-teamnews](https://www.tntsports.co.uk/betting/tips/wales-vs-portugal-prediction-tips-and-odds-nations-league-17-11-26/) · [Sumber por-medical](https://www.abola.pt/noticias/medico-da-selecao-explica-dispensa-de-bernardo-silva-a-posicao-foi-correta-2026111617005371230) · [Sumber por-departures](https://as.com/futbol/internacional/bernardo-silva-tocado-vuelve-a-madrid-f202611-n/)

**Pola data:** Keunggulan volume dan kualitas skuad Portugal bertemu Wales yang gagal mencetak pada tiga laga. Empat BTTS Portugal berlawanan dengan produktivitas Wales, sehingga BTTS ditahan. Kekalahan 1–4 tetap dihitung, tidak dibuang.

**Taktik/konteks:** Inferensi: Portugal bisa mengontrol tempo karena seri cukup; absennya Dias/Palhinha dapat mengurangi kestabilan transisi tanpa otomatis membuat Wales mencetak gol. Wales kembali dari Oslo ke Cardiff; Portugal dari pertandingan di Braga ke Cardiff. Asal perjalanan ini berdasarkan jadwal, bukan data rute atau jarak tempuh aktual. Tidak tersedia data event lengkap untuk mengukur pressing, transisi, kualitas crossing atau set piece. Tidak dibuat bonus persen dari narasi ini.

### Keputusan per target, seluruhnya dari snapshot yang sama

| Target | Utama (kualitatif) | Beta V2 aktif | Hybrid aktif | Alasan filter Hybrid |
|---|---|---|---|---|
| 1X2 | Portugal menang · Rendah | Portugal menang · 66,0% | Portugal menang · 66,0% | Arah utama dan Beta sepakat, ambang terpenuhi |
| BTTS | Observasi | Observasi | Observasi | Observasi utama dipertahankan |
| Total 2,5 | Observasi | Observasi | Observasi | Observasi utama dipertahankan |

**Fokus Beta:** Portugal menang · 66,0%. **Fokus Hybrid:** Portugal menang · 66,0%.

**Alasan dan kontra utama yang dibekukan:**

- 1X2: Portugal empat kemenangan, produksi 17,8 tembakan/6,8 SoT; Wales kalah 4/5.; Portugal masih mengejar posisi pertama, bukan sekadar laga tanpa target. Kontra/batas: Dias dan Palhinha skors; Bernardo Silva pulang; baru kalah 1–4.; Hanya seri sudah cukup; Wales bermain di Cardiff.
- BTTS: Portugal BTTS 4/5 dan Wales belum clean sheet. Kontra/batas: Wales gagal mencetak 3/5; Ampadu skors dan kondisi Neco Williams melemahkan kepastian serangan.
- Total 2,5: Portugal Over 4/5. Kontra/batas: Wales Under 3/5; perubahan pertahanan Portugal dan tempo mengejar seri bisa memberi skenario berlawanan.

**Skenario utama, bukan exact-score pick:** 0–2. **Pemicu penilaian ulang:** Jika Portugal merotasi luas di depan atau Wales dapat menekan bek pengganti, arah tandang semakin rapuh. Jangan menaikkan keyakinan hanya karena favorit.

**Clean sheet model mentah:** Wales 21,8%, Portugal 32,2%, dari resep mentah strength_h730. Ini estimasi Poisson mentah tanpa kalibrasi khusus clean sheet; berbeda dari frekuensi CS historis dan bukan konsekuensi tunggal tabel marginal terkalibrasi.

**Sensitivitas lima laga lama (diagnostik):** menghilangkan satu dari 9 pertandingan unik secara bergantian menghasilkan perubahan arah 1X2/BTTS/total sebanyak 0/0/0. Ini diagnostik rumus lima laga mentah, bukan uji sensitivitas rating Beta V2 atau interval keyakinan; hasil ekstrem tidak dibuang dari model.

| Resep mentah | Laju gol H/A | Skor MC teratas | Frekuensi sampel |
|---|---|---|---|
| strength_h730 | 1,13/1,52 | 1–1 | 12,4% |
| strength_h365_plus_friendlies | 1,14/1,41 | 1–1 | 12,0% |

MC: 10.000 sampel **per resep** dengan seed tetap. Skor paling sering tetap hanya satu skenario; tidak otomatis menjadi pilihan 1X2/BTTS/total terkalibrasi.

**Pembanding pasar:** DraftKings via ESPN, diambil 17 Nov 2026 19.55.25 WIB, waktu quote asli N/A. Harga Amerika H/D/A 550/380.0/-250; peluang tanpa margin secara proporsional 14,3%/19,4%/66,4% (margin mentah 7,6%). Line gol **3,5**, Over/Under 120.0/-150.0. Line 3,5 tidak dibandingkan langsung dengan probabilitas target 2,5. [Feed](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861189)

Jumlah provider independen terverifikasi **1/3**. Spread bid/ask, kedalaman, BTTS quote dan perubahan 30 menit sebelum kickoff N/A. Belum cukup untuk menyebut anomali terkonfirmasi, informasi internal, keunggulan harga atau keuntungan yang dapat dieksekusi.

## 3. Bosnia & Herzegovina vs Rumania — B4

**Jadwal/venue terverifikasi:** 18 November 02.45 WIB; Bilino Polje Stadium, Zenica, Bosnia and Herzegovina; kandang fisik. [UEFA](https://www.uefa.com/uefanationsleague/match/2047917--bosnia-and-herzegovina-vs-romania/)

**Motivasi:** Bosnia 8 poin sudah pasti kedua. Rumania 3 mengejar Polandia 4; posisi keempat berujung play-off B/C, posisi ketiga tetap B. Bukan degradasi otomatis sesuai aturan lama. [UEFA: keadaan grup dan aturan](https://www.uefa.com/uefanationsleague/news/02ab-2209792f2fda-6a523d4500bb-1000--nations-league-latest-on-quarter-final-qualification-prom/)

### Bosnia and Herzegovina: lima laga lengkap

| Tanggal | Lawan | H/A/N | GF–GA (90m) | Hasil | xG/xGA | Tembakan | SoT | Bola % | Sumber |
|---|---|---|---|---|---|---:|---:|---:|---|
| 2026-09-25 | Poland | A | 0–0 | D | N/A / N/A | 9 | 1 | 50,2 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861055) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861055) |
| 2026-09-28 | Romania | A | 4–2 | W | N/A / N/A | 15 | 7 | 43,6 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861078) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861078) |
| 2026-10-02 | Sweden | H | 1–1 | D | N/A / N/A | 4 | 2 | 50,6 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861107) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861107) |
| 2026-10-05 | Poland | H | 1–0 | W | N/A / N/A | 9 | 1 | 44,5 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861133) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861133) |
| 2026-11-14 | Sweden | A | 2–3 | L | N/A / N/A | 16 | 7 | 57,8 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861166) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861166) |

Bentuk **D-W-D-W-L**; penguasaan rata-rata 49,34% (n=5), kartu merah total 0. Venue: home: n=2, GF–GA 2–1, menang 1; away: n=3, GF–GA 6–5, menang 1. Jeda antar-kickoff 72 jam, bukan pengukuran pemulihan individual.

Gol menit 76–90+: GF 2 / GA 0, cakupan 5/5. Hanya hitungan event yang cocok dengan skor akhir; tidak dipakai sebagai tambahan koefisien model.

### Romania: lima laga lengkap

| Tanggal | Lawan | H/A/N | GF–GA (90m) | Hasil | xG/xGA | Tembakan | SoT | Bola % | Sumber |
|---|---|---|---|---|---|---:|---:|---:|---|
| 2026-09-25 | Sweden | A | 1–2 | L | N/A / N/A | 10 | 1 | 40,3 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861051) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861051) |
| 2026-09-28 | Bosnia and Herzegovina | H | 2–4 | L | N/A / N/A | 13 | 4 | 56,4 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861078) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861078) |
| 2026-10-02 | Poland | A | 0–6 | L | N/A / N/A | 10 | 3 | 33,2 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861108) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861108) |
| 2026-10-05 | Sweden | H | 0–1 | L | N/A / N/A | 13 | 4 | 52,1 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861128) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861128) |
| 2026-11-14 | Poland | H | 2–1 | W | N/A / N/A | 11 | 4 | 44,3 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861168) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861168) |

Bentuk **L-L-L-L-W**; penguasaan rata-rata 45,26% (n=5), kartu merah total 1.0. Venue: home: n=3, GF–GA 4–6, menang 1; away: n=2, GF–GA 1–8, menang 0. Jeda antar-kickoff 72 jam, bukan pengukuran pemulihan individual.

Gol menit 76–90+: GF 0 / GA 2, cakupan 5/5. Hanya hitungan event yang cocok dengan skor akhir; tidak dipakai sebagai tambahan koefisien model.

### H2H dan relevansi

| Tanggal | Pertemuan | Skor 90m | Kompetisi | Sumber |
|---|---|---|---|---|
| 2022-06-07 | Bosnia and Herzegovina–Romania | 1–0 | UEFA Nations League | [Arsip](https://github.com/martj42/international_results/blob/b0948cb558c927c357db4067eac5b37b96d0e4bb/results.csv#L45317) |
| 2022-09-26 | Romania–Bosnia and Herzegovina | 4–1 | UEFA Nations League | [Arsip](https://github.com/martj42/international_results/blob/b0948cb558c927c357db4067eac5b37b96d0e4bb/results.csv#L45608) |
| 2025-03-21 | Romania–Bosnia and Herzegovina | 0–1 | FIFA World Cup qualification | [Arsip](https://github.com/martj42/international_results/blob/b0948cb558c927c357db4067eac5b37b96d0e4bb/results.csv#L48235) |
| 2025-11-15 | Bosnia and Herzegovina–Romania | 3–1 | FIFA World Cup qualification | [Arsip](https://github.com/martj42/international_results/blob/b0948cb558c927c357db4067eac5b37b96d0e4bb/results.csv#L48976) |
| 2026-09-28 | Romania–Bosnia and Herzegovina | 2–4 | UEFA Nations League | [Arsip](https://www.espn.com/soccer/match/_/gameId/401861078) |

Pertemuan grup 2026 paling relevan. Laga lama/uji coba ditampilkan sebagai konteks; kesinambungan semua pelatih dan susunan historis tidak terverifikasi, sehingga tidak diperlakukan sebagai kekuatan tim saat ini. Penguasaan/xG H2H lintas periode yang sebanding N/A; pertandingan grup yang sama sudah ada dalam lima laga dan tidak dihitung sebagai bukti independen tambahan.

### Pemain dan XI perkiraan

| Tim | Pemain/peran | Status sumber | Pengaruh yang dinilai | Sumber |
|---|---|---|---|---|
| Bosnia and Herzegovina | Haris Tabakovic / Striker | doubtful | Keluar pada menit 39 melawan Swedia dengan masalah lutut; Mahmic opsi. | [Berita](https://www.sportsmole.co.uk/football/bosnia-herzegovina/uefa-nations-league/preview/bosnia-hvina-vs-romania-prediction-team-news-lineups_609182.html) |
| Bosnia and Herzegovina | Dennis Hadzikadunic / Bek tengah | injured_reported | Katic/Radeljic diproyeksikan menjaga pusat pertahanan. | [Berita](https://www.sportsmole.co.uk/football/bosnia-herzegovina/uefa-nations-league/preview/bosnia-hvina-vs-romania-prediction-team-news-lineups_609182.html) |
| Romania | Tudor Baluta / Gelandang | suspended | Cicaldau/Screciu/Dragomir menjadi opsi lini tengah. | [Berita](https://www.sportsmole.co.uk/football/bosnia-herzegovina/uefa-nations-league/preview/bosnia-hvina-vs-romania-prediction-team-news-lineups_609182.html) |

**XI Bosnia & Herzegovina (perkiraan):** Zlomislic; Dedic, Katic, Radeljic, Kolasinac; Bajraktarevic, Basic, Gigovic, Alajbegovic; Mahmic, Demirovic.

**XI Rumania (perkiraan):** Hindrich; Ratiu, Coubis, Dragusin, Eissat; Cicaldau, Screciu, Dragomir; Ianis Hagi; Coman, Man.

XI perkiraan sekunder; kesiapan Tabakovic dan potensi rotasi Bosnia belum dikonfirmasi. [Sumber bih-rou-preview](https://www.sportsmole.co.uk/football/bosnia-herzegovina/uefa-nations-league/preview/bosnia-hvina-vs-romania-prediction-team-news-lineups_609182.html)

**Pola data:** Empat gol pada pertemuan pertama menyumbang separuh GF Bosnia, sedangkan 0–6 menyumbang 43% GA Rumania. Dua skor besar tidak dihapus; keduanya alasan menahan kepastian pada total gol.

**Taktik/konteks:** Inferensi: kebutuhan Rumania menang bisa memperlebar ruang, tetapi Bosnia yang sudah aman bisa menurunkan intensitas. Tidak ada data event cukup untuk klaim pressing khusus. Rumania berpindah dari pertandingan kandang ke Zenica; rincian rute/kedatangan tidak terverifikasi. Tidak tersedia data event lengkap untuk mengukur pressing, transisi, kualitas crossing atau set piece. Tidak dibuat bonus persen dari narasi ini.

### Keputusan per target, seluruhnya dari snapshot yang sama

| Target | Utama (kualitatif) | Beta V2 aktif | Hybrid aktif | Alasan filter Hybrid |
|---|---|---|---|---|
| 1X2 | Bosnia & Herzegovina menang · Sedang | Observasi | Observasi | Arah utama dan Beta berbeda |
| BTTS | BTTS Ya · Rendah | Observasi | Observasi | Arah utama dan Beta berbeda |
| Total 2,5 | Observasi | Observasi | Observasi | Observasi utama dipertahankan |

**Fokus Beta:** Observasi. **Fokus Hybrid:** Observasi.

**Alasan dan kontra utama yang dibekukan:**

- 1X2: Bosnia kalah hanya sekali, tidak kalah pada dua laga kandang UNL; menang 4–2 pada pertemuan pertama.; Rumania kebobolan 14 gol; kalah dalam dua tandang grup. Kontra/batas: Bosnia sudah pasti kedua dan dapat merotasi; Rumania baru menang atas Polandia.; Tabakovic diragukan, Hadzikadunic absen.
- BTTS: Bosnia dan Rumania sama-sama BTTS 3/5; Rumania harus mengejar kemenangan. Kontra/batas: Rumania gagal mencetak pada dua laga; Bosnia tiga laga terakhir kandang/kelompok tidak selalu terbuka.
- Total 2,5: Rumania Over 4/5 dan mengejar tiga poin. Kontra/batas: Bosnia Under 3/5; skor 0–6 menyumbang 6 dari 14 kebobolan Rumania sehingga rerata rentan hasil ekstrem.

**Skenario utama, bukan exact-score pick:** 2–1. **Pemicu penilaian ulang:** Rotasi luas Bosnia atau Tabakovic/penyerang utama lain tidak tersedia dapat menghapus keunggulan kandang. Gol awal Rumania mengubah keseimbangan kebutuhan.

**Clean sheet model mentah:** Bosnia & Herzegovina 32,0%, Rumania 24,2%, dari resep mentah strength_h730. Ini estimasi Poisson mentah tanpa kalibrasi khusus clean sheet; berbeda dari frekuensi CS historis dan bukan konsekuensi tunggal tabel marginal terkalibrasi.

**Sensitivitas lima laga lama (diagnostik):** menghilangkan satu dari 9 pertandingan unik secara bergantian menghasilkan perubahan arah 1X2/BTTS/total sebanyak 0/2/2. Ini diagnostik rumus lima laga mentah, bukan uji sensitivitas rating Beta V2 atau interval keyakinan; hasil ekstrem tidak dibuang dari model.

| Resep mentah | Laju gol H/A | Skor MC teratas | Frekuensi sampel |
|---|---|---|---|
| strength_h730 | 1,42/1,14 | 1–1 | 12,2% |
| strength_h365_plus_friendlies | 1,62/1,01 | 1–1 | 11,8% |

MC: 10.000 sampel **per resep** dengan seed tetap. Skor paling sering tetap hanya satu skenario; tidak otomatis menjadi pilihan 1X2/BTTS/total terkalibrasi.

**Pembanding pasar:** DraftKings via ESPN, diambil 17 Nov 2026 19.55.25 WIB, waktu quote asli N/A. Harga Amerika H/D/A 110/245.0/220; peluang tanpa margin secara proporsional 44,2%/26,9%/29,0% (margin mentah 7,9%). Line gol **2,5**, Over/Under -135.0/105.0. Line ini sesuai target 2,5, tetapi harga belum diverifikasi lintas provider. [Feed](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861196)

Jumlah provider independen terverifikasi **1/3**. Spread bid/ask, kedalaman, BTTS quote dan perubahan 30 menit sebelum kickoff N/A. Belum cukup untuk menyebut anomali terkonfirmasi, informasi internal, keunggulan harga atau keuntungan yang dapat dieksekusi.

## 4. Hungaria vs Irlandia Utara — B2

**Jadwal/venue terverifikasi:** 18 November 02.45 WIB; Puskás Aréna, Budapest, Hungary; kandang fisik. [UEFA](https://www.uefa.com/uefanationsleague/match/2047921--hungary-vs-northern-ireland/)

**Motivasi:** Hungaria 10 poin harus menang untuk promosi langsung; Irlandia Utara 11 cukup seri. Keduanya sudah pasti dua besar. [UEFA: keadaan grup dan aturan](https://www.uefa.com/uefanationsleague/news/02ab-2209792f2fda-6a523d4500bb-1000--nations-league-latest-on-quarter-final-qualification-prom/)

### Hungary: lima laga lengkap

| Tanggal | Lawan | H/A/N | GF–GA (90m) | Hasil | xG/xGA | Tembakan | SoT | Bola % | Sumber |
|---|---|---|---|---|---|---:|---:|---:|---|
| 2026-09-25 | Ukraine | H | 0–1 | L | N/A / N/A | 17 | 4 | 57 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861054) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861054) |
| 2026-09-28 | Northern Ireland | A | 0–0 | D | N/A / N/A | 13 | 1 | 63,9 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861079) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861079) |
| 2026-10-02 | Georgia | H | 1–0 | W | N/A / N/A | 26 | 8 | 41,9 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861102) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861102) |
| 2026-10-05 | Ukraine | N | 2–1 | W | N/A / N/A | 10 | 4 | 47,7 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861134) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861134) |
| 2026-11-14 | Georgia | A | 2–0 | W | N/A / N/A | 12 | 6 | 46,6 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861164) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861164) |

Bentuk **L-D-W-W-W**; penguasaan rata-rata 51,42% (n=5), kartu merah total 0. Venue: home: n=2, GF–GA 1–1, menang 1; away: n=2, GF–GA 2–0, menang 1; neutral: n=1, GF–GA 2–1, menang 1. Jeda antar-kickoff 74,75 jam, bukan pengukuran pemulihan individual.

Gol menit 76–90+: GF 2 / GA 1, cakupan 5/5. Hanya hitungan event yang cocok dengan skor akhir; tidak dipakai sebagai tambahan koefisien model.

### Northern Ireland: lima laga lengkap

| Tanggal | Lawan | H/A/N | GF–GA (90m) | Hasil | xG/xGA | Tembakan | SoT | Bola % | Sumber |
|---|---|---|---|---|---|---:|---:|---:|---|
| 2026-09-25 | Georgia | A | 1–0 | W | N/A / N/A | 12 | 5 | 37,8 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861049) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861049) |
| 2026-09-28 | Hungary | H | 0–0 | D | N/A / N/A | 10 | 3 | 36,1 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861079) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861079) |
| 2026-10-02 | Ukraine | N | 3–0 | W | N/A / N/A | 10 | 3 | 27,6 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861106) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861106) |
| 2026-10-05 | Georgia | H | 0–0 | D | N/A / N/A | 15 | 5 | 38,3 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861132) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861132) |
| 2026-11-14 | Ukraine | H | 1–0 | W | N/A / N/A | 15 | 5 | 38,1 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861169) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861169) |

Bentuk **W-D-W-D-W**; penguasaan rata-rata 35,58% (n=5), kartu merah total 0. Venue: home: n=3, GF–GA 1–0, menang 1; away: n=1, GF–GA 1–0, menang 1; neutral: n=1, GF–GA 3–0, menang 1. Jeda antar-kickoff 72 jam, bukan pengukuran pemulihan individual.

Gol menit 76–90+: GF 1 / GA 0, cakupan 5/5. Hanya hitungan event yang cocok dengan skor akhir; tidak dipakai sebagai tambahan koefisien model.

### H2H dan relevansi

| Tanggal | Pertemuan | Skor 90m | Kompetisi | Sumber |
|---|---|---|---|---|
| 2008-11-19 | Northern Ireland–Hungary | 0–2 | Friendly | [Arsip](https://github.com/martj42/international_results/blob/b0948cb558c927c357db4067eac5b37b96d0e4bb/results.csv#L32605) |
| 2014-09-07 | Hungary–Northern Ireland | 1–2 | UEFA Euro qualification | [Arsip](https://github.com/martj42/international_results/blob/b0948cb558c927c357db4067eac5b37b96d0e4bb/results.csv#L38060) |
| 2015-09-07 | Northern Ireland–Hungary | 1–1 | UEFA Euro qualification | [Arsip](https://github.com/martj42/international_results/blob/b0948cb558c927c357db4067eac5b37b96d0e4bb/results.csv#L39102) |
| 2022-03-29 | Northern Ireland–Hungary | 0–1 | Friendly | [Arsip](https://github.com/martj42/international_results/blob/b0948cb558c927c357db4067eac5b37b96d0e4bb/results.csv#L45140) |
| 2026-09-28 | Northern Ireland–Hungary | 0–0 | UEFA Nations League | [Arsip](https://www.espn.com/soccer/match/_/gameId/401861079) |

Pertemuan grup 2026 paling relevan. Laga lama/uji coba ditampilkan sebagai konteks; kesinambungan semua pelatih dan susunan historis tidak terverifikasi, sehingga tidak diperlakukan sebagai kekuatan tim saat ini. Penguasaan/xG H2H lintas periode yang sebanding N/A; pertandingan grup yang sama sudah ada dalam lima laga dan tidak dihitung sebagai bukti independen tambahan.

### Pemain dan XI perkiraan

| Tim | Pemain/peran | Status sumber | Pengaruh yang dinilai | Sumber |
|---|---|---|---|---|
| Hungary | Willi Orban / Milan Vitalis / Bek tengah / gelandang | suspended | Attila Szalai/Rajmund Toth diproyeksikan masuk. | [Berita](https://www.sportsmole.co.uk/football/hungary/nations-league-predictions/preview/hungary-vs-n-ireland-prediction-team-news-lineups_609115.html) |
| Hungary | Dominik Szoboszlai / Kreator | fitness_watch | Diharapkan bermain, tetapi keluhan kondisi sebelumnya menuntut konfirmasi XI. | [Berita](https://www.sportsmole.co.uk/football/hungary/nations-league-predictions/preview/hungary-vs-n-ireland-prediction-team-news-lineups_609115.html) |
| Northern Ireland | Jamie Donley / Striker | suspended | Magennis kandidat pengganti; pemain lain di kamp dilaporkan tersedia. | [Berita](https://www.irishfa.com/news/2026/november/o-neill-wants-players-to-show-spirit-and-conviction-against-hungary) |
| Northern Ireland | Michael ONeill / Pelatih | touchline_suspension | Taktik disiapkan sebelumnya; staf mengambil komunikasi dari pinggir lapangan. | [Berita](https://www.irishfa.com/news/2026/november/o-neill-wants-players-to-show-spirit-and-conviction-against-hungary) |

**XI Hungaria (perkiraan):** B Toth; Osvath, Szalai, Csinger, Kerkez; R Toth, Schafer; Sallai, Szoboszlai, Nagy; Varga.

**XI Irlandia Utara (perkiraan):** P Charles; Atcheson, McConville, Brown; Devlin, Hume, S Charles, Devenny; Galbraith, Magennis, Price.

Proyeksi sekunder dengan larangan bermain dikonfirmasi Irish FA untuk Donley; tidak semua nama pengganti terkonfirmasi. [Sumber hun-nir-preview](https://www.sportsmole.co.uk/football/hungary/nations-league-predictions/preview/hungary-vs-n-ireland-prediction-team-news-lineups_609115.html) · [Sumber ifa-preview](https://www.irishfa.com/news/2026/november/o-neill-wants-players-to-show-spirit-and-conviction-against-hungary)

**Pola data:** NI belum kebobolan dalam lima laga; Hungaria hanya kebobolan dua. Kemenangan tandang 3–0 NI adalah satu-satunya laga lebih dari satu gol mereka, sehingga rata-rata tidak menyiratkan serangan produktif merata.

**Taktik/konteks:** Inferensi: NI tidak harus membuka laga, sementara Hungaria mungkin menaikkan risiko setelah turun minum. Absennya Orban menghalangi penyamaan clean sheet historis dengan peluang pasti. NI dari laga Belfast ke Budapest; rincian transportasi dan pemulihan individual tidak tersedia. Tidak tersedia data event lengkap untuk mengukur pressing, transisi, kualitas crossing atau set piece. Tidak dibuat bonus persen dari narasi ini.

### Keputusan per target, seluruhnya dari snapshot yang sama

| Target | Utama (kualitatif) | Beta V2 aktif | Hybrid aktif | Alasan filter Hybrid |
|---|---|---|---|---|
| 1X2 | Observasi | Observasi | Observasi | Observasi utama dipertahankan |
| BTTS | BTTS Tidak · Sedang | BTTS Tidak · 60,2% | BTTS Tidak · 60,2% | Arah utama dan Beta sepakat, ambang terpenuhi |
| Total 2,5 | Under 2,5 · Relatif kuat | Under 2,5 · 64,4% | Under 2,5 · 64,4% | Arah utama dan Beta sepakat, ambang terpenuhi |

**Fokus Beta:** Under 2,5 · 64,4%. **Fokus Hybrid:** Under 2,5 · 64,4%.

**Alasan dan kontra utama yang dibekukan:**

- 1X2: Hungaria menang tiga kali beruntun dan menjadi tuan rumah. Kontra/batas: Irlandia Utara belum kebobolan dan belum kalah; Orban serta Vitalis skors; hasil seri cukup bagi tamu.
- BTTS: Irlandia Utara clean sheet 5/5; Hungaria clean sheet 3/5; pertemuan pertama 0–0. Kontra/batas: Orban absen; Hungaria harus mengejar menang sehingga risiko transisi menit akhir meningkat.
- Total 2,5: Empat dari lima laga masing-masing tim Under; NI mencetak lebih dari satu hanya sekali.; Donley skors mengurangi opsi penyerang NI; struktur pertahanan tamu terjaga. Kontra/batas: Gol cepat mengubah kebutuhan taktik; kehilangan Orban dapat merusak keseimbangan Hungaria.

**Skenario utama, bukan exact-score pick:** 1–0. **Pemicu penilaian ulang:** Gol awal, penalti atau Hungaria tertinggal dapat meniadakan tempo rendah. Ketiadaan Orban dapat memberi NI jalur gol meski Donley absen.

**Clean sheet model mentah:** Hungaria 42,6%, Irlandia Utara 31,8%, dari resep mentah strength_h730. Ini estimasi Poisson mentah tanpa kalibrasi khusus clean sheet; berbeda dari frekuensi CS historis dan bukan konsekuensi tunggal tabel marginal terkalibrasi.

**Sensitivitas lima laga lama (diagnostik):** menghilangkan satu dari 9 pertandingan unik secara bergantian menghasilkan perubahan arah 1X2/BTTS/total sebanyak 4/0/0. Ini diagnostik rumus lima laga mentah, bukan uji sensitivitas rating Beta V2 atau interval keyakinan; hasil ekstrem tidak dibuang dari model.

| Resep mentah | Laju gol H/A | Skor MC teratas | Frekuensi sampel |
|---|---|---|---|
| strength_h730 | 1,15/0,85 | 1–0 | 15,4% |
| strength_h365_plus_friendlies | 1,16/0,85 | 1–0 | 14,9% |

MC: 10.000 sampel **per resep** dengan seed tetap. Skor paling sering tetap hanya satu skenario; tidak otomatis menjadi pilihan 1X2/BTTS/total terkalibrasi.

**Pembanding pasar:** DraftKings via ESPN, diambil 17 Nov 2026 19.55.25 WIB, waktu quote asli N/A. Harga Amerika H/D/A -105/215.0/300; peluang tanpa margin secara proporsional 47,4%/29,4%/23,2% (margin mentah 8,0%). Line gol **2,5**, Over/Under 135.0/-175.0. Line ini sesuai target 2,5, tetapi harga belum diverifikasi lintas provider. [Feed](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861191)

Jumlah provider independen terverifikasi **1/3**. Spread bid/ask, kedalaman, BTTS quote dan perubahan 30 menit sebelum kickoff N/A. Belum cukup untuk menyebut anomali terkonfirmasi, informasi internal, keunggulan harga atau keuntungan yang dapat dieksekusi.

## 5. Irlandia vs Kosovo — B3

**Jadwal/venue terverifikasi:** 18 November 02.45 WIB; Aviva Stadium, Dublin, ; kandang fisik. [UEFA](https://www.uefa.com/uefanationsleague/match/2047923--republic-of-ireland-vs-kosovo/)

**Motivasi:** Ireland 5 poin harus menang untuk melewati Kosovo 6 dan mengambil posisi kedua; seri mempertahankan keunggulan Kosovo. [UEFA: keadaan grup dan aturan](https://www.uefa.com/uefanationsleague/news/02ab-2209792f2fda-6a523d4500bb-1000--nations-league-latest-on-quarter-final-qualification-prom/)

### Republic of Ireland: lima laga lengkap

| Tanggal | Lawan | H/A/N | GF–GA (90m) | Hasil | xG/xGA | Tembakan | SoT | Bola % | Sumber |
|---|---|---|---|---|---|---:|---:|---:|---|
| 2026-09-24 | Kosovo | A | 0–1 | L | N/A / N/A | 3 | 1 | 42,7 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861045) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861045) |
| 2026-09-27 | Israel | N | 3–0 | W | N/A / N/A | 9 | 3 | 35,9 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861072) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861072) |
| 2026-10-01 | Austria | H | 2–2 | D | N/A / N/A | 9 | 3 | 41,9 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861094) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861094) |
| 2026-10-04 | Israel | N | 1–1 | D | N/A / N/A | 16 | 4 | 54,9 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861124) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861124) |
| 2026-11-14 | Austria | A | 0–1 | L | N/A / N/A | 17 | 7 | 44,9 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861170) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861170) |

Bentuk **L-W-D-D-L**; penguasaan rata-rata 44,06% (n=5), kartu merah total 0. Venue: home: n=1, GF–GA 2–2, menang 0; away: n=2, GF–GA 0–2, menang 0; neutral: n=2, GF–GA 4–1, menang 1. Jeda antar-kickoff 72 jam, bukan pengukuran pemulihan individual.

Gol menit 76–90+: GF 0 / GA 3, cakupan 5/5. Hanya hitungan event yang cocok dengan skor akhir; tidak dipakai sebagai tambahan koefisien model.

### Kosovo: lima laga lengkap

| Tanggal | Lawan | H/A/N | GF–GA (90m) | Hasil | xG/xGA | Tembakan | SoT | Bola % | Sumber |
|---|---|---|---|---|---|---:|---:|---:|---|
| 2026-09-24 | Republic of Ireland | H | 1–0 | W | N/A / N/A | 22 | 8 | 57,3 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861045) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861045) |
| 2026-09-27 | Austria | A | 1–3 | L | N/A / N/A | 6 | 1 | 48 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861071) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861071) |
| 2026-10-01 | Israel | N | 0–0 | D | N/A / N/A | 18 | 3 | 54,7 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861095) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861095) |
| 2026-10-04 | Austria | H | 1–1 | D | N/A / N/A | 10 | 5 | 35,8 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861121) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861121) |
| 2026-11-14 | Israel | H | 0–0 | D | N/A / N/A | 16 | 3 | 46 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861163) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861163) |

Bentuk **W-L-D-D-D**; penguasaan rata-rata 48,36% (n=5), kartu merah total 1.0. Venue: home: n=3, GF–GA 2–1, menang 1; away: n=1, GF–GA 1–3, menang 0; neutral: n=1, GF–GA 0–0, menang 0. Jeda antar-kickoff 77,75 jam, bukan pengukuran pemulihan individual.

Gol menit 76–90+: GF 2 / GA 1, cakupan 5/5. Hanya hitungan event yang cocok dengan skor akhir; tidak dipakai sebagai tambahan koefisien model.

### H2H dan relevansi

| Tanggal | Pertemuan | Skor 90m | Kompetisi | Sumber |
|---|---|---|---|---|
| 2026-09-24 | Kosovo–Republic of Ireland | 1–0 | UEFA Nations League | [Arsip](https://www.espn.com/soccer/match/_/gameId/401861045) |

Pertemuan grup 2026 paling relevan. Laga lama/uji coba ditampilkan sebagai konteks; kesinambungan semua pelatih dan susunan historis tidak terverifikasi, sehingga tidak diperlakukan sebagai kekuatan tim saat ini. Penguasaan/xG H2H lintas periode yang sebanding N/A; pertandingan grup yang sama sudah ada dalam lima laga dan tidak dihitung sebagai bukti independen tambahan.

### Pemain dan XI perkiraan

| Tim | Pemain/peran | Status sumber | Pengaruh yang dinilai | Sumber |
|---|---|---|---|---|
| Republic of Ireland | Nathan Collins / Kapten / bek tengah | withdrawn | Egan atau OBrien pengganti posisi; Jimmy Dunne masuk skuad. | [Berita](https://www.fai.ie/latest/match-preview-mnt-republic-ireland-v-kosovo/) |
| Republic of Ireland | James Abankwah / Bek | available | FAI mengonfirmasi pulih dari kram. | [Berita](https://www.fai.ie/latest/match-preview-mnt-republic-ireland-v-kosovo/) |
| Kosovo | Edon Zhegrova / Penyerang sayap | withdrawn_reported | RTE dan Irish Times melaporkan cedera/pulang; tidak dimasukkan ke proyeksi meski bermain 14 November. | [Berita](https://www.rte.ie/sport/soccer/2026/1116/1599361-republic-of-ireland-v-kosovo-all-you-need-to-know/) |
| Kosovo | Veldin Hodza / Gelandang | suspended | Rexhbecaj kandidat menggantikan setelah kartu merah melawan Israel. | [Berita](https://www.rte.ie/sport/soccer/2026/1116/1599361-republic-of-ireland-v-kosovo-all-you-need-to-know/) |

**XI Irlandia (perkiraan):** Kelleher; Abankwah, OShea, Egan, Scales, Manning; Azaz, Molumby; Moylan, Idah; Parrott.

**XI Kosovo (perkiraan):** Saipi; Kamberi, Krasniqi, Hajrizi; Vojvoda, Rexhbecaj, Avdullahu, Gallapeni; Rashica, Zabergja; Muriqi.

XI perkiraan Irish Times 16 November; susunan/formasi dapat berubah, bukan XI resmi. [Sumber fai-preview](https://www.fai.ie/latest/match-preview-mnt-republic-ireland-v-kosovo/) · [Sumber irl-kos-teamnews](https://www.rte.ie/sport/soccer/2026/1116/1599361-republic-of-ireland-v-kosovo-all-you-need-to-know/) · [Sumber irl-kos-xi](https://www.irishtimes.com/sport/soccer/2026/11/16/irelands-nations-league-campaign-comes-down-to-must-win-kosovo-clash/)

**Pola data:** Kosovo tiga hasil seri beruntun dan Under 4/5, tetapi membuat 16 tembakan tanpa gol melawan Israel. Puasa gol bukan bukti tidak mampu mencipta peluang; kebutuhan Ireland menang meningkatkan risiko di ujung laga.

**Taktik/konteks:** Inferensi: Ireland lebih banyak mengambil inisiatif; Kosovo dapat melindungi ruang tanpa selalu bertahan rendah. Tidak ada parameter motivasi atau cedera baru yang diterapkan numerik. Ireland kembali dari Linz, Kosovo setelah bermain di Pristina; jadwal diketahui, rute dan durasi perjalanan tidak. Tidak tersedia data event lengkap untuk mengukur pressing, transisi, kualitas crossing atau set piece. Tidak dibuat bonus persen dari narasi ini.

### Keputusan per target, seluruhnya dari snapshot yang sama

| Target | Utama (kualitatif) | Beta V2 aktif | Hybrid aktif | Alasan filter Hybrid |
|---|---|---|---|---|
| 1X2 | Irlandia menang · Rendah | Observasi | Observasi | Arah utama dan Beta berbeda |
| BTTS | Observasi | BTTS Tidak · 59,3% | Observasi | Observasi utama dipertahankan |
| Total 2,5 | Under 2,5 · Sedang | Under 2,5 · 61,3% | Under 2,5 · 61,3% | Arah utama dan Beta sepakat, ambang terpenuhi |

**Fokus Beta:** Under 2,5 · 61,3%. **Fokus Hybrid:** Under 2,5 · 61,3%.

**Alasan dan kontra utama yang dibekukan:**

- 1X2: FAI mengonfirmasi target menang dan rekor tanpa kalah kandang lebih panjang; Kosovo belum menang dalam empat laga grup terakhir.; Zhegrova absen dan Hodza skors mempersempit opsi lawan. Kontra/batas: Ireland hanya menang 1/5; kalah pada pertemuan pertama; Collins tidak tersedia.
- BTTS: Collins absen dapat memberi ruang untuk Muriqi. Kontra/batas: Kosovo dua kali gagal mencetak dan tanpa Zhegrova; Ireland dua kali gagal mencetak.
- Total 2,5: Kosovo Under 4/5; Ireland Under 3/5; pertemuan pertama 1–0.; Tamu dapat mempertahankan posisi kedua dengan hasil seri. Kontra/batas: Ireland harus menang; Collins absen dan tekanan menit akhir bisa membuka laga.

**Skenario utama, bukan exact-score pick:** 1–0. **Pemicu penilaian ulang:** Gol cepat Kosovo memaksa Ireland mengejar. Kehilangan Collins dapat membuat peluang Muriqi lebih bernilai; ketajaman Parrott bisa mempercepat terbukanya skor.

**Clean sheet model mentah:** Irlandia 40,5%, Kosovo 31,2%, dari resep mentah strength_h730. Ini estimasi Poisson mentah tanpa kalibrasi khusus clean sheet; berbeda dari frekuensi CS historis dan bukan konsekuensi tunggal tabel marginal terkalibrasi.

**Sensitivitas lima laga lama (diagnostik):** menghilangkan satu dari 9 pertandingan unik secara bergantian menghasilkan perubahan arah 1X2/BTTS/total sebanyak 1/0/0. Ini diagnostik rumus lima laga mentah, bukan uji sensitivitas rating Beta V2 atau interval keyakinan; hasil ekstrem tidak dibuang dari model.

| Resep mentah | Laju gol H/A | Skor MC teratas | Frekuensi sampel |
|---|---|---|---|
| strength_h730 | 1,16/0,9 | 1–0 | 14,7% |
| strength_h365_plus_friendlies | 1,28/0,89 | 1–0 | 14,2% |

MC: 10.000 sampel **per resep** dengan seed tetap. Skor paling sering tetap hanya satu skenario; tidak otomatis menjadi pilihan 1X2/BTTS/total terkalibrasi.

**Pembanding pasar:** DraftKings via ESPN, diambil 17 Nov 2026 19.55.27 WIB, waktu quote asli N/A. Harga Amerika H/D/A 100/215.0/285; peluang tanpa margin secara proporsional 46,4%/29,5%/24,1% (margin mentah 7,7%). Line gol **2,5**, Over/Under 135.0/-175.0. Line ini sesuai target 2,5, tetapi harga belum diverifikasi lintas provider. [Feed](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861192)

Jumlah provider independen terverifikasi **1/3**. Spread bid/ask, kedalaman, BTTS quote dan perubahan 30 menit sebelum kickoff N/A. Belum cukup untuk menyebut anomali terkonfirmasi, informasi internal, keunggulan harga atau keuntungan yang dapat dieksekusi.

## 6. Israel vs Austria — B3

**Jadwal/venue terverifikasi:** 18 November 02.45 WIB; Nagyerdei Stadium, Debrecen, Hungary; **netral secara fisik**. [UEFA](https://www.uefa.com/uefanationsleague/match/2047916--israel-vs-austria/)

**Motivasi:** Austria 11 poin sudah pasti promosi. Israel 3 perlu mengejar hasil sambil bergantung laga Ireland–Kosovo; jangan menyamakan kebutuhan menang dengan bonus kekuatan. [UEFA: keadaan grup dan aturan](https://www.uefa.com/uefanationsleague/news/02ab-2209792f2fda-6a523d4500bb-1000--nations-league-latest-on-quarter-final-qualification-prom/)

### Israel: lima laga lengkap

| Tanggal | Lawan | H/A/N | GF–GA (90m) | Hasil | xG/xGA | Tembakan | SoT | Bola % | Sumber |
|---|---|---|---|---|---|---:|---:|---:|---|
| 2026-09-24 | Austria | A | 1–3 | L | N/A / N/A | 5 | 1 | 48,1 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861048) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861048) |
| 2026-09-27 | Republic of Ireland | N | 0–3 | L | N/A / N/A | 8 | 4 | 64,1 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861072) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861072) |
| 2026-10-01 | Kosovo | N | 0–0 | D | N/A / N/A | 10 | 3 | 45,3 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861095) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861095) |
| 2026-10-04 | Republic of Ireland | N | 1–1 | D | N/A / N/A | 10 | 2 | 45,1 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861124) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861124) |
| 2026-11-14 | Kosovo | A | 0–0 | D | N/A / N/A | 6 | 3 | 54 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861163) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861163) |

Bentuk **L-L-D-D-D**; penguasaan rata-rata 51,32% (n=5), kartu merah total 1.0. Venue: away: n=2, GF–GA 1–3, menang 0; neutral: n=3, GF–GA 1–4, menang 0. Jeda antar-kickoff 77,75 jam, bukan pengukuran pemulihan individual.

Gol menit 76–90+: GF 0 / GA 2, cakupan 5/5. Hanya hitungan event yang cocok dengan skor akhir; tidak dipakai sebagai tambahan koefisien model.

### Austria: lima laga lengkap

| Tanggal | Lawan | H/A/N | GF–GA (90m) | Hasil | xG/xGA | Tembakan | SoT | Bola % | Sumber |
|---|---|---|---|---|---|---:|---:|---:|---|
| 2026-09-24 | Israel | H | 3–1 | W | N/A / N/A | 19 | 9 | 51,9 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861048) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861048) |
| 2026-09-27 | Kosovo | H | 3–1 | W | N/A / N/A | 11 | 6 | 52 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861071) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861071) |
| 2026-10-01 | Republic of Ireland | A | 2–2 | D | N/A / N/A | 16 | 7 | 58,1 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861094) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861094) |
| 2026-10-04 | Kosovo | A | 1–1 | D | N/A / N/A | 13 | 4 | 64,2 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861121) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861121) |
| 2026-11-14 | Republic of Ireland | H | 1–0 | W | N/A / N/A | 21 | 8 | 55,1 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861170) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861170) |

Bentuk **W-W-D-D-W**; penguasaan rata-rata 56,26% (n=5), kartu merah total 0. Venue: home: n=3, GF–GA 7–2, menang 3; away: n=2, GF–GA 3–3, menang 0. Jeda antar-kickoff 72 jam, bukan pengukuran pemulihan individual.

Gol menit 76–90+: GF 5 / GA 1, cakupan 5/5. Hanya hitungan event yang cocok dengan skor akhir; tidak dipakai sebagai tambahan koefisien model.

### H2H dan relevansi

| Tanggal | Pertemuan | Skor 90m | Kompetisi | Sumber |
|---|---|---|---|---|
| 2019-03-24 | Israel–Austria | 4–2 | UEFA Euro qualification | [Arsip](https://github.com/martj42/international_results/blob/b0948cb558c927c357db4067eac5b37b96d0e4bb/results.csv#L42397) |
| 2019-10-10 | Austria–Israel | 3–1 | UEFA Euro qualification | [Arsip](https://github.com/martj42/international_results/blob/b0948cb558c927c357db4067eac5b37b96d0e4bb/results.csv#L43035) |
| 2021-09-04 | Israel–Austria | 5–2 | FIFA World Cup qualification | [Arsip](https://github.com/martj42/international_results/blob/b0948cb558c927c357db4067eac5b37b96d0e4bb/results.csv#L44402) |
| 2021-11-12 | Austria–Israel | 4–2 | FIFA World Cup qualification | [Arsip](https://github.com/martj42/international_results/blob/b0948cb558c927c357db4067eac5b37b96d0e4bb/results.csv#L44713) |
| 2026-09-24 | Austria–Israel | 3–1 | UEFA Nations League | [Arsip](https://www.espn.com/soccer/match/_/gameId/401861048) |

Pertemuan grup 2026 paling relevan. Laga lama/uji coba ditampilkan sebagai konteks; kesinambungan semua pelatih dan susunan historis tidak terverifikasi, sehingga tidak diperlakukan sebagai kekuatan tim saat ini. Penguasaan/xG H2H lintas periode yang sebanding N/A; pertandingan grup yang sama sudah ada dalam lima laga dan tidak dihitung sebagai bukti independen tambahan.

### Pemain dan XI perkiraan

| Tim | Pemain/peran | Status sumber | Pengaruh yang dinilai | Sumber |
|---|---|---|---|---|
| Israel | Raz Shlomo / Bek tengah | suspended_reported | Feingold/Nachmias/Stoinov diproyeksikan mengisi lini belakang. | [Berita](https://www.sportsmole.co.uk/football/israel/uefa-nations-league/preview/israel-vs-austria-prediction-team-news-lineups_609141.html) |
| Austria | David Alaba / Marcel Sabitzer / Bek / gelandang | not_selected_reported | Bukan kejutan baru; baseline performa sudah dibentuk tanpa mereka. | [Berita](https://www.sportsmole.co.uk/football/israel/uefa-nations-league/preview/israel-vs-austria-prediction-team-news-lineups_609141.html) |
| Austria | Carney Chukwuemeka / Marco Grull / Gelandang / sayap | withdrawn_reported | Keluhan otot dilaporkan sebelum laga Irlandia; pilihan pemain pelapis perlu XI resmi. | [Berita](https://www.oefb.at/oefb/News/Nationalteam-Vorschau-AUT-IRL/) |

**XI Israel (perkiraan):** Daniel Peretz; Dasa, Feingold, Nachmias, Stoinov, Revivo; Abada, Azoulay, Dor Peretz, Gloukh; Turgeman.

**XI Austria (perkiraan):** Jungwirth; Posch, Svoboda, Affengruber, Prass; Seiwald, Laimer; Demir, Baumgartner, Schmid; Kalajdzic.

Proyeksi sekunder yang mengantisipasi rotasi; starter kiper maupun striker belum resmi. [Sumber isr-aut-preview](https://www.sportsmole.co.uk/football/israel/uefa-nations-league/preview/israel-vs-austria-prediction-team-news-lineups_609141.html) · [Sumber oefb-preview](https://www.oefb.at/oefb/News/Nationalteam-Vorschau-ISR-AUT/) · [Sumber oefb-absences](https://www.oefb.at/oefb/News/Nationalteam-Vorschau-AUT-IRL/)

**Pola data:** Austria mencetak dalam 5/5 dan empat kali BTTS; Israel hanya dua gol dan tiga hasil seri beruntun. Dua sinyal BTTS berbeda arah, sehingga perhitungan nama besar di lini depan tidak dipakai untuk memaksa BTTS.

**Taktik/konteks:** Inferensi: Austria berpeluang mengatur menit dan Israel perlu menambah risiko. Debrecen netral membatasi penggunaan keuntungan kandang administratif. Austria dari Linz menuju Debrecen; Israel bermain di negara ketiga. Rute, jumlah pendukung dan waktu kedatangan belum diperoleh. Tidak tersedia data event lengkap untuk mengukur pressing, transisi, kualitas crossing atau set piece. Tidak dibuat bonus persen dari narasi ini.

### Keputusan per target, seluruhnya dari snapshot yang sama

| Target | Utama (kualitatif) | Beta V2 aktif | Hybrid aktif | Alasan filter Hybrid |
|---|---|---|---|---|
| 1X2 | Austria menang · Rendah | Austria menang · 71,5% | Austria menang · 71,5% | Arah utama dan Beta sepakat, ambang terpenuhi |
| BTTS | Observasi | Observasi | Observasi | Observasi utama dipertahankan |
| Total 2,5 | Observasi | Under 2,5 · 57,5% | Observasi | Observasi utama dipertahankan |

**Fokus Beta:** Austria menang · 71,5%. **Fokus Hybrid:** Austria menang · 71,5%.

**Alasan dan kontra utama yang dibekukan:**

- 1X2: Austria tidak terkalahkan, 16 tembakan dan 6,8 SoT per laga; Israel belum menang dan hanya dua gol.; Pertemuan pertama dimenangi Austria 3–1; venue Debrecen bukan keuntungan kandang fisik Israel. Kontra/batas: Austria sudah pasti promosi, membuka rotasi; ada beberapa absensi menyerang.; Israel membutuhkan hasil positif dan tiga laga terakhir berakhir seri.
- BTTS: Austria BTTS 4/5. Kontra/batas: Israel gagal mencetak 3/5 dan membuat 2,6 SoT per laga; XI Austria belum resmi.
- Total 2,5: Austria mencetak dua gol per laga. Kontra/batas: Israel tiga hasil seri dengan gol sedikit; prioritas Austria sudah tercapai, tempo/rotasi belum terkonfirmasi.

**Skenario utama, bukan exact-score pick:** 0–2. **Pemicu penilaian ulang:** Rotasi tujuh-delapan posisi atau turunnya intensitas Austria dapat membuat arah tandang rapuh. Konfirmasi XI lebih penting daripada rekor H2H lama.

**Clean sheet model mentah:** Israel 20,6%, Austria 35,6%, dari resep mentah strength_h730. Ini estimasi Poisson mentah tanpa kalibrasi khusus clean sheet; berbeda dari frekuensi CS historis dan bukan konsekuensi tunggal tabel marginal terkalibrasi.

**Sensitivitas lima laga lama (diagnostik):** menghilangkan satu dari 9 pertandingan unik secara bergantian menghasilkan perubahan arah 1X2/BTTS/total sebanyak 0/0/0. Ini diagnostik rumus lima laga mentah, bukan uji sensitivitas rating Beta V2 atau interval keyakinan; hasil ekstrem tidak dibuang dari model.

| Resep mentah | Laju gol H/A | Skor MC teratas | Frekuensi sampel |
|---|---|---|---|
| strength_h730 | 1,03/1,58 | 0–1 | 12,0% |
| strength_h365_plus_friendlies | 0,94/1,43 | 0–1 | 12,8% |

MC: 10.000 sampel **per resep** dengan seed tetap. Skor paling sering tetap hanya satu skenario; tidak otomatis menjadi pilihan 1X2/BTTS/total terkalibrasi.

**Pembanding pasar:** DraftKings via ESPN, diambil 17 Nov 2026 19.55.28 WIB, waktu quote asli N/A. Harga Amerika H/D/A 290/280.0/-125; peluang tanpa margin secara proporsional 23,8%/24,5%/51,7% (margin mentah 7,5%). Line gol **3,5**, Over/Under 135.0/-175.0. Line 3,5 tidak dibandingkan langsung dengan probabilitas target 2,5. [Feed](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861193)

Jumlah provider independen terverifikasi **1/3**. Spread bid/ask, kedalaman, BTTS quote dan perubahan 30 menit sebelum kickoff N/A. Belum cukup untuk menyebut anomali terkonfirmasi, informasi internal, keunggulan harga atau keuntungan yang dapat dieksekusi.

## 7. Polandia vs Swedia — B4

**Jadwal/venue terverifikasi:** 18 November 02.45 WIB; Municipal Stadium Wroclaw, Wroclaw, Poland; kandang fisik. [UEFA](https://www.uefa.com/uefanationsleague/match/2047922--poland-vs-sweden/)

**Motivasi:** Swedia 13 poin sudah pasti pertama dan promosi. Polandia 4 harus menjaga diri dari Rumania 3; bila turun keempat, konsekuensinya play-off B/C menurut UEFA terbaru. [UEFA: keadaan grup dan aturan](https://www.uefa.com/uefanationsleague/news/02ab-2209792f2fda-6a523d4500bb-1000--nations-league-latest-on-quarter-final-qualification-prom/)

### Poland: lima laga lengkap

| Tanggal | Lawan | H/A/N | GF–GA (90m) | Hasil | xG/xGA | Tembakan | SoT | Bola % | Sumber |
|---|---|---|---|---|---|---:|---:|---:|---|
| 2026-09-25 | Bosnia and Herzegovina | H | 0–0 | D | N/A / N/A | 14 | 4 | 49,8 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861055) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861055) |
| 2026-09-28 | Sweden | A | 1–3 | L | N/A / N/A | 18 | 7 | 47,4 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861080) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861080) |
| 2026-10-02 | Romania | H | 6–0 | W | N/A / N/A | 24 | 9 | 66,8 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861108) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861108) |
| 2026-10-05 | Bosnia and Herzegovina | A | 0–1 | L | N/A / N/A | 18 | 4 | 55,5 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861133) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861133) |
| 2026-11-14 | Romania | A | 1–2 | L | N/A / N/A | 15 | 3 | 55,7 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861168) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861168) |

Bentuk **D-L-W-L-L**; penguasaan rata-rata 55,04% (n=5), kartu merah total 0. Venue: home: n=2, GF–GA 6–0, menang 1; away: n=3, GF–GA 2–6, menang 0. Jeda antar-kickoff 72 jam, bukan pengukuran pemulihan individual.

Gol menit 76–90+: GF 2 / GA 1, cakupan 5/5. Hanya hitungan event yang cocok dengan skor akhir; tidak dipakai sebagai tambahan koefisien model.

### Sweden: lima laga lengkap

| Tanggal | Lawan | H/A/N | GF–GA (90m) | Hasil | xG/xGA | Tembakan | SoT | Bola % | Sumber |
|---|---|---|---|---|---|---:|---:|---:|---|
| 2026-09-25 | Romania | H | 2–1 | W | N/A / N/A | 11 | 4 | 59,7 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861051) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861051) |
| 2026-09-28 | Poland | H | 3–1 | W | N/A / N/A | 12 | 6 | 52,6 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861080) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861080) |
| 2026-10-02 | Bosnia and Herzegovina | A | 1–1 | D | N/A / N/A | 8 | 4 | 49,4 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861107) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861107) |
| 2026-10-05 | Romania | A | 1–0 | W | N/A / N/A | 12 | 2 | 47,9 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861128) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861128) |
| 2026-11-14 | Bosnia and Herzegovina | H | 3–2 | W | N/A / N/A | 13 | 7 | 42,2 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861166) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861166) |

Bentuk **W-W-D-W-W**; penguasaan rata-rata 50,36% (n=5), kartu merah total 0. Venue: home: n=3, GF–GA 8–4, menang 3; away: n=2, GF–GA 2–1, menang 1. Jeda antar-kickoff 72 jam, bukan pengukuran pemulihan individual.

Gol menit 76–90+: GF 0 / GA 1, cakupan 5/5. Hanya hitungan event yang cocok dengan skor akhir; tidak dipakai sebagai tambahan koefisien model.

### H2H dan relevansi

| Tanggal | Pertemuan | Skor 90m | Kompetisi | Sumber |
|---|---|---|---|---|
| 2004-06-05 | Sweden–Poland | 3–1 | Friendly | [Arsip](https://github.com/martj42/international_results/blob/b0948cb558c927c357db4067eac5b37b96d0e4bb/results.csv#L28269) |
| 2021-06-23 | Sweden–Poland | 3–2 | UEFA Euro | [Arsip](https://github.com/martj42/international_results/blob/b0948cb558c927c357db4067eac5b37b96d0e4bb/results.csv#L44215) |
| 2022-03-29 | Poland–Sweden | 2–0 | FIFA World Cup qualification | [Arsip](https://github.com/martj42/international_results/blob/b0948cb558c927c357db4067eac5b37b96d0e4bb/results.csv#L45118) |
| 2026-03-31 | Sweden–Poland | 3–2 | FIFA World Cup qualification | [Arsip](https://github.com/martj42/international_results/blob/b0948cb558c927c357db4067eac5b37b96d0e4bb/results.csv#L49308) |
| 2026-09-28 | Sweden–Poland | 3–1 | UEFA Nations League | [Arsip](https://www.espn.com/soccer/match/_/gameId/401861080) |

Pertemuan grup 2026 paling relevan. Laga lama/uji coba ditampilkan sebagai konteks; kesinambungan semua pelatih dan susunan historis tidak terverifikasi, sehingga tidak diperlakukan sebagai kekuatan tim saat ini. Penguasaan/xG H2H lintas periode yang sebanding N/A; pertandingan grup yang sama sudah ada dalam lima laga dan tidak dihitung sebagai bukti independen tambahan.

### Pemain dan XI perkiraan

| Tim | Pemain/peran | Status sumber | Pengaruh yang dinilai | Sumber |
|---|---|---|---|---|
| Poland | Jakub Kiwior / Bek tengah | suspended_reported | Potulski/Kedziora menjadi kandidat; meningkatkan ketidakpastian pertahanan. | [Berita](https://www.sportsmole.co.uk/football/poland/uefa-nations-league/preview/poland-vs-sweden-prediction-team-news-lineups_609183.html) |
| Poland | Piotr Zielinski / Kamil Grabara / Gelandang / kiper | out_reported | Szymanski/Nowak dan Dragowski diproyeksikan menggantikan. | [Berita](https://www.sportsmole.co.uk/football/poland/uefa-nations-league/preview/poland-vs-sweden-prediction-team-news-lineups_609183.html) |
| Poland | Matty Cash / Bek sayap | doubtful | Masalah kaki; Pyrka opsi jika absen. | [Berita](https://www.sportsmole.co.uk/football/poland/uefa-nations-league/preview/poland-vs-sweden-prediction-team-news-lineups_609183.html) |
| Sweden | Lucas Bergvall / Patrik Walemark / Gelandang / sayap | injured_reported | Larsson/Ayari tersedia pada proyeksi; jangan memakai berita Isak September sebagai absensi November. | [Berita](https://www.sportsmole.co.uk/football/poland/uefa-nations-league/preview/poland-vs-sweden-prediction-team-news-lineups_609183.html) |

**XI Polandia (perkiraan):** Dragowski; Pyrka, Potulski, Kedziora, Kubiak; Regula, Szymanski, Nowak, Zalewski; Lewandowski, Swiderski.

**XI Swedia (perkiraan):** Johansson; Svensson, Lagerbielke, Lindelof, Gudmundsson; Elanga, Larsson, Ayari, Nanasi; Gyokeres, Isak.

Proyeksi Sports Mole; XI resmi Swedia 14 November hanya pembanding kontinuitas. Belum ada konfirmasi rotasi atau Isak absen November. [Sumber pol-swe-preview](https://www.sportsmole.co.uk/football/poland/uefa-nations-league/preview/poland-vs-sweden-prediction-team-news-lineups_609183.html) · [Sumber swe-last-xi](https://www.svenskfotboll.se/nyheter/landslag/2026/11/herrlandslaget-startelva/)

**Pola data:** Polandia 17,8 tembakan/5,4 SoT, Swedia 11,2/4,6, tetapi 75% gol Polandia datang pada satu laga 6–0. Serangan Swedia lebih merata. Peluang BTTS tidak boleh disebut pasti karena Polandia dua kali gagal mencetak.

**Taktik/konteks:** Inferensi: kebutuhan Polandia mengamankan poin dapat meningkatkan volume; Swedia dapat mengubah menit bermain setelah promosi. Tidak ada bukti xG atau pressing event yang lengkap. Swedia setelah laga kandang menuju Wroclaw; jadwal sebagai proksi, bukan verifikasi jalur penerbangan. Tidak tersedia data event lengkap untuk mengukur pressing, transisi, kualitas crossing atau set piece. Tidak dibuat bonus persen dari narasi ini.

### Keputusan per target, seluruhnya dari snapshot yang sama

| Target | Utama (kualitatif) | Beta V2 aktif | Hybrid aktif | Alasan filter Hybrid |
|---|---|---|---|---|
| 1X2 | Observasi | Observasi | Observasi | Observasi utama dipertahankan |
| BTTS | BTTS Ya · Sedang | Observasi | Observasi | Dukungan di bawah ambang 55% |
| Total 2,5 | Over 2,5 · Sedang | Observasi | Observasi | Dukungan di bawah ambang 55% |

**Fokus Beta:** Observasi. **Fokus Hybrid:** Observasi.

**Alasan dan kontra utama yang dibekukan:**

- 1X2: Swedia belum kalah, empat kemenangan, unggul kualitas performa grup. Kontra/batas: Swedia sudah promosi sehingga rotasi mungkin; Polandia tanpa kalah pada dua kandang fisik grup.; Satu feed pasar justru mengunggulkan Polandia; belum ada tiga pembanding independen.
- BTTS: Swedia mencetak 5/5 dan kebobolan 4/5; Polandia menghadapi absensi di pertahanan.; Kedua tim menghasilkan SoT 5,4 dan 4,6 per laga; Polandia perlu mengamankan posisi ketiga. Kontra/batas: Enam dari delapan gol Polandia berasal dari satu laga; XI Swedia dan kondisi Cash belum resmi.
- Total 2,5: Kedua tim Over 3/5; pertemuan pertama 3–1. Kontra/batas: Polandia dua kali gagal mencetak; skenario rotasi dapat mengurangi daya serang Swedia.

**Skenario utama, bukan exact-score pick:** 1–2. **Pemicu penilaian ulang:** Jika Gyokeres dan Isak sama-sama dicadangkan atau Polandia memakai bentuk sangat konservatif, dukungan BTTS/Over melemah. Feed pasar yang memfavoritkan Polandia perlu dipantau tanpa menyimpulkan bocoran.

**Clean sheet model mentah:** Polandia 26,8%, Swedia 18,7%, dari resep mentah strength_h730. Ini estimasi Poisson mentah tanpa kalibrasi khusus clean sheet; berbeda dari frekuensi CS historis dan bukan konsekuensi tunggal tabel marginal terkalibrasi.

**Sensitivitas lima laga lama (diagnostik):** menghilangkan satu dari 9 pertandingan unik secara bergantian menghasilkan perubahan arah 1X2/BTTS/total sebanyak 6/1/3. Ini diagnostik rumus lima laga mentah, bukan uji sensitivitas rating Beta V2 atau interval keyakinan; hasil ekstrem tidak dibuang dari model.

| Resep mentah | Laju gol H/A | Skor MC teratas | Frekuensi sampel |
|---|---|---|---|
| strength_h730 | 1,68/1,32 | 1–1 | 11,5% |
| strength_h365_plus_friendlies | 1,68/1,28 | 1–1 | 11,7% |

MC: 10.000 sampel **per resep** dengan seed tetap. Skor paling sering tetap hanya satu skenario; tidak otomatis menjadi pilihan 1X2/BTTS/total terkalibrasi.

**Pembanding pasar:** DraftKings via ESPN, diambil 17 Nov 2026 19.55.27 WIB, waktu quote asli N/A. Harga Amerika H/D/A 110/270.0/200; peluang tanpa margin secara proporsional 44,1%/25,0%/30,9% (margin mentah 8,0%). Line gol **3,5**, Over/Under 130.0/-165.0. Line 3,5 tidak dibandingkan langsung dengan probabilitas target 2,5. [Feed](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861195)

Jumlah provider independen terverifikasi **1/3**. Spread bid/ask, kedalaman, BTTS quote dan perubahan 30 menit sebelum kickoff N/A. Belum cukup untuk menyebut anomali terkonfirmasi, informasi internal, keunggulan harga atau keuntungan yang dapat dieksekusi.

## 8. Ukraina vs Georgia — B2

**Jadwal/venue terverifikasi:** 18 November 02.45 WIB; Košická futbalová aréna (KFA), Kosice, Slovakia; **netral secara fisik**. [UEFA](https://www.uefa.com/uefanationsleague/match/2047918--ukraine-vs-georgia/)

**Motivasi:** Ukraina 4 poin cukup seri untuk tetap di League B. Georgia 2 harus menang agar melewati Ukraina dan menghindari play-off B/C. [UEFA: keadaan grup dan aturan](https://www.uefa.com/uefanationsleague/news/02ab-2209792f2fda-6a523d4500bb-1000--nations-league-latest-on-quarter-final-qualification-prom/)

### Ukraine: lima laga lengkap

| Tanggal | Lawan | H/A/N | GF–GA (90m) | Hasil | xG/xGA | Tembakan | SoT | Bola % | Sumber |
|---|---|---|---|---|---|---:|---:|---:|---|
| 2026-09-25 | Hungary | A | 1–0 | W | N/A / N/A | 10 | 3 | 43 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861054) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861054) |
| 2026-09-28 | Georgia | A | 0–0 | D | N/A / N/A | 7 | 2 | 51,2 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861075) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861075) |
| 2026-10-02 | Northern Ireland | N | 0–3 | L | N/A / N/A | 11 | 2 | 72,4 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861106) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861106) |
| 2026-10-05 | Hungary | N | 1–2 | L | N/A / N/A | 17 | 2 | 52,3 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861134) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861134) |
| 2026-11-14 | Northern Ireland | A | 0–1 | L | N/A / N/A | 7 | 2 | 61,9 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861169) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861169) |

Bentuk **W-D-L-L-L**; penguasaan rata-rata 56,16% (n=5), kartu merah total 1.0. Venue: away: n=3, GF–GA 1–1, menang 1; neutral: n=2, GF–GA 1–5, menang 0. Jeda antar-kickoff 72 jam, bukan pengukuran pemulihan individual.

Gol menit 76–90+: GF 1 / GA 1, cakupan 5/5. Hanya hitungan event yang cocok dengan skor akhir; tidak dipakai sebagai tambahan koefisien model.

### Georgia: lima laga lengkap

| Tanggal | Lawan | H/A/N | GF–GA (90m) | Hasil | xG/xGA | Tembakan | SoT | Bola % | Sumber |
|---|---|---|---|---|---|---:|---:|---:|---|
| 2026-09-25 | Northern Ireland | H | 0–1 | L | N/A / N/A | 11 | 5 | 62,2 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861049) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861049) |
| 2026-09-28 | Ukraine | H | 0–0 | D | N/A / N/A | 14 | 5 | 48,8 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861075) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861075) |
| 2026-10-02 | Hungary | A | 0–1 | L | N/A / N/A | 8 | 3 | 58,1 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861102) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861102) |
| 2026-10-05 | Northern Ireland | A | 0–0 | D | N/A / N/A | 7 | 2 | 61,7 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861132) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861132) |
| 2026-11-14 | Hungary | H | 0–2 | L | N/A / N/A | 7 | 1 | 53,4 | [Skor](https://www.espn.com/soccer/match/_/gameId/401861164) · [Statistik](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861164) |

Bentuk **L-D-L-D-L**; penguasaan rata-rata 56,84% (n=5), kartu merah total 0. Venue: home: n=3, GF–GA 0–3, menang 0; away: n=2, GF–GA 0–1, menang 0. Jeda antar-kickoff 74,75 jam, bukan pengukuran pemulihan individual.

Gol menit 76–90+: GF 0 / GA 2, cakupan 5/5. Hanya hitungan event yang cocok dengan skor akhir; tidak dipakai sebagai tambahan koefisien model.

### H2H dan relevansi

| Tanggal | Pertemuan | Skor 90m | Kompetisi | Sumber |
|---|---|---|---|---|
| 2007-09-08 | Georgia–Ukraine | 1–1 | UEFA Euro qualification | [Arsip](https://github.com/martj42/international_results/blob/b0948cb558c927c357db4067eac5b37b96d0e4bb/results.csv#L31236) |
| 2015-06-09 | Georgia–Ukraine | 1–2 | Friendly | [Arsip](https://github.com/martj42/international_results/blob/b0948cb558c927c357db4067eac5b37b96d0e4bb/results.csv#L38750) |
| 2024-10-11 | Ukraine–Georgia | 1–0 | UEFA Nations League | [Arsip](https://github.com/martj42/international_results/blob/b0948cb558c927c357db4067eac5b37b96d0e4bb/results.csv#L47786) |
| 2024-11-16 | Georgia–Ukraine | 1–1 | UEFA Nations League | [Arsip](https://github.com/martj42/international_results/blob/b0948cb558c927c357db4067eac5b37b96d0e4bb/results.csv#L47984) |
| 2026-09-28 | Georgia–Ukraine | 0–0 | UEFA Nations League | [Arsip](https://www.espn.com/soccer/match/_/gameId/401861075) |

Pertemuan grup 2026 paling relevan. Laga lama/uji coba ditampilkan sebagai konteks; kesinambungan semua pelatih dan susunan historis tidak terverifikasi, sehingga tidak diperlakukan sebagai kekuatan tim saat ini. Penguasaan/xG H2H lintas periode yang sebanding N/A; pertandingan grup yang sama sudah ada dalam lima laga dan tidak dihitung sebagai bukti independen tambahan.

### Pemain dan XI perkiraan

| Tim | Pemain/peran | Status sumber | Pengaruh yang dinilai | Sumber |
|---|---|---|---|---|
| Georgia | Khvicha Kvaratskhelia / Penyerang/kreator | out_reported | Davitashvili/Kvernadze memberi opsi, Mikautadze tetap ujung serangan. | [Berita](https://www.sportsmole.co.uk/football/ukraine/uefa-nations-league/preview/ukraine-vs-georgia-prediction-team-news-lineups_609161.html) |
| Georgia | Giorgi Tsitaishvili / Sayap | suspended_reported | Pembaruan sekunder menyebut akumulasi; Davitashvili alternatif. | [Berita](https://www.forebet.com/en/football-match-previews/32393-fine-margins-loom-as-ukraine-face-goal-shy-georgia) |
| Georgia | Giorgi Kochorashvili / Gelandang | available_reported | Dilaporkan selesai menjalani skorsing; opsi mengganti proyeksi Gagnidze/Mekvabishvili. | [Berita](https://www.forebet.com/en/football-match-previews/32393-fine-margins-loom-as-ukraine-face-goal-shy-georgia) |

**XI Ukraina (perkiraan):** Trubin; Krupskyi, Zabarnyi, Matvienko, Mykolenko; Andriyevskiy, Yarmoliuk, Ocheretko, Sudakov; Dovbyk, Krasnopir.

**XI Georgia (perkiraan):** Mamardashvili; Kakabadze, Goglichidze, Dvali, Lochoshvili; Chakvetadze, Mekvabishvili; Kvernadze, Kochorashvili, Davitashvili; Mikautadze.

Gabungan proyeksi sekunder, dengan Kochorashvili sebagai opsi setelah kembali. Posisi dan XI belum resmi. [Sumber ukr-geo-preview](https://www.sportsmole.co.uk/football/ukraine/uefa-nations-league/preview/ukraine-vs-georgia-prediction-team-news-lineups_609161.html) · [Sumber ukr-geo-teamnews](https://www.forebet.com/en/football-match-previews/32393-fine-margins-loom-as-ukraine-face-goal-shy-georgia)

**Pola data:** Ukraina dan Georgia sama-sama lebih dari 56% penguasaan bola, tetapi hanya 2,2 dan 3,2 SoT per laga. Dominasi bola bukan bukti peluang berkualitas. Seluruh Georgia Under; kebutuhan menang tetap membuat menit akhir berisiko.

**Taktik/konteks:** Inferensi: Georgia mungkin lebih agresif setelah jeda jika belum unggul. Ukraina dapat menjaga kedalaman; tidak memperoleh keuntungan kandang geografis dari bermain di Slovakia. Kedua tim menuju Košice; Ukraina dari Belfast, Georgia dari laga di Tbilisi. Rincian perjalanan/pemulihan individual belum diverifikasi. Tidak tersedia data event lengkap untuk mengukur pressing, transisi, kualitas crossing atau set piece. Tidak dibuat bonus persen dari narasi ini.

### Keputusan per target, seluruhnya dari snapshot yang sama

| Target | Utama (kualitatif) | Beta V2 aktif | Hybrid aktif | Alasan filter Hybrid |
|---|---|---|---|---|
| 1X2 | Ukraina menang · Rendah | Observasi | Observasi | Arah utama dan Beta berbeda |
| BTTS | BTTS Tidak · Sedang | BTTS Tidak · 58,6% | BTTS Tidak · 58,6% | Arah utama dan Beta sepakat, ambang terpenuhi |
| Total 2,5 | Under 2,5 · Relatif kuat | Under 2,5 · 65,2% | Under 2,5 · 65,2% | Arah utama dan Beta sepakat, ambang terpenuhi |

**Fokus Beta:** Under 2,5 · 65,2%. **Fokus Hybrid:** Under 2,5 · 65,2%.

**Alasan dan kontra utama yang dibekukan:**

- 1X2: Georgia belum mencetak dalam lima laga; Kvaratskhelia absen; Ukraina memiliki opsi penyerang yang lebih banyak. Kontra/batas: Ukraina kalah tiga kali beruntun dan hanya dua gol; venue Košice netral, bukan kandang fisik.
- BTTS: Georgia gagal mencetak 5/5; Ukraina gagal mencetak 3/5; pertemuan pertama 0–0. Kontra/batas: Georgia harus menang dan dapat meningkatkan risiko di akhir; nol gol historis tidak berarti peluang gol nol.
- Total 2,5: Georgia Under 5/5, hanya empat kebobolan; Ukraina 2 GF dan 6 GA dalam lima laga.; Ukraina dapat bertahan di B dengan seri, sedangkan masalah penyelesaian kedua tim belum teratasi. Kontra/batas: Gol cepat/penalti/kartu dapat mengubah struktur; Georgia wajib mengambil risiko jika belum unggul.

**Skenario utama, bukan exact-score pick:** 1–0. **Pemicu penilaian ulang:** Gol awal Georgia, penalti atau kartu merah dapat memaksa Ukraina menyerang dan meniadakan struktur Under. Puasa gol Georgia bukan probabilitas nol.

**Clean sheet model mentah:** Ukraina 37,4%, Georgia 32,5%, dari resep mentah strength_h730. Ini estimasi Poisson mentah tanpa kalibrasi khusus clean sheet; berbeda dari frekuensi CS historis dan bukan konsekuensi tunggal tabel marginal terkalibrasi.

**Sensitivitas lima laga lama (diagnostik):** menghilangkan satu dari 9 pertandingan unik secara bergantian menghasilkan perubahan arah 1X2/BTTS/total sebanyak 0/0/0. Ini diagnostik rumus lima laga mentah, bukan uji sensitivitas rating Beta V2 atau interval keyakinan; hasil ekstrem tidak dibuang dari model.

| Resep mentah | Laju gol H/A | Skor MC teratas | Frekuensi sampel |
|---|---|---|---|
| strength_h730 | 1,12/0,98 | 1–0 | 13,6% |
| strength_h365_plus_friendlies | 1,04/0,93 | 0–0 | 14,7% |

MC: 10.000 sampel **per resep** dengan seed tetap. Skor paling sering tetap hanya satu skenario; tidak otomatis menjadi pilihan 1X2/BTTS/total terkalibrasi.

**Pembanding pasar:** DraftKings via ESPN, diambil 17 Nov 2026 19.55.28 WIB, waktu quote asli N/A. Harga Amerika H/D/A 110/220.0/250; peluang tanpa margin secara proporsional 44,3%/29,1%/26,6% (margin mentah 7,4%). Line gol **2,5**, Over/Under 125.0/-160.0. Line ini sesuai target 2,5, tetapi harga belum diverifikasi lintas provider. [Feed](https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.nations/summary?event=401861190)

Jumlah provider independen terverifikasi **1/3**. Spread bid/ask, kedalaman, BTTS quote dan perubahan 30 menit sebelum kickoff N/A. Belum cukup untuk menyebut anomali terkonfirmasi, informasi internal, keunggulan harga atau keuntungan yang dapat dieksekusi.

## Batas data dan pemeriksaan ulang

- Seluruh XI masih perkiraan. Tidak ada pemantauan otomatis atau klaim konfirmasi XI pada jam pertandingan.
- Tidak ada xG/xGA dalam 40 summary ESPN: cakupan 0/5 per tim. Tembakan tidak diubah menjadi xG dengan koefisien tebakan.
- Metadata neutralSite ESPN tidak selalu mengenali kandang administratif di negara ketiga; venue dikoreksi pada data laporan sesuai alamat stadion, flag provider tetap tersimpan.
- Norwegia cukup menang atas Denmark menurut UEFA; klaim sekunder wajib menang tiga gol ditolak.
- Aturan degradasi lama pada beberapa pratinjau tidak dipakai. Wales sudah masuk play-off A/B; posisi keempat B menuju play-off B/C.
- Proyeksi Portugal yang masih memasukkan Bernardo Silva dianggap kedaluwarsa. Berita Isak meninggalkan kamp pada September tidak diterapkan ke November.
- Satu feed odds bukan tiga bookmaker independen. Perbedaan favorit dan line total 3,5 versus target 2,5 tidak dianggap anomali terkonfirmasi.
- Model utama untuk input Hybrid dibuat sebagai forecast baru dengan metode tetap; keputusan lama dan koefisien utama tidak diubah.
- Upaya pencarian pembanding Betfair/Pinnacle tidak menghasilkan quote terkini yang dapat disejajarkan; situs berita yang menyalin harga tidak dihitung sebagai bookmaker independen.
- Jadwal pemeriksaan yang disarankan: XI resmi sekitar satu jam sebelum kickoff, lalu berita/harga kontrak yang sama pada 30 menit terakhir. Tidak ada pemantauan otomatis yang sedang berjalan. Informasi baru harus menjadi revisi baru dengan alasan; snapshot ini tetap utuh.

## Rencana evaluasi sesudah laga

Isi skor 90 menit + injury time di **file hasil baru**, lengkap sumber dan waktu pengambilan. Jangan mengubah prediksi, fokus, atau ambang 55%. Laporkan benar/jumlah terbit untuk 1X2, BTTS, total, dan fokus; laporkan cakupan dan observasi. Bandingkan Beta–Hybrid pada target/laga yang sama, dan Hybrid–utama pada subset yang sama, agar abstensi tidak menciptakan kesan peningkatan semu. Probabilitas Beta dapat dinilai dengan Brier/log loss setelah hasil; utama kualitatif tidak diberi metrik probabilitas buatan.

Semua delapan hasil **menunggu pertandingan**. Persentase akurasi matchday ini belum ada. Analisis adalah bahan pertimbangan, bukan hasil mutlak.

## Identitas arsip

- Snapshot utama: `b4379cc9c776421ba62e087d115664bd`; eksperimen: `9d9c316e2d92502e1965b8bf5267e862`.
- Model, input dan keputusan telah dicocokkan ulang; 160.000 skenario mentah dapat direproduksi dengan seed tetap. Selisih MC–analitik mentah terbesar 1,22 poin persentase. Selisih kecil simulasi bukan kesalahan prediksi dan tidak menjadi alasan mengganti fokus.
- Manifest berisi SHA-256 file. Semua file paket model lama (80) tetap identik.

