# Analisis yang dibekukan sebelum tahap penilaian

Sembilan laga pada **5 November 2026 WIB / 4 November Eropa**. Cutoff informasi **4 November 19.00 WIB (12:00 UTC)**. Dibuat sekarang sebagai rekonstruksi; hasil sudah terekspos, jadi bukan uji buta. Halaman historis tidak memiliki arsip versi asli yang lengkap.

Model tetap: λ kandang = (GF kandang lima laga + GA tandang lima laga)/10; λ tandang simetris. Gol Poisson independen; tanpa bobot tambahan untuk kandang, cedera, motivasi, H2H, xG, atau pasar. Ambang BTTS/Over 2,5 adalah 50%; 1X2 memilih peluang terbesar. Semua angka provisional dan belum terkalibrasi.

Prediksi memakai lima laga kompetitif seluruh kompetisi, 90 menit + injury time. Adu penalti tidak dihitung sebagai kemenangan 90 menit. Rekaman skor target tidak dibaca oleh jalur prediksi.

## Batas cakupan

- 90 team-match observations; shared historical fixtures appear for both teams and are not independent samples.
- Score data: ESPN plus explicit domestic supplements; statistics left missing for supplements to avoid unharmonized provider means.
- No consistent five-match xG series was obtained: all xG values remain null. This tests the goal-only baseline, not the full skill.
- Target results were exposed by the user's image, verification snippets and dynamic result headers on otherwise dated preview pages. No target scores, incidents or lineups enter these features.
- Original versions of live API/website data are not archived; calendar dates before cutoff are necessary but not proof of point-in-time availability.
- No prices/liquidity snapshots from three independent sources; the last-30-minute market rule is outside the common 12:00 UTC cutoff and is not tested.
- No verified travel route, role-weighted absence model, standings-based intensity measurement, pressing/crossing event model or season-adjusted opponent-strength estimate.

Dua flag `both_conceded_ge4of5` dan `both_low_clean_sheet` ekuivalen secara matematis pada jendela lima laga; jangan menghitungnya sebagai dua bukti terpisah. Gol menit akhir bukan ukuran intensitas pressing/tembakan.

## AEK Athens — Real Madrid

### Data

**AEK Athens**. Urutan tertua → terbaru; skor dari sudut tim.

| Tanggal | Lawan | Venue | Skor 90m | Tembakan | xG/xGA | Sumber |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-10-14 | Shakhtar Donetsk | away | 1–3 | 13 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401915406) |
| 2026-10-20 | Manchester City | away | 1–5 | 11 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401915401) |
| 2026-10-24 | Panetolikos | home | 5–0 | 26 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401896744) |
| 2026-10-28 | PAOK | away | 1–3 | N/A | N/A | [data](https://www.365scores.com/football/match/greece-cup-87/aek-athens-paok-1024-1029-87) |
| 2026-11-01 | Panathinaikos | away | 0–2 | 15 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401896736) |

GF **8**; GA/laga **2.60**; hasil **L-L-W-L-L**; PPG **0.60**. Clean sheet **1/5**; BTTS **3/5**. Tembakan rerata 16.2 (cakupan 4/5); xG 0/5. Perubahan PPG 3 laga terbaru vs 2 sebelumnya +1.00; ini tren hasil, bukan tren xG.

Gol 76–90+: cetak 1, kebobolan 3; hanya 4/5 laga dengan event lengkap.

**Real Madrid**. Urutan tertua → terbaru; skor dari sudut tim.

| Tanggal | Lawan | Venue | Skor 90m | Tembakan | xG/xGA | Sumber |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-10-14 | AS Roma | away | 4–3 | 16 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401915414) |
| 2026-10-18 | Sevilla | home | 4–1 | 15 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401882839) |
| 2026-10-21 | RB Leipzig | home | 4–1 | 18 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401915313) |
| 2026-10-25 | Barcelona | away | 2–1 | 10 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401882832) |
| 2026-11-01 | Racing Santander | away | 3–0 | 22 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401882819) |

GF **17**; GA/laga **1.20**; hasil **W-W-W-W-W**; PPG **3.00**. Clean sheet **1/5**; BTTS **4/5**. Tembakan rerata 16.2 (cakupan 5/5); xG 0/5. Perubahan PPG 3 laga terbaru vs 2 sebelumnya +0.00; ini tren hasil, bukan tren xG.

Gol 76–90+: cetak 7, kebobolan 2; hanya 5/5 laga dengan event lengkap.

### Pola dan konteks sebelum cutoff

H2H empat laga (1985 dan 2002): masing-masing satu menang, dua seri; bobot sangat rendah karena usang. AEK W10-D1-L1 pada 12 laga kandang Eropa; Madrid tiga kemenangan dari tiga laga UCL.

