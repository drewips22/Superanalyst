# Pengembangan model UCL — v0.4.0 eksperimental

**Ketiga model pilihan validasi membaik terhadap baseline gol lima laga pada 378 laga uji yang sama.** Peningkatan terjadi di masing-masing musim 2024/25 dan 2025/26. Ini hasil rekonstruksi historis dengan batas sumber yang dijelaskan di bawah, bukan janji akurasi pertandingan mendatang.

## Rancangan yang dikunci

- Corpus: 25.496 pertandingan historis dari jadwal ESPN; 25.472 memiliki skor 90 menit yang dapat digunakan, 24 tidak terverifikasi dan tidak masuk latihan/fitur. Tidak ada laga target UCL yang kehilangan label 90 menit.
- Seluruh 878 laga fase utama/knockout UCL enam musim tercakup. Musim 2020/21–2022/23 membentuk riwayat awal; 2023/24 (125 laga) untuk pemilihan varian; 2024/25 dan 2025/26 (189 + 189 laga) untuk pengujian.
- Semua 378 laga uji mempunyai ≥5 hasil historis tercakup per tim. Tidak ada penghapusan kekalahan, kartu merah, skor ekstrem, atau label unlucky dari cohort uji.
- Cutoff tiap laga T-24 jam. Model dipasang ulang per bulan, hanya memakai data sebelum cutoff paling awal bulan itu; jendela latihan empat tahun, waktu paruh bobot recency 365 hari. Hasil laga sebelumnya boleh memasuki fit berikutnya sesuai jadwal yang sudah ditetapkan.
- Dua belas varian dipilih hanya dari validasi. Pemilihan per target dikunci sebelum prediksi uji; seluruh prediksi uji disimpan sebelum tahap penilaian. [Spesifikasi](experiment.json), [input/checksum](input-manifest.json), [pilihan validasi](selection.json), [pembekuan uji](test-freeze.json).

## Hasil utama

Nilai kesalahan lebih kecil berarti lebih baik. Penurunan kesalahan relatif bukan kenaikan akurasi dalam poin persentase.

| Target | Metrik utama | Baseline 5 laga | Model pilihan | Kesalahan turun | Pilihan tepat: lama → baru |
| --- | --- | ---: | ---: | ---: | ---: |
| Pemenang/seri | log_loss_1x2 | 1.0033 | 0.9211 | 8.2% | 200/378 (52.9%) → 218/378 (57.7%) |
| BTTS | brier_btts | 0.2541 | 0.2451 | 3.6% | 204/378 (54.0%) → 211/378 (55.8%) |
| Over 2,5 | brier_over_2_5 | 0.2348 | 0.2226 | 5.2% | 235/378 (62.2%) → 251/378 (66.4%) |

Model pemenang memperkirakan kekuatan serangan/pertahanan, kandang, form 10 laga, istirahat/kepadatan jadwal, serta proxy performa poin fase UCL. Model BTTS yang terpilih adalah rata-rata gol 20 laga; model total gol adalah kekuatan tim tanpa tambahan kandang. Ini **tiga model target terpisah**; tidak diklaim sebagai satu distribusi gol gabungan yang sama.

Ketiga target lolos aturan peningkatan yang ditetapkan: metrik utama gabungan membaik, metrik pendamping tidak memburuk, dan metrik utama membaik dalam kedua musim uji. [Evaluasi lengkap](evaluation.json).

| Musim uji | Target | Baseline | Model pilihan |
| --- | --- | ---: | ---: |
| 2024/25 | Pemenang/seri | 0.9952 | 0.8972 |
| 2024/25 | BTTS | 0.2676 | 0.2552 |
| 2024/25 | Over 2,5 | 0.2463 | 0.2305 |
| 2025/26 | Pemenang/seri | 1.0113 | 0.9450 |
| 2025/26 | BTTS | 0.2407 | 0.2349 |
| 2025/26 | Over 2,5 | 0.2234 | 0.2147 |

Sampel uji memuat 190 kemenangan kandang, 61 seri dan 127 kemenangan tandang; BTTS ya 206/tidak 172; Over 2,5 ya 247/tidak 131. Berbeda dari sembilan laga sebelumnya, terdapat kedua kelas hasil untuk target biner.

## Ketidakpastian

Perbandingan berpasangan dengan pengambilan ulang 18 blok bulan, 2.000 pengulangan, seed 1729:

