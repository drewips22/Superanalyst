# Lingkungan plugin ChatGPT

Paket Superanalyst memuat skill, referensi dan alat Python. Metode analisis sama dengan salinan lokal; pemasangan plugin tidak menambahkan layanan xG berbayar, akun pasar, atau koneksi GitHub pribadi secara otomatis.

Gunakan kemampuan penelusuran dan perhitungan yang memang tersedia pada chat. Bila alat eksekusi atau sumber data tidak tersedia, laporkan batasnya dan gunakan penilaian kualitatif sesuai panduan. Jangan mengklaim telah menjalankan skrip atau melihat data hanya karena filenya berada dalam paket.

Untuk menjalankan contoh/replay, temukan akar paket yang memiliki `plugin.json` dan `skills/superanalyst/`; perintah dalam [panduan alat](tools.md) relatif terhadap akar itu. Alat dasar memakai pustaka standar; fit/replay penelitian memerlukan dependensi opsional di `requirements-research.txt`. Jangan memindahkan model UCL ke timnas tanpa validasi.

Paket cloud tidak bergantung pada drive C:, program Windows, server lokal, hooks, atau MCP lokal. Link penelitian relatif menunjuk ke materi di dalam paket. Arsip pengguna di komputer tidak otomatis tersinkron; hanya bukti yang benar-benar disertakan saat pembuatan paket tersedia di akun.

Salinan pilot UNL, bila ada, berada pada `reference-cases/unl-2026-11-12/`. `portable-evidence-manifest.json` menjelaskan checksum salinan dan batas bukti. Jangan mengubah salinan yang sudah dinilai untuk memperbaiki hasil. Buat prediksi dan berkas penilaian baru untuk laga berikutnya.