[UEFA, 2026-10-29](https://www.uefa.com/uefachampionsleague/news/02aa-21f1e3404d4f-9a655a026d64-1000--champions-league-matchday-4-aek-athens-vs-real-madrid-facts/).

Laporan pralaga: Strakosha absen; Joao Mario dan Rota diragukan. Madrid tanpa Rodrygo dan Asencio, Valverde kembali berlatih. Status ini laporan media, belum daftar resmi pada cutoff. Empat kekalahan AEK dalam lima laga cocok setelah laga piala yang hilang dilengkapi. [Laporan, pembaruan 2026-11-03](https://www.sportsmole.co.uk/football/real-madrid/champions-league/preview/aek-athens-vs-real-madrid-prediction-team-news-lineups_608272.html).

Line-up resmi belum digunakan. Motivasi dikaji sebagai kebutuhan poin fase liga, tanpa bonus intensitas/top-4. Jarak aktual, pola crossing/set piece/pressing dan tiga sumber pasar belum lengkap. Anomali pasar 30 menit sebelum kickoff berada setelah cutoff ini dan tidak dinilai.

Flag yang ditetapkan sebelum penilaian: `{"both_scored_ge4of5": true, "both_conceded_ge4of5": true, "both_low_clean_sheet": true, "one_high_clean_sheet": false, "both_historical_btts_majority": true, "away_model_favourite": true, "both_shots_12_to_15": null}`.

### Keputusan provisional

1 **15.1%** / X **15.1%** / 2 **69.8%**; pilihan **away**. BTTS **71.6%** (ya); Over 2,5 **81.5%** (ya).

λ 1.40–3.00. Estimasi clean sheet laga ini 5.0% / 24.7%; berbeda dari frekuensi historis di atas.

Perubahan XI, kondisi pemain atau kekuatan lawan yang tidak tertangkap gol lima laga dapat mengubah penilaian; belum diberi penyesuaian numerik. Analisis adalah bahan pertimbangan, bukan hasil mutlak.

## Fenerbahce — Liverpool

### Data

**Fenerbahce**. Urutan tertua → terbaru; skor dari sudut tim.

| Tanggal | Lawan | Venue | Skor 90m | Tembakan | xG/xGA | Sumber |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-10-14 | Aston Villa | away | 0–6 | 15 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401915409) |
| 2026-10-17 | Alanyaspor | home | 3–0 | 24 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401888273) |
| 2026-10-20 | Slavia Prague | home | 2–2 | 15 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401915403) |
| 2026-10-26 | Galatasaray | away | 1–2 | 4 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401888265) |
| 2026-10-31 | Goztepe | home | 1–2 | 18 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401888258) |

GF **7**; GA/laga **2.40**; hasil **L-W-D-L-L**; PPG **0.80**. Clean sheet **1/5**; BTTS **3/5**. Tembakan rerata 15.2 (cakupan 5/5); xG 0/5. Perubahan PPG 3 laga terbaru vs 2 sebelumnya -1.17; ini tren hasil, bukan tren xG.

Gol 76–90+: cetak 1, kebobolan 4; hanya 5/5 laga dengan event lengkap.

**Liverpool**. Urutan tertua → terbaru; skor dari sudut tim.

| Tanggal | Lawan | Venue | Skor 90m | Tembakan | xG/xGA | Sumber |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-10-17 | Brentford | away | 2–1 | 21 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401879262) |
| 2026-10-20 | Villarreal | home | 4–3 | 22 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401915397) |
| 2026-10-25 | Brighton & Hove Albion | home | 2–0 | 13 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401878765) |
| 2026-10-28 | Chelsea | home | 1–1 | 10 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401921842) |
| 2026-11-01 | Arsenal | home | 0–1 | 17 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401879246) |

GF **9**; GA/laga **1.20**; hasil **W-W-W-D-L**; PPG **2.00**. Clean sheet **1/5**; BTTS **3/5**. Tembakan rerata 16.6 (cakupan 5/5); xG 0/5. Perubahan PPG 3 laga terbaru vs 2 sebelumnya -1.67; ini tren hasil, bukan tren xG.

Gol 76–90+: cetak 0, kebobolan 1; hanya 5/5 laga dengan event lengkap.

### Pola dan konteks sebelum cutoff

Pertemuan pertama. Liverpool menang tiga laga UCL; Fenerbahce belum menang sembilan laga UCL. Dirk Kuyt menjadi pelatih interim pada 28 Oktober: jendela lima laga melintasi pergantian pelatih. Rekor historis Liverpool di Turki buruk, tetapi sampelnya kecil dan lintas era.

[UEFA, 2026-10-29](https://www.uefa.com/uefachampionsleague/news/02aa-21f1da098d6d-779ef87732a5-1000--champions-league-matchday-4-fenerbahce-vs-liverpool-facts/).

Laporan pralaga mencantumkan Asensio, Oosterwolde, Oppong absen; Ake diragukan. Liverpool: Frimpong, Leoni, Bradley, Ekitike, Gravenberch absen. Besarnya efek tiap pemain belum ditaksir; lima nama tidak otomatis berarti minus 22%. [Laporan, pembaruan 2026-11-03](https://www.sportsmole.co.uk/football/fenerbahce/champions-league/team-news/fenerbahce-vs-liverpool-injury-suspension-list-predicted-xis_608295.html).

Line-up resmi belum digunakan. Motivasi dikaji sebagai kebutuhan poin fase liga, tanpa bonus intensitas/top-4. Jarak aktual, pola crossing/set piece/pressing dan tiga sumber pasar belum lengkap. Anomali pasar 30 menit sebelum kickoff berada setelah cutoff ini dan tidak dinilai.

Flag yang ditetapkan sebelum penilaian: `{"both_scored_ge4of5": true, "both_conceded_ge4of5": true, "both_low_clean_sheet": true, "one_high_clean_sheet": false, "both_historical_btts_majority": true, "away_model_favourite": true, "both_shots_12_to_15": false}`.

### Keputusan provisional

1 **23.3%** / X **20.9%** / 2 **55.8%**; pilihan **away**. BTTS **63.8%** (ya); Over 2,5 **66.0%** (ya).

λ 1.30–2.10. Estimasi clean sheet laga ini 12.2% / 27.3%; berbeda dari frekuensi historis di atas.

Perubahan XI, kondisi pemain atau kekuatan lawan yang tidak tertangkap gol lima laga dapat mengubah penilaian; belum diberi penyesuaian numerik. Analisis adalah bahan pertimbangan, bukan hasil mutlak.

## Borussia Dortmund — Real Betis

### Data

**Borussia Dortmund**. Urutan tertua → terbaru; skor dari sudut tim.

| Tanggal | Lawan | Venue | Skor 90m | Tembakan | xG/xGA | Sumber |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-10-17 | 1. FC Union Berlin | away | 0–0 | 12 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401884769) |
| 2026-10-20 | Sabah FK | away | 2–1 | 22 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401915404) |
| 2026-10-24 | Eintracht Frankfurt | home | 1–0 | 18 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401884763) |
| 2026-10-27 | Werder Bremen | home | 3–2 | 12 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401917030) |
| 2026-10-31 | Bayern Munich | away | 2–2 | 12 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401884754) |

