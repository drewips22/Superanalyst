# Protokol keputusan v1.1

Mulai 13 November 2026, versi plugin 0.4.2. Perubahan ini dipilih sebelum prediksi matchday berikutnya. Acuan analisis tetap `qualitative_superanalyst_national_team_pilot_v1`; tidak ada jendela fitur, koefisien, probabilitas atau bobot tim yang diganti karena satu sesi berhasil.

## Tiga keputusan terpisah

Setiap target `1x2`, `btts` dan `total_2_5` mencatat:

- `pick`: H/D/A untuk 1X2, true/false untuk BTTS, over/under untuk total 2,5; null bila observasi.
- `confidence`: low/medium/relatively_strong untuk pilihan yang diterbitkan; null bila observasi. Label ini kualitatif, bukan peluang terkalibrasi.
- `status`: provisional atau analisis_layak bila dipilih; observasi atau tidak_cukup_data bila belum dipilih.
- `supporting_evidence` dan `contradicting_evidence`: bukti untuk target tersebut, bukan hanya untuk pemenang.
- `abstain_reason`: alasan ketika pick kosong. Pilihan seri harus didukung bukti untuk hasil seri; jangan menggunakannya sebagai sinonim belum tahu pemenang.

Skenario skor disimpan terpisah. Bila bukti BTTS atau total lebih lemah daripada arah pemenang, tampilkan perbedaan itu; tidak perlu memaksakan seluruh target. Laporkan cakupan keputusan agar pengurangan pilihan tidak tampak sebagai kenaikan akurasi tanpa konteks.

## Pemeriksaan pemain dan sumber

Catat sumber serta waktu pengecekan ketersediaan, peran pemain, apakah XI resmi sudah diumumkan, dan konflik yang belum selesai. Bila pemain sekaligus disebut absen dan masuk perkiraan XI, tandai konflik atau jangan tampilkan XI yang meragukan. Pada analisis jauh sebelum kickoff, hasil tetap provisional; tidak mengarang pengumuman XI.

Jika pembaruan setelah XI resmi benar-benar dilakukan, simpan snapshot baru dengan waktu dan alasan. Jangan menjanjikan pemantauan otomatis atau mengklaim pembaruan yang tidak pernah direkam. Informasi baru tidak dimasukkan kembali ke snapshot lama.

Cocokkan skor/penalti/kartu pada agregat dengan event bila tersedia. Perbedaan menjadi peringatan kualitas sumber, bukan alasan mengubah nilai atau menambah penalti numerik secara diam-diam. Jangan mencampur statistik 120 menit dengan skor 90 menit; venue netral dan kandang administratif harus dibedakan dari kandang sebenarnya.

## Batas evaluasi

Arsip pilot lama tetap dinilai 8 pilihan 1X2, 6 BTTS dan 6 total sesuai pilihan yang diterbitkan saat itu. Format baru hanya berlaku pada prediksi baru. Kesalahan tidak dibuang sebagai unlucky. Perbaikan pencatatan dapat diperiksa sekarang; klaim peningkatan kemampuan prediksi memerlukan pertandingan baru.

Gunakan `scripts/forecast_archive.py validate` untuk memeriksa snapshot baru jika tersedia Python. Perintah `grade` menilai pilihan kualitatif dari label 90 menit yang diberikan tanpa mengubah arsip sumber. Alat ini bukan model probabilitas dan tidak menilai Brier/log loss ketika tidak ada probabilitas.
