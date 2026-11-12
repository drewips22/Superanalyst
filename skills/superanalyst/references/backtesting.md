# Protokol evaluasi dan backtest

## Tujuan dan status

Uji apakah fitur meningkatkan prediksi pertandingan berikutnya, serta apakah probabilitas sesuai frekuensi hasilnya. Jangan menilai metode hanya dari beberapa prediksi yang berhasil. Repo v0.4.0 menyediakan model penelitian terlatih, dengan pemilihan pada 125 laga dan peningkatan terhadap baseline lima laga pada 378 laga UCL dua musim uji terpisah. Ini rekonstruksi dengan proxy ketersediaan data, belum merupakan konfirmasi pada forecast yang direkam saat itu. Studi xG tambahan juga dipisahkan dari UCL. Lihat [catatan penelitian](research-log.md) dan [batas model](trained-models.md).

## Bekukan rancangan eksperimen

Sebelum melihat hasil test, catat:

- Kompetisi, kategori tim, musim, cakupan hasil waktu normal, dan kebijakan laga tunda/ditinggalkan/void.
- Target: 1X2, BTTS, clean sheet, atau jumlah gol; metrik utama untuk setiap target.
- Horizon: misalnya T-24 jam, T-60, T-30, atau T-5 menit. Setiap horizon menjadi eksperimen tersendiri. Label `T-30` harus sesuai selisih cap waktu aktual dan toleransi yang sudah ditetapkan.
- Jendela fitur, bobot recency, aturan H2H, definisi absensi/motivasi/anomali, dan kebijakan data hilang.
- Model pembanding, periode train/validation/test, metrik keberhasilan, serta aturan pemilihan laga.

Tetapkan jumlah liga dan kandidat fitur dengan sadar; banyak percobaan meningkatkan peluang menemukan pola kebetulan. Simpan juga percobaan yang tidak berhasil.

## Data yang tersedia pada waktunya

Setiap prediksi menyimpan `as_of`, `recorded_at`, `kickoff_at`, waktu terakhir fitur `features_available_at`, versi data/model, serta sumber. Hubungan yang diperlukan:

```text
features_available_at <= as_of <= recorded_at < kickoff_at
```

`available_at` adalah waktu informasi benar-benar tersedia, bukan sekadar tanggal pertandingan. `retrieved_at` adalah waktu pengunduhan. Arsip yang diunduh sekarang boleh membantu rekonstruksi historis hanya jika ketersediaan saat itu dapat dibuktikan; jangan memalsukan waktu pencatatan lama. Bedakan **forecast yang dibekukan saat itu** dari **backtest rekonstruksi saat ini**.

Evaluator memisahkan dua mode:

- `forecast` (bawaan untuk kompatibilitas): urutan waktu di atas tetap berlaku, termasuk `recorded_at` sebelum kickoff.
- `retrospective_reconstruction`: `as_of < kickoff_at <= reconstructed_at`, tanpa `recorded_at` fiktif. Wajib isi `point_in_time_verified` dan `reconstruction_notes`. `features_available_at` boleh null bila waktu ketersediaan asli belum dapat dibuktikan; jika ada nilainya, tetap harus <= `as_of`.

Kedua mode tidak digabung dalam satu skor kelompok. Rekonstruksi dengan sumber yang tidak diarsipkan harus diberi label batasnya; mode ini tidak mengubahnya menjadi uji buta. Catat waktu kejadian dan waktu pengunduhan secara terpisah. Untuk backtest luas, gunakan dataset point-in-time dan kode walk-forward; jangan memilih fitur setelah melihat hasil.

Hindari kebocoran melalui klasemen akhir musim, versi xG yang direvisi belakangan, cedera yang baru diumumkan setelah cutoff, line-up resmi pada prediksi T-24 jam, closing odds setelah cutoff, serta statistik pertandingan target. Hasil final hanya menjadi label setelah laga selesai.

## Pemisahan kronologis

1. Mulai dengan blok latihan yang mendahului blok validasi.
2. Pilih parameter dan kalibrasi dari latihan/validasi tersebut.
3. Bekukan, lalu prediksi blok waktu berikutnya yang belum dilihat.
4. Geser cutoff maju; jika melatih ulang, gunakan hanya data yang sudah selesai dan tersedia saat itu.
5. Sisakan musim/blok paling akhir sebagai evaluasi final yang tidak dipakai memilih fitur.

