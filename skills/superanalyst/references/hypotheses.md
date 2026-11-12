# Daftar hipotesis dan penelitian awal

Ditinjau: **11 November 2026**. Ini penelusuran awal sumber terarah, bukan tinjauan sistematis menyeluruh. "Belum terverifikasi" berarti bukti yang diperiksa belum mendukung rumus tersebut, bukan klaim bahwa pengaruhnya mustahil ada.

## H01 — Tiga atau lebih pemain cedera mengurangi peluang menang 22%

**Status:** arah hubungan didukung penelitian; ambang tiga pemain dan besar 22% belum terverifikasi.

Studi prospektif Hägglund dkk. mengikuti 24 tim profesional pria selama 11 musim. Beban cedera lebih rendah dan ketersediaan pemain lebih tinggi berkaitan dengan performa musim yang lebih baik. Unit analisis dan hasilnya tidak menetapkan potongan peluang kemenangan tetap untuk satu laga dengan tiga pemain absen. Ini hubungan observasional, bukan eksperimen tentang penalti universal. [Abstrak penelitian, 2013](https://pubmed.ncbi.nlm.nih.gov/23645832/)

**Uji:** gunakan daftar absensi yang sudah diketahui saat prediksi, peluang menjadi starter/menit sebelumnya, posisi, lama absen, kualitas pengganti, dan perubahan dari laga sebelumnya. Kontrol kekuatan tim/lawan, venue, kompetisi, serta kepadatan jadwal. Bandingkan model tanpa fitur absensi, hitungan sederhana, dan fitur berbobot peran. Jangan memakai nilai pemain yang diperbarui setelah pertandingan.

Definisikan "22%" dahulu: peluang awal 50% yang turun 22% **relatif** menjadi 39%, sedangkan turun **22 poin persentase** menjadi 28%. Tidak ada potongan yang aktif di skill ini.

## H02 — Win rate kandang 35% lebih tinggi daripada tandang

**Status:** home advantage didukung, angka universal 35% belum terverifikasi.

Analisis 17.376 laga Bundesliga oleh Beckmann menemukan bahwa efek kandang dan kontribusi jarak berubah sepanjang periode studi. Hasil ini tidak menghasilkan satu pengali kemenangan yang berlaku untuk semua liga dan musim. [Penelitian home advantage dan jarak, terbit daring 2021](https://link.springer.com/article/10.1007/s12662-021-00787-7)

**Uji:** hitung win rate home/away per liga dan musim memakai seluruh hasil termasuk seri pada denominator. Laporkan selisih poin persentase dan perubahan relatif `(home_rate/away_rate - 1)`; bila away_rate nol, perubahan relatif tidak terdefinisi. Sesuaikan kekuatan tim/lawan, venue netral, serta jadwal. Proporsi poin yang dimenangkan di kandang bukan win rate kandang.

## H03 — Jarak perjalanan meningkatkan kerugian tim tandang

**Status:** masuk akal sebagai fitur, tetapi pengaruhnya bergantung konteks.

Pada studi Bundesliga tersebut, hubungan jarak dengan home advantage melemah dari waktu ke waktu dan tidak signifikan pada periode modern yang dianalisis. Temuan dari satu negara tidak boleh langsung digeneralisasi ke perjalanan lintas zona waktu atau liga lain. [Beckmann](https://link.springer.com/article/10.1007/s12662-021-00787-7)

**Uji:** jarak/durasi perjalanan, pergantian zona waktu, hari istirahat, asal perjalanan aktual, jadwal, dan interaksi dengan kompetisi. Kontrol venue dan kekuatan tim. Catat jika hanya tersedia proxy jarak antarkota.

## H04 — Zona degradasi menaikkan tekel dan pressing 18%

**Status:** angka 18% serta penyamaan tekel dengan pressing belum terverifikasi.

Penelitian Link atas 1.211 pertandingan Bundesliga dan divisi keduanya membahas pentingnya laga dan aktivitas pemain. Abstraknya melaporkan perubahan pada beberapa metrik aktivitas, dengan perbedaan antarliga. Ukuran duel, pelanggaran, dan lari cepat tidak identik dengan tekel atau pressing; penelitian itu tidak menetapkan aturan degradasi +18%. Akses yang diperiksa hanya abstrak, bukan keseluruhan bab. [Match Importance Affects Player Activity, 2018](https://link.springer.com/chapter/10.1007/978-3-658-21177-6_5)

**Uji:** definisikan posisi/zona dan peluang konsekuensi klasemen dari informasi sebelum laga, lalu ukur tekel per menit tanpa bola, pressure events, high turnovers, dan PPDA dari provider yang sama. PPDA lebih rendah dapat menandakan intensitas lebih tinggi; jangan menukar arah tandanya. Kontrol penguasaan bola, lawan, skor saat kejadian, kartu merah, fase musim, dan pelatih. Faktor yang diketahui setelah kickoff hanya dipakai untuk penelitian penjelas, bukan fitur prediksi prapertandingan.

## H05 — Perburuan top 4 meningkatkan konsistensi hasil

**Status:** hipotesis belum tervalidasi.

Tim kuat lebih mungkin berada di papan atas, sehingga korelasi posisi dan hasil belum menunjukkan pengaruh motivasi. Definisikan konsistensi terlebih dahulu, misalnya variasi residual poin terhadap ekspektasi model dasar atau stabilitas xGD pada jendela berikutnya. Jangan memilih metrik setelah melihat hasil terbaik.

**Uji:** gunakan status perburuan kualifikasi dan sisa pertandingan yang diketahui saat cutoff, kontrol kualitas awal tim serta lawan, dan bandingkan di musim berikutnya. Periksa aturan kompetisi; jumlah tempat kualifikasi tidak selalu empat.

## H06 — Pola serangan/pertahanan meningkatkan BTTS

**Status:** kumpulan kandidat fitur, belum menjadi aturan universal.

Uji rata-rata 12–15 tembakan, kualitas peluang, kejadian 76–90+, serangan sayap/transisi, xGA set piece, crossing, serta ruang setelah pressing. Jangan mengarang pola taktik ketika data event tidak tersedia. Contoh kebobolan 1–2 gol pada empat/lima laga dan clean sheet 18–24% bukan hasil pengukuran yang sudah ada.

**Uji:** bandingkan tambahan setiap fitur dengan baseline xG/kekuatan tim dan laju gol liga. Hindari memasukkan fitur berulang tanpa menilai sumbangan tambahannya. Gunakan Brier, log loss, dan kalibrasi BTTS pada data di luar pelatihan; akurasi label saja tidak cukup.

## H07 — Pembalikan pasar T-30 menandakan informasi internal

**Status:** pembalikan dapat menjadi pemicu pemeriksaan; penyebabnya belum terbukti dari grafik saja.

Hipotesis efisiensi pasar membahas bagaimana informasi tercermin dalam harga. Penerapannya pada Polymarket sepak bola perlu diuji, dan tidak membuktikan bahwa setiap lonjakan berasal dari bocoran cedera atau rotasi. Landasan konsep: [Fama, 1970](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1540-6261.1970.tb00518.x) dan [pembahasan RBA](https://www.rba.gov.au/publications/rdp/1995/9501/introduction.html). Batas penerapan ini adalah penilaian metodologis Superanalyst.

**Uji:** tetapkan jendela T-30, definisi perubahan, ketahanan pergerakan, spread dan likuiditas sebelum pengujian. Cocokkan dengan waktu berita publik, pengumuman XI, serta tiga pasar sebanding. Pisahkan berita terkonfirmasi, mikrostruktur/likuiditas, dan penyebab tak diketahui. Bandingkan model lapangan saja, pasar saja, dan kombinasi; nilai tambahan informasi di luar sampel.

## Catatan empiris 12 November 2026

[Pengembangan UCL](../../../backtests/ucl-model-upgrade-v1/review.md) menguji kekuatan tim/lawan, jendela 5/10/20, kandang, istirahat, H2H, proxy jarak kota dan proxy poin fase UCL. Resep berbeda per target dipilih pada 125 laga validasi, kemudian membaik terhadap gol5 pada 378 laga dua musim uji. Ini tidak menaksir efek psikologis, tidak membuktikan angka 22%/35%/18%, dan tidak menyatakan setiap komponen memberi manfaat sendiri di luar sampel.

[Studi xG tambahan](../../../backtests/xg-domestic-2015-v1/review.md) berada di dua liga pria 2015/16. Campuran membantu pemenang terhadap baseline gol5 pada sampel itu, tetapi BTTS dan total gol berbasis xG murni tidak membaik. Perbandingan jendela yang sama ditandai sebagai diagnosis posthoc; belum menjadi dasar mengaktifkan xG pada UCL modern.

Absensi berbobot peran/pengganti dan anomali pasar belum memiliki arsip sebelum cutoff yang cukup dalam pekerjaan ini. Validasi cap waktu dan sumber sudah tersedia, tetapi efek prediktifnya tetap belum diuji. [Status cakupan](../../../backtests/ucl-model-upgrade-v1/coverage-status.json).

## Cara memperbarui status

Gunakan status `hipotesis`, `didukung pada konteks tertentu`, `tidak didukung pada sampel uji`, atau `belum dapat dinilai`. Simpan ID eksperimen, sumber/dataset, periode, cutoff, ukuran sampel, versi fitur/model, efek beserta ketidakpastiannya, dan metrik out-of-sample. Koefisien baru hanya aktif dalam model dan konteks yang benar-benar diuji. Jangan mengubah semua hipotesis menjadi aturan hanya karena satu musim terlihat cocok.