GF **8**; GA/laga **1.00**; hasil **D-W-W-W-D**; PPG **2.20**. Clean sheet **2/5**; BTTS **3/5**. Tembakan rerata 15.2 (cakupan 5/5); xG 0/5. Perubahan PPG 3 laga terbaru vs 2 sebelumnya +0.33; ini tren hasil, bukan tren xG.

Gol 76–90+: cetak 3, kebobolan 0; hanya 5/5 laga dengan event lengkap.

**Real Betis**. Urutan tertua → terbaru; skor dari sudut tim.

| Tanggal | Lawan | Venue | Skor 90m | Tembakan | xG/xGA | Sumber |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-10-14 | FC Porto | home | 3–2 | 17 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401915408) |
| 2026-10-17 | Barcelona | home | 2–5 | 6 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401882846) |
| 2026-10-21 | Feyenoord Rotterdam | home | 1–0 | 23 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401915389) |
| 2026-10-25 | Celta Vigo | away | 0–0 | 15 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401882833) |
| 2026-10-31 | Málaga | home | 2–1 | 23 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401882825) |

GF **8**; GA/laga **1.60**; hasil **W-L-W-D-W**; PPG **2.00**. Clean sheet **2/5**; BTTS **3/5**. Tembakan rerata 16.8 (cakupan 5/5); xG 0/5. Perubahan PPG 3 laga terbaru vs 2 sebelumnya +0.83; ini tren hasil, bukan tren xG.

Gol 76–90+: cetak 1, kebobolan 1; hanya 5/5 laga dengan event lengkap.

### Pola dan konteks sebelum cutoff

Pertemuan pertama. Dortmund W15-D7-L2 pada 24 laga kandang UCL; Betis menang tiga laga pertama UCL. Kekuatan kandang dan hasil UCL memberi sinyal yang berlawanan.

[UEFA, 2026-10-29](https://www.uefa.com/uefachampionsleague/news/02aa-21f1de7f45fc-cdaf195b2b31-1000--champions-league-matchday-4-borussia-dortmund-vs-real-betis-/).

Laporan pralaga: Dortmund tanpa Kaua Prates; Betis tanpa Cucho Hernandez dan Junior Firpo. XI masih perkiraan, tidak digunakan sebagai susunan resmi. [Laporan, pembaruan 2026-11-03](https://www.sportsmole.co.uk/football/betis/champions-league/preview/dortmund-vs-betis-prediction-team-news-lineups_608279.html).

Line-up resmi belum digunakan. Motivasi dikaji sebagai kebutuhan poin fase liga, tanpa bonus intensitas/top-4. Jarak aktual, pola crossing/set piece/pressing dan tiga sumber pasar belum lengkap. Anomali pasar 30 menit sebelum kickoff berada setelah cutoff ini dan tidak dinilai.

Flag yang ditetapkan sebelum penilaian: `{"both_scored_ge4of5": true, "both_conceded_ge4of5": false, "both_low_clean_sheet": false, "one_high_clean_sheet": false, "both_historical_btts_majority": true, "away_model_favourite": false, "both_shots_12_to_15": false}`.

### Keputusan provisional

1 **44.4%** / X **24.5%** / 2 **31.1%**; pilihan **home**. BTTS **58.1%** (ya); Over 2,5 **55.4%** (ya).

λ 1.60–1.30. Estimasi clean sheet laga ini 27.3% / 20.2%; berbeda dari frekuensi historis di atas.

Perubahan XI, kondisi pemain atau kekuatan lawan yang tidak tertangkap gol lima laga dapat mengubah penilaian; belum diberi penyesuaian numerik. Analisis adalah bahan pertimbangan, bukan hasil mutlak.

## FC Porto — Napoli

### Data

**FC Porto**. Urutan tertua → terbaru; skor dari sudut tim.

| Tanggal | Lawan | Venue | Skor 90m | Tembakan | xG/xGA | Sumber |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-10-14 | Real Betis | away | 2–3 | 11 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401915408) |
| 2026-10-20 | PSV Eindhoven | home | 0–1 | 14 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401915398) |
| 2026-10-24 | Gil Vicente | away | 1–0 | 12 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401885417) |
| 2026-10-28 | Academico Viseu | home | 1–0 | N/A | N/A | [data](https://flashsportapp.com/en/football/match/fc-porto-academico-viseu-2026-10-28-1589437/) |
| 2026-10-31 | Estoril | home | 4–0 | 24 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401885404) |

