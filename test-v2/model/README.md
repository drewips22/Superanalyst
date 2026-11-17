# Superanalyst Beta V2 — eksperimen terpisah

Versi `superanalyst-beta-v2.0.0-experimental`, dibuat 17 November 2026.
Model utama `qualitative_superanalyst_national_team_pilot_v1`, skill terpasang,
forecast lama, poster, serta MC10K v1 tetap utuh. Direktori ini tidak mengganti
router atau metode operasional mana pun. Semua pemakaian versi baru bersifat eksplisit.

## Yang berubah

- Estimasi gol memakai model riset timnas yang sudah dipilih sebelumnya:
  kekuatan serang/bertahan dan lawan, kompetisi, venue netral/kandang,
  regularisasi, riwayat enam tahun, serta bobot usia hasil. Tidak memindahkan bobot UCL.
- Resep tetap: waktu paruh 730 hari untuk 1X2/BTTS; 365 hari dengan intercept
  persahabatan tersendiri untuk total gol. Kalibrator tetap berasal dari 2020–2021.
- Pilihan lemah menjadi `observe`, dengan `pick: null`. Arah tanpa ambang tetap
  tersimpan sebagai diagnosis dan tidak ikut dihitung sebagai pilihan aktif.
- Fokus memakai peluang sesudah kalibrasi. Aturan `max_p55` dipilih pada
  410 laga UEFA 2022–2023 dari lima kandidat yang dicatat seluruhnya.
  Angka 55% adalah ambang eksperimen, bukan klaim akurasi atau keuntungan.
- Sensitivitas lima laga menandai arah yang berubah ketika satu hasil
  dikeluarkan. Tidak ada skor ekstrem yang dibuang dari model karena hasil aktual.
- MC 10.000 per resep tetap ada untuk skenario mentah; pilihan tidak mengikuti
  variasi sampling. Marginal terkalibrasi lintas target bukan satu distribusi skor.
- Input hasil, prediksi terlambat, data masa depan, skor bukan 90 menit,
  duplikasi, tim/kompetisi tak dikenal, dan penimpaan berkas ditolak.
- Kelengkapan riwayat kedua tim harus diperiksa sebelum prediksi nyata.
  Audit yang hilang/stale atau hasil terbaru yang belum masuk fit menyebabkan observasi.
  Audit yang disuplai tetap merupakan pernyataan bersumber yang perlu diverifikasi,
  bukan verifikasi eksternal otomatis oleh mesin.

## Hybrid Beta

`superanalyst-hybrid-beta-v1.0.0-experimental` membaca salinan keputusan utama,
lalu hanya mempertahankan arah yang sejalan dengan angka Beta V2 dan ambangnya.
Fokus utama dipertahankan bila lolos; bila tidak, fokus dipilih dari target utama
yang masih didukung. Observasi utama tidak dapat berubah menjadi pilihan baru.
Probabilitas pendukung tetap milik beta. Jurnal, keyakinan, dan metode utama asli
tidak diubah dan tidak diberi probabilitas buatan.

## Hasil dan batas bukti

Pada analisis ulang historis 2024–2025: 438 laga UEFA dipertimbangkan, 379 fokus
diterbitkan, 271 benar (71,50%), dan 59 observasi. Baseline gol5 benar 217/379
(57,26%) pada laga yang sama; pada seluruh 438 laga baseline benar 249/438.
Subset UNL: beta 90/133 (67,67%), cakupan 133/156; baseline 74/133 (55,64%) pada
laga yang sama. Probabilitas semua 438 laga tetap dinilai, termasuk observasi.

Ini penggunaan ulang studi historis yang sudah pernah ditinjau; **bukan uji
buta baru**. Pemilihan resep awal 2018–2019, kalibrasi 2020–2021, pemilihan aturan
fokus baru 2022–2023, evaluasi aturan fokus 2024–2025. Kebijakan ditetapkan sebelum
tahap penilaian baru, tetapi pengetahuan hasil masa lalu tidak dapat dihapus.
Baseline historis memakai batas laju 0,05–12 dari studi lama; MC10K prospektif
lama mengizinkan laju nol. Jangan menyebut kedua implementasi identik pada batas itu.

Diagnosis 22 laga November: utama 18/22, beta lama 13/22, Beta V2 14/19 dengan
tiga observasi, Hybrid 14/16 dengan enam observasi. Pada 16 laga Hybrid yang sama,
utama juga 14/16. Angka ini posthoc, bukan pengganti skor forecast asli atau bukti
Hybrid lebih baik. Pada matchday terbaru Beta V2 masih salah pada Under Estonia,
Under Makedonia Utara, dan Malta menang. Tidak memilih ulang aturan setelah kegagalan ini.

## Menjalankan

Inferensi dan rekaman membutuhkan Python 3.11+ serta pustaka standar saja.
Fit membutuhkan NumPy/SciPy sesuai `requirements-research.txt` repo; tidak ada
dependensi baru. Dari akar repo:

```powershell
python -B backtests/unl-beta-v2/predict.py --help
python -B -m unittest discover -s backtests/unl-beta-v2/tests -v
python -B -m unittest discover -s tests -v
```

Arsip hasil dan paket model lokal:
`../`.
Lihat README paket untuk contoh input, pencatatan, refit, dan verifikasi mandiri.

Untuk mengulang pemilihan historis gunakan **direktori run baru**, bukan arsip lama:

```powershell
python -B backtests/unl-beta-v2/research.py select --source runs/national-team-upgrade-v1 --run <run-baru>
python -B backtests/unl-beta-v2/research.py evaluate --source runs/national-team-upgrade-v1 --run <run-baru>
```

`select` membekukan aturan dan hash kode sebelum `evaluate`. Kode dan protokol
yang dibekukan tidak boleh diedit untuk memperbaiki skor lama. Revisi prediktif
berikutnya mendapat ID eksperimen baru. Simpan seluruh kandidat, termasuk yang kalah.

## Data terbaru dan batas model

Refit 17 November menggunakan basis publik yang dipin sampai 6 Oktober 2026,
ditambah 41 hasil UNL terverifikasi 12–16 November. Jeda konservatif tiga hari
membatasi latihan sampai 14 November: 25 hasil baru dapat dipakai, 16 hasil
15–16 November belum dipakai. Update global di luar UEFA tidak diklaim lengkap.
Tanggal refit bukan bukti semua data global terbaru telah tersedia.

Lima kompetitif terakhir tetap disajikan pada laporan lengkap. Peluang model
tidak menggantikan pemeriksaan XI, pemain/pelatih, motivasi, xG, atau pasar.
Fitur tersebut belum memiliki koefisien baru yang teruji. Tidak ada perubahan
peluang manual otomatis, pemantauan jadwal, atau publikasi/pengiriman pesan otomatis.

Sumber metodologi ditinjau 17 November 2026:
[dataset dan cakupan skor](https://github.com/martj42/international_results),
[model kekuatan berbobot waktu](https://arxiv.org/abs/1705.09575),
[validasi kronologis](https://otexts.com/fpp3/toolbox.html#time-series-cross-validation),
[kalibrasi dan batas Brier](https://scikit-learn.org/stable/modules/calibration.html).
Angka kinerja berasal dari eksperimen lokal, bukan dari referensi itu.
