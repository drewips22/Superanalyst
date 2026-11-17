# Test V2 — Superanalyst

Eksperimen **Beta V2** dan **Hybrid Beta**, terpisah dari model utama.
Model utama `qualitative_superanalyst_national_team_pilot_v1` tetap menjadi acuan;
unggahan ini hanya menambahkan folder `test-v2/` dan tidak mengganti skill operasional.

- [Laporan pengembangan dan batas hasil](Laporan-Pengembangan-Beta-V2.md)
- [Unduh paket lengkap](Superanalyst-Beta-V2.zip)
- [Kode dan protokol eksperimen](model/README.md)
- [Paket parameter](model-package.json), [aturan fokus](focus-selection.json)
- [Hasil historis](artifacts/historical-evaluation.json)
- [Diagnosis November — posthoc](artifacts/november-posthoc-evaluation.json)
- [Manifest publikasi](publication-manifest.json)

## Temuan

Pada 379 laga aktif yang sama dari periode historis 2024–2025, Beta V2 benar
271/379 (71,50%); baseline gol5 217/379 (57,26%). Beta V2 menerbitkan fokus pada
379 dari 438 laga dan mengobservasi 59. Ini analisis ulang historis yang sudah
pernah ditinjau, bukan uji buta baru atau akurasi forecast langsung.

Pada diagnosis ulang 22 laga November, utama asli 18/22, beta lama 13/22,
Beta V2 posthoc 14/19 dengan tiga observasi, Hybrid posthoc 14/16 dengan enam
observasi. Pada 16 laga yang sama, utama juga 14/16; angka Hybrid tidak
membuktikan manfaat tambahan. Rumania ekstra tetap dinilai terpisah.

## Menjalankan

Unduh ZIP lalu ekstrak, atau jalankan dari folder `test-v2` setelah clone:

```sh
python -B verify.py
python -B model/predict.py --help
python -B -m unittest discover -s model/tests -v
```

Inferensi dan audit memakai pustaka standar Python 3.11+. Fit memerlukan
NumPy/SciPy; tanpa keduanya dua tes fitting berstatus skip. Contoh pada
`examples/` memakai tim fiktif A/B dan bukan jadwal nyata; tanggalnya bisa kedaluwarsa.

Rekam forecast nyata baru hanya dengan data yang diperbarui dan diperiksa,
sebelum kickoff, menggunakan berkas keluaran baru:

```sh
python -B model/predict.py --package model-package.json --selection focus-selection.json --inputs input-baru.json --output snapshot-baru.json
```

Untuk mengulang fit cutoff eksperimen dengan dependensi riset terpasang:

```sh
python -B model/train.py --base-data data/base-matches.jsonl --base-package data/base-package.json --base-protocol data/base-protocol.json --updates data/verified-updates.jsonl --as-of-date 2026-11-17 --output paket-refit-baru.json
```

Paket refit 17 November memakai jeda konservatif tiga hari, sehingga latihan
hanya sampai 14 November. Update mencakup 41 hasil UNL 12–16 November; pembaruan
global di luar UEFA tidak diklaim lengkap. Untuk prediksi mendatang perbarui
data, audit kelengkapan riwayat, cutoff, dan parameter lewat fit baru.

## Salinan publik

Snapshot lokal asli dipertahankan. Salinan ini hanya menyederhanakan referensi
alamat komputer dan menyesuaikan petunjuk publikasi; peluang, skor, fokus,
koefisien dan timestamp eksperimen dipertahankan. Rincian perubahan dan checksum
ada di [catatan salinan](publication-copy.json). Daftar lengkap alamat arsip
komputer tidak diterbitkan; verifikasi 407 berkas asli dilakukan pada paket lokal.
`verify.py` publik memeriksa isi paket dan replay, tanpa memerlukan berkas pribadi.

Data dasar berasal dari [international_results](https://github.com/martj42/international_results)
berlisensi CC0; sumber hasil tambahan tersimpan per baris. Unggahan ini tidak
menjadikan rekonstruksi historis sebagai forecast yang dicatat sebelum laga.