GF **8**; GA/laga **0.80**; hasil **L-L-W-W-W**; PPG **1.80**. Clean sheet **3/5**; BTTS **1/5**. Tembakan rerata 15.2 (cakupan 4/5); xG 0/5. Perubahan PPG 3 laga terbaru vs 2 sebelumnya +3.00; ini tren hasil, bukan tren xG.

Gol 76–90+: cetak 0, kebobolan 1; hanya 4/5 laga dengan event lengkap.

**Napoli**. Urutan tertua → terbaru; skor dari sudut tim.

| Tanggal | Lawan | Venue | Skor 90m | Tembakan | xG/xGA | Sumber |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-10-17 | Venezia | away | 0–1 | 29 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401874760) |
| 2026-10-20 | Bodo/Glimt | home | 4–3 | 17 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401915400) |
| 2026-10-24 | AS Roma | home | 3–3 | 15 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401874948) |
| 2026-10-28 | Monza | away | 4–1 | 16 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401874799) |
| 2026-11-01 | Juventus | away | 0–2 | 8 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401874949) |

GF **11**; GA/laga **2.00**; hasil **L-W-D-W-L**; PPG **1.40**. Clean sheet **0/5**; BTTS **3/5**. Tembakan rerata 17.0 (cakupan 5/5); xG 0/5. Perubahan PPG 3 laga terbaru vs 2 sebelumnya -0.17; ini tren hasil, bukan tren xG.

Gol 76–90+: cetak 2, kebobolan 3; hanya 5/5 laga dengan event lengkap.

### Pola dan konteks sebelum cutoff

H2H dua tie: Napoli menang dua kali 1-0 pada 1974; Porto 1-0 dan 2-2 pada 2014. Porto kalah empat laga Eropa beruntun; Napoli tidak menang tujuh laga tandang UCL (D1-L6). Jangan menilai hanya nama besar atau hasil domestik.

[UEFA, 2026-10-29](https://www.uefa.com/uefachampionsleague/news/02aa-21f247ff9ab6-c7c38d19e243-1000--champions-league-matchday-4-porto-vs-napoli-facts/).

Laporan pagi pralaga menyebut Napoli hanya memiliki 13 pemain lapangan, Hojlund pulih dan De Bruyne diragukan. Delapan nama disebut cedera: Alisson Santos, Favasuli, Neres, Badiashile, Spinazzola, Lobotka, Di Lorenzo, Olivera. Artikel mengandung ketidakkonsistenan narasi dengan perkiraan gelandang; XI dan jumlah pasti tidak dijadikan fitur numerik. [Laporan, pembaruan 2026-11-04T09:32:00+01:00](https://football-italia.net/champions-league-porto-v-napoli-line-ups-tv/).

Line-up resmi belum digunakan. Motivasi dikaji sebagai kebutuhan poin fase liga, tanpa bonus intensitas/top-4. Jarak aktual, pola crossing/set piece/pressing dan tiga sumber pasar belum lengkap. Anomali pasar 30 menit sebelum kickoff berada setelah cutoff ini dan tidak dinilai.

Flag yang ditetapkan sebelum penilaian: `{"both_scored_ge4of5": false, "both_conceded_ge4of5": false, "both_low_clean_sheet": false, "one_high_clean_sheet": true, "both_historical_btts_majority": false, "away_model_favourite": false, "both_shots_12_to_15": null}`.

### Keputusan provisional

1 **44.9%** / X **22.8%** / 2 **32.3%**; pilihan **home**. BTTS **64.8%** (ya); Over 2,5 **64.1%** (ya).

λ 1.80–1.50. Estimasi clean sheet laga ini 22.3% / 16.5%; berbeda dari frekuensi historis di atas.

Perubahan XI, kondisi pemain atau kekuatan lawan yang tidak tertangkap gol lima laga dapat mengubah penilaian; belum diberi penyesuaian numerik. Analisis adalah bahan pertimbangan, bukan hasil mutlak.

## Lens — Como

### Data

**Lens**. Urutan tertua → terbaru; skor dari sudut tim.

| Tanggal | Lawan | Venue | Skor 90m | Tembakan | xG/xGA | Sumber |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Sporting CP | home | 0–2 | 21 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401915418) |
| 2026-10-17 | Troyes | away | 3–1 | 13 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401876431) |
| 2026-10-21 | Club Brugge | away | 0–3 | 19 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401915388) |
| 2026-10-24 | Paris FC | home | 2–1 | 9 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401876427) |
| 2026-10-30 | Lille | away | 0–1 | 5 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401876420) |

GF **5**; GA/laga **1.60**; hasil **L-W-L-W-L**; PPG **1.20**. Clean sheet **0/5**; BTTS **2/5**. Tembakan rerata 13.4 (cakupan 5/5); xG 0/5. Perubahan PPG 3 laga terbaru vs 2 sebelumnya -0.50; ini tren hasil, bukan tren xG.

Gol 76–90+: cetak 1, kebobolan 1; hanya 5/5 laga dengan event lengkap.

**Como**. Urutan tertua → terbaru; skor dari sudut tim.

