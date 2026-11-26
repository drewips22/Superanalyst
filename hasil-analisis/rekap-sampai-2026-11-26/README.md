# Rekap akurasi Superanalyst

**Sampai 26 November 2026 WIB.** Model Utama mencakup **111 laga** dengan **66/98 fokus tepat (67,3%)**. Angka itu meliputi 65/97 fokus pada arsip serta satu prioritas chat, yaitu Ekuador menang.

Rekap ini mengambil prediksi dari chat, poster, arsip lokal, dan laporan matchday. Hasil aktual memakai 90 menit termasuk injury time. Penyebut menghitung pilihan yang aktif dan memiliki hasil akhir. Setiap laga Model Utama memakai pilihan awal. [Data rekap dan rujukan sumber](evaluasi.json)

## Model Utama per matchday

| Sesi | Laga | Fokus | 1X2 | BTTS | Over/Under 2,5 | Skor tepat |
|---|---:|---:|---:|---:|---:|---:|
| UNL 13 Nov · pilot awal | 8 | — | 7/8 | 5/6 | 5/6 | 5/8 |
| UNL 14 Nov · poster awal | 10 | 8/10 | 5/7 | 6/8 | 3/5 | 1/10 |
| Persahabatan 14 Nov | 4 | 1/1 | 3/4 | 3/3 | 2/3 | 1/4 |
| UNL 15 Nov · dini hari | 7 | 4/6 | 3/4 | 3/4 | 4/5 | 1/7 |
| UNL 15–16 Nov | 8 | 8/8 | 3/4 | 4/5 | 6/6 | 0/8 |
| UNL 17 Nov | 8 | 6/8 | 5/6 | 2/6 | 3/5 | 1/8 |
| UNL 18 Nov · snapshot awal | 8 | 5/7 | 2/4 | 4/5 | 4/6 | 2/8 |
| Liga Eropa 21 Nov | 19 | 10/19 | 10/14 | 5/12 | 3/10 | 2/19 |
| Liga Eropa 22 Nov | 21 | 14/21 | 9/17 | 10/18 | 10/15 | 1/21 |
| UCL 25 Nov | 9 | 4/9 | 6/8 | 2/5 | 3/6 | 1/9 |
| UCL 26 Nov | 9 | 6/9 | 4/7 | 2/7 | 4/5 | 1/9 |
| **Total** | **111** | **66/98 · 67,3%** | **57/83 · 68,7%** | **46/79 · 58,2%** | **47/72 · 65,3%** | **16/111 · 14,4%** |

Ketiga target aktif menghasilkan **150/234 · 64,1%**. Waktu publikasi sebelum kickoff untuk dua pilihan Argentina–Uruguay belum terverifikasi. Jika dua pilihan itu dikeluarkan, hasilnya **150/232 · 64,7%**.

