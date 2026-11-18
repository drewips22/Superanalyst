# Evaluasi Superanalyst — UNL 18 November 2026

Delapan laga kickoff pukul 02.45 WIB. Prediksi dibekukan pada 17 Nov 2026 20.21.27 WIB. Penilaian memakai skor 90 menit termasuk injury time. [Skor resmi UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-results/)

| Ukuran | Utama | Beta V2 | Hybrid |
|---|---:|---:|---:|
| Fokus | 6/8 (75,0%) | 3/5 (60,0%) | 3/5 (60,0%) |
| Semua pilihan aktif | 11/15 (73,3%) | 6/9 (66,7%) | 4/7 (57,1%) |
| 1X2 | 4/5 (80,0%) | 1/2 (50,0%) | 1/2 (50,0%) |
| BTTS | 4/5 (80,0%) | 2/3 (66,7%) | 1/2 (50,0%) |
| Total 2,5 | 3/5 (60,0%) | 3/4 (75,0%) | 2/3 (66,7%) |

Utama menerbitkan pilihan pada 15/24 target dan fokus pada 8/8 laga. Beta V2 menerbitkan pilihan pada 9/24 target dan fokus pada 5/8 laga. Hybrid menerbitkan pilihan pada 7/24 target dan fokus pada 5/8 laga. Observasi dikeluarkan dari penyebut akurasi.

Kelima fokus yang diterbitkan kedua eksperimen persis sama dengan fokus Utama pada kelima laga itu. Ketiganya benar 3/5 pada irisan tersebut. Ketiganya juga benar 4/7 pada tujuh pasangan laga dan target yang dipilih bersama. Keunggulan Utama di ringkasan datang dari cakupan di luar irisan. Dua pilihan tambahan Beta sama-sama benar dan menjelaskan selisihnya dengan Hybrid.

| Laga | Aktual | Fokus Utama | Fokus Beta V2 | Fokus Hybrid |
|---|---:|---|---|---|
| Denmark–Norwegia | 2–3 | BTTS Ya · benar | Observasi | Observasi |
| Wales–Portugal | 2–3 | Portugal menang · benar | Portugal menang · 66,0% · benar | Portugal menang · 66,0% · benar |
| Bosnia & Herzegovina–Rumania | 2–1 | Bosnia & Herzegovina menang · benar | Observasi | Observasi |
| Hungaria–Irlandia Utara | 1–1 | Under 2,5 · benar | Under 2,5 · 64,4% · benar | Under 2,5 · 64,4% · benar |
| Irlandia–Kosovo | 3–0 | Under 2,5 · meleset | Under 2,5 · 61,3% · meleset | Under 2,5 · 61,3% · meleset |
| Israel–Austria | 1–1 | Austria menang · meleset | Austria menang · 71,5% · meleset | Austria menang · 71,5% · meleset |
| Polandia–Swedia | 1–1 | BTTS Ya · benar | Observasi | Observasi |
| Ukraina–Georgia | 1–0 | Under 2,5 · benar | Under 2,5 · 65,2% · benar | Under 2,5 · 65,2% · benar |

## Pilihan yang membedakan model

- Beta V2 benar pada BTTS Tidak Irlandia–Kosovo (59,3%) dan Under 2,5 Israel–Austria (57,5%). Hybrid mempertahankan observasi dari model utama pada kedua target itu.
- Utama benar pada 7 dari 8 pilihannya yang disaring Hybrid. Pada tiga laga tanpa fokus eksperimen, Utama benar pada fokus Denmark–Norwegia (BTTS Ya), Bosnia–Rumania (Bosnia menang), dan Polandia–Swedia (BTTS Ya). Pilihan Over 2,5 Polandia–Swedia tetap meleset.

## Telaah setelah laga

- **Israel 1–1 Austria.** Fokus Austria menang (71,5%) meleset pada kedua eksperimen. Utama sudah menandai potensi rotasi dengan keyakinan rendah. ÖFB mengumumkan rencana rotasi sebelum laga dan laporan pertandingan menunjukkan delapan pergantian starter dibanding laga melawan Irlandia. Pengumuman itu tidak terbaca lengkap dalam pratinjau awal. Beta memakai kekuatan tim dan venue, tanpa masukan susunan pemain. Ini kasus yang layak diuji pada beberapa matchday sebelum rotasi dijadikan filter. [ÖFB](https://www.oefb.at/oefb/News/Nationalteam-Vorschau-ISR-AUT) · [ORF](https://sport.orf.at/stories/3165057)
- **Irlandia 3–0 Kosovo.** Fokus Under 2,5 (61,3%) meleset. Kosovo kehilangan Kreshnik Hajrizi pada menit ke-26 dan Troy Parrott mencetak dua penalti. BTTS Tidak Beta benar karena seluruh gol datang dari Irlandia. Kartu dan penalti tetap tercakup dalam hasil penilaian. [FAI](https://www.fai.ie/latest/report-republic-ireland-3-0-kosovo-great-night-aviva/)
- **Hungaria 1–1 Irlandia Utara.** Under 2,5 benar dan BTTS Tidak meleset. Varga membuka skor di menit ke-35 dan Devenny menyamakan kedudukan di menit ke-65. Rekor lima clean sheet Irlandia Utara berakhir meski laga tetap berjumlah dua gol. [Irish FA](https://www.irishfa.com/news/2026/november/northern-ireland-reach-league-a-with-superb-draw-against-hungary)
- **Denmark 2–3 Norwegia.** BTTS Ya (52,1%) dan Over 2,5 (54,3%) berada di bawah ambang tetap 55% Beta, sehingga keduanya tidak diterbitkan. Utama mengambil kedua pilihan dengan benar. UEFA mencatat Norwegia membalikkan ketertinggalan 0–2 dan Haaland memastikan kemenangan lewat penalti di injury time. [UEFA](https://www.uefa.com/uefanationsleague/news/02ab-22146db70e40-12d581ab82a9-1000--uefa-nations-league-matchday-6-round-up-erling-haaland-tak/)

## Kualitas probabilitas Beta V2

Metrik dihitung pada kedelapan laga, termasuk observasi. Brier 1X2 menjumlahkan galat kuadrat tiga kelas. Brier BTTS dan total memakai probabilitas kejadian positif. Log loss memakai log natural. Sampel ini terlalu kecil untuk menilai kalibrasi jangka panjang.

| Target | Brier | Log loss |
|---|---:|---:|
| 1X2 | 0,6902 | 1,1141 |
| BTTS | 0,2551 | 0,7035 |
| Total 2,5 | 0,2331 | 0,6580 |

Hasil delapan laga ini memberi contoh biaya penyaringan Hybrid. Untuk menguji apakah biaya itu berulang, bandingkan akurasi dan cakupan dengan aturan yang sama pada beberapa matchday berikutnya.