| Tanggal | Lawan | Venue | Skor 90m | Tembakan | xG/xGA | Sumber |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Fiorentina | away | 3–1 | 16 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401874774) |
| 2026-10-21 | Manchester United | home | 4–1 | 11 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401915395) |
| 2026-10-24 | Sassuolo | home | 2–0 | 14 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401874961) |
| 2026-10-27 | Torino | away | 3–1 | 18 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401874786) |
| 2026-11-01 | Venezia | home | 1–0 | 19 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401875002) |

GF **13**; GA/laga **0.60**; hasil **W-W-W-W-W**; PPG **3.00**. Clean sheet **2/5**; BTTS **3/5**. Tembakan rerata 15.6 (cakupan 5/5); xG 0/5. Perubahan PPG 3 laga terbaru vs 2 sebelumnya +0.00; ini tren hasil, bukan tren xG.

Gol 76–90+: cetak 4, kebobolan 1; hanya 5/5 laga dengan event lengkap.

### Pola dan konteks sebelum cutoff

Pertemuan pertama. Lens tanpa clean sheet dalam 16 laga UCL dan kebobolan lebih dulu pada 11/12. Como mencetak gol lebih dulu di ketiga laga UCL; dua kemenangan kandang 4-1, satu kekalahan tandang 2-3. Ini mendukung potensi gol Como, bukan skor ekstrem tertentu.

[UEFA, 2026-10-29](https://www.uefa.com/uefachampionsleague/news/02aa-21f2406c63cc-0217bb294013-1000--champions-league-matchday-4-lens-vs-como-facts/).

Ketersediaan pemain belum terverifikasi dari versi berita yang lolos cutoff; tidak diasumsikan skuad lengkap.

Preview Lens-Como ditemukan dengan pembaruan 4 November 13:45, melewati cutoff 12:00 UTC; status cedera tidak diambil dari versi itu.

Line-up resmi belum digunakan. Motivasi dikaji sebagai kebutuhan poin fase liga, tanpa bonus intensitas/top-4. Jarak aktual, pola crossing/set piece/pressing dan tiga sumber pasar belum lengkap. Anomali pasar 30 menit sebelum kickoff berada setelah cutoff ini dan tidak dinilai.

Flag yang ditetapkan sebelum penilaian: `{"both_scored_ge4of5": false, "both_conceded_ge4of5": false, "both_low_clean_sheet": false, "one_high_clean_sheet": false, "both_historical_btts_majority": false, "away_model_favourite": true, "both_shots_12_to_15": false}`.

### Keputusan provisional

1 **13.1%** / X **19.4%** / 2 **67.4%**; pilihan **away**. BTTS **48.3%** (tidak); Over 2,5 **55.4%** (ya).

λ 0.80–2.10. Estimasi clean sheet laga ini 12.2% / 44.9%; berbeda dari frekuensi historis di atas.

Perubahan XI, kondisi pemain atau kekuatan lawan yang tidak tertangkap gol lima laga dapat mengubah penilaian; belum diberi penyesuaian numerik. Analisis adalah bahan pertimbangan, bukan hasil mutlak.

## PSV Eindhoven — Club Brugge

### Data

**PSV Eindhoven**. Urutan tertua → terbaru; skor dari sudut tim.

| Tanggal | Lawan | Venue | Skor 90m | Tembakan | xG/xGA | Sumber |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-10-13 | RB Leipzig | away | 0–1 | 11 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401915434) |
| 2026-10-17 | ADO Den Haag | away | 1–2 | 15 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401875582) |
| 2026-10-20 | FC Porto | away | 1–0 | 18 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401915398) |
| 2026-10-25 | Feyenoord Rotterdam | home | 1–1 | 19 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401875568) |
| 2026-10-31 | Willem II | home | 7–0 | 20 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401875564) |

GF **10**; GA/laga **0.80**; hasil **L-L-W-D-W**; PPG **1.40**. Clean sheet **2/5**; BTTS **2/5**. Tembakan rerata 16.6 (cakupan 5/5); xG 0/5. Perubahan PPG 3 laga terbaru vs 2 sebelumnya +2.33; ini tren hasil, bukan tren xG.

Gol 76–90+: cetak 2, kebobolan 1; hanya 5/5 laga dengan event lengkap.

**Club Brugge**. Urutan tertua → terbaru; skor dari sudut tim.

| Tanggal | Lawan | Venue | Skor 90m | Tembakan | xG/xGA | Sumber |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Internazionale | away | 4–3 | 18 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401915413) |
| 2026-10-17 | Sporting Lokeren | home | 1–0 | N/A | N/A | [data](https://www.voetbalprimeur.be/wedstrijden/2026-10-17/club-brugge-vs-sc-lokeren-temse/wedstrijd) |
| 2026-10-21 | Lens | home | 3–0 | 11 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401915388) |
| 2026-10-25 | Sint-Truidense | home | 3–2 | 12 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401878964) |
| 2026-10-30 | Zulte-Waregem | away | 4–2 | 17 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401878956) |

GF **15**; GA/laga **1.40**; hasil **W-W-W-W-W**; PPG **3.00**. Clean sheet **2/5**; BTTS **3/5**. Tembakan rerata 14.5 (cakupan 4/5); xG 0/5. Perubahan PPG 3 laga terbaru vs 2 sebelumnya +0.00; ini tren hasil, bukan tren xG.

Gol 76–90+: cetak 1, kebobolan 3; hanya 4/5 laga dengan event lengkap.

### Pola dan konteks sebelum cutoff

