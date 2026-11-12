# Catatan pengembangan empiris

Ditinjau 12 November 2026. Hasil di sini berasal dari rekonstruksi dengan hasil historis sudah terekspos dan versi sumber asli tidak sepenuhnya diarsipkan. Tidak ada koefisien universal yang disahkan; parameter terlatih hanya berlaku dalam varian dan cakupan penelitiannya.

## Pengembangan terlatih v0.4.0

[Laporan UCL dua musim](../../../backtests/ucl-model-upgrade-v1/review.md): corpus 25.496 catatan laga, 125 laga validasi 2023/24, 378 laga uji 2024/25–2025/26. Pilihan dikunci sebelum penilaian uji, dengan fit bulanan yang hanya memakai data terdahulu. Dibanding baseline lima laga, log loss 1X2 turun 8,2%, Brier BTTS 3,6%, Brier Over 2,5 5,2%; masing-masing juga membaik di kedua musim uji. Itu penurunan kesalahan, bukan tambahan poin persentase akurasi.

Resep eksperimental yang lolos memakai model berbeda per target: kekuatan tim/kandang/form10/istirahat/proxy poin fase untuk 1X2, gol20 untuk BTTS, kekuatan tim untuk total gol. Lihat [panduan pemakaian](trained-models.md). H2H dan jarak antarkota tidak dipilih karena tidak menambah perbaikan pada validasi. Efek motivasi psikologis, absensi, dan anomali pasar belum ditaksir; angka 22%, 35%, 18% tetap tidak aktif.

[Studi xG terpisah](../../../backtests/xg-domestic-2015-v1/review.md) memuat 760 laga dua liga pria 2015/16, dengan 179 validasi dan 222 uji. Campuran gol+xG jendela 10 memperbaiki prediksi pemenang terhadap gol5, tetapi xG murni tidak memperbaiki BTTS/total gol. Kontrol jendela yang sama ditambahkan sesudah penilaian dan diberi label posthoc; jangan menganggap seluruh keuntungan campuran sebagai efek xG atau memindahkannya ke UCL modern.

Catatan pengguna tentang Fenerbahçe beruntung disimpan sebagai diagnosis tidak terverifikasi. Kekalahan Liverpool tetap dinilai. Snapshot model lama, fitur, kode dan hasil tidak diubah untuk membuat prediksi lama terlihat lebih baik. Koefisien terlatih hanya berlaku pada varian dan cakupan penelitian masing-masing; belum menjadi angka universal skill.

## Sesi Rabu Matchday 4 UCL 2026/27

[Laporan lengkap sembilan laga](../../../backtests/ucl-2026-11-04/review.md), cutoff 4 November 2026 12:00 UTC. Lima laga kompetitif terakhir untuk 18 tim; 90 catatan tim-laga. Skor 90 menit tersedia 90/90, tembakan 80/90, xG konsisten 0/90. Sumber serta waktu pengambilan ada di [ledger fitur](../../../backtests/ucl-2026-11-04/features.json).

Baseline `last5-goals-mean-poisson-experimental-v1` tetap tanpa penyesuaian: 1X2 6/9, BTTS 7/9, Over 2,5 8/9. Sembilan hasil semuanya BTTS dan Over 2,5. Brier lebih baik daripada pembanding uniform pada cohort ini, tetapi tidak ada kelas negatif untuk menguji daya pemilah BTTS, dan ini bukan uji di luar sampel yang buta.

### Temuan untuk proses data

- Jadwal yang disebut seluruh kompetisi tetap dapat melewatkan piala domestik. PAOK–AEK, Porto–Viseu dan Brugge–Lokeren dilengkapi sebelum pembekuan. Slavia dan Sabah membutuhkan sumber domestik lain. Wajib periksa kelengkapan sebelum menyebut lima laga terakhir.
- Hasil adu penalti bukan kemenangan 90 menit. Arsenal–Fleetwood 1–1, Liverpool–Chelsea 1–1 dan City–Brighton 2–2 disimpan sebagai seri, dengan skor dua babak normal.
- Gol lima laga mentah lintas liga belum sebanding: Slavia–Arsenal dan Viking–Sabah menjadi kegagalan pilihan pemenang. Kekuatan lawan adalah kandidat fitur berikutnya; dua kegagalan ini tidak menaksir bobotnya.
- Tujuh dari sepuluh gol PSV berasal dari satu kemenangan 7–0. Tampilkan distribusi/rentang dan kontribusi laga terbesar bersama rata-rata. Jangan menambah bobot kemenangan besar setelah mengetahui hasil berikutnya.

### Hipotesis yang belum lolos uji

- Kedua tim mencetak gol ≥4/5: kelompok memenuhi 7/7 BTTS, tidak memenuhi juga 2/2. Belum ada daya pemilah yang terukur.
- Kedua tim kebobolan ≥4/5 dan masing-masing clean sheet ≤1/5 adalah flag yang sama pada jendela lima laga. Jangan dihitung ganda.
- Setidaknya satu tim memiliki ≥3 clean sheet pada tiga pasangan; semuanya tetap BTTS. Ini menolak kepastian berbasis clean sheet saja pada contoh tersebut, bukan membuktikan tidak ada nilai prediktifnya secara umum.
- Rentang tembakan 12–15 untuk kedua tim: tidak ada kasus memenuhi di empat pasangan dengan data penuh, lima pasangan tidak lengkap. Belum teruji.
- Berita absensi/pergantian pelatih dan catatan kandang/tandang tersedia untuk sebagian laga, tetapi tidak masuk baseline. Efek tambahannya belum diukur; angka 22%, 35%, 18% tetap tidak aktif.
- Kartu merah, gol set piece dan transisi pada pertandingan target dicatat hanya setelah prediksi dibekukan. Urutan waktu harus diperiksa: Napoli dan Sabah sudah tertinggal ketika mendapat kartu merah. Kejadian itu tidak boleh dipindahkan menjadi fitur pralaga.

### Eksperimen berikutnya

Tetapkan sampel berurutan sebelum hasil, termasuk BTTS tidak dan Under 2,5. Gunakan data lebih panjang sebelum cutoff untuk mengestimasi kekuatan tim/lawan, kandang dan tingkat gol liga. Tambahkan fitur satu per satu pada cohort dan horizon sama; ukur Brier, log loss, kalibrasi dan cakupan pada blok berikutnya. Uji aturan observasi ketika informasi penting bertentangan, tanpa menerapkannya surut pada kasus yang sudah dinilai.

Pasar T-30 menit memerlukan eksperimen terpisah dan snapshot tiga sumber dengan kontrak/waktu sebanding. Tidak ada pengujian anomali pasar atau keuntungan transaksi pada studi ini.
