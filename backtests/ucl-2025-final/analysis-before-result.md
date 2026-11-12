# PSG–Inter: analisis dengan batas informasi sebelum final

**Kesimpulan eksperimen: PSG menjadi hasil 1X2 dengan peluang terbesar, sedangkan baseline condong ke BTTS. Status analisis: provisional.** Ini hanya satu rekonstruksi historis untuk mencoba proses Superanalyst.

| Pengaturan | Nilai |
| --- | --- |
| Pertandingan | Final UEFA Champions League 2024/25, PSG–Inter |
| Venue | Munich Football Arena, Munich; netral |
| Kickoff | 31 Mei 2025 21.00 CEST / **1 Juni 2025 02.00 WIB** |
| Batas informasi | **30 Mei 2025 19.00 WIB** / 12.00 UTC |
| Horizon | 31 jam sebelum kickoff |
| Cakupan | 90 menit + injury time; tanpa extra time dan adu penalti |
| Waktu penyusunan sebenarnya | 12 November 2026; waktu eksekusi tepat disimpan pada `prediction.json` |
| Jenis uji | Rekonstruksi retrospektif; bukan prediksi yang direkam pada 2025 dan bukan uji buta |

Jadwal dan venue didukung pengumuman Inter bertanggal 29 Mei 2025. Konferensi pers resmi kedua tim pada 30 Mei dijadwalkan setelah batas informasi di atas, sehingga isi konferensi itu dikeluarkan dari analisis ini. [Jadwal kegiatan jelang final](https://www.inter.it/en/news/activities-eve-final-champions-league-psg-inter-24-25)

Halaman historis diambil sekarang. Versi aslinya saat itu tidak seluruhnya diarsipkan; panel performa terkini atau tautan pertandingan setelah cutoff pada halaman yang sama diabaikan. Data kejadian pertandingan lama membantu rekonstruksi, tetapi tidak membuktikan bahwa setiap angka xG yang sekarang tampil identik dengan versi yang tersedia pada 2025. Angka berikut tidak memakai statistik pertandingan final sebagai fitur.

## Data: lima laga terakhir

Urutan terlama → terbaru; skor selalu dari perspektif tim yang dianalisis. H/A/N berarti kandang/tandang/netral. N/A adalah data yang tidak digunakan atau belum diperoleh dengan cakupan yang sesuai.

### Paris Saint-Germain

| Tanggal 2025 | Lawan | H/A/N | Skor 90m | Hasil | xG–xGA | Tembakan | SoT | Possession |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 Mei | Strasbourg | A | 1–2 | L | 1,73–0,73 [S1] | 20 | 4 | 64% |
| 7 Mei | Arsenal | H | 2–1 | W | 1,74–2,91 [S2] | 11 | 6 | 46% |
| 10 Mei | Montpellier | A | 4–1 | W | 1,50–0,61 [F1] | 10 | N/A | 70% |
| 17 Mei | Auxerre | H | 3–1 | W | 3,11–0,63 [S3] | 21 | 9 | 67% |
| 24 Mei | Reims, final Coupe de France | N | 3–0 | W | 3,13–0,15 [F2] | 20 | 8 | 76% |

Skor diperiksa pada match centre resmi PSG; URL tiap laga disimpan di [data masukan](features.json). Statistik diterbitkan oleh Sporting Life/Opta dan FotMob/Opta. Kedua seri penerbit ditampilkan terpisah untuk perhitungan xG karena versi model historisnya belum diverifikasi identik.

[S1: Strasbourg–PSG](https://www.sportinglife.com/football/live/188450/strasbourg-vs-paris-saint-germain/stats) · [S2: PSG–Arsenal](https://www.sportinglife.com/football/live/205833/paris-saint-germain-vs-arsenal/stats) · [S3: PSG–Auxerre](https://www.sportinglife.com/football/live/188528/paris-saint-germain-vs-auxerre/stats) · [F1: Montpellier–PSG](https://www.fotmob.com/fr/matches/paris-saint-germain-vs-montpellier/3c8ddj) · [F2: PSG–Reims](https://www.fotmob.com/en-GB/matches/reims-vs-paris-saint-germain/37cq5t).

### Inter

| Tanggal 2025 | Lawan | H/A/N | Skor 90m | Hasil | xG–xGA | Tembakan | SoT | Possession |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 Mei | Hellas Verona | H | 1–0 | W | 1,34–0,29 [S4] | 9 | 2 | 69% |
| 6 Mei | Barcelona | H | **3–3** | D | N/A | N/A | N/A | N/A |
| 11 Mei | Torino | A | 2–0 | W | 2,60–1,57 [S5] | N/A | N/A | N/A |
| 18 Mei | Lazio | H | 2–2 | D | 1,13–2,09 [S6] | 10 | 3 | 56% |
| 23 Mei | Como | A | 2–0 | W | 1,39–1,25 [S7] | N/A | 7 | 61% |

**Inter–Barcelona: 3–3 pada akhir waktu normal, kemudian 4–3 setelah extra time.** Gol menit 99 dikeluarkan dari GF. Statistik agregat yang mencakup 120 menit juga dikeluarkan karena pemisahan 90 menit belum diperoleh. [Laporan resmi Inter, 6 Mei](https://www.inter.it/en/news/inter-barcelona-champions-league-24-25)

[S4: Inter–Verona](https://www.sportinglife.com/football/live/192275/internazionale-vs-hellas-verona/stats) · [S5: Torino–Inter](https://www.sportinglife.com/football/live/192079/torino-vs-internazionale/commentary) · [S6: Inter–Lazio](https://www.sportinglife.com/football/live/192203/internazionale-vs-lazio/stats) · [S7: Como–Inter](https://www.sportinglife.com/football/live/192244/como-vs-internazionale).

### Ringkasan terhitung

| Metrik | PSG | Inter |
| --- | --- | --- |
| Gol dicetak / kebobolan | **13 / 5** | **10 / 5** |
| Rata-rata gol dicetak | 2,60 | 2,00 |
| Rata-rata kebobolan | **1,00** | **1,00** |
| W-D-L pada 90m | 4–0–1 | 3–2–0 |
| Poin per laga | 2,40 | 2,20 |
| Clean sheet historis | **1/5 = 20%** | **3/5 = 60%** |
| Gagal mencetak gol | 0/5 | 0/5 |
| BTTS historis | 4/5 = 80% | 2/5 = 40% |
| Tembakan per laga | 16,40; lengkap 5/5 | 9,50; hanya 2/5, tidak mewakili lima laga |
| SoT per laga | 6,75; tersedia 4/5 | 4,00; tersedia 3/5 |
| Gol dicetak menit 76–90+ | 1 gol pada 1/5 laga | 2 gol pada 2/5 laga |
| Gol kebobolan menit 76–90+ | 1 gol | 2 gol |

Ringkasan xG **tidak digabung lintas seri penerbit**:

| Seri yang dibaca | n | xG/laga | xGA/laga | xGD/laga |
| --- | --- | --- | --- | --- |
| PSG, Sporting Life/Opta | 3/5 | 2,19 | 1,42 | +0,77 |
| PSG, FotMob/Opta | 2/5 | 2,32 | 0,38 | +1,94 |
| Inter, Sporting Life/Opta | 4/5 | 1,62 | 1,30 | +0,32 |

Ini bukan perbandingan xG yang sepenuhnya setara: kelompok PSG berbeda lawan, sedangkan kelompok Inter mengecualikan Barcelona. Rata-rata musim dan penyesuaian kekuatan lawan belum dimasukkan.

**Inferensi tren:** empat kemenangan beruntun menunjukkan hasil PSG membaik. Namun kemenangan atas Arsenal terjadi saat xG PSG lebih rendah, dan empat gol atas Montpellier melampaui xG 1,50. Hasil menang tidak otomatis berarti kualitas peluang selalu naik. Inter tidak kalah dalam lima laga pada 90 menit, dengan hasil dua pertandingan Eropa/liganya tetap menunjukkan kemungkinan kebobolan beberapa gol. Kemenangan atas Como juga perlu konteks kartu merah Reina; ini tercatat dalam laporan klub sebelum final. [Como–Inter, 23 Mei](https://www.inter.it/en/news/como-inter-serie-a-24-25)

## Pola gol dan H2H

Sebelum final ini, belum ada pertemuan resmi kompetitif. Lima pertemuan terakhir berikut merupakan laga persahabatan atau turnamen pramusim; possession belum diperoleh.

| Tanggal | Skor PSG–Inter pada waktu normal | BTTS |
| --- | --- | --- |
| 30 Desember 2014 | 1–0 | Tidak |
| 30 Desember 2015 | 1–0 | Tidak |
| 24 Juli 2016 | 3–1 | Ya |
| 27 Juli 2019 | 1–1 | Ya |
| 1 Agustus 2023 | 1–2 | Ya |

Ringkasan: PSG 3 menang, 1 seri, 1 kalah; gol 7–4; BTTS 3/5. Perubahan susunan pemain dan jarak waktu membuatnya tidak cukup kuat untuk memberi bonus probabilitas. Adu penalti diabaikan. [Riwayat resmi Inter, terbit 24 Mei 2025](https://www.inter.it/en/news/final-champions-league-inter-psg-fixture-history)

## Line-up, absensi, dan motivasi

**Belum ada XI resmi dalam horizon ini.** Skenario susunan berikut adalah perkiraan analitis berdasarkan susunan terdahulu dan kabar yang masuk sebelum cutoff:

- **PSG, 4-3-3:** Donnarumma; Hakimi, Marquinhos, Pacho, Nuno Mendes; João Neves, Vitinha, Fabián Ruiz; Doué/Barcola, Dembélé, Kvaratskhelia.
- **Inter, 3-5-2:** Sommer; Pavard bila siap/Bisseck, Acerbi, Bastoni; Dumfries, Barella, Çalhanoğlu, Mkhitaryan, Dimarco; Thuram, Lautaro.

Inzaghi pada 26 Mei menyatakan Lautaro dalam kondisi baik dan menyampaikan optimisme soal Pavard serta Zielinski. Optimisme belum menjadi kepastian starter. Tidak ada dasar untuk menerapkan penalti otomatis “3+ absen = minus 22%”. [Keterangan resmi Inzaghi](https://www.inter.it/en/news/media-day-champions-league-final-press-conference-inzaghi)

Laporan Le Parisien bertanggal 30 Mei pukul 11.29 waktu Prancis menyebut grup PSG berisi 22 pemain, termasuk Kimpembe dan Kvaratskhelia. Dengan interpretasi CEST, publikasinya sekitar 09.29 UTC, sebelum cutoff 12.00 UTC. Laporan ini mendukung ketersediaan dalam grup, bukan kepastian kondisi penuh atau starter; versi historis aslinya tidak diarsipkan. [Laporan grup PSG](https://www.leparisien.fr/sports/football/psg/psg-inter-milan-le-groupe-parisien-sans-absent-et-avec-kimpembe-30-05-2025-QHZ42DRA5NBYVG4QQHTDEGU3UY.php)

**Konteks:** ini final di venue netral, sehingga label home PSG tidak memperoleh bonus kandang. Selisih tanggal dari laga terakhir ke final adalah tujuh hari untuk PSG dan delapan hari untuk Inter. Durasi perjalanan, titik keberangkatan aktual, dan kondisi istirahat tidak terverifikasi; tidak ada koreksi jarak yang diterapkan. Kedua tim punya target trofi yang sama, sehingga aturan degradasi atau perburuan top 4 tidak relevan untuk pertandingan ini. Motivasi tidak diberi pengali angka.

## Potensi BTTS

**Bukti yang mendukung:** kedua tim selalu mencetak gol pada lima laga terakhir. PSG mencatat BTTS pada 4/5 laga. Inter menghadapi pertandingan terbuka melawan Barcelona dan Lazio. PSG mempunyai ancaman di sisi sayap melalui Hakimi/Mendes, sedangkan dua penyerang dan wing-back Inter menjadi skenario ancaman balik; ini pembacaan taktik dari peran pemain, bukan pengukuran pressing atau pola crossing yang lengkap.

**Bukti yang melemahkan:** Inter mencatat tiga clean sheet. Pola kedua tim sama-sama mencetak gol belum konsisten karena BTTS Inter hanya 2/5. Jumlah gol PSG pada 15 menit akhir juga tidak mendukung klaim bahwa kedua tim selalu meningkatkan produksi gol pada interval itu. Data intensitas tembakan, xG per interval, pressing, dan peluang dari set piece belum lengkap; kerentanan spesifik tidak dipastikan dari skor saja.

## Baseline numerik yang dibekukan

Model: `last5-goals-mean-poisson-experimental-v1`. Ini baseline sederhana untuk pengujian proses, belum model terlatih atau terkalibrasi. Parameter ditetapkan dari aturan yang disimpan di [spesifikasi eksperimen](experiment.json):

```text
lambda_PSG   = (GF/laga PSG + GA/laga Inter) / 2 = (2,6 + 1,0) / 2 = 1,8
lambda_Inter = (GF/laga Inter + GA/laga PSG) / 2 = (2,0 + 1,0) / 2 = 1,5
```

Kedua jumlah gol diasumsikan Poisson independen. Tidak ada koreksi cedera, motivasi, H2H, xG, kandang, atau pasar. Hanya sepuluh skor historis di atas yang membentuk parameter numerik.

| Keluaran | Probabilitas eksperimen |
| --- | --- |
| PSG menang pada 90m | **44,92%** |
| Seri pada 90m | **22,77%** |
| Inter menang pada 90m | **32,32%** |
| BTTS ya | **64,85%** |
| Clean sheet PSG | 22,31% |
| Clean sheet Inter | 16,53% |
| Skor tunggal paling mungkin | 1–1; hanya 9,96% |

Angka 1X2 dibulatkan masing-masing sehingga tampilan dapat berjumlah 100,01%; nilai penuh berjumlah 100%. Clean sheet model untuk laga ini berbeda dari frekuensi historis, khususnya Inter 60%. Perbedaan itu menjadi alasan menjaga status provisional, bukan menganggap frekuensi lima laga sebagai probabilitas pertandingan baru. Skor modal 1–1 tidak bertentangan dengan PSG menjadi hasil 1X2 terbesar karena kemenangan PSG menjumlahkan banyak kemungkinan skor.

**Keputusan yang akan dinilai:** pilihan 1X2 = PSG, dengan aturan peluang terbesar; pilihan BTTS = ya, dengan ambang 50%. PSG tetap di bawah 50%, jadi ini bukan pernyataan dominasi peluang. Pembuktian mutu model memerlukan banyak laga dan pembanding di luar sampel.

## Pasar dan pemeriksaan anomali

Quote arsip yang sebanding pada cutoff: **0 dari 3 sumber pembanding**. Tidak ada klaim anomali Polymarket atau konfirmasi dari pasar. Closing odds yang muncul setelah cutoff tidak menggantikan data pasar pada horizon ini.

Pergerakan T-30 menit terjadi setelah cutoff T-31 jam. Untuk menguji sinyal itu, diperlukan eksperimen lain dengan snapshot T-30 yang benar-benar tersedia saat itu. Berita atau harga sesudah cutoff tidak mengubah prediksi ini.

## Batas keputusan

Skenario yang dapat mengubah penilaian sebelum laga adalah ketidaktersediaan pemain inti yang terkonfirmasi, formasi atau XI yang berbeda dari perkiraan, serta perbedaan besar kekuatan lawan setelah model diperluas. Semuanya perlu snapshot baru dengan alasan perubahan; output eksperimen ini tetap disimpan.

Kualitas skor historis cukup untuk baseline, tetapi kualitas backtest keseluruhan terbatas oleh satu laga, pemilihan kasus, versi sumber yang tidak diarsipkan, dan sebagian metrik yang hilang. Hasil final yang sudah publik bisa diketahui analis; aturan deterministik membantu keterulangan, tetapi tidak menghilangkan hindsight bias dari pemilihan kasus dan narasi. Analisis ini menjadi bahan pertimbangan, bukan hasil mutlak.