Pertemuan pertama. PSV mencetak gol pada 21 laga kandang Eropa berturut-turut; Brugge kebobolan pada 11 laga tandang UCL berturut-turut. Sebanyak 18 laga UCL terakhir Brugge menghasilkan tiga gol atau lebih. Sampel panjang ini tetap tidak memberi kepastian.

[UEFA, 2026-10-29](https://www.uefa.com/uefachampionsleague/news/02aa-21f1d4d07022-d86866ad160c-1000--champions-league-matchday-4-psv-eindhoven-vs-club-brugge-/).

Laporan pralaga: PSV tanpa Ouaissa, Plea, Schouten; Wanner dan Lammers perlu pemeriksaan. Brugge tanpa Ordonez. Tiga pemain atau lebih absen tidak menjadi koefisien tetap. Kemenangan PSV 7-0 hanya satu dari lima observasi. [Laporan, pembaruan 2026-11-03](https://www.sportsmole.co.uk/football/psv-eindhoven/champions-league/preview/psv-vs-brugge-prediction-team-news-lineups_608251.html).

Line-up resmi belum digunakan. Motivasi dikaji sebagai kebutuhan poin fase liga, tanpa bonus intensitas/top-4. Jarak aktual, pola crossing/set piece/pressing dan tiga sumber pasar belum lengkap. Anomali pasar 30 menit sebelum kickoff berada setelah cutoff ini dan tidak dinilai.

Flag yang ditetapkan sebelum penilaian: `{"both_scored_ge4of5": true, "both_conceded_ge4of5": false, "both_low_clean_sheet": false, "one_high_clean_sheet": false, "both_historical_btts_majority": false, "away_model_favourite": true, "both_shots_12_to_15": null}`.

### Keputusan provisional

1 **35.0%** / X **21.8%** / 2 **43.1%**; pilihan **away**. BTTS **69.5%** (ya); Over 2,5 **69.7%** (ya).

λ 1.70–1.90. Estimasi clean sheet laga ini 15.0% / 18.3%; berbeda dari frekuensi historis di atas.

Perubahan XI, kondisi pemain atau kekuatan lawan yang tidak tertangkap gol lima laga dapat mengubah penilaian; belum diberi penyesuaian numerik. Analisis adalah bahan pertimbangan, bukan hasil mutlak.

## RB Leipzig — Manchester City

### Data

**RB Leipzig**. Urutan tertua → terbaru; skor dari sudut tim.

| Tanggal | Lawan | Venue | Skor 90m | Tembakan | xG/xGA | Sumber |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-10-17 | Bayern Munich | away | 1–6 | 12 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401884772) |
| 2026-10-21 | Real Madrid | away | 1–4 | 11 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401915313) |
| 2026-10-24 | SV Elversberg | home | 4–0 | 13 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401884762) |
| 2026-10-27 | Rot-Weiss Essen | away | 2–1 | 11 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401917027) |
| 2026-10-31 | Schalke 04 | away | 2–0 | 18 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401884747) |

GF **10**; GA/laga **2.20**; hasil **L-L-W-W-W**; PPG **1.80**. Clean sheet **2/5**; BTTS **3/5**. Tembakan rerata 13.0 (cakupan 5/5); xG 0/5. Perubahan PPG 3 laga terbaru vs 2 sebelumnya +3.00; ini tren hasil, bukan tren xG.

Gol 76–90+: cetak 7, kebobolan 2; hanya 5/5 laga dengan event lengkap.

**Manchester City**. Urutan tertua → terbaru; skor dari sudut tim.

| Tanggal | Lawan | Venue | Skor 90m | Tembakan | xG/xGA | Sumber |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-10-17 | Ipswich Town | home | 3–2 | 19 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401879259) |
| 2026-10-20 | AEK Athens | home | 5–1 | 17 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401915401) |
| 2026-10-24 | Aston Villa | away | 1–2 | 15 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401879256) |
| 2026-10-28 | Brighton & Hove Albion | home | 2–2 | 13 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401921834) |
| 2026-10-31 | Brighton & Hove Albion | home | 0–1 | 21 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401879245) |

GF **11**; GA/laga **1.60**; hasil **W-W-L-D-L**; PPG **1.40**. Clean sheet **0/5**; BTTS **4/5**. Tembakan rerata 17.0 (cakupan 5/5); xG 0/5. Perubahan PPG 3 laga terbaru vs 2 sebelumnya -2.67; ini tren hasil, bukan tren xG.

Gol 76–90+: cetak 1, kebobolan 1; hanya 5/5 laga dengan event lengkap.

### Pola dan konteks sebelum cutoff

H2H dan kabar pemain belum dibuktikan dari versi sumber yang lolos cutoff. Preview yang ditemukan diperbarui 5 November, sehingga dikeluarkan. Lima hasil terakhir menunjukkan Leipzig bangkit tiga kemenangan, City tanpa kemenangan 90 menit dalam tiga laga terbaru; kekuatan lawan berbeda.

Ketersediaan pemain belum terverifikasi dari versi berita yang lolos cutoff; tidak diasumsikan skuad lengkap.

Line-up resmi belum digunakan. Motivasi dikaji sebagai kebutuhan poin fase liga, tanpa bonus intensitas/top-4. Jarak aktual, pola crossing/set piece/pressing dan tiga sumber pasar belum lengkap. Anomali pasar 30 menit sebelum kickoff berada setelah cutoff ini dan tidak dinilai.

