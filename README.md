# Superanalyst

**Data → pola → keputusan** untuk analisis pertandingan sepak bola mendatang.

Superanalyst adalah repo skill untuk Codex. Isinya mengubah rancangan analisis menjadi prosedur yang bisa diulang, diperiksa sumbernya, dan dievaluasi setelah pertandingan. Bahasa utama: Indonesia.

**Status: v0.2.0 — kerangka penelitian dengan satu studi rekonstruksi historis.** Repo GitHub **private** tersedia di [drewips22/Superanalyst](https://github.com/drewips22/Superanalyst). Contoh dalam `examples/` tetap sintetis; kasus nyata pertama berada di `backtests/`. Akurasi strategi dan kalibrasi model pada banyak laga belum diukur.

## Uji pertandingan pertama

[PSG–Inter, final UCL 2025: analisis dan evaluasi](backtests/ucl-2025-final/review.md), dengan cutoff **30 Mei 2025 19.00 WIB**, 31 jam sebelum kickoff. Baseline gol lima laga menghasilkan PSG 44,92%, seri 22,77%, Inter 32,32%, dan BTTS 64,85%. Hasil aktual PSG 5–0 Inter: pilihan pemenang tepat, BTTS keliru.

Analisis dibuat pada November 2026 sebagai **rekonstruksi**, bukan forecast yang direkam pada 2025. Data asli pada saat itu tidak seluruhnya diarsipkan, sehingga kasus ini bukan uji buta. Spesifikasi, sepuluh laga historis, analisis, probabilitas, checksum, label hasil, dan cara mengulang evaluasi tersedia di folder kasus. Satu laga belum menguji keseluruhan kriteria Superanalyst.

## Cakupan

| Bagian | Yang diperiksa |
| --- | --- |
| Performa terbaru | Lima laga terakhir: gol, kebobolan, xG/xGA, W-D-L, tembakan, dan tren |
| Pola gol dan H2H | Skor, BTTS, penguasaan bola, konteks pertemuan, perubahan tim |
| Line-up dan motivasi | Cedera/absen, rotasi, kandang/tandang, perjalanan, istirahat, klasemen |
| Potensi BTTS | Kualitas serangan, pertahanan, menit akhir, transisi, set piece, clean sheet |
| Anomali pasar | Perubahan menjelang kickoff, berita, spread, likuiditas, aturan kontrak |
| Verifikasi | Tiga sumber pasar pembanding bila tersedia, kecocokan dengan kondisi lapangan |

Angka “3+ pemain absen → peluang menang turun 22%”, “home +35%”, dan “zona degradasi → intensitas +18%” disimpan sebagai **hipotesis belum terverifikasi secara universal**. Temuan awal dan rancangan pengujiannya ada di [daftar hipotesis](skills/superanalyst/references/hypotheses.md).

## Memakai skill

Untuk memakai salinan lokal dalam chat yang dapat mengakses folder ini:

> Baca `skills/superanalyst/SKILL.md`, lalu gunakan Superanalyst untuk menganalisis [tim kandang] vs [tim tandang] pada [tanggal dan kompetisi].

Untuk memasangnya agar tersedia di chat lain, minta Codex memasang folder `skills/superanalyst` dari salinan repo ini menggunakan mekanisme instalasi skill yang tersedia. **Pembuatan repo ini belum memasang skill secara global.**

Untuk memasang dari repo private melalui akun yang memiliki akses:

```text
$skill-installer pasang skill dari repo drewips22/Superanalyst, path skills/superanalyst.
```

Contoh pemakaian setelah terpasang:

```text
$superanalyst analisis Arsenal vs Chelsea pada [tanggal], kompetisi [nama].
Gunakan batas informasi saat ini. Bahas 1X2, BTTS, dan data yang belum tersedia.
```

```text
$superanalyst periksa pergerakan pasar untuk [laga dan tautan kontrak].
Bandingkan tiga sumber, aturan penyelesaian, serta berita line-up.
```

```text
$superanalyst evaluasi arsip prediksi ini secara kronologis.
Pisahkan horizon prediksi, model, liga, dan data sintetis dari data nyata.
```

Struktur skill mengikuti [dokumentasi resmi pembuatan skill](https://learn.chatgpt.com/docs/build-skills). Ketersediaan berita dan xG bergantung pada sumber yang dapat diakses; repo tidak menyertakan langganan data atau pengambil data otomatis.

## Isi repo

```text
skills/superanalyst/
  SKILL.md                         panduan utama
  agents/openai.yaml               nama dan pemicu skill
  references/
    methodology.md                definisi data, tren, dan BTTS
    hypotheses.md                 bukti awal dan hipotesis yang perlu diuji
    markets.md                    protokol perbandingan pasar
    backtesting.md                evaluasi tanpa kebocoran data masa depan
    tools.md                      format input dan penggunaan alat
  assets/report-template.md        format laporan pertandingan
  scripts/
    stats.py                      ringkasan lima laga dan distribusi Poisson
    evaluate.py                   Brier, log loss, dan tabel kalibrasi
examples/                          contoh sintetis yang bisa dijalankan
tests/                             pengujian perilaku perhitungan
backtests/ucl-2025-final/           kasus historis, prediksi, dan evaluasi terpisah
```

## Menjalankan alat

Gunakan Python 3.11 atau lebih baru. Alat hanya memakai pustaka standar, tanpa paket tambahan. Jalankan dari akar repo; ganti `python` dengan lokasi interpreter Python bila diperlukan.

```sh
python skills/superanalyst/scripts/stats.py summary examples/team-history.synthetic.json
python skills/superanalyst/scripts/stats.py poisson --home-rate 1.6 --away-rate 1.2
python skills/superanalyst/scripts/evaluate.py examples/predictions.synthetic.jsonl
python -m unittest discover -s tests -v
python backtests/ucl-2025-final/run.py verify
```

Parameter 1.6 dan 1.2 di atas adalah **contoh perhitungan**, bukan estimasi untuk tim nyata. Kalkulator Poisson tidak melatih model atau menentukan parameter sendiri. Evaluator menilai prediksi yang sudah disimpan; pelatihan dan pengujian kronologis mengikuti [protokol backtest](skills/superanalyst/references/backtesting.md).

Pemeriksaan: **35 tes perhitungan dan validasi lolos**. Kasus historis dapat dihitung ulang dan dicek melalui checksum. Pemeriksaan struktur skill dan tautan internal juga dilakukan. Tes memvalidasi paket dan perhitungan; mutu prediksi tetap perlu pengujian banyak laga di luar sampel.

## Pengembangan berikutnya

1. Tentukan kompetisi awal dan sumber data yang tersedia secara konsisten.
2. Kumpulkan statistik, berita, dan snapshot pasar dengan waktu ketersediaannya.
3. Tetapkan model pembanding serta batas waktu prediksi sebelum melihat hasil uji.
4. Uji fitur satu per satu: lima laga, H2H, pemain absen, perjalanan, motivasi, lalu pasar.
5. Catat hasil uji pada musim berikutnya, kalibrasi, cakupan data, dan kegagalan prediksi.

Data berlisensi dan arsip prediksi pribadi disimpan di `data/` atau `runs/`, yang diabaikan Git. Masukkan ke repo hanya bila hak penggunaan dan kebutuhan berbagi sudah jelas. Belum ada lisensi distribusi publik yang dipilih untuk proyek private ini.

## Repo GitHub private

Repo tersedia di [drewips22/Superanalyst](https://github.com/drewips22/Superanalyst). Untuk mengambil salinan, gunakan akun yang mempunyai akses:

```sh
git clone https://github.com/drewips22/Superanalyst.git
```

Salinan folder lokal sudah terhubung ke `origin`. Setelah membuat commit perubahan yang diinginkan:

```sh
git push
```

Paket ZIP berisi source tanpa riwayat Git. Gunakan salinan hasil clone bila ingin melanjutkan pengembangan dengan riwayat commit yang sama.
