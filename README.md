# Superanalyst

**Data → pola → keputusan** untuk analisis pertandingan sepak bola mendatang.

Superanalyst adalah repo skill untuk Codex. Isinya mengubah rancangan analisis menjadi prosedur yang bisa diulang, diperiksa sumbernya, dan dievaluasi setelah pertandingan. Bahasa utama: Indonesia.

**Status: v0.4.2 — keyakinan per target; acuan UNL dan model penelitian UCL tidak diubah.** Repo GitHub **private** tersedia di [drewips22/Superanalyst](https://github.com/drewips22/Superanalyst). Contoh dalam `examples/` tetap sintetis; studi nyata berada di `backtests/`. Hasil rekonstruksi membaik terhadap baseline lima laga, dengan batas sumber dan kebutuhan konfirmasi pada prediksi yang benar-benar direkam sebelum kickoff.

## Perbaikan pencatatan v0.4.2

[Protokol keputusan v1.1](skills/superanalyst/references/decision-quality.md) memisahkan keyakinan dan status setiap target, membuat observasi 1X2 eksplisit, serta mencatat konflik pemain dan sumber. Metode kualitatif, jendela lima laga, bobot dan seluruh arsip lama dipertahankan. Enam tes baru memeriksa cutoff, observasi, tipe target dan penilaian tanpa mengubah input. Peningkatan akurasi belum diklaim; perlu prediksi baru.

## Acuan UNL yang dipertahankan

Pengguna menetapkan metode `qualitative_superanalyst_national_team_pilot_v1` sebagai [acuan kerja UNL](skills/superanalyst/references/unl-baseline.md) pada 13 November 2026. Prediksi prospektif delapan laga sesi pertama menghasilkan 1X2 7/8, BTTS 5/6, total 2,5 gol 5/6, dan skenario skor tepat 5/8. Semua kekeliruan tetap dihitung. Ini hasil satu sesi, bukan akurasi jangka panjang, kalibrasi probabilitas atau bukti keunggulan terhadap pasar.

Urutan data → pola → keputusan dan keenam kelompok analisis tetap berlaku. Usulan pengembangan dicatat terpisah; tidak ada bobot baru yang diaktifkan berdasarkan satu matchday. [Spesifikasi acuan](skills/superanalyst/assets/unl-baseline-policy.json).

## Plugin untuk akun ChatGPT

Manifest `plugin.json` di akar repo mengemas skill sebagai plugin. Paket privat dapat dipasang melalui fitur plugin akun yang tersedia; pemasangan lokal ke `~/.codex/skills` tidak menyinkronkan skill ke ChatGPT HP. Plugin akun yang didukung tersedia di ChatGPT web, desktop dan mobile sesuai [dokumentasi OpenAI](https://learn.chatgpt.com/docs/plugins).

Keberadaan manifest atau ZIP tidak membuktikan pemasangan cloud selesai. Konfirmasi status pada halaman plugin akun setelah unggah dan pemasangan. Paket tidak membutuhkan MCP atau hooks lokal; lihat [panduan lingkungan plugin](skills/superanalyst/references/plugin-runtime.md). Arsip pribadi tetap di luar Git; bukti pilot terpilih dapat dibawa dalam paket privat tanpa mengubah arsip asli.

## Pengembangan model: 378 laga uji UCL

[Laporan lengkap](backtests/ucl-model-upgrade-v1/review.md) memakai corpus 25.496 laga historis, 125 laga UCL untuk memilih varian, lalu **378 laga UCL 2024/25–2025/26** untuk pengujian kronologis. Pilihan dikunci sebelum tahap penilaian uji; model dipasang ulang bulanan hanya dengan informasi yang mendahului cutoff T-24 jam.

| Target | Kesalahan probabilitas: lama → baru | Penurunan relatif | Pilihan tepat: lama → baru |
| --- | ---: | ---: | ---: |
| Pemenang/seri | Log loss 1,0033 → 0,9211 | **8,2%** | 52,9% → 57,7% |
| BTTS | Brier 0,2541 → 0,2451 | **3,6%** | 54,0% → 55,8% |
| Over 2,5 | Brier 0,2348 → 0,2226 | **5,2%** | 62,2% → 66,4% |

Ketiga target membaik pada masing-masing musim uji dan lolos batas peningkatan yang sudah ditetapkan. Target memakai model berbeda: pemenang memakai kekuatan tim/lawan + kandang + form10 + istirahat + proxy poin fase UCL; BTTS memakai gol 20 laga; total gol memakai kekuatan tim. [Kebijakan dan batas pemakaian](skills/superanalyst/references/trained-models.md).

Ini **rekonstruksi dengan sumber historis yang diambil sekarang**, bukan uji buta penuh atau forecast yang direkam saat itu. Ketersediaan hasil menggunakan proxy waktu, cakupan kompetisi dapat terbatas, dan kalibrasi untuk pemakaian langsung belum disahkan. Model belum dibandingkan dengan arsip pasar pada waktu yang sama. Snapshot bulanan lama dipakai untuk replay; laga mendatang memerlukan data terbaru dan fit ulang.

[Studi tambahan xG](backtests/xg-domestic-2015-v1/review.md) memakai 760 laga dua liga pria 2015/16, dengan 222 laga uji terpisah. Campuran gol+xG membaik untuk pemenang, tetapi tidak untuk BTTS/total gol; ini tidak otomatis diterapkan ke UCL. Absensi berbobot peran dan anomali pasar masih membutuhkan arsip sebelum cutoff. [Status setiap faktor](backtests/ucl-model-upgrade-v1/coverage-status.json).

Catatan pengguna tentang Fenerbahçe beruntung disimpan sebagai [hipotesis diagnosis](backtests/ucl-model-upgrade-v1/fenerbahce-liverpool-diagnostic.json). Hasil pertandingan tetap dihitung dalam evaluasi.

## Sembilan laga UCL pada 5 November 2026 WIB

[Laporan per laga dan pola](backtests/ucl-2026-11-04/review.md) memakai cutoff **4 November 19.00 WIB**, sebelum sembilan laga sesi Rabu Matchday 4 (tanggal UEFA 4 November). Aturan gol lima laga yang sama dengan kasus pertama menghasilkan **1X2 tepat 6/9, BTTS 7/9, Over 2,5 8/9**. Pilihan pemenang yang keliru: Liverpool, Slavia, Sabah.

Seluruh sembilan hasil ternyata BTTS dan Over 2,5, sehingga sampel ini belum menguji kemampuan pola membedakan kejadian positif dan negatif. Hasil sudah terlihat pada lampiran dan sumber dinamis: ini **rekonstruksi, bukan uji buta**. Prediksi dan masukan dibekukan sebelum tahap penilaian; versi sumber asli tidak seluruhnya diarsipkan. xG konsisten belum diperoleh; angka ini hanya menilai baseline gol, bukan seluruh kriteria skill. Lihat [catatan pengembangan dari kasus ini](skills/superanalyst/references/research-log.md).

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
    research/                     kolektor, fitur kausal, fit model, dan validasi konteks
examples/                          contoh sintetis yang bisa dijalankan
tests/                             pengujian perilaku perhitungan
backtests/ucl-2025-final/           kasus historis, prediksi, dan evaluasi terpisah
backtests/ucl-2026-11-04/           sembilan laga UCL, pola, dan evaluasi terpisah
backtests/ucl-model-upgrade-v1/     validasi 125 laga dan uji UCL 378 laga
backtests/xg-domestic-2015-v1/      studi xG tambahan dua liga
requirements-research.txt          dependensi opsional untuk model terlatih
```

## Menjalankan alat

Gunakan Python 3.11 atau lebih baru. Alat dasar statistik/evaluasi memakai pustaka standar. Penelitian model terlatih memakai NumPy dan SciPy untuk optimasi dengan gradien analitik. Jalankan dari akar repo; ganti `python` dengan lokasi interpreter Python bila diperlukan.

```sh
python skills/superanalyst/scripts/stats.py summary examples/team-history.synthetic.json
python skills/superanalyst/scripts/stats.py poisson --home-rate 1.6 --away-rate 1.2
python skills/superanalyst/scripts/evaluate.py examples/predictions.synthetic.jsonl
python -m unittest discover -s tests -v
python backtests/ucl-2025-final/run.py verify
python backtests/ucl-2026-11-04/run.py verify
```

Untuk mengulang probabilitas dan skor penelitian dari snapshot yang tersimpan di repo, tanpa mengunduh seluruh corpus:

```sh
python -m pip install -r requirements-research.txt
python backtests/ucl-model-upgrade-v1/replay.py
python backtests/xg-domestic-2015-v1/replay.py
```

Parameter 1.6 dan 1.2 di atas adalah **contoh perhitungan**, bukan estimasi untuk tim nyata. Kalkulator Poisson tidak melatih model atau menentukan parameter sendiri. Evaluator menilai prediksi yang sudah disimpan; pelatihan dan pengujian kronologis mengikuti [protokol backtest](skills/superanalyst/references/backtesting.md).

Pemeriksaan: **74 tes perhitungan dan validasi** dengan dependensi penelitian. Studi historis dapat dihitung ulang dan dicek melalui checksum; penelitian baru menyediakan replay model/fitur dan skor. Pemeriksaan struktur skill dan tautan internal juga dilakukan. Tes memvalidasi kode; bukti mutu prediksi berasal dari evaluasi pertandingan, dengan batas sumber yang dijelaskan pada setiap studi.

## Pengembangan berikutnya

1. Konfirmasi resep UCL pada prediksi baru yang dikunci sebelum kickoff, lalu periksa kalibrasinya.
2. Kumpulkan xG UCL yang konsisten, pengumuman absensi berbobot peran, dan snapshot pasar bertimestamp.
3. Uji tambahan fitur pada cohort/horizon yang sama; pertahankan eksperimen yang tidak berhasil.
4. Uji efek di liga/horizon lain sebelum memperluas cakupan resep terpilih.
5. Simpan seluruh hasil termasuk kekalahan favorit dan diagnosis sesudah laga.

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
