# Model Utama Superanalyst

**Model Utama** adalah pilihan default Superanalyst untuk laga klub dan tim nasional sejak 21 November 2026. Metode ini berasal dari acuan kualitatif yang disetujui pada 13 November 2026. Gunakan label **Model Utama** pada analisis baru. Jurnal memakai ID metode `qualitative_superanalyst_national_team_pilot_v1` agar prediksi dapat dinilai bersama arsip dengan metode yang sama. [Spesifikasi metode](../assets/unl-baseline-policy.json)

Pertahankan keseluruhan pendekatan sesi UNL 13 November 2026 WIB, termasuk kesalahan yang terjadi. Keberhasilan tujuh laga tidak dipakai untuk memilih ulang aturan hanya dari tujuh pemenang tersebut.

## Yang menjadi acuan

1. Urutan data → pola → keputusan dan keenam kelompok analisis pada SKILL.md tetap berlaku.
2. Gunakan lima laga kompetitif terakhir secara kronologis dan bahas laga persahabatan secara terpisah. Perbarui data setiap pertandingan. Untuk klub, gunakan klasemen dan catatan kandang atau tandang liga sebagai pembanding. Untuk tim nasional, gunakan konteks fase kompetisi. Pada UEFA Nations League, bandingkan dengan empat laga fase grup terbaru bila tersedia.
3. Tampilkan gol, rata-rata kebobolan, hasil dan poin per laga, tembakan/tepat sasaran, clean sheet/BTTS historis, H2H relevan dan gol menit akhir. xG/xGA yang belum diperoleh tetap N/A dengan cakupan yang jelas.
4. Periksa kualitas lawan, skor ekstrem, usia data, venue netral, serta konteks kartu merah. Konteks membantu membaca data; tidak berarti pertandingan boleh dihapus tanpa aturan yang ditetapkan sebelumnya.
5. Gunakan berita primer terbaru untuk cedera, skorsing, ketersediaan, pelatih dan motivasi klasemen. XI perkiraan tetap berlabel perkiraan. Tidak mengarang rute perjalanan atau menit pemulihan klub.
6. Pisahkan arah 1X2, BTTS, total gol dan skenario skor. Keyakinan arah pemenang bukan probabilitas terkalibrasi untuk semua target. Bila bukti belum cukup, pertahankan observasi yang dijelaskan, seperti BTTS/total pada Ceko–Spanyol dalam pilot.
7. Gunakan keyakinan kualitatif per target. Jalankan model terlatih dan varian eksperimen hanya atas permintaan pengguna dengan cakupan validasi yang sesuai. Model Utama menggunakan aturan dan koefisien yang tercantum pada spesifikasi metode.
8. Verifikasi pasar bila data tersedia; jika tiga pembanding independen, waktu, kontrak, spread dan likuiditas belum dapat disamakan, nyatakan pemeriksaan belum lengkap. Jangan menyimpulkan anomali atau informasi internal.
9. Catat prediksi sebelum kickoff, pertahankan snapshot awal, dan simpan revisi/penilaian terpisah. Seluruh kesalahan tetap dihitung; unlucky hanya diagnosis sesudah pertandingan.

## Bukti sesi pertama

Prediksi dicatat 12 November 2026 pukul 18.04 WIB untuk delapan laga 13 November WIB. Hasil 90 menit dikonfirmasi melalui [UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/) dan ESPN, lalu dinilai terhadap snapshot asli:

| Target | Benar / dinilai |
| --- | ---: |
| Arah 1X2 | 7/8 |
| BTTS | 5/6 |
| Total 2,5 gol | 5/6 |
| Skenario skor tepat | 5/8 |

Italia–Prancis salah pada seri dan Under; Inggris–Kroasia salah pada BTTS Tidak. Dua laga observasi tetap memiliki pilihan 1X2 dalam arsip sehingga keduanya tetap dinilai. Tidak ada penyesuaian denominator sesudah melihat hasil.

Ini satu matchday prospektif, bukan bukti akurasi jangka panjang atau keunggulan atas pasar. Tidak ada probabilitas awal sehingga Brier/log loss tidak dapat dihitung. Arsip asli tetap lokal di `runs/unl-2026-11-12/`; salinan bukti terpilih dapat disertakan dalam paket privat pada `reference-cases/unl-2026-11-12/`.

## Perbaikan pencatatan yang disetujui

Versi plugin 0.4.2 menambahkan [protokol keputusan v1.1](decision-quality.md): keyakinan/status terpisah per target, observasi terstruktur, pengecekan konflik pemain serta kualitas sumber. Berlaku untuk snapshot baru; tidak menghapus pilihan lama dan tidak mengganti metode atau bobot acuan.

Perbandingan manfaat snapshot XI resmi, model rating lawan dan tambahan fitur xG tetap memerlukan pengujian. Jangan menyebut perbaikan pencatatan sebagai peningkatan akurasi sebelum dibuktikan pada pertandingan baru. Acuan kerja ini tetap memakai fakta terbaru; yang ditahan adalah pengaktifan koefisien baru tanpa pengujian.
