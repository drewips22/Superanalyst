# Hasil uji pertama Superanalyst: PSG–Inter

**Pilihan pemenang tepat, BTTS keliru.** Baseline berbasis lima laga condong ke PSG dan BTTS ya; hasil aktual final adalah **PSG 5–0 Inter**. Ini satu rekonstruksi historis dengan batas informasi **30 Mei 2025 pukul 19.00 WIB**, bukan prediksi yang sungguh direkam pada 2025. [Hasil resmi UEFA](https://www.uefa.com/uefachampionsleague/news/0290-1bbe6365b47a-0668db2bbcb1-1000--2024-25-champions-league-all-the-results/)

Laga berlangsung pada 31 Mei 2025 waktu Munich, atau 1 Juni 2025 pukul 02.00 WIB. Penilaian memakai hasil 90 menit + injury time.

## Prediksi yang disimpan dan hasil akhir

| Target | Keluaran sebelum penilaian | Hasil aktual | Penilaian |
| --- | --- | --- | --- |
| Pemenang 1X2 | PSG, 44,92%; seri 22,77%; Inter 32,32% | PSG menang | Pilihan teratas tepat |
| BTTS | Ya, 64,85% | Tidak | Pilihan keliru |
| Skor tunggal paling mungkin | 1–1, peluang 9,96% | 5–0 | Tidak terjadi |
| Clean sheet PSG | 22,31% | Ya | Kejadian yang diberi peluang terjadi |
| Clean sheet Inter | 16,53% | Tidak | Tidak terjadi |

Clean sheet dilaporkan sebagai probabilitas, bukan dua pilihan tambahan yang dipilih setelah melihat hasil. Tidak ada klaim "akurasi 100%" dari satu pemenang yang tepat. Skor modal hanyalah satu kombinasi; probabilitasnya kecil dan tidak berarti model mengharapkan 1–1 dengan pasti.

## Apa yang sebenarnya diuji

Model eksperimen `last5-goals-mean-poisson-experimental-v1` menerima **hanya gol waktu normal dari lima laga terakhir setiap tim** sebagai parameter kuantitatif:

```text
PSG: 13 gol dicetak, 5 kebobolan dalam 5 laga
Inter: 10 gol dicetak, 5 kebobolan dalam 5 laga

lambda_PSG   = (2,6 + 1,0) / 2 = 1,8
lambda_Inter = (2,0 + 1,0) / 2 = 1,5
```

Gol kedua tim diasumsikan Poisson independen. Tidak ada angka bonus/penalti cedera, motivasi, kandang, H2H, xG, atau pasar. xG dan berita diperiksa sebagai konteks kualitatif pada [laporan analisis](analysis-before-result.md), tetapi belum dilatih menjadi fitur model. Karena itu, uji ini belum menilai manfaat seluruh kriteria Superanalyst.

Pembersihan data yang berpengaruh: Inter–Barcelona **3–3 pada 90 menit**, meskipun skor akhirnya 4–3 setelah extra time. Gol menit 99 serta statistik 120 menit tidak masuk sebagai fitur 90 menit. [Laporan klub sebelum final](https://www.inter.it/en/news/inter-barcelona-champions-league-24-25)

## Penilaian probabilitas

| Metrik pada satu laga | Baseline lima laga | Pembanding konstan netral |
| --- | --- | --- |
| Brier 1X2, jumlah tiga squared errors | **0,4597** | 0,6667, dengan peluang masing-masing 1/3 |
| Log loss 1X2 | **0,8004** | 1,0986 |
| Brier BTTS | **0,4205** | 0,2500, dengan peluang 50% |
| Log loss BTTS | **1,0454** | 0,6931 |

Semakin rendah semakin baik. Pada laga ini, baseline lebih baik dari pembanding konstan untuk 1X2 dan lebih buruk untuk BTTS. Pembanding tersebut bukan probabilitas pasar atau model kekuatan tim. Sampel **n=1** tidak cukup untuk menilai kalibrasi, signifikansi, atau keunggulan strategi.

Model memberi probabilitas sekitar **0,58%** untuk kombinasi skor 5–0. Kejadian dengan probabilitas kecil tetap bisa terjadi. Satu hasil tidak membuktikan model salah secara statistik, tetapi jelas tidak cukup untuk menganggap estimasi skornya andal.

## Pelajaran yang boleh diambil

1. **Pemenang dan BTTS adalah target berbeda.** Menebak tim yang menang tidak membuat analisis jumlah gol atau kedua tim mencetak gol otomatis benar.
2. **Bukti berlawanan perlu tetap terlihat.** Inter memiliki clean sheet 3/5 laga, sedangkan PSG mencatat BTTS 4/5. Baseline gol sederhana memberi BTTS 64,85%, tetapi narasi sebelum penilaian sudah memberi status provisional karena sinyal bertentangan.
3. **Kualitas lawan belum disesuaikan.** Menggabungkan laga domestik dan Eropa tanpa kekuatan lawan, rotasi, dan kartu merah dapat menghasilkan laju gol yang kurang sesuai untuk final netral.
4. **xG belum diuji sebagai fitur.** Seri xG PSG berasal dari dua penerbit dan sebagian statistik Inter mencakup extra time. Penambahan fitur memerlukan data dengan definisi dan cakupan yang konsisten.
5. **Pasar T-30 tidak diuji di sini.** Jendela itu berada setelah cutoff T-31 jam; tiga quote arsip yang sebanding juga belum terkumpul. Tidak ada kesimpulan anomali Polymarket.

Angka awal 22%, 35%, dan 18% tetap hipotesis. Hasil ini tidak mengaktifkan, mengganti, atau mengoptimalkan koefisien tersebut.

## Keterulangan dan batas integritas

Urutan yang tersimpan:

1. [Spesifikasi eksperimen](experiment.json), [data masukan](features.json), dan [analisis](analysis-before-result.md).
2. [Prediksi tanpa label hasil](prediction.json) dibuat pada **12 November 2026 00:13:13 UTC**, lalu dimasukkan ke commit `6498002` sebelum label ditambahkan.
3. [Manifest checksum](frozen-inputs.json) merekam prediksi, masukan, dan kode perhitungannya.
4. [Hasil aktual](outcome.json) dibaca hanya oleh tahap penilaian; [evaluasi lengkap](evaluation.json) dan [log rekonstruksi](scored-reconstruction.jsonl) disimpan terpisah.

Penguncian ini membuktikan urutan penyimpanan **pada rekonstruksi 2026**, bukan bahwa analis tidak pernah mengetahui hasil final. Laga dipilih sebagai contoh yang terdokumentasi, bukan sampel acak; hasilnya sudah publik dan bisa diketahui analis. Versi sumber historis tidak seluruhnya diarsipkan. Bias pemilihan kasus dan hindsight tetap menjadi batas uji ini.

Untuk memeriksa ulang hasil tanpa menimpa snapshot, jalankan dari akar repo:

```sh
python backtests/ucl-2025-final/run.py verify
python skills/superanalyst/scripts/evaluate.py backtests/ucl-2025-final/scored-reconstruction.jsonl
```

Perintah `predict` dan `grade` sengaja menolak menimpa file yang sudah ada. Untuk eksperimen baru, gunakan direktori baru dengan spesifikasi sendiri.

## Pengujian berikutnya

Bekukan daftar laga lebih dulu, misalnya seluruh perempat final sampai final UCL 2024/25, tanpa memilih berdasarkan hasil. Gunakan horizon yang sama pada setiap laga, lalu bandingkan baseline kekuatan tim, gol lima laga, xG, dan pasar pada cutoff yang setara. Variasi fitur dipilih dari periode latihan/validasi sebelum periode uji. Pengujian lebih luas itu belum dijalankan pada rilis ini.
