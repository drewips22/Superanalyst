# Backtest sembilan laga UCL — 5 November 2026 WIB

Baseline lima laga menghasilkan **6/9 pilihan pemenang**, **7/9 BTTS**, dan **8/9 Over 2,5** yang tepat. Ini rekonstruksi historis, bukan bukti akurasi untuk pertandingan mendatang.

## Batas waktu dan integritas

Tanggal pada gambar adalah **5 November 2026 WIB**, sama dengan **4 November di kalender UEFA**. Dua laga mulai 00.45 WIB, tujuh lainnya 03.00 WIB. Cohort mencakup seluruh sembilan laga pada gambar, yaitu sesi Rabu Matchday 4; sembilan laga sesi Selasa berada di luar permintaan ini.

Cutoff bersama: **4 November 2026 pukul 19.00 WIB / 12:00 UTC**, 5 jam 45 menit sampai 8 jam sebelum kickoff. Statistik pertandingan target, line-up resmi setelah cutoff dan berita terbaru setelah cutoff tidak menjadi fitur.

Skor sudah terlihat pada lampiran pengguna, beberapa cuplikan pencarian, dan header hasil dinamis di halaman preview. Karena itu ini **bukan uji buta penuh**. Analisis memakai aturan lama yang deterministik, tanpa mengubah parameter untuk mengejar hasil. Tanggal artikel pralaga tidak membuktikan seluruh versi halaman sama seperti saat cutoff; `point_in_time_verified=false`.

[Analisis prapenilaian](analysis-before-result.md), [data masukan](features.json), [aturan eksperimen](experiment.json), dan [sembilan prediksi](predictions.json) dibekukan pada commit **7814517** sebelum pengambilan label hasil terpisah. [Checksum](frozen-inputs.json) mempertahankan berkas tersebut. Nama `analysis-before-result` berarti sebelum tahap penilaian dalam rekonstruksi ini, bukan ditulis sebelum kickoff asli.

## Perbandingan prediksi dan hasil

Model: rata-rata gol cetak tim dan kebobolan lawan dari lima laga, lalu Poisson independen. Tidak ada tambahan angka untuk kandang, cedera, motivasi, H2H, xG atau pasar. 1X2 memilih probabilitas terbesar; BTTS dan Over 2,5 memilih ya bila ≥50%. Persentase belum dikalibrasi.

| Laga | P(1/X/2) | Pilihan 1X2 | Hasil 90m | BTTS: P(ya), pilihan | Over 2,5: P(ya), pilihan |
| --- | --- | --- | --- | --- | --- |
| AEK Athens–Real Madrid | 15.1/15.1/69.8% | Real Madrid ✓ | 2-3 | 71.6%, ya ✓ | 81.5%, ya ✓ |
| Fenerbahce–Liverpool | 23.3/20.9/55.8% | Liverpool ✗ | 3-2 | 63.8%, ya ✓ | 66.0%, ya ✓ |
| Borussia Dortmund–Real Betis | 44.4/24.5/31.1% | Borussia Dortmund ✓ | 2-1 | 58.1%, ya ✓ | 55.4%, ya ✓ |
| FC Porto–Napoli | 44.9/22.8/32.3% | FC Porto ✓ | 4-1 | 64.8%, ya ✓ | 64.1%, ya ✓ |
| Lens–Como | 13.1/19.4/67.4% | Como ✓ | 1-9 | 48.3%, tidak ✗ | 55.4%, ya ✓ |
| PSV Eindhoven–Club Brugge | 35.0/21.8/43.1% | Club Brugge ✓ | 1-2 | 69.5%, ya ✓ | 69.7%, ya ✓ |
| RB Leipzig–Manchester City | 32.2/20.3/47.5% | Manchester City ✓ | 2-3 | 74.2%, ya ✓ | 76.2%, ya ✓ |
| Slavia Prague–Arsenal | 48.8/26.0/25.2% | Slavia Prague ✗ | 1-2 | 49.1%, tidak ✗ | 45.6%, tidak ✗ |
| Viking FK–Sabah FK | 31.7/20.9/47.4% | Sabah FK ✗ | 4-1 | 71.7%, ya ✓ | 73.1%, ya ✓ |