| Target | Selisih kesalahan baru − lama | Rentang persentil 95% |
| --- | ---: | --- |
| Pemenang/seri | -0.0822 | -0.1276 sampai -0.0442 |
| BTTS | -0.0090 | -0.0159 sampai -0.0024 |
| Over 2,5 | -0.0123 | -0.0219 sampai -0.0022 |

Seluruh rentang berada di sisi negatif pada sampel ini. Pengambilan ulang blok waktu tidak menghapus ketidakpastian akibat revisi sumber, pemilihan model, ketergantungan antarpertandingan atau perpindahan format kompetisi. Status tetap **eksperimental/provisional** dan belum terkalibrasi untuk pemakaian langsung. Tidak ada laju gol yang terkena batas numerik pada prediksi uji.

## Apa yang diuji satu per satu

Angka berikut berasal dari **validasi**, bukan pemilihan ulang berdasarkan hasil uji.

| Varian | Log loss 1X2 | Brier BTTS | Brier Over 2,5 |
| --- | ---: | ---: | ---: |
| `goals_last5_baseline` | 1.0734 | 0.2606 | 0.2746 |
| `goals_last10` | 1.0281 | 0.2527 | 0.2643 |
| `goals_last20` | 1.0443 | 0.2445 | 0.2545 |
| `team_strength` | 0.9753 | 0.2450 | 0.2417 |
| `team_strength_home` | 0.9689 | 0.2445 | 0.2429 |
| `team_strength_home_form5` | 0.9660 | 0.2469 | 0.2469 |
| `team_strength_home_form10` | 0.9647 | 0.2471 | 0.2467 |
| `team_strength_home_form20` | 0.9709 | 0.2460 | 0.2456 |
| `team_strength_home_form10_rest` | 0.9609 | 0.2477 | 0.2450 |
| `team_strength_home_form10_rest_h2h` | 0.9626 | 0.2475 | 0.2446 |
| `team_strength_home_form10_rest_travel` | 0.9625 | 0.2474 | 0.2455 |
| `team_strength_home_form10_rest_motivation` | 0.9461 | 0.2519 | 0.2435 |

- Penyesuaian kekuatan tim/lawan menurunkan kesalahan terhadap rata-rata lima laga pada validasi; model gabungan pilihan kemudian juga lolos pengujian dua musim.
- Form 5, 10 dan 20 laga dibandingkan. Form 10 masuk model pemenang terpilih; jendela 20 terpilih untuk BTTS. Tidak ada satu jendela yang dinyatakan terbaik untuk semua target.
- Tambahan H2H dan jarak antarkota tidak memperbaiki log loss validasi dibanding varian form10 + istirahat. Keduanya tidak diaktifkan pada resep terpilih; ini tidak membuktikan tidak ada manfaat dalam semua konteks.
- Nama internal `motivation` berarti **proxy poin per laga dan jumlah laga fase UCL yang sudah berlangsung**, bukan ukuran motivasi psikologis, pressing, tekel, perburuan top-4 atau bonus +18%. Efek psikologisnya belum diuji.
- Varian yang tampak terbaik setelah melihat hasil uji tidak menggantikan pilihan validasi. Misalnya model gabungan mencatat BTTS uji lebih baik daripada jendela 20, tetapi model BTTS pilihan tetap jendela 20.

## Yang belum boleh diklaim

[Studi xG tambahan](../xg-domestic-2015-v1/review.md) memakai dua liga pria 2015/16 dan tidak otomatis berlaku untuk UCL modern. Absensi berbobot peran/pengganti belum mempunyai arsip pengumuman yang cukup dengan cap waktu sebelum cutoff. Line-up aktual pertandingan tidak dimasukkan ke prediksi T-24 jam.

