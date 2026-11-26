# Superanalyst · Evaluasi UCL Matchday 5

**26 November 2026 WIB · Liga Champions 2026/27 · 9/9 hasil akhir terverifikasi.** Skor mencakup 90 menit dan injury time. [Hasil resmi UEFA](https://www.uefa.com/uefachampionsleague/news/02a8-2174c9e9019d-f909a77bd77a-1000--2026-27-champions-league-a/) · [RTÉ Sport](https://www.rte.ie/sport/results/soccer/champions-league/47760/results/)

**Model Utama benar di 6/9 · 66,7% fokus. Dixon–Coles benar di 5/9 · 55,6% dengan fokusnya sendiri.**

## Model Utama dan XI Resmi v1

| Target | Model Utama, 9 laga | Model Utama, 2 laga 00.45 | XI Resmi v1, 2 laga 00.45 |
|---|---:|---:|---:|
| Fokus | 6/9 · 66,7% | 1/2 · 50,0% | 1/2 · 50,0% |
| 1X2 | 4/7 · 57,1% | 1/1 · 100,0% | 1/1 · 100,0% |
| BTTS | 2/7 · 28,6% | 1/2 · 50,0% | 0/1 · 0,0% |
| Over/Under 2,5 | 4/5 · 80,0% | 1/2 · 50,0% | 1/1 · 100,0% |
| Skor tepat | 1/9 · 11,1% | 0/2 · 0,0% | 0/2 · 0,0% |

Penyebut menghitung pilihan aktif. BTTS berarti kedua tim mencetak gol. Arsip XI resmi tersedia untuk dua laga pukul 00.45 WIB.

| WIB | Laga | FT | Fokus Model Utama | Fokus XI Resmi v1 | Fokus Dixon–Coles |
|---|---|:---:|---|---|---|
| 00.45 | Sabah FC – Barcelona | [1–4](https://www.uefa.com/uefachampionsleague/match/2049642--sabah-vs-barcelona/) | Barcelona menang · Relatif kuat ✓ | Barcelona menang · Relatif kuat ✓ | Over 2,5 · 80,5% ✓ |
| 00.45 | Slavia Praha – Villarreal | [0–1](https://www.uefa.com/uefachampionsleague/match/2049641--slavia-praha-vs-villarreal/) | BTTS Ya · Sedang ✗ | BTTS Ya · Rendah ✗ | Over 2,5 · 58,6% ✗ |
| 03.00 | Atlético Madrid – Viking | [2–0](https://www.uefa.com/uefachampionsleague/match/2049636--atleti-vs-viking/) | Atlético menang · Sedang ✓ | — | BTTS Ya · 55,3% ✗ |
| 03.00 | Club Brugge – Liverpool | [0–3](https://www.uefa.com/uefachampionsleague/match/2049638--club-brugge-vs-liverpool/) | Over 2,5 · Relatif kuat ✓ | — | Over 2,5 · 89,3% ✓ |
| 03.00 | Inter – Stuttgart | [2–0](https://www.uefa.com/uefachampionsleague/match/2049635--inter-vs-stuttgart/) | Inter menang · Rendah ✓ | — | Over 2,5 · 67,1% ✗ |
| 03.00 | Lille – Bayern | [2–1](https://www.uefa.com/uefachampionsleague/match/2049639--lille-vs-bayern-munchen/) | Bayern menang · Sedang ✗ | — | Bayern menang · 64,7% ✗ |
| 03.00 | PSG – AS Roma | [2–2](https://www.uefa.com/uefachampionsleague/match/2049634--paris-vs-roma/) | Over 2,5 · Relatif kuat ✓ | — | Over 2,5 · 72,3% ✓ |
| 03.00 | Shakhtar Donetsk – Fenerbahçe | [0–1](https://www.uefa.com/uefachampionsleague/match/2049640--shakhtar-vs-fenerbahce/) | Under 2,5 · Rendah ✓ | — | Under 2,5 · 52,6% ✓ |
| 03.00 | Sporting CP – Manchester United | [2–2](https://www.uefa.com/uefachampionsleague/match/2049637--sporting-cp-vs-man-utd/) | Sporting CP menang · Sedang ✗ | — | Over 2,5 · 68,0% ✓ |

### Dampak XI resmi pukul 00.45 WIB

- **Sabah–Barcelona (1–4).** Fokus Barcelona menang tetap benar. BTTS Ya yang masuk observasi ternyata benar. Over 2,5 tetap benar setelah keyakinannya turun dari sedang ke rendah. Skenario 1–3 dan revisi 0–2 sama-sama meleset.
- **Slavia–Villarreal (0–1).** Fokus BTTS Ya tetap meleset setelah keyakinannya turun dari sedang ke rendah. Over 2,5 yang masuk observasi ternyata meleset. Skenario 2–1 dan revisi 1–1 sama-sama meleset.

## Eksperimen probabilitas

| Varian | Log loss 1X2 | Brier BTTS | Brier Over 0,5 | Brier Over 1,5 | Brier Over 2,5 | Brier Over 3,5 | Arah pada target fokus Model Utama |
|---|---:|---:|---:|---:|---:|---:|---:|
| Poisson kontrol | 1,1707 | 0,2956 | 0,0019 | 0,1542 | 0,2068 | 0,2133 | 5/9 · 55,6% |
| Poisson xG disesuaikan | 1,1138 | 0,2894 | 0,0018 | 0,1462 | 0,1900 | 0,2112 | 5/9 · 55,6% |
| Dixon–Coles | 1,1107 | 0,2844 | 0,0009 | 0,1435 | 0,1900 | 0,2112 | 5/9 · 55,6% |

Log loss dan Brier lebih baik jika nilainya lebih kecil. Pada sembilan laga ini, Dixon–Coles mencatat log loss 1X2 dan Brier BTTS terendah dari ketiga varian.

Kolom terakhir memakai target fokus Model Utama yang dipilih sebelum kickoff. Fokus Dixon–Coles di tabel laga mengambil probabilitas terbesar dari pilihan 1X2, BTTS dan Over/Under 2,5.

## Arsip prediksi

- **Model Utama** dicatat 25 November 2026 pukul 16.31.43 WIB · snapshot `211df5015f454193a50b95802b0ba280`.
- **XI Resmi v1** dicatat 26 November 2026 pukul 00.04.19 WIB · snapshot `69fe13b89aa44d29a2ec866908a45172`.
- **Eksperimen** dicatat 25 November 2026 pukul 16.53.58 WIB · snapshot `abcc10ae7a45`.

Pilihan per target, probabilitas, perubahan XI dan hasil penilaian tersedia di [evaluasi.json](evaluasi.json).