Flag yang ditetapkan sebelum penilaian: `{"both_scored_ge4of5": true, "both_conceded_ge4of5": false, "both_low_clean_sheet": false, "one_high_clean_sheet": false, "both_historical_btts_majority": true, "away_model_favourite": true, "both_shots_12_to_15": false}`.

### Keputusan provisional

1 **32.2%** / X **20.3%** / 2 **47.5%**; pilihan **away**. BTTS **74.2%** (ya); Over 2,5 **76.2%** (ya).

λ 1.80–2.20. Estimasi clean sheet laga ini 11.1% / 16.5%; berbeda dari frekuensi historis di atas.

Perubahan XI, kondisi pemain atau kekuatan lawan yang tidak tertangkap gol lima laga dapat mengubah penilaian; belum diberi penyesuaian numerik. Analisis adalah bahan pertimbangan, bukan hasil mutlak.

## Slavia Prague — Arsenal

### Data

**Slavia Prague**. Urutan tertua → terbaru; skor dari sudut tim.

| Tanggal | Lawan | Venue | Skor 90m | Tembakan | xG/xGA | Sumber |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-10-17 | Hradec Kralove | home | 0–0 | N/A | N/A | [data](https://www.betexplorer.com/football/team/slavia-prague/viXGgnyB/results/) |
| 2026-10-20 | Fenerbahce | away | 2–2 | 15 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401915403) |
| 2026-10-24 | Mlada Boleslav | home | 1–1 | N/A | N/A | [data](https://www.betexplorer.com/football/team/slavia-prague/viXGgnyB/results/) |
| 2026-10-27 | Brno | home | 4–0 | N/A | N/A | [data](https://www.betexplorer.com/football/team/slavia-prague/viXGgnyB/results/) |
| 2026-10-31 | Jablonec | away | 5–0 | N/A | N/A | [data](https://www.betexplorer.com/football/team/slavia-prague/viXGgnyB/results/) |

GF **12**; GA/laga **0.60**; hasil **D-D-D-W-W**; PPG **1.80**. Clean sheet **3/5**; BTTS **2/5**. Tembakan rerata 15.0 (cakupan 1/5); xG 0/5. Perubahan PPG 3 laga terbaru vs 2 sebelumnya +1.33; ini tren hasil, bukan tren xG.

Gol 76–90+: cetak 1, kebobolan 0; hanya 1/5 laga dengan event lengkap.

**Arsenal**. Urutan tertua → terbaru; skor dari sudut tim.

| Tanggal | Lawan | Venue | Skor 90m | Tembakan | xG/xGA | Sumber |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Nottingham Forest | away | 1–0 | 9 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401878769) |
| 2026-10-21 | Bayern Munich | away | 2–2 | 14 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401915312) |
| 2026-10-24 | Everton | home | 2–0 | 20 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401878768) |
| 2026-10-27 | Fleetwood Town | away | 1–1 | 26 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401921835) |
| 2026-11-01 | Liverpool | away | 1–0 | 10 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401879246) |

GF **7**; GA/laga **0.60**; hasil **W-D-W-D-W**; PPG **2.20**. Clean sheet **3/5**; BTTS **2/5**. Tembakan rerata 15.8 (cakupan 5/5); xG 0/5. Perubahan PPG 3 laga terbaru vs 2 sebelumnya +0.33; ini tren hasil, bukan tren xG.

Gol 76–90+: cetak 2, kebobolan 0; hanya 5/5 laga dengan event lengkap.

### Pola dan konteks sebelum cutoff

Arsenal belum kalah dalam lima H2H (W3-D2), termasuk 3-0 di Praha pada 2025; Slavia tanpa gol pada tiga laga kandang H2H. Slavia tanpa kemenangan pada 18 laga Eropa; tren domestik yang kuat perlu dipisahkan dari level lawan UCL.

[UEFA, 2026-10-29](https://www.uefa.com/uefachampionsleague/news/02aa-21f243b9af8c-03bb9fc28b53-1000--champions-league-matchday-4-slavia-praha-vs-arsenal-facts/).

Laporan pralaga: Slavia tanpa Chory (skorsing), Ogbu, Kante, Pitak; beberapa pemain diragukan. Arsenal tanpa Saka, Eze diragukan. Belum susunan resmi. [Laporan, pembaruan 2026-11-03](https://www.sportsmole.co.uk/football/arsenal/champions-league/team-news/slavia-prague-vs-arsenal-injury-suspension-list-predicted-xis_608248.html).

Pelatih Slavia membahas sakit dalam skuad serta perubahan peran Nowak setelah kemenangan di Jablonec. Ini konteks ketersediaan dan taktik dari klub, tidak diterjemahkan menjadi persentase kemenangan. [Laporan, pembaruan 2026-10-31](https://www.slavia.cz/article/35936/).

Line-up resmi belum digunakan. Motivasi dikaji sebagai kebutuhan poin fase liga, tanpa bonus intensitas/top-4. Jarak aktual, pola crossing/set piece/pressing dan tiga sumber pasar belum lengkap. Anomali pasar 30 menit sebelum kickoff berada setelah cutoff ini dan tidak dinilai.

Flag yang ditetapkan sebelum penilaian: `{"both_scored_ge4of5": true, "both_conceded_ge4of5": false, "both_low_clean_sheet": false, "one_high_clean_sheet": true, "both_historical_btts_majority": false, "away_model_favourite": false, "both_shots_12_to_15": null}`.

### Keputusan provisional

1 **48.8%** / X **26.0%** / 2 **25.2%**; pilihan **home**. BTTS **49.1%** (tidak); Over 2,5 **45.6%** (tidak).

λ 1.50–1.00. Estimasi clean sheet laga ini 36.8% / 22.3%; berbeda dari frekuensi historis di atas.

Perubahan XI, kondisi pemain atau kekuatan lawan yang tidak tertangkap gol lima laga dapat mengubah penilaian; belum diberi penyesuaian numerik. Analisis adalah bahan pertimbangan, bukan hasil mutlak.

## Viking FK — Sabah FK

### Data

**Viking FK**. Urutan tertua → terbaru; skor dari sudut tim.

| Tanggal | Lawan | Venue | Skor 90m | Tembakan | xG/xGA | Sumber |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Bayern Munich | home | 3–3 | 8 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401915411) |
| 2026-10-17 | Fredrikstad | home | 3–2 | 12 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401843459) |
| 2026-10-21 | Aston Villa | away | 1–3 | 10 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401915394) |
| 2026-10-25 | Tromso | home | 3–1 | 9 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401843373) |
| 2026-10-30 | Bodo/Glimt | away | 2–3 | 18 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401843468) |

