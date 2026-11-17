# Hasil pengembangan Superanalyst Beta V2

Selesai 17 November 2026. **Model utama tidak diubah.** Beta baru dan Hybrid dibuat sebagai eksperimen terpisah, lengkap dengan mesin, paket parameter, audit, contoh, dan hasil pengujian.

## Perbaikan yang diimplementasikan

1. **Pembentukan peluang:** model kekuatan tim/lawan, kandang/netral, kompetisi, regularisasi dan bobot usia data menggantikan rerata lima skor sebagai satu-satunya sumber peluang beta. Lima laga tetap tersimpan untuk ringkasan dan sensitivitas.
2. **Kalibrasi per target:** memakai kalibrator riset timnas 2020–2021 yang sudah dibekukan. Tidak membuat penalti cedera, motivasi, pelatih, atau bobot UCL baru.
3. **Fokus dan observasi:** aturan `max_p55` dipilih pada 410 laga 2022–2023 dari lima kandidat, dengan syarat cakupan minimal 70%. Fokus memakai peluang sesudah kalibrasi; target di bawah 55% tidak diterbitkan sebagai pilihan aktif.
4. **Sensitivitas:** arah lima laga yang mudah berubah ditandai. Skor ekstrem tetap dipertahankan; pengeluaran satu laga hanya uji diagnosis, bukan perbaikan hasil surut.
5. **Kualitas data dan arsip:** validasi cutoff, hasil 90 menit, kelengkapan riwayat, fit yang stale, tim/kompetisi tak dikenal, null/observasi, fokus, serta rekaman tanpa penimpaan. Hasil aktual dipisahkan dari masukan prediksi.
6. **Hybrid Beta:** salinan keputusan utama disaring lewat dukungan numerik. Target observasi utama tetap observasi dan probabilitas tidak pernah diklaim sebagai probabilitas model utama.

MC 10.000 dipertahankan sebagai skenario mentah per resep. Ia tidak menentukan pilihan. Marginal setelah kalibrasi memakai resep berbeda dan **tidak membentuk satu distribusi skor gabungan**.

## Evaluasi historis 2024–2025

Pemilihan resep awal 2018–2019, kalibrasi 2020–2021, pemilihan fokus baru 2022–2023, lalu penilaian fokus pada 2024–2025. Ini analisis ulang studi yang sudah pernah ditinjau, **bukan uji buta baru atau akurasi forecast langsung**. Semua 438 distribusi tetap dinilai, termasuk yang fokusnya observasi.

| Strategi fokus | Benar / pilihan | Cakupan dari 438 laga |
|---|---:|---:|
| Baseline gol5 historis | 249/438 (56,85%) | 438/438 (100,00%) |
| Model kekuatan, belum kalibrasi | 293/438 (66,89%) | 438/438 (100,00%) |
| Model + kalibrasi, tanpa observasi fokus | 300/438 (68,49%) | 438/438 (100,00%) |
| Beta V2 terpilih | 271/379 (71,50%) | 379/438 (86,53%) |

Pada **379 laga aktif yang sama**, baseline 217/379 (57,26%); Beta V2 271/379 (71,50%). Jadi selisih ini juga terlihat ketika denominator disamakan. Interval bootstrap per bulan untuk selisih akurasi: +9,94 hingga +19,50 poin persentase, hanya 11 bulan aktif; bukan jaminan peluang laga berikutnya.

Subset UNL: Beta V2 90/133 (67,67%), cakupan 133/156; baseline pada 133 laga yang sama 74/133 (55,64%). Subset ini hanya mencakup tiga bulan aktif sehingga intervalnya perlu dibaca hati-hati.

| Metrik seluruh 438 laga; lebih kecil lebih baik | Gol5 | Beta V2 |
|---|---:|---:|
| Log loss 1X2 | 0.9486 | 0.8282 |
| Brier BTTS | 0.2618 | 0.2458 |
| Brier Over 2,5 | 0.2648 | 0.2425 |

Brier 1X2 memakai jumlah tiga kelas tanpa dibagi tiga; log loss dibatasi secara numerik pada 1e-15. Kalibrasi tidak selalu menambah manfaat: Brier total model mentah 0,2399 menjadi 0,2425 setelah kalibrasi. Versi terkalibrasi tetap dipertahankan sesuai protokol, tanpa memilih ulang setelah melihat hasil. Baseline historis memakai batas laju 0,05–12; beta prospektif lama mengizinkan nol. Perbandingan historis ini bukan penyandingan langsung angka akurasi 22 laga November.

## Diagnosis ulang arsip November

**Seluruh hasil November sudah diketahui sebelum eksperimen dibuat.** Dua baris lama adalah forecast asli; dua baris baru adalah rekonstruksi posthoc. Skor lama tidak diganti.

