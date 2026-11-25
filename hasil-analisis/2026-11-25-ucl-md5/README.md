# Superanalyst · Evaluasi UCL Matchday 5

**25 November 2026 WIB · Liga Champions 2026/27 · 9/9 hasil akhir terverifikasi UEFA.** Evaluasi dicatat pukul 05.40.02 WIB. Skor mencakup 90 menit dan injury time. [Hasil resmi UEFA](https://www.uefa.com/uefachampionsleague/news/02a8-2174c9e9019d-f909a77bd77a-1000--2026-27-champions-league-all-the-league-phase-f/)

## Model Utama dan XI Resmi v1

**Pada delapan laga dengan fokus di kedua versi, akurasinya sama, 4/8 (50,0%).** Galatasaray–Aston Villa selesai 1–0, sehingga pencabutan BTTS Ya menghapus satu fokus yang salah dari cakupan XI. Cakupan fokus turun dari 9/9 ke 8/9 laga.

| Target | Model Utama | XI Resmi v1 | Model Utama → XI pada laga yang sama |
|---|---:|---:|---:|
| Fokus | 4/9 · 44,4% | 4/8 · 50,0% | 4/8 → 4/8 |
| 1X2 | 6/8 · 75,0% | 6/8 · 75,0% | 6/8 → 6/8 |
| BTTS | 2/5 · 40,0% | 2/4 · 50,0% | 2/4 → 2/4 |
| Over/Under 2,5 | 3/6 · 50,0% | 3/7 · 42,9% | 3/6 → 3/6 |
| Skor tepat | 1/9 · 11,1% | 0/9 · 0,0% | 1/9 → 0/9 |

Observasi dikeluarkan dari penyebut target. Akurasi fokus memakai pilihan yang ditetapkan sebelum kickoff.

| WIB | Laga | FT | Fokus awal | Fokus XI | Skenario skor awal → XI |
|---|---|:---:|---|---|:---:|
| 00.45 | Bodø/Glimt – LASK | [1–0](https://www.uefa.com/uefachampionsleague/match/2049629--bodo-glimt-vs-lask/) | BTTS Ya · Sedang ✗ | BTTS Ya · Sedang ✗ | 2–1 ✗ → 2–1 ✗ |
| 00.45 | Galatasaray – Aston Villa | [1–0](https://www.uefa.com/uefachampionsleague/match/2049631--galatasaray-vs-aston-villa/) | BTTS Ya · Rendah ✗ | Observasi | 1–1 ✗ → 1–1 ✗ |
| 03.00 | Arsenal – Borussia Dortmund | [1–1](https://www.uefa.com/uefachampionsleague/match/2049627--arsenal-vs-b-dortmund/) | Arsenal · Sedang ✗ | Arsenal · Sedang ✗ | 2–1 ✗ → 2–1 ✗ |
| 03.00 | Como – AEK Athens | [1–0](https://www.uefa.com/uefachampionsleague/match/2049633--como-vs-aek-athens/) | Como · Relatif kuat ✓ | Como · Relatif kuat ✓ | 3–1 ✗ → 3–1 ✗ |
| 03.00 | Feyenoord – FC Porto | [0–1](https://www.uefa.com/uefachampionsleague/match/2049628--feyenoord-vs-porto/) | Over 2,5 · Relatif kuat ✗ | Over 2,5 · Sedang ✗ | 1–2 ✗ → 1–2 ✗ |
| 03.00 | Manchester City – Napoli | [2–2](https://www.uefa.com/uefachampionsleague/match/2049626--man-city-vs-napoli/) | Manchester City · Relatif kuat ✗ | Manchester City · Relatif kuat ✗ | 3–0 ✗ → 2–0 ✗ |
| 03.00 | RB Leipzig – Lens | [3–1](https://www.uefa.com/uefachampionsleague/match/2049630--leipzig-vs-lens/) | RB Leipzig · Sedang ✓ | RB Leipzig · Sedang ✓ | 2–1 ✗ → 2–1 ✗ |
| 03.00 | Real Madrid – PSV Eindhoven | [5–1](https://www.uefa.com/uefachampionsleague/match/2049625--real-madrid-vs-psv/) | Real Madrid · Relatif kuat ✓ | Real Madrid · Relatif kuat ✓ | 3–1 ✗ → 3–1 ✗ |
| 03.00 | Slovan Bratislava – Real Betis | [0–2](https://www.uefa.com/uefachampionsleague/match/2049632--s-bratislava-vs-real-betis/) | Real Betis · Relatif kuat ✓ | Real Betis · Relatif kuat ✓ | 0–2 ✓ → 0–3 ✗ |

## Dampak perubahan setelah XI resmi

- **Galatasaray–Aston Villa (1–0).** BTTS Ya · Rendah → Observasi menghapus satu pilihan dan satu fokus yang salah.
- **Feyenoord–Porto (0–1).** Keyakinan BTTS Ya turun Sedang → Rendah dan Over 2,5 turun Relatif kuat → Sedang. Keduanya tetap meleset.
- **Manchester City–Napoli (2–2).** Keyakinan Over 2,5 turun Sedang → Rendah, tetapi Over tembus. Skenario 3–0 dan 2–0 sama-sama meleset.
- **Slovan Bratislava–Real Betis (0–2).** Observasi → Over 2,5 · Rendah menambah satu pilihan yang meleset. Skenario 0–2 yang sebelumnya tepat berubah menjadi 0–3.

## xG disesuaikan dan Dixon–Coles

Ketiga distribusi numerik dinilai pada sembilan laga yang sama. Nilai lebih kecil menunjukkan galat lebih rendah. Probabilitas prapertandingan dipakai dengan presisi arsip.

| Metrik | Poisson kontrol | Poisson xG disesuaikan | Dixon–Coles |
|---|---:|---:|---:|
| 1X2 · log loss | 1,0425 | 1,0269 | 1,0292 |
| BTTS · Brier | 0,2397 | 0,2469 | 0,2422 |
| Over 0,5 · Brier | 0,0013 | 0,0014 | 0,0007 |
| Over 1,5 · Brier | 0,3157 | 0,3104 | 0,3026 |
| Over 2,5 · Brier | 0,3080 | 0,3088 | 0,3088 |
| Over 3,5 · Brier | 0,2031 | 0,2061 | 0,2061 |

Penyesuaian kekuatan lawan menurunkan log loss 1X2 terhadap kontrol. Dixon–Coles mencatat Brier Over 1,5 terendah. Poisson kontrol unggul pada BTTS, Over 2,5, dan Over 3,5. Semua hasil ini berasal dari sembilan laga pada satu matchday.

## Catatan snapshot

- Model Utama, 23/11/2026 05.04.57 WIB. Snapshot `d31c143eaaf34e018627f742449e45d5`.
- XI Resmi 00.45 WIB, 25/11/2026 00.19.04 WIB. Snapshot `f663d15154374ca98dfb705e37673235`.
- XI Resmi 03.00 WIB, 25/11/2026 02.13.32 WIB. Snapshot `de708691a8254ba184b4b5d25034be66`.
- Probabilitas numerik tercatat 24/11/2026 pukul 15.32.45 WIB.
- [Data evaluasi per laga, keputusan, keyakinan, dan probabilitas](evaluasi.json).
