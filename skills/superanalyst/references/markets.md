# Membaca anomali pasar

Gunakan bagian ini jika pengguna meminta pemeriksaan pasar, atau jika data pasar yang sebanding tersedia dalam analisis pertandingan. Bila tidak ada, tandai bagian pasar N/A dan lanjutkan analisis lapangan.

## 1. Samakan objek yang dibandingkan

Verifikasi tim, kompetisi, kickoff, venue, dan aturan penyelesaian setiap kontrak. **Menang dalam 90 menit**, **menang termasuk extra time**, dan **lolos babak berikutnya** adalah kejadian berbeda. Baca penanganan seri, pertandingan tunda, pembatalan, dan void. BTTS juga harus memiliki cakupan waktu yang sama.

Pasar biner "tim A menang: Yes/No" tidak setara dengan "A atau B menang": No bisa mencakup seri. Untuk 1X2, hasil home/draw/away harus saling eksklusif dan meliputi seluruh hasil yang dimaksud. Jangan mencampurkan tiga kontrak yang berbeda definisinya agar jumlah terlihat 100%.

## 2. Catat data yang diperlukan

Simpan URL dan ID kontrak/outcome, teks aturan atau rujukannya, cap waktu UTC, waktu ke kickoff, bid terbaik, ask terbaik, midpoint, last trade beserta waktunya, spread, kedalaman di sekitar harga, volume pada jendela pengamatan, dan jenis harga yang ditampilkan. Pisahkan angka yang tidak diperoleh dari nilai nol.

Dokumentasi Polymarket menyatakan harga berasal dari order book; tampilan memakai midpoint, atau last trade ketika spread melebihi batas tertentu. Harga tampilan tidak selalu harga yang dapat dieksekusi, dan order besar dapat mengubah harga. Karena aturan produk bisa berubah, periksa dokumentasi saat mengambil data. [Dokumentasi harga dan order book](https://docs.polymarket.com/concepts/prices-orderbook)

Implikasi analisis: perubahan grafik bisa mencerminkan transaksi tipis, quote yang ditarik, pergantian jenis harga tampilan, pembaruan yang terlambat, atau berita. Semua itu **calon penjelasan**, bukan kesimpulan penyebab tanpa bukti. Volume tidak sama dengan jumlah orang yang percaya pada suatu hasil.

## 3. Ukur gerakan tanpa memilih contoh setelah hasil diketahui

Untuk penelitian T-30, tentukan terlebih dahulu snapshot yang diambil, misalnya T-60, T-30, T-10, dan T-5 menit. T-60 dan seterusnya diukur terhadap kickoff yang benar-benar dijadwalkan saat itu; catat revisi jadwal. Pilih toleransi waktu sebelum evaluasi dan jangan mengisi snapshot yang hilang dengan harga sesudah cutoff.

```text
delta_pp = 100 × (p_baru - p_lama)
perubahan_relatif = p_baru / p_lama - 1   [hanya jika p_lama > 0]
```

"Berbalik dominan" perlu definisi: apakah home berpindah dari lebih tinggi ke lebih rendah dibanding away, atau melewati ambang tertentu? Dalam 1X2, hasil seri juga bisa menjadi favorit. Jangan memaksakan ambang 50% pada setiap favorit tiga arah.

Ambang perubahan harga, durasi bertahan, spread maksimum, dan kedalaman minimum adalah parameter penelitian yang ditetapkan dari data latih/validasi. Tiga puluh menit adalah jendela observasi usulan pengguna, bukan hukum bahwa informasi penting selalu tiba pada waktu itu.

## 4. Periksa tiga sumber pembanding

Upayakan tiga **sumber pasar independen** pada kontrak dan waktu yang sama. Situs agregator yang menyalin feed yang sama tidak dihitung sebagai sumber independen. Situs berita memverifikasi berita pemain, tetapi tidak menggantikan quote pasar pembanding. Nama sumber bukan kewajiban jika layanan tidak dapat diakses.

Untuk odds desimal bookmaker pada satu pasar 1X2 lengkap:

```text
q_i = 1 / odds_i
p_i = q_i / sum(q)   [normalisasi margin secara proporsional]
overround = sum(q) - 1
```

Gunakan odds ketiga hasil dari bookmaker dan snapshot yang sama. Ini pendekatan penghilangan margin, bukan probabilitas "benar". Jangan menerapkannya secara buta pada kumpulan harga Polymarket, pasar exchange, kontrak tumpang tindih, atau data dengan outcome hilang. Pertimbangkan bid/ask dan kesamaan aturan. Laporan tidak perlu menghitung kelayakan transaksi kecuali pengguna memintanya.

| Sumber | Kontrak/cakupan | Waktu | Harga/odds | Jenis harga | Spread/depth | Sebanding? |
| --- | --- | --- | --- | --- | --- | --- |
| Isi data aktual | Isi | ISO 8601 | Isi | Bid/ask/mid/last | Isi/N/A | Ya/tidak + alasan |

Jika hanya dua pembanding tersedia, tulis **2/3, pemeriksaan belum lengkap**. Jangan mengarang sumber ketiga atau mengklaim konsensus.

## 5. Cocokkan dengan lapangan

Susun kronologi perubahan harga, publikasi berita, pengumuman XI, dan pembaruan statistik yang relevan. Cek cedera mendadak, rotasi, pergantian kiper, formasi, venue, cuaca jika relevan dan terverifikasi, serta kesalahan pemetaan kontrak.

- **Berita terkonfirmasi dan beberapa sumber bergerak:** konsisten dengan respons pasar atas berita tersebut; belum membuktikan hubungan sebab-akibat atau bocoran.
- **Satu pasar berubah dengan spread lebar/depth tipis:** observasi mikrostruktur dan likuiditas.
- **Pasar dan statistik berbeda tanpa penjelasan:** red flag untuk pemeriksaan, bukan bukti bahwa pasar atau model pasti salah.
- **Sumber/waktu tidak sebanding:** tidak cukup data untuk menyimpulkan anomali.

Jangan mengganti probabilitas model lapangan secara diam-diam agar sama dengan pasar. Simpan model lapangan dan estimasi pasar terpisah. Bila menggunakan model gabungan, bobotnya harus ditentukan dan diuji secara historis. Pemeriksaan ini bersifat analitis; repo tidak mengirim order.
