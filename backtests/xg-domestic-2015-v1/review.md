# Studi tambahan xG — dua liga pria 2015/16

<img src="../../assets/attribution/statsbomb.png" alt="StatsBomb data attribution" width="180">

Sumber: **StatsBomb Open Data**. [Repo dan ketentuan atribusi](https://github.com/hudl/open-data). Hasil penelitian ini menggunakan data StatsBomb, tanpa menyatakan dukungan atau afiliasi dari penyedia.

## Cakupan

760 pertandingan lengkap Premier League dan Serie A 2015/16, dengan agregasi xG pre-shot StatsBomb hanya periode 1 dan 2. Gol event cocok dengan seluruh 760 skor. Riwayat hanya mencakup pertandingan liga; laga piala dan Eropa tidak masuk jendela ini.

Agustus–Desember membentuk riwayat awal; Januari–Februari 2016 memilih jendela dan campuran (179 laga validasi); Maret–Mei menilai hasil (222 laga uji). Timestamp asli xG dan versi model penyedia ketika itu tidak dibuktikan: `point_in_time_verified=false`. Ini bukti tambahan dari liga domestik lama, **bukan uji xG di UCL modern**.

Sepuluh pilihan dibandingkan: jendela 5/10 laga dan bobot xG 0%, 25%, 50%, 75%, 100%. Pilihan dikunci sebelum penilaian uji. Hanya xG dari pertandingan terdahulu yang masuk fitur; xG laga target tidak digunakan.

## Hasil pilihan validasi

| Target | Pilihan | Baseline gol 5 laga | Model pilihan | Lolos batas studi tambahan? |
| --- | --- | ---: | ---: | --- |
| Pemenang/seri | `goals10-alpha0.5` | 1.0505 | 1.0212 | Ya, hanya cakupan tambahan ini |
| BTTS | `goals5-alpha1` | 0.2459 | 0.2465 | Tidak |
| Over 2,5 | `goals5-alpha1` | 0.2503 | 0.2562 | Tidak |

Campuran gol+xG 50:50 dengan jendela 10 laga menurunkan log loss pemenang sekitar 2,8% dibanding baseline gol 5 laga dan membaik pada kedua liga. Pilihan xG murni untuk BTTS dan total gol tidak membaik pada uji, sehingga tidak dipromosikan.

## Memisahkan pengaruh xG dari jendela

Pilihan pemenang mengubah dua hal sekaligus: jendela dan bobot xG. Pemeriksaan kontrol jendela 10 laga yang ditambahkan **sesudah penilaian** menghasilkan log loss gol-saja 1.0279, versus campuran 1.0212. Selisih sekitar 0,65% ini lebih kecil daripada perbandingan ke baseline 5 laga.

[Kontrol tambahan](posthoc-window-control.json) tidak dipakai memilih ulang model atau menaikkan status. Karena dibuat setelah hasil terbuka, ulangi pembandingan dengan jendela sama pada periode baru sebelum menyimpulkan besarnya manfaat xG. Jangan menyebut seluruh keuntungan 2,8% sebagai pengaruh xG saja.

## Batas dan replay

Data diambil dari ekspor terbuka sekarang; tanggal hanya presisi hari. Hasil historis dianggap tersedia mulai tengah malam UTC berikutnya, dan cutoff fitur tengah malam UTC pada hari sebelum tanggal target. Ini proxy konservatif, bukan klaim arsip T-24 jam yang presisi. Model xG penyedia bisa berbeda dari versi yang tersedia pada 2015/16.

[Spesifikasi](experiment.json), [pilihan validasi](selection.json), [hasil lengkap per liga](evaluation.json). Tidak ada klaim keunggulan pasar atau kalibrasi untuk laga masa depan. Kasus ini tidak mengaktifkan xG secara otomatis dalam resep UCL.

```sh
python backtests/xg-domestic-2015-v1/replay.py
```

Replay menggunakan ringkasan fitur dan label yang tersimpan; fit/pengambilan ulang event memerlukan corpus lokal StatsBomb. Analisis merupakan bahan penelitian, bukan hasil mutlak.
