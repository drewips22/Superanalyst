# Metodologi analisis pertandingan

## 1. Definisi dan provenance

Gunakan identitas pertandingan, bukan hanya nama klub: kompetisi, musim, kategori tim (senior/usia muda, putra/putri), tanggal, kickoff dengan zona waktu, stadion, dan kandang/tandang/netral. Periksa jadwal resmi terbaru. Semua hasil dasar memakai 90 menit termasuk injury time, tanpa extra time atau penalti penentuan pemenang.

Catat sumber untuk setiap kelompok data: URL, penyedia, waktu publikasi/tersedia, waktu diambil, dan batas `as_of`. Prioritas sumber menurut jenis fakta:

| Fakta | Prioritas |
| --- | --- |
| Jadwal, venue, klasemen, skorsing | Penyelenggara kompetisi/federasi |
| Line-up, kabar pemain | Line-up resmi; pengumuman klub; konferensi pers; reporter yang mengutip sumber langsung |
| Skor dan statistik | Match centre resmi atau penyedia statistik dengan definisi konsisten |
| xG dan kejadian taktik | Penyedia event data dan dokumentasi model/metrik |
| Harga dan aturan pasar | Halaman kontrak, order book, riwayat transaksi dari pasar itu sendiri |

Tanggal artikel dan pertandingan yang dibahas bisa berbeda. Berita lama yang muncul lagi di pencarian tidak menjadi kabar baru. Bila dua sumber bertentangan, jelaskan konflik, cek sumber primer terbaru, dan pertahankan ketidakpastian yang belum terselesaikan.

## 2. Lima laga terakhir

Ambil lima pertandingan kompetitif tim yang benar-benar selesai sebelum `as_of`. Secara default gunakan semua kompetisi, nyatakan cakupannya, dan tandai perbedaan kualitas lawan/kompetisi. Jangan memilih lima laga yang paling mendukung prediksi. Persahabatan, pertandingan batal, dan pertandingan belum selesai dipisahkan. Jika hanya tiga laga tersedia, tampilkan tiga; jangan mengarang dua lainnya.

Sajikan tabel kronologis terlama → terbaru, berisi lawan, venue, skor, hasil, gol untuk/lawan, xG/xGA, tembakan, tembakan tepat sasaran, dan penguasaan bola bila tersedia. Gunakan skor dan statistik waktu normal yang sama. Data 120 menit tidak boleh dicampur dengan skor 90 menit; jika pemisahan tidak tersedia, tandai metrik tersebut hilang.

Perhitungan dengan `n` pertandingan:

- `GF = sum(gol_dicetak)`; `GA_per_match = sum(kebobolan) / n`.
- `PPG = (3 × menang + seri) / n`.
- `xG_per_match = sum(xG tersedia) / jumlah laga dengan xG`.
- `xGA_per_match` memakai denominator xGA yang tersedia.
- `xGD` dihitung hanya pada laga yang punya **pasangan** xG dan xGA. Jangan mengurangkan dua rata-rata dari himpunan laga berbeda.
- `clean_sheet_rate = jumlah laga GA=0 / n`.
- `failed_to_score_rate = jumlah laga GF=0 / n`; `BTTS_rate = jumlah laga GF>0 dan GA>0 / n`.

Laporkan jumlah data tersedia untuk setiap metrik. Nol xG yang diketahui tetap nol; xG yang tidak diperoleh tetap kosong. Jangan mengubah tembakan menjadi xG dengan koefisien tebakan.