| Model | Mode | Benar / pilihan | Observasi dari 22 |
|---|---|---:|---:|
| Utama | Forecast asli | 18/22 (81,82%) | 0 |
| Beta MC10K lama | Forecast asli | 13/22 (59,09%) | 0 |
| Beta V2 | Posthoc | 14/19 (73,68%) | 3 |
| Hybrid Beta | Posthoc | 14/16 (87,50%) | 6 |

**Pada 16 laga Hybrid yang sama, utama juga 14/16.** Angka Hybrid 87,5% tidak membuktikan tambahan manfaat terhadap utama; ia terutama mengurangi pilihan. Pada 19 laga aktif Beta V2, utama 16/19, beta lama 11/19, Beta V2 14/19. Rumania tambahan tetap di luar kelompok utama 22 laga dan dinilai terpisah dalam JSON.

| Laga terbaru dan skor | Utama asli | Beta V2 posthoc | Hybrid posthoc |
|---|---|---|---|
| Estonia–Bulgaria 2–1 | Under 2,5 | Under 2,5 | Under 2,5 |
| Islandia–Luksemburg 3–0 | Islandia menang | Islandia menang | Islandia menang |
| Lituania–Liechtenstein 2–1 | Lituania menang | Lituania menang | Lituania menang |
| Jerman–Belanda 5–0 | BTTS Ya | Observasi | Observasi |
| Yunani–Serbia 1–0 | Yunani menang | BTTS Tidak | Observasi |
| Makedonia Utara–Slovenia 0–3 | Slovenia menang | Under 2,5 | BTTS Tidak |
| Swiss–Skotlandia 4–0 | Swiss menang | Swiss menang | Swiss menang |
| Gibraltar–Malta 1–1 | Under 2,5 | Malta menang | Under 2,5 |

Beta V2 masih gagal pada Under Estonia, Under Makedonia Utara, dan Malta menang. Ia tidak diubah lagi agar cocok dengan delapan hasil tersebut. Main tidak mengalami perubahan pilihan, keyakinan, fokus, koefisien, atau poster.

## Kesiapan dan pemeriksaan

Paket refit 17 November tersedia: 3,075 laga kompetitif untuk model 730 hari; 4,623 laga termasuk persahabatan terpisah untuk model total. Basis sumber dipin sampai 6 Oktober, ditambah 41 hasil UNL 12–16 November. Jeda tiga hari membuat hanya 25 update sampai 14 November yang masuk latihan; 16 hasil 15–16 November tetap tersimpan untuk fit berikutnya. Update global di luar UEFA tidak diklaim lengkap.

- 18 pengujian eksperimen lulus, termasuk optimizer nyata, pengubahan label masa depan yang tidak mengubah fit terdahulu, observasi, konsistensi main dan batas waktu.
- 95 pengujian sistem lama lulus. Replay studi lama memeriksa 47.660 baris fitur tim dan 12.204 pasangan model/laga.
- Verifikasi paket mengulang 848 baris historis, 438 hasil evaluasi, pemilihan pada 410 laga, 23 rekonstruksi, serta hash seluruh arsip utama yang dilindungi.
- Contoh CLI bersifat sintetis dan tidak dimasukkan ke akurasi nyata. Tidak ada forecast nyata baru atau pemantauan otomatis yang dibuat dalam pekerjaan ini.

Model utama tetap acuan. Beta V2 layak diuji berdampingan pada prediksi baru yang benar-benar dicatat sebelum kickoff. Hybrid tetap kandidat sekunder; belum ada bukti tambahan manfaat pada sampel November. Snapshot baru harus menyebut versi, cutoff, aturan fokus dan denominator sendiri.

## Sumber dan berkas

Angka berasal dari arsip lokal yang dibekukan. Landasan rancangan: [dataset](https://github.com/martj42/international_results), [kekuatan tim berbobot waktu](https://arxiv.org/abs/1705.09575), [pengujian kronologis](https://otexts.com/fpp3/toolbox.html#time-series-cross-validation), dan [kalibrasi](https://scikit-learn.org/stable/modules/calibration.html). Sumber dipin dan ketersediaan historis presisi tidak sepenuhnya terverifikasi; hash dan replay tidak mengubahnya menjadi uji buta.

Kode pada `model/`; paket terkini `model-package.json`; aturan fokus `focus-selection.json`; seluruh skor pada `artifacts/`; sumber dan fit pembanding pada `data/`; pemeriksaan mandiri `verify.py`. Arsip awal disimpan lokal. Salinan publik ini diunggah ke folder test-v2; keputusan prediktif dan hasilnya tetap sama.
