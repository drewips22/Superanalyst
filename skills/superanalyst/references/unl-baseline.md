# Acuan operasional UNL v1

Ditetapkan pengguna pada 13 November 2026. ID metode: `qualitative_superanalyst_national_team_pilot_v1`. Statusnya **acuan kerja kualitatif**, belum model probabilitas tim nasional terkalibrasi. Spesifikasi mesin ada di [kebijakan acuan](../assets/unl-baseline-policy.json).

Pertahankan keseluruhan pendekatan sesi UNL 13 November 2026 WIB, termasuk kesalahan yang terjadi. Keberhasilan tujuh laga tidak dipakai untuk memilih ulang aturan hanya dari tujuh pemenang tersebut.

## Yang menjadi acuan

1. Urutan data → pola → keputusan dan keenam kelompok analisis pada SKILL.md tetap berlaku.
2. Gunakan lima laga kompetitif terakhir, urut kronologis; pisahkan persahabatan. Bandingkan dengan empat laga UNL terbaru pada fase grup bila tersedia. Perbarui datanya untuk setiap pertandingan baru, bukan menggunakan rating lama.
3. Tampilkan gol, rata-rata kebobolan, hasil dan poin per laga, tembakan/tepat sasaran, clean sheet/BTTS historis, H2H relevan dan gol menit akhir. xG/xGA yang belum diperoleh tetap N/A dengan cakupan yang jelas.
4. Periksa kualitas lawan, skor ekstrem, usia data, venue netral, serta konteks kartu merah. Konteks membantu membaca data; tidak berarti pertandingan boleh dihapus tanpa aturan yang ditetapkan sebelumnya.
5. Gunakan berita primer terbaru untuk cedera, skorsing, ketersediaan, pelatih dan motivasi klasemen. XI perkiraan tetap berlabel perkiraan. Tidak mengarang rute perjalanan atau menit pemulihan klub.
6. Pisahkan arah 1X2, BTTS, total gol dan skenario skor. Keyakinan arah pemenang bukan probabilitas terkalibrasi untuk semua target. Bila bukti belum cukup, pertahankan observasi yang dijelaskan, seperti BTTS/total pada Ceko–Spanyol dalam pilot.
7. Tetap kualitatif sampai ada model timnas yang layak diuji. Koefisien 22%, 35%, 18%, probabilitas clean sheet contoh dan bobot UCL tidak aktif pada acuan ini.
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

## Usulan yang tetap terpisah

Pencatatan keyakinan/status per target yang lebih rinci, abstain 1X2 terstruktur, perbandingan snapshot XI resmi, model rating lawan dan penambahan xG merupakan calon pengembangan. Jangan mengubah bobot atau menyebutnya meningkatkan akurasi sebelum rancangan dibekukan dan diuji pada pertandingan baru. Acuan kerja ini tidak menghalangi memakai fakta terbaru; yang ditahan adalah pengaktifan metode atau koefisien baru tanpa pengujian.
