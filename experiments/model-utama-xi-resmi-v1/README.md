# Model Utama + XI Resmi v1

Eksperimen opsional untuk mengukur dampak susunan resmi terhadap
keputusan Model Utama. Pertanyaan uji: apakah revisi berdasarkan XI resmi
lebih sering memperbaiki fokus daripada membuat pilihan sebelumnya meleset?
Status per **24 November 2026 WIB** adalah protokol uji prospektif.
Cohort awal terdiri dari sembilan laga fase liga UCL Matchday 5 pada
25 November 2026 WIB, selama kedua XI terverifikasi dan revisi tercatat
sebelum kickoff. [Jadwal UEFA](https://www.uefa.com/uefachampionsleague/news/02a8-2174c9e9019d-f909a77bd77a-1000--2026-27-champions-league-all-the-league-phase-f/)

| Saat dicatat | Isi |
|---|---|
| Sebelum XI terbit | Prediksi awal Model Utama dan fokus asli tiap laga. |
| Setelah XI terbit, sebelum kickoff | Versi eksperimen dari riset yang sama. Catat kedua sumber resmi, perbedaan dari perkiraan, peran pemain dan dampaknya pada target. Rekam juga laga yang penilaiannya tetap sama. |
| Setelah FT | Daftar hasil resmi waktu normal, termasuk injury time, dalam berkas hasil terpisah. |

Gunakan 1X2, BTTS, dan total 2,5 untuk perbandingan dengan jurnal asli.
Catat skenario skor dan perubahan keyakinan **rendah, sedang, relatif kuat**
sebagai diagnosis. Status observasi dipakai bila bukti belum cukup.
Judul eksperimen ada di laporan dan folder ini. Isi `analysis_method`
tetap ID Model Utama pada kedua jurnal karena perlakuan yang diuji ialah
informasi XI resmi.

## Mencatat dan membandingkan

Ikuti [jurnal keputusan Superanalyst](../../skills/superanalyst/references/decision-journal.md).
Salin fakta riset awal untuk versi XI. Tambahkan
`inputs.facts.lineup_confirmations` sebagai objek yang memetakan
`match_id` ke `{"home_source_id": "...", "away_source_id": "..."}`.
Kedua ID boleh menunjuk match centre resmi yang menampilkan XI dua tim.
Catat kapan XI tersedia dan diperiksa dalam `inputs.sources`. Untuk revisi
yang memengaruhi keputusan, isi `lineup_confirmation` dan `lineup_delta`
sesuai protokol jurnal.

Jika jadwal terbagi dua gelombang, simpan satu versi XI per gelombang dengan
jurnal awal yang sama sebagai `--previous`. Untuk laga di luar gelombang itu,
catat pengeluaran dari lingkup melalui `scope_change` pada review.
Jalankan pembanding pada tiap gelombang dan gabungkan hanya laga berbeda.
Tampilkan laga yang tidak punya versi XI tepat waktu dalam cakupan total.

```sh
python skills/superanalyst/scripts/decision_journal.py record forecast-xi.json inputs-xi.json --previous jurnal-awal.json --review review-xi.json --out jurnal-xi.json
python experiments/model-utama-xi-resmi-v1/compare.py jurnal-awal.json jurnal-xi.json
python experiments/model-utama-xi-resmi-v1/compare.py jurnal-awal.json jurnal-xi.json --hasil hasil-90m.json
```

Format hasil mengikuti evaluator jurnal. `--hasil` menerima sebuah daftar
objek dengan `match_id`, `scope: "90m"`, `status: "completed"`,
`home_goals`, dan `away_goals`.

Nilai utama adalah jumlah **salah → benar** dan **benar → salah** pada
fokus untuk laga selesai yang punya pilihan pada kedua versi. Laporkan juga
keduanya benar/keduanya salah lewat total benar dan penyebut bersama,
cakupan pilihan, serta perubahan ke/dari observasi. Perubahan fokus dinilai
terhadap fokus masing-masing versi. Nilai 1X2, BTTS, dan total gol juga
disajikan agar dampak pada target yang sama bisa dilihat.
Bukti sembilan laga digunakan sebagai awal pencatatan. Klaim peningkatan perlu
diuji pada matchday berikutnya dengan [protokol evaluasi kronologis](../../skills/superanalyst/references/backtesting.md).