Pasar belum menjadi pembanding yang dinilai: arsip quote yang dapat diverifikasi pada cutoff sama, ditambah spread/depth dan tiga sumber independen, belum tersedia dalam pekerjaan ini. Akses arsip publik Polymarket dicoba tetapi tidak berhasil; itu bukan bukti bahwa pasarnya tidak ada. Jangan menyebut model mengalahkan pasar. [Dokumentasi riwayat harga Polymarket](https://docs.polymarket.com/api-reference/markets/get-prices-history).

Validator [konteks pemain/pasar](../../skills/superanalyst/scripts/research/context.py) sudah menolak pengumuman/quote sesudah cutoff, membedakan sumber independen dan mempertahankan nilai hilang. Tes validator tidak mengukur manfaat prediktif absensi atau pasar. Status lengkap: [cakupan pengujian](coverage-status.json).

## Catatan Liverpool dan keberuntungan

Pendapat pengguna bahwa Fenerbahce beruntung disimpan sebagai **hipotesis diagnosis sesudah laga**. Model pralaga memang mengunggulkan Liverpool 55,8%; probabilitas kemenangan Fenerbahce 23,3%. Statistik tersedia menunjukkan Liverpool unggul tembakan 22–17 dan penguasaan bola 67,6%–32,4%, tetapi tembakan tepat sasaran 6–6 dan xG sebanding belum tersedia.

Karena itu penyebab keberuntungan belum dapat dipastikan. Kekalahan pilihan Liverpool tetap dihitung; studi sembilan laga sebelumnya tetap 6/9 untuk 1X2. [Diagnosis bersumber](fenerbahce-liverpool-diagnostic.json). Pertandingan November 2026 ini juga berada di luar cohort model utama yang berakhir Mei 2026.

## Dasar model dan batas data

Laju gol memakai regresi Poisson dengan parameter serangan tim, kelemahan pertahanan lawan, intercept kompetisi dan—sesuai varian—efek kandang global/per kompetisi serta kovariat kausal. Parameter tim diberi regularisasi; model tidak memakai nilai akhir klasemen sebagai fitur. Landasan keluarga model: [Dixon–Coles](https://doi.org/10.1111/1467-9876.00065). Implementasi ini bukan reproduksi penuh koreksi skor rendah Dixon–Coles.

Bobot/penalti tercatat dalam spesifikasi. Koefisien dibatasi −3 sampai 3 untuk kestabilan optimasi; prediksi laju dibatasi 0,02–12, tanpa pemotongan yang aktif pada uji ini. Form memakai lima pseudo-observasi prior; prior rerata gol kompetisi ditarik ke rerata data terdahulu dengan bobot 100. Semua itu dikunci sebelum validasi, bukan dipilih dari hasil uji.

Sumber utama adalah ekspor jadwal historis ESPN yang diambil sekarang. Ketersediaan hasil menggunakan **proxy kickoff +4 jam**, bukan waktu publikasi arsip yang terbukti. Data kompetisi/piala dapat tidak lengkap meskipun jadwal disebut seluruh kompetisi; interval istirahat dan form berarti berdasarkan laga yang tercakup. Skor extra time/penalti dipisahkan memakai skor dua babak normal. `point_in_time_verified=false`.

Jarak perjalanan memakai koordinat kota venue [GeoNames](https://www.geonames.org/export/) dan kota kandang terakhir yang sudah teramati, bukan rute perjalanan aktual atau lokasi hotel. Koordinat berasal dari ekspor geografis saat penelitian. Model diuji pada format grup lama saat validasi dan format liga 36 tim pada musim uji; [penjelasan format UEFA](https://www.uefa.com/uefachampionsleague/news/0268-12157d69ce2d-9f011c70f6fa-1000--new-format-for-champions-league-post-2024-everything-you-ne/).

## Mengulang dan memakai resep

Pasang dependensi opsional penelitian, lalu ulangi probabilitas dan skor dari snapshot yang masuk repo:

```sh
python -m pip install -r requirements-research.txt
python backtests/ucl-model-upgrade-v1/replay.py
```

Replay tidak memerlukan seluruh corpus lokal. [Masukan prediksi](forecast-inputs.json) diekspor setelah penilaian dari corpus fitur yang checksum-nya sudah dikunci sebelumnya; berisi 503 fixture validasi/uji. Fit ulang lengkap memerlukan ekspor lokal asli beserta checksum di manifest. Ekspor sumber baru dapat berubah; jangan menimpa eksperimen ini untuk menyamakan hasil.

Untuk laga mendatang, gunakan data terbaru dan pasang ulang resep sesuai cutoff/horizon yang tepat. JSON model bulanan 2024–2026 di folder ini adalah bukti replay, bukan rating terkini. [Kebijakan target terpilih](../../skills/superanalyst/assets/validated-policy.json). Analisis tetap bahan pertimbangan, bukan hasil mutlak.
