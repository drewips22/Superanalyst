# Catatan pengembangan empiris

Ditinjau 12 November 2026. Hasil di sini berasal dari rekonstruksi dengan hasil historis sudah terekspos dan versi sumber asli tidak sepenuhnya diarsipkan. Tidak ada koefisien baru yang disahkan.

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