Gunakan satu provider dan jenis metrik yang sama. xG, non-penalty xG, dan post-shot xG tidak saling menggantikan. Catat versi model bila tersedia: pembaruan model dapat mengubah seri historis. Penyedia xG sendiri menjelaskan bahwa hasil bergantung pada data dan rancangan model. [StatsBomb, 2022](https://blogarchive.statsbomb.com/articles/soccer/upgrading-expected-goals/)

### Tren hasil dan kualitas

Tampilkan urutan W-D-L serta xGD per laga. Bila kelima laga lengkap, selisih PPG tiga laga terbaru terhadap dua sebelumnya dapat menjadi **ringkasan deskriptif**, bukan uji signifikansi atau koefisien prediksi. Selisih xGD hanya dibandingkan jika kedua subperiode punya data pasangan lengkap yang sebanding.

Bandingkan dengan musim berjalan atau periode lebih panjang yang juga berada sebelum `as_of`. Bahas kualitas lawan, kartu merah, penalti, rotasi, dan kepadatan jadwal. Satu kemenangan besar dapat mengangkat rata-rata; hasil menang dengan xGD menurun berarti sinyal yang bercampur. Hindari kesimpulan otomatis bahwa selisih gol aktual terhadap xG pasti berbalik pada pertandingan berikutnya.

### Kandang/tandang

Lima laga keseluruhan tetap ditampilkan. Tambahkan rekam kandang tim tuan rumah dan tandang tim tamu pada jendela lebih panjang bila tersedia; jangan mengganti lima laga keseluruhan dengan lima kandang/tandang tanpa memberi label. Laporkan jumlah pertandingan setiap kelompok dan pisahkan venue netral. Efek kandang yang sudah ada pada model tidak ditambahkan kembali sebagai bonus.

## 3. Pola gol dan H2H

Mulai dari sampai lima H2H terbaru sebelum cutoff, dengan tanggal dan kompetisi. Jika sangat lama atau lintas rezim pelatih/susunan pemain, jelaskan relevansinya yang terbatas; jumlah lima bukan kewajiban mengisi kekosongan. Ringkas total/rata-rata gol, frekuensi BTTS dan clean sheet, W-D-L dari perspektif tim yang konsisten, serta penguasaan bola jika tersedia.

Periksa apakah pola bertahan setelah memperhatikan venue, kekuatan tim, kartu merah, dan rotasi. Penguasaan bola tinggi bisa berarti dominasi, sirkulasi tanpa ancaman, atau lawan sengaja bertahan; periksa xG, lokasi peluang, dan keadaan skor. Jangan menafsirkan satu kemenangan H2H sebagai bukti pola yang berulang.

## 4. Line-up, perjalanan, dan motivasi

Catat setiap pemain relevan: peran, status **out/suspended/doubtful/available**, sumber, waktu pembaruan, perkiraan peluang bermain bila memang ada sumber/model, menit historis, dan pengganti. Jumlah pemain absen saja tidak menunjukkan besarnya dampak. Tiga cadangan dan tiga pemain inti memiliki implikasi berbeda. Absensi lama mungkin sudah tercermin dalam performa terakhir.

Labeli XI sebagai **resmi** hanya setelah diumumkan klub/kompetisi. Saat masih perkiraan, susun skenario utama dan alternatif. Periksa kembali setelah pengumuman resmi bila pengguna menjalankan analisis mendekati kickoff.

Untuk perjalanan, gunakan asal perjalanan yang diketahui: setelah tur atau laga tandang, tim belum tentu berangkat dari kota markas. Catat jarak, metode estimasi, durasi bila tersedia, pergantian zona waktu, waktu kedatangan, hari istirahat, dan jadwal sebelumnya. Jarak garis lurus antarkota adalah proxy, bukan durasi perjalanan atau bukti kelelahan.

Untuk motivasi, dokumentasikan posisi/poin klasemen sebelum laga, sisa pertandingan, jarak ke degradasi/target kualifikasi, aturan tiebreak, dan laga berikutnya. Verifikasi apakah "top 4" benar-benar batas kualifikasi di kompetisi dan musim tersebut. Kebutuhan menang bisa meningkatkan risiko taktik atau tekanan; tidak otomatis meningkatkan kualitas maupun konsistensi hasil. Dalam laga dua leg, gunakan agregat dan aturan kompetisi yang benar.

## 5. BTTS dan clean sheet

Untuk masing-masing tim, cari bukti tentang:

- **Serangan:** xG/xG per shot, tembakan dan tepat sasaran, masuk kotak penalti, serangan sisi sayap, transisi, serta produktivitas set piece.
- **Pertahanan lawan:** xGA, peluang yang diizinkan, lokasi/tipenya, pertahanan crossing, set piece, dan ruang setelah pressing.
- **Menit akhir:** gol, tembakan, dan xG menit 76–90+ dengan definisi interval provider. Bedakan kondisi sedang unggul/tertinggal, kartu merah, dan perubahan pemain. Gol menit akhir saja tidak membuktikan intensitas tinggi sepanjang interval.

Rata-rata 12–15 tembakan atau kebobolan 1–2 gol dalam empat dari lima laga adalah calon fitur. Perlu kualitas peluang, lawan, dan konteks; tidak menjadi syarat lulus BTTS.

### Probabilitas gabungan

Misalkan `H` dan `A` adalah jumlah gol tuan rumah dan tamu:

```text
P(BTTS) = 1 - P(H=0) - P(A=0) + P(H=0, A=0)
clean_sheet_home = P(A=0)
clean_sheet_away = P(H=0)
```

Dua probabilitas clean sheet saja belum menentukan probabilitas BTTS tanpa ketergantungan antargol. Batas matematis dari marginal `cH`, `cA` adalah:

```text
max(0, 1-cH-cA) <= P(BTTS) <= min(1-cH, 1-cA)
```

Di bawah asumsi gol Poisson **independen** dengan laju `lambda_home` dan `lambda_away`:

```text
P(H=h, A=a) = Poisson(h; lambda_home) × Poisson(a; lambda_away)
P(BTTS) = (1-exp(-lambda_home)) × (1-exp(-lambda_away))
P(clean_sheet_home) = exp(-lambda_away)
P(clean_sheet_away) = exp(-lambda_home)
```

Contoh hipotetis clean sheet tim A 18–22% dan tim B 20–24% menghasilkan BTTS sekitar **59,3–65,6% jika diasumsikan independen**. Ini rentang sensitivitas dari input contoh, bukan interval keyakinan, dan bukan estimasi untuk pertandingan nyata. Frekuensi clean sheet pada lima laga tidak boleh langsung disubstitusi sebagai marginal laga berikutnya.

### Mengestimasi laju gol

Pilihan baseline yang bisa diuji adalah regresi Poisson pada gol waktu normal dengan kekuatan serang tim, pertahanan lawan, dan efek kandang liga. Latih hanya dari laga sebelum cutoff, gunakan regularisasi, dan catat jendela latih, identifikasi parameter, bobot recency, serta model/version. Tim baru membutuhkan prior liga dan label ketidakpastian. Nilai parameter atau bobot dipilih dari data latih/validasi, bukan ditebak dari lima laga.

xG historis dapat menjadi fitur atau target alternatif dengan metode yang sesuai, namun rata-rata xG lima laga bukan otomatis `lambda` untuk lawan berikutnya. Untuk rilis ini, kalkulator menerima laju yang ditentukan pengguna/model; tidak ada pelatihan model otomatis. Bila laju belum memiliki dasar yang dapat diaudit, laporkan kesimpulan kualitatif.

Model independen mengabaikan hubungan skor, perubahan taktik, dan beberapa dinamika skor rendah. Evaluasi kalibrasi sebelum memperlakukan outputnya sebagai probabilitas andal. Simpan analisis lapangan lebih dahulu sebelum melihat pasar bila ingin membandingkan keduanya secara jujur.

## 6. Kesimpulan

Sampaikan arah hasil yang paling didukung, bukti yang melemahkannya, skenario line-up, dan faktor yang dapat membalik penilaian. Kualitas data tinggi berarti sumbernya baik, bukan berarti hasil pertandingan pasti. Gunakan status provisional/observasi jika sumber penting bertentangan atau susunan pemain belum jelas. Gunakan tidak cukup data bila pertandingan, skor historis, atau dasar probabilitas tidak dapat diverifikasi.