GF **12**; GA/laga **2.40**; hasil **D-W-L-W-L**; PPG **1.40**. Clean sheet **0/5**; BTTS **5/5**. Tembakan rerata 11.4 (cakupan 5/5); xG 0/5. Perubahan PPG 3 laga terbaru vs 2 sebelumnya -1.00; ini tren hasil, bukan tren xG.

Gol 76–90+: cetak 2, kebobolan 1; hanya 5/5 laga dengan event lengkap.

**Sabah FK**. Urutan tertua → terbaru; skor dari sudut tim.

| Tanggal | Lawan | Venue | Skor 90m | Tembakan | xG/xGA | Sumber |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Slavia Prague | home | 2–0 | 13 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401915436) |
| 2026-10-17 | Qabala | away | 4–0 | N/A | N/A | [data](https://www.soccerbase.com/teams/team.sd?teamTabs=results&team_id=6814) |
| 2026-10-20 | Borussia Dortmund | home | 1–2 | 13 | N/A | [data](https://www.espn.com/soccer/match/_/gameId/401915404) |
| 2026-10-25 | Qarabag | home | 0–0 | N/A | N/A | [data](https://www.soccerbase.com/teams/team.sd?teamTabs=results&team_id=6814) |
| 2026-10-30 | Turan | away | 2–3 | N/A | N/A | [data](https://www.soccerbase.com/teams/team.sd?teamTabs=results&team_id=6814) |

GF **9**; GA/laga **1.00**; hasil **W-W-L-D-L**; PPG **1.40**. Clean sheet **3/5**; BTTS **2/5**. Tembakan rerata 13.0 (cakupan 2/5); xG 0/5. Perubahan PPG 3 laga terbaru vs 2 sebelumnya -2.67; ini tren hasil, bukan tren xG.

Gol 76–90+: cetak 1, kebobolan 0; hanya 2/5 laga dengan event lengkap.

### Pola dan konteks sebelum cutoff

Pertemuan pertama. Viking mencetak gol dalam 11 laga Eropa berturut-turut; tujuh laga kandang terakhir menghasilkan setidaknya tiga gol. Sabah kalah dalam tiga lawatan Eropa terakhir. Perjalanan Azerbaijan-Norwegia relevan secara kualitatif; rute dan jarak tempuh aktual belum diverifikasi.

[UEFA, 2026-10-29](https://www.uefa.com/uefachampionsleague/news/02aa-21f1d1379305-528a9ab315f6-1000--champions-league-matchday-4-viking-vs-sabah-facts/).

Laporan pralaga: Viking tanpa Baertelsen, Berisha, Bjorshol, D'Agostino, Roseth; Sabah perlu menilai Simic. Lima absensi perlu dinilai berdasarkan peran/menit, bukan dihitung sebagai penalti tetap. [Laporan, pembaruan 2026-11-03](https://www.sportsmole.co.uk/football/viking-fk/champions-league/preview/viking-fk-vs-sabah-prediction-team-news-lineups_608281.html).

Line-up resmi belum digunakan. Motivasi dikaji sebagai kebutuhan poin fase liga, tanpa bonus intensitas/top-4. Jarak aktual, pola crossing/set piece/pressing dan tiga sumber pasar belum lengkap. Anomali pasar 30 menit sebelum kickoff berada setelah cutoff ini dan tidak dinilai.

Flag yang ditetapkan sebelum penilaian: `{"both_scored_ge4of5": true, "both_conceded_ge4of5": false, "both_low_clean_sheet": false, "one_high_clean_sheet": true, "both_historical_btts_majority": false, "away_model_favourite": true, "both_shots_12_to_15": null}`.

### Keputusan provisional

1 **31.7%** / X **20.9%** / 2 **47.4%**; pilihan **away**. BTTS **71.7%** (ya); Over 2,5 **73.1%** (ya).

λ 1.70–2.10. Estimasi clean sheet laga ini 12.2% / 18.3%; berbeda dari frekuensi historis di atas.

Perubahan XI, kondisi pemain atau kekuatan lawan yang tidak tertangkap gol lima laga dapat mengubah penilaian; belum diberi penyesuaian numerik. Analisis adalah bahan pertimbangan, bukan hasil mutlak.

