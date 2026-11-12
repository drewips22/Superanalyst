---
name: superanalyst
description: Analisis prapertandingan sepak bola dengan lima laga terakhir, xG, H2H, line-up, motivasi, BTTS, dan perbandingan pasar; serta evaluasi prediksi historis. Gunakan untuk prediksi laga mendatang, laporan Superanalyst, atau backtest sepak bola.
---

# Superanalyst

Susun analisis dalam urutan **data → pola → keputusan**. Jawab dalam bahasa pengguna; bahasa bawaan Indonesia. Versi awal ini adalah kerangka penelitian, belum merupakan model prediksi yang terkalibrasi.

## Pilih pekerjaan

- **Analisis pertandingan:** baca [metodologi](references/methodology.md), lalu gunakan [format laporan](assets/report-template.md).
- **Pergerakan pasar/Polymarket:** baca juga [protokol pasar](references/markets.md).
- **Menguji aturan atau prediksi:** baca [daftar hipotesis](references/hypotheses.md) dan [protokol backtest](references/backtesting.md).
- **Perhitungan berulang:** gunakan [panduan alat](references/tools.md). Alat menghitung statistik dan mengevaluasi probabilitas; pengumpulan berita serta penentuan parameter tetap memerlukan sumber dan metode yang dijelaskan.

## Kunci pertandingan dan batas waktu

Pastikan tim, kompetisi, tanggal, kickoff, zona waktu, dan venue. Bila jadwal ambigu, cari jadwal resmi sebelum meminta informasi yang masih kurang. Tampilkan waktu pengguna; gunakan WIB bila pengguna tidak menentukan zona waktu lain. Simpan waktu mesin sebagai ISO 8601 dengan offset.

Catat `as_of` (batas informasi) sebelum analisis. Untuk prediksi nyata, verifikasi jadwal, statistik, berita, klasemen, dan ketersediaan pemain dengan sumber terkini. Untuk rekonstruksi historis, hanya gunakan informasi yang tersedia sebelum `as_of`; berita dan hasil setelahnya bukan fitur. Bila penelusuran tidak tersedia, jelaskan cakupan data yang diberikan dan jangan menyebutnya berita terbaru.

Rekonstruksi yang dibuat sekarang wajib mencatat `reconstructed_at` sebenarnya dan batas arsip sumber, tanpa `recorded_at` fiktif sebelum kickoff. Pisahkan penilaian rekonstruksi dari forecast yang benar-benar direkam saat itu. Bekukan aturan dan masukan sebelum tahap penilaian; keterulangan perhitungan tidak sama dengan uji buta bila hasil historis sudah diketahui.

Standar hasil adalah **90 menit + injury time**, tanpa extra time atau adu penalti. Bedakan hasil 1X2, lolos babak berikutnya, dan hasil kontrak pasar. Periksa venue netral, laga tunda, dan perubahan kickoff.

## Data: enam kelompok wajib

1. **Lima laga terakhir setiap tim.** Tampilkan pertandingan satu per satu, tanggal, lawan, kandang/tandang/netral, skor, xG/xGA, tembakan, serta sumber. Hitung total gol dicetak, rata-rata kebobolan, W-D-L, poin per laga, xG/xGA, dan selisih xG. Jelaskan tren hasil dan tren kualitas peluang secara terpisah. Tambahkan pembanding musim atau periode lebih panjang bila tersedia. Lima laga adalah jendela pengamatan, bukan bukti statistik yang kuat dengan sendirinya.
2. **Pola gol dan H2H.** Ringkas pertemuan relevan: gol, BTTS, menang/seri/kalah, dan penguasaan bola bila tersedia. Tulis rentang tanggal dan perubahan pelatih/susunan pemain. H2H lama dan penguasaan bola tidak otomatis menentukan keunggulan saat ini.
3. **Line-up dan konteks.** Pisahkan susunan resmi dari perkiraan; daftar cedera, skorsing, keraguan tampil, dan rotasi. Nilai peran, menit bermain, kualitas pengganti, dan kabar terbaru. Periksa performa kandang/tandang, waktu istirahat, perjalanan, zona waktu, klasemen, target kompetisi, dan situasi dua leg bila relevan.
4. **BTTS.** Bandingkan xG serang dengan xGA lawan, tembakan dan kualitasnya, serangan sayap/transisi, set piece/crossing, ruang di belakang pressing, serta aktivitas menit 76–90+. Cantumkan clean sheet historis dan estimasi clean sheet laga ini sebagai dua hal berbeda. Semua pola taktik perlu data kejadian atau laporan tepercaya.
5. **Anomali pasar.** Bila pasar relevan tersedia, catat kontrak, waktu, harga, spread, kedalaman, dan perubahan sekitar 30 menit sebelum kickoff. Cari konfirmasi perubahan line-up/berita; pergerakan harga sendiri tidak membuktikan informasi internal.
6. **Pemeriksaan anomali.** Upayakan tiga sumber pasar pembanding yang independen, dengan kontrak dan waktu yang sebanding; cocokkan dengan statistik serta berita lapangan. Jika hanya satu atau dua tersedia, nyatakan jumlahnya dan tandai pemeriksaan belum lengkap. Ketidaksinkronan menjadi alasan observasi lebih lanjut.

## Pola: hubungkan bukti tanpa mengarang kepastian

- Labeli **fakta terverifikasi**, **inferensi**, **hipotesis**, dan **data tidak tersedia**. Sertakan tautan serta waktu publikasi/pengambilan untuk informasi penting.
- Data hilang tetap `null`/N/A, bukan nol. Laporkan denominator, misalnya xG tersedia 3/5 laga. Gunakan provider, jenis xG, dan cakupan waktu yang konsisten; jangan merata-ratakan provider yang berbeda tanpa harmonisasi.
- Angka awal **22%**, **35%**, dan **18%** bukan koefisien aktif. Lihat status dan cara mengujinya di daftar hipotesis. Contoh **12–15 tembakan**, **kebobolan 1–2 gol**, dan **clean sheet 18–24%** juga bukan ambang universal.
- Jangan menghitung bukti berulang sebagai faktor terpisah: hasil, gol, dan xG saling berkaitan; efek kandang bisa sudah terkandung dalam model; pasar bisa sudah merespons cedera.
- Bedakan persen relatif dari poin persentase. Jelaskan dasar setiap penyesuaian numerik. Jika belum ada model yang layak, berikan penilaian kualitatif dan skenario, bukan probabilitas karangan.

## Keputusan: simpulkan sesuai kualitas bukti

Tutup dengan kecenderungan 1X2, BTTS, skenario yang mengubah penilaian, kualitas data, dan status **analisis layak / provisional / observasi / tidak cukup data**. Status ini adalah kelayakan analisis, bukan instruksi transaksi.

Jika ada probabilitas, tulis model/versinya, parameter, asumsi, sumber, dan apakah sudah dikalibrasi. Probabilitas 1X2 berjumlah 100%; BTTS dihitung dari distribusi gabungan gol. Skor paling mungkin hanyalah salah satu skenario dan dapat memiliki peluang kecil. Bedakan rentang sensitivitas dari interval keyakinan statistik.

Simpan prediksi sebelum kickoff bila akan dievaluasi; revisi menjadi snapshot baru dengan alasan perubahan. Jangan menimpa prediksi setelah hasil diketahui. Jadwal cek ulang sebelum kickoff adalah saran pemeriksaan, bukan klaim pemantauan otomatis sedang berjalan. Akhiri secara singkat bahwa analisis menjadi bahan pertimbangan, bukan hasil mutlak.
