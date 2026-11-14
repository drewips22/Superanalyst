# Konteks pertandingan persahabatan

Ditinjau 14 November 2026. Ini pemeriksaan relevansi data untuk pertandingan persahabatan senior; tidak mengaktifkan bobot baru, mengubah acuan UNL, atau menganggap model penelitian UCL telah tervalidasi untuk timnas. Kategori usia/putra/putri tetap harus cocok. Jangan memasukkan hasil U20 sebagai hasil tim senior.

## Dua lapisan riwayat

Pertahankan tabel lima laga kompetitif sebagaimana [metodologi](methodology.md), lalu tampilkan uji coba terbaru secara terpisah beserta tanggal, lawan, venue dan skor 90 menit. Nyatakan jika salah satu lapisan tidak tersedia atau tidak diperiksa. Jangan menggabungkan statistik dua lapisan tanpa rancangan bobot yang telah diuji.

Untuk setiap tim, jelaskan umur catatan kompetitif terakhir, level lawan, pelatih, pemain inti yang masih relevan, dan perubahan besar sejak periode itu. Hasil lama tetap fakta yang berguna, tetapi keterwakilannya terhadap tim sekarang perlu dinilai. Jangan menetapkan batas umur atau penalti keyakinan universal dari beberapa laga yang baru selesai.

| Pemeriksaan | Kandang | Tandang |
|---|---|---|
| Laga kompetitif terakhir dan umur data | | |
| Uji coba terbaru yang diperiksa, tanggal dan lawan | | |
| Perubahan pelatih/inti pemain sejak sampel | | |
| XI resmi/perkiraan/tidak tersedia, sumber dan waktu | | |
| Aturan pergantian pemain: terverifikasi/belum diketahui | | |
| Keterwakilan data dan bukti yang berlawanan per target | | |

Aturan pergantian dan tujuan eksperimen pelatih perlu sumber; jangan menganggap semua persahabatan menggunakan batas yang sama. Konfirmasi XI tidak menghilangkan ketidakpastian susunan babak kedua. Kebutuhan mencoba pemain tidak otomatis menghasilkan gol lebih banyak atau lebih sedikit.

## Keputusan dan pengujian

Nilai 1X2, BTTS dan total secara terpisah. Arah unggulan tidak mengisi pilihan clean sheet/Under secara otomatis; banyak nama menyerang tidak mengisi BTTS Ya secara otomatis. Pola lawan lemah, risiko seri dan pergantian bek yang sudah diketahui tetap dicatat sebagai bukti berlawanan.

Tetapkan fokus sebelum hasil dan jelaskan alasannya berdasarkan target itu. Jika bukti belum cukup, gunakan observasi sesuai protokol yang sudah ada. Profil ini tidak memaksa seluruh laga persahabatan menjadi observasi dan tidak menurunkan keyakinan dengan persentase karangan.

Uji kandidat pembobotan dua lapisan riwayat pada sampel serta horizon yang sama dengan acuan, sebelum diterapkan. Simpan juga eksperimen yang tidak membaik. Kejadian kartu merah, penalti dan gol bunuh diri pada target hanya dipakai untuk diagnosis pascalaga; perlakukan kemenangan dan kekalahan secara simetris.

## Input jurnal

Untuk `profile: friendly`, `friendly_context` dipetakan berdasarkan ID laga. Tiap sisi menyimpan `last_competitive_at` (ISO ber-offset atau null), `recent_friendlies_reviewed` (boolean), `history_representativeness` (penjelasan nyata), dan `lineup_status` (`official`, `projected`, `unavailable`). `substitution_rules` menyimpan `status: verified` dengan `maximum` dan `source_id`, atau `status: unknown` dengan `maximum: null`.

Pemeriksaan mesin hanya memastikan konteks tersebut dinyatakan dan waktu/tipe datanya layak. Ia tidak mengukur kekuatan tim, menaksir efek pergantian pemain, memutuskan pilihan, atau menjamin bahwa kabar yang diisi benar. Terapkan [jurnal keputusan](decision-journal.md) untuk rekaman dan revisi; arsip lama tetap utuh.