Seluruh skor dicocokkan dengan [rangkuman UEFA](https://www.uefa.com/uefachampionsleague/news/02ab-21fe508a035b-5eed0199e0b2-1000--champions-league-round-up-como-equal-biggest-ever-win-real/) dan [label hasil bersumber per laga](outcomes.json); tidak hanya menyalin gambar.

| Metrik (lebih kecil lebih baik) | Model gol lima laga | Pembanding tanpa informasi |
| --- | ---: | ---: |
| Brier 1X2 (jumlah tiga kelas) | 0.5200 | 0.6667 |
| Log loss 1X2 | 0.8815 | 1.0986 |
| Brier BTTS | 0.1418 | 0.2500 |
| Log loss BTTS | 0.4658 | 0.6931 |
| Brier Over 2,5 | 0.1326 | 0.2500 |
| Log loss Over 2,5 | 0.4419 | 0.6931 |

Pembanding memakai 1/3 tiap kelas 1X2 dan 1/2 untuk dua target biner; bukan model kekuatan liga atau odds pasar. Cakupan 9/9. Angka lebih baik pada sembilan laga ini belum membuktikan keunggulan berulang, kalibrasi atau keuntungan. [Evaluasi lengkap dan bin kalibrasi](evaluation.json).

## Pola yang ditetapkan sebelum tahap penilaian

| Flag dari lima laga sebelumnya | Memenuhi | Tidak memenuhi | Belum diketahui | BTTS aktual pada yang memenuhi |
| --- | ---: | ---: | ---: | ---: |
| Kedua tim mencetak gol ≥4/5 | 7 | 2 | 0 | 7/7 |
| Kedua tim kebobolan ≥4/5 | 2 | 7 | 0 | 2/2 |
| Kedua tim clean sheet ≤1/5 | 2 | 7 | 0 | 2/2 |
| Setidaknya satu tim clean sheet ≥3/5 | 3 | 6 | 0 | 3/3 |
| Masing-masing tim BTTS ≥3/5 | 4 | 5 | 0 | 4/4 |
| Tim tandang pilihan teratas model | 6 | 3 | 0 | 6/6 |
| Kedua tim rerata tembakan 12–15 (data penuh/sebanding) | 0 | 4 | 5 | 0/0 |

**Tidak ada kasus negatif BTTS atau Over 2,5:** semuanya terjadi 9/9. Pada flag kedua tim mencetak gol ≥4/5, kelompok memenuhi 7/7 BTTS, tetapi kelompok tidak memenuhi juga 2/2. Jadi flag itu belum menunjukkan daya pemilah. Aturan selalu memilih BTTS ya akan mendapat 9/9 pada sampel ini; itu hanya pembanding deskriptif sesudah hasil, bukan strategi yang tervalidasi.

Dua flag kebobolan ≥4/5 dan clean sheet ≤1/5 identik pada jendela lima laga. Keduanya tidak boleh dijumlahkan sebagai bukti independen. Sebaliknya, ketiga laga dengan setidaknya satu tim memiliki ≥3 clean sheet tetap BTTS: Porto–Napoli, Slavia–Arsenal, Viking–Sabah. Clean sheet historis perlu dinilai bersama kualitas lawan.

Tidak satu pun dari empat pasangan dengan data tembakan lengkap memenuhi rentang 12–15 untuk kedua tim; lima pasangan lain tidak lengkap. Dengan demikian ambang ini belum teruji, bukan terbukti salah atau benar. Gol menit akhir juga tidak membuktikan kedua tim menekan lebih intens tanpa data tembakan/pressing per interval.

## Pembacaan per laga: bukti lama, lalu hasil

- **AEK–Madrid:** AEK GF 8/GA 13 dan Madrid GF 17/GA 6; kedua tim hanya satu clean sheet. Pilihan Madrid 69,8% dan BTTS 71,6% sejalan dengan hasil 2–3. Itu tetap menyisakan 30,2% untuk hasil selain kemenangan Madrid.
- **Fenerbahce–Liverpool:** model memilih Liverpool 55,8%, lalu kalah 2–3; peluang kemenangan Fenerbahce 23,3% bukan nol. Berita sebelum cutoff menyebut pelatih interim baru dan absensi kedua tim. Ini kandidat alasan menambah ketidakpastian, bukan bukti bahwa pergantian pelatih menyebabkan kemenangan atau dasar memberi bonus baru setelah hasil.
- **Dortmund–Betis:** GF sama-sama 8; GA Dortmund 5 versus Betis 8. Model memberi Dortmund 44,4%, pilihan relatif dalam laga terbuka, dan hasil 2–1 sesuai. Rekor kandang UCL mendukung konteks, tetapi pengaruh tambahannya tidak dihitung dalam model.
- **Porto–Napoli:** Porto memiliki tiga clean sheet, Napoli nol dalam lima laga; model tetap BTTS 64,8% karena pertahanan Napoli juga lemah dan serangan Napoli produktif. Porto 44,9% menang, hasil 4–1. Berita pralaga tentang absensi Napoli adalah konteks yang relevan; satu kemenangan lawan tim cedera tidak menaksir efek universal minus 22%.
- **Lens–Como:** Como lima kemenangan, GF 13/GA 3; Lens tanpa clean sheet, GF 5/GA 8. Arah kemenangan Como 67,4% cocok, tetapi BTTS 48,3% salah. Peluang skor tepat 1–9 dalam model hanya **0,0096%**; model tidak meramalkan pembantaian itu. Skor ekstrem menegaskan perlunya menguji distribusi gol yang lebih lentur pada sampel lain.
- **PSV–Brugge:** kemenangan PSV 7–0 menyumbang 7 dari 10 gol lima laganya; sisanya hanya tiga gol dalam empat laga. Brugge menang kelima laga dan mencetak 15 gol. Model memilih Brugge 43,1%, BTTS 69,5%; hasil 1–2 sesuai. Pelajaran: lihat sebaran per laga, jangan hanya rata-rata yang ditarik satu kemenangan besar.
- **Leipzig–City:** Leipzig baru tiga kemenangan, tetapi sebelumnya kebobolan 6 dari Bayern dan 4 dari Madrid; City tanpa clean sheet dalam lima laga. Model memilih City 47,5%, BTTS 74,2%, hasil 2–3 sesuai. Tren menang terbaru tidak otomatis menghapus kualitas lawan dan kerentanan bertahan.
- **Slavia–Arsenal:** Slavia GF 12/GA 3 versus Arsenal GF 7/GA 3 membuat model mentah memilih Slavia 48,8%, BTTS tidak dan Under 2,5. Ketiganya keliru pada 1–2. Lawan domestik Slavia berbeda level dari rangkaian Arsenal termasuk Bayern dan Liverpool. H2H/reputasi kompetitif juga bertentangan dengan baseline. Perbaikan yang perlu diuji adalah penyesuaian kekuatan lawan/liga dan aturan observasi yang ditetapkan sebelum eksperimen baru; tidak mengganti prediksi kasus ini menjadi Arsenal.
- **Viking–Sabah:** Viking GA 12 dan Sabah GA 5 membuat model memilih Sabah 47,4%; hasil 4–1 keliru. Catatan tandang Eropa Sabah yang buruk dan pola gol kandang Viking sudah tersedia sebelum cutoff, tetapi tidak masuk baseline. Clean sheet liga Azerbaijan tidak serta-merta setara dengan menghadapi Bayern/Aston Villa. Pengaruh kandang/perjalanan masih hipotesis, bukan +35% yang langsung dipasang.

## Pisahkan kejadian laga dari fitur pralaga

[Timeline Porto–Napoli](https://www.espn.com/soccer/match/_/gameId/401915301): Napoli mendapat kartu merah menit 88 saat sudah tertinggal **1–3**; satu gol penalti Porto terjadi sesudahnya. [Timeline Viking–Sabah](https://www.espn.com/soccer/match/_/gameId/401915302): Sabah dikartu merah menit 77 saat sudah tertinggal **1–2**, kemudian kebobolan dua lagi. Kartu bisa memengaruhi margin akhir, tetapi urutan ini tidak membuktikan bahwa kartu menciptakan pemenangnya. AEK juga memiliki kartu merah yang tercatat pada 90+5; insiden disimpan hanya untuk audit sesudah laga.

Dua gol Porto berasal dari sundulan setelah sepak pojok, sedangkan gol penentu Brugge berasal dari transisi, menurut timeline dan rangkuman UEFA. Itu observasi pada pertandingan target. Kita belum memiliki pengukuran kerentanan set piece/crossing sebelum cutoff yang konsisten untuk sembilan pasangan, sehingga ini **kandidat fitur berikutnya**, bukan klaim bahwa faktor itu sudah diprediksi.

## Perubahan yang layak untuk pengembangan

1. Wajib cek cakupan seluruh kompetisi, termasuk piala domestik. Data awal melewatkan PAOK–AEK, Porto–Viseu, dan Brugge–Lokeren; ketiganya dilengkapi sebelum pembekuan. Slavia/Sabah membutuhkan sumber domestik tambahan.
2. Simpan lawan dan level kompetisi, rentang serta median gol, dan kontribusi laga terbesar. Uji model kekuatan tim/lawan dan efek kandang yang ditaksir dari data lebih panjang, lalu bandingkan pada blok waktu berikutnya.
3. Bedakan hasil, xG, dan probabilitas. Cakupan xG konsisten pada kasus ini 0/90; jangan menyebutnya uji xG. Tembakan tersedia 80/90 catatan tim-laga, bukan 80 pertandingan independen.
4. Catat pergantian pelatih, absensi berbobot peran/menit dan waktu istirahat/perjalanan. Status laporan media tidak otomatis susunan resmi. Fitur 22%/35%/18% tetap hipotesis yang tidak aktif.
5. Tetapkan sampel berikutnya secara berurutan, termasuk pertandingan yang berakhir tanpa BTTS/di bawah 2,5. Bekukan fitur dan aturan sebelum hasil; pisahkan pengembangan dari evaluasi berikutnya. Sembilan pertandingan satu sesi tidak cukup untuk mengkalibrasi model.
6. Anomali pasar belum diuji: tidak ada arsip harga, spread dan kedalaman dari tiga sumber pada waktu sebanding. Untuk T-30 menit, buat eksperimen horizon terpisah; jangan memasukkan informasi itu ke prediksi cutoff 12:00 UTC.

## Mengulang pemeriksaan

```sh
python backtests/ucl-2026-11-04/run.py verify
python skills/superanalyst/scripts/evaluate.py backtests/ucl-2026-11-04/scored-reconstruction.jsonl
```

Verifikasi menghitung ulang sembilan prediksi dan evaluasi, memeriksa checksum, serta menolak penggantian snapshot. [Runner](run.py) memisahkan tahap `predict`, `grade`, dan `verify`. Gunakan folder eksperimen baru untuk revisi. Analisis adalah bahan pertimbangan, bukan hasil mutlak.