Jangan mengacak baris pertandingan lintas waktu. Semua snapshot dari satu laga harus berada di blok yang sama. Saat bootstrap untuk ketidakpastian, kelompokkan snapshot satu laga; pertimbangkan blok waktu agar ketergantungan jadwal tidak dianggap sebagai sampel independen.

## Model pembanding dan ablation

Bandingkan pada kumpulan laga serta cutoff yang sama:

1. Frekuensi hasil liga dari data latih sebelum cutoff.
2. Baseline kekuatan tim dan efek kandang, misalnya regresi Poisson yang ditaksir dari data latih.
3. Baseline + fitur lima laga/xG.
4. Tambahkan H2H, absensi, perjalanan, motivasi, lalu fitur taktik satu per satu.
5. Pasar saja pada cutoff yang sama, dan model gabungan bila memang dikembangkan.

Catat perubahan cakupan saat fitur baru menghilangkan banyak laga. Nilai perbandingan pada subset bersama sekaligus laporkan cakupan total. Closing price dapat menjadi pembanding tambahan setelahnya; jangan menyebutnya baseline dengan informasi yang setara jika diperoleh lebih dekat ke kickoff.

## Metrik

Untuk probabilitas `p` dan label one-hot `y`:

```text
Brier 1X2 = mean(sum_k (p_k - y_k)^2)   [tanpa dibagi 3; rentang 0–2]
Log loss 1X2 = mean(-ln(p_hasil))
Brier BTTS = mean((p_BTTS - y_BTTS)^2)  [rentang 0–1]
Log loss BTTS = mean(-y*ln(p) - (1-y)*ln(1-p))
```

Semakin kecil semakin baik. Untuk komputasi log loss, evaluator membatasi probabilitas yang dipilih ke `[1e-15, 1-1e-15]` dan mencantumkan batas tersebut. Brier menggunakan probabilitas asli.

Laporkan tabel kalibrasi: jumlah laga, rerata probabilitas, dan proporsi kejadian pada interval probabilitas yang ditetapkan di awal. Evaluator memakai sepuluh interval sama lebar untuk setiap hasil dan BTTS; bin kecil tidak membuktikan kalibrasi. Sertakan ketidakpastian dengan metode yang sesuai ketika data nyata cukup; evaluator awal tidak otomatis menghitung interval keyakinan.

Akurasi pilihan teratas boleh menjadi metrik sekunder. Hasil skor tepat bersifat lebih sulit dan tidak sama dengan kualitas 1X2/BTTS. Evaluasi per liga, musim, horizon, kualitas data, dan model; hindari menggabungkan model atau horizon berbeda menjadi satu angka tanpa penjelasan.

Jika kelak pengguna meminta evaluasi keuntungan, hitung biaya, spread, slippage, void, waktu quote, dan harga yang benar-benar bisa dieksekusi. Keuntungan tidak disimpulkan dari akurasi saja.

## Arsip, revisi, dan abstain

Simpan prediksi awal secara append-only. Revisi punya `prediction_id` baru, alasan, dan cap waktu. Saat menilai satu model/horizon, pilih snapshot sesuai aturan sebelum melihat hasil; jangan memilih revisi terbaik sesudahnya. Evaluator menolak duplikasi pertandingan dalam satu kelompok model/horizon/kompetisi.

Log juga keputusan `observe` atau `insufficient_data`. Laporan evaluasi harus menunjukkan berapa laga dipertimbangkan, diprediksi, dilewati, belum selesai, dan selesai. Probabilitas yang tidak dikeluarkan tidak menjadi nol. Cakupan tinggi/rendah harus dibaca bersama skor kualitas prediksi.

Gabungkan label hasil setelah laga selesai tanpa mengubah isi prediksi. Catat ID laga, skor 90 menit, waktu selesai, status final, dan sumber hasil. Jika rekonstruksi hanya memiliki tanggal selesai UTC yang dapat dibuktikan, gunakan `completed_date_utc` dan biarkan `finished_at` null; jangan mengarang presisi jam. Pada forecast nyata gunakan arsip prediksi terpisah atau hash/commit sebelum kickoff; pemeriksaan timestamp saja tidak membuktikan bahwa file tidak pernah diedit.

## Syarat menaikkan versi

Simpan laporan eksperimen berisi ukuran sampel, periode, baseline, perubahan metrik, kalibrasi, cakupan, sumber, dan batas ketidakpastian. Naikkan versi model hanya jika manfaat terlihat pada blok waktu berikutnya dan tidak hanya akibat perubahan pemilihan laga. Jika belum ada bukti yang cukup, pertahankan fitur sebagai hipotesis.
