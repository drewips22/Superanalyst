# UNL 17–18 November 2026 — Beta V2 dan Hybrid

Delapan pertandingan, kickoff 18 November pukul 02.45 WIB. Prediksi direkam nyata sebelum kickoff dengan cutoff 17 November pukul 20.21.27 WIB. Hasil aktual belum tersedia.

Baca [analisis lengkap](Analisis-Lengkap-Beta-V2-Hybrid.md) untuk lima laga setiap tim, 16 XI perkiraan, konteks, H2H, tiga target, probabilitas, pasar dan sensitivitas.

- Beta V2: 9 target aktif, fokus 5 laga. Hybrid: 7 target aktif, fokus 5 laga.
- `experimental-forecast-v1.json` berisi kedua model; `main-forecast-v1.json` memuat input kualitatif utama yang dibekukan sebelum inferensi Beta.
- `main-journal-v1.json` merekam fakta dan keputusan utama. Metode utama dan semua arsip lama tetap.
- `model-package-forecast-v1.json` adalah fit baru dengan resep yang tetap, skor latihan paling akhir 14 November dan penyangga tiga hari.
- Kalibrasi historis belum membuktikan akurasi pada matchday ini. Probabilitas Hybrid adalah dukungan Beta, bukan probabilitas gabungan baru.
- Dua resep MC mentah × 10.000 sampel × 8 laga = 160.000 skenario. Hasil MC bukan distribusi gabungan marginal terkalibrasi.

## Integritas dan reproduksi

`publication-manifest-v1.json` adalah daftar hash byte file publik. `original-local-manifest-v1.json` dan `freeze-receipt-v1.json` mempertahankan hash sumber asli. Satu file pembaruan latihan menghapus lokasi arsip lokal dari 41 baris; nilai skor, tim, tanggal, venue, dan URL sumber tetap. Karena itu hash file pembaruan publik berbeda dari `updates_sha256` sumber asli pada paket fit. Tidak ada perubahan parameter atau prediksi akibat penghapusan lokasi tersebut.

Kode model yang tetap tersedia di `../../model/`. Inferensi dapat dihitung kembali dari paket fit dan `beta-inputs-v1.json`; jangan menggunakan mode rekonstruksi untuk mengganti rekaman forecast ini. Cek `verification-v1.json` dan `delivery-qa-v1.json` untuk hasil verifikasi.

## Penilaian sesudah pertandingan

Gunakan `outcomes-pending-v1.json` sebagai format, lalu buat file hasil baru dengan skor 90 menit, URL sumber dan waktu verifikasi. Jangan menimpa file pending atau snapshot prediksi. Hitung akurasi per target dan fokus beserta cakupan; bandingkan kedua model pada subset laga/target yang sama. Akurasi aktual saat penerbitan: menunggu hasil.