Sumber utama meliputi [arsip evaluasi](https://github.com/drewips22/Superanalyst/tree/69d78d9870d636944b9b9aac1ba2a5ad0100b54d/hasil-analisis), [pilot UNL](https://github.com/drewips22/Superanalyst/blob/69d78d9870d636944b9b9aac1ba2a5ad0100b54d/skills/superanalyst/references/unl-baseline.md), dan [arsip UNL November](https://github.com/drewips22/Superanalyst/blob/69d78d9870d636944b9b9aac1ba2a5ad0100b54d/test-v2/artifacts/november-posthoc-evaluation.json). Lima hasil akhir liga yang melengkapi arsip sementara tercantum di [evaluasi.json](evaluasi.json).

## Prediksi chat dan analisis live

| Sesi chat umum | 1X2 | Skor tepat |
|---|---:|---:|
| UCL 20–21 Okt | 4/9 | 1/9 |
| UCL 21–22 Okt | 6/9 | 1/9 |
| UCL 5 Nov | 7/9 | 1/9 |
| UNL 13 Nov · chat umum | 6/8 | 3/8 |
| UNL 14 Nov · chat umum | 6/11 | 1/11 |
| **Total** | **29/46 · 63,0%** | **7/46 · 15,2%** |

Arah 1X2 untuk dua sesi Oktober berasal dari skenario skor awal. Prediksi chat umum dapat mencakup laga yang juga dinilai oleh Model Utama. [Hasil UCL UEFA](https://www.uefa.com/uefachampionsleague/news/02a8-2174c9e9019d-f909a77bd77a-1000--2026-27-champions-league-a/) · [Hasil UNL UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/)

- Piala Dunia U-17 19 November mencatat 2/3 · 66,7% prioritas tepat, 8/17 · 47,1% pilihan aktif tepat, dan 0/8 skor tepat. [Hasil Piala Dunia U-17 FIFA](https://www.fifa.com/en/articles/round-up-matchday-one-doha)
- UNL live 16 November mencatat 3/3 pilihan aktif tepat dan 0/4 skor tepat. Dua kejadian pada Belgia–Italia sudah terpenuhi ketika analisis dibuat. [Hasil UNL UEFA](https://www.uefa.com/uefanationsleague/news/02a2-1fea18abbcbc-456e846509e7-1000--2026-27-uefa-nations-league-all-the-league-phase-fixtures/)

## Eksperimen

| Model | Dasar penilaian | Akurasi |
|---|---|---:|
| XI Resmi v1 · UCL | Fokus aktif | 5/10 · 50,0% |
| Poisson kontrol · UCL | Arah untuk target fokus Model Utama | 9/18 · 50,0% |
| Poisson xG disesuaikan · UCL | Arah untuk target fokus Model Utama | 10/18 · 55,6% |
| Dixon–Coles · UCL | Arah untuk target fokus Model Utama | 10/18 · 55,6% |
| Total Gol v1 · UCL 25 Nov | Arah Over/Under 2,5 | 3/9 · 33,3% |
| Poisson liga Eropa | Fokus aktif | 7/13 · 53,8% |
| Poisson UNL · 5 laga | Arah untuk target fokus Model Utama | 4/6 · 66,7% |
| Poisson UNL · 4 laga | Arah untuk target fokus Model Utama | 4/6 · 66,7% |
| Beta lama MC10K | Fokus aktif | 14/23 · 60,9% |
| Beta riset timnas v1 | Fokus aktif | 3/5 · 60,0% |
| Beta V2 | Fokus aktif | 3/5 · 60,0% |
| Hybrid Beta | Fokus aktif | 3/5 · 60,0% |
| Kontrol BTTS | Arah BTTS 22 Nov | 11/21 · 52,4% |
| BTTS kandang/tandang | Arah BTTS 22 Nov | 11/21 · 52,4% |

Pada sepuluh laga UCL dengan fokus aktif di kedua versi, Model Utama dan XI Resmi v1 sama-sama tepat **5/10**. Poisson kontrol, Poisson xG disesuaikan, dan Dixon–Coles memakai target fokus awal Model Utama pada 18 laga UCL. [Evaluasi 25 November](https://github.com/drewips22/Superanalyst/blob/69d78d9870d636944b9b9aac1ba2a5ad0100b54d/hasil-analisis/2026-11-25-ucl-md5/evaluasi.json) · [Evaluasi 26 November](https://github.com/drewips22/Superanalyst/blob/69d78d9870d636944b9b9aac1ba2a5ad0100b54d/hasil-analisis/2026-11-26-ucl-md5/evaluasi.json)

Pada uji UNL 18 November, Model Utama, Beta V2, dan Hybrid masing-masing tepat 3/5 pada lima fokus bersama. Hasil historis Beta V2 dan evaluasi ulang Hybrid tersedia di berkas pengembangan. [Evaluasi UNL 18 November](https://github.com/drewips22/Superanalyst/blob/69d78d9870d636944b9b9aac1ba2a5ad0100b54d/test-v2/forecasts/unl-2026-11-17-18/evaluation/evaluasi-v1.json) · [Laporan pengembangan Beta V2](https://github.com/drewips22/Superanalyst/blob/69d78d9870d636944b9b9aac1ba2a5ad0100b54d/test-v2/Laporan-Pengembangan-Beta-V2.md)

## Struktur data

- `model_utama` memuat rekap per sesi, penyebut tiap metrik, dan pengecualian waktu penerbitan.
- `standalone_chat` dan `other_forecasts` memuat pilihan serta skor akhir yang dapat ditelusuri untuk sesi chat umum, U-17, dan live.
- `experiments` memuat hasil per model dan perbandingan pada laga yang sama. `historical_reference` menyimpan angka dari evaluasi historis.
- `sources` menunjuk laporan dan data yang dipakai. `final_scores_backfilled` mendokumentasikan lima skor yang melengkapi evaluasi liga sebelumnya.

Untuk memperpanjang rekap, catat snapshot dan laga baru dengan waktu kickoff WIB, pertahankan angka arsip ini, lalu hitung kembali pembilang dan penyebut dari pilihan aktif yang sudah memiliki hasil akhir.
