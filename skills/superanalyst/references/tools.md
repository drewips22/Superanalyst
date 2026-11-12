# Panduan alat dan format input

Semua alat memakai Python 3.11+ dan pustaka standar. Jalankan dari akar repo. Alat tidak mengambil berita, mengunduh statistik, melatih model, atau memantau pasar secara otomatis. Hasil JSON ditulis ke layar; arahkan ke file dalam `runs/` bila ingin menyimpannya.

## Ringkasan lima laga

```sh
python skills/superanalyst/scripts/stats.py summary examples/team-history.synthetic.json
```

Objek JSON tingkat atas:

| Field | Jenis | Makna |
| --- | --- | --- |
| `team` | string | Tim yang menjadi perspektif GF/GA |
| `as_of` | ISO 8601 ber-offset | Batas informasi |
| `synthetic` | boolean | Wajib; true hanya untuk contoh buatan |
| `matches` | array | Riwayat pertandingan tim |

Setiap laga memakai `match_id`, `kickoff_at`, `status`, dan `competitive`. Untuk laga kompetitif yang selesai, isi `finished_at` serta `available_at`: waktu hasil dan metrik baris itu sudah tersedia. Laga yang belum selesai, nonkompetitif, atau baru tersedia setelah cutoff dikeluarkan dengan alasan. Dari laga yang layak, pilih lima berdasarkan kickoff terbaru dan tampilkan terlama dahulu. `available_at` konservatif untuk satu baris; pisahkan dataset jika tiap metrik memiliki waktu ketersediaan yang berbeda.

Field untuk laga yang masuk ringkasan:

- `opponent`, `competition`, `source_url`: string sumber dan konteks.
- `scope`: `90m` untuk skor **dan** statistik; `venue`: `home`, `away`, atau `neutral`.
- `goals_for`, `goals_against`: bilangan bulat tidak negatif dari perspektif `team`.
- `xg_for`, `xg_against`: angka tidak negatif atau `null`. Jika salah satunya ada, wajib isi `xg_provider` dan `xg_definition`, misalnya `pre_shot_all_including_penalties_v1`. Semua data xG yang dipilih harus memakai provider/definisi yang sama.
- `shots`, `shots_on_target`: bilangan bulat tidak negatif atau `null`; SoT tidak melebihi shots.
- `possession_pct`: 0–100 atau `null`.
- `goals_for_76_plus`, `goals_against_76_plus`: gol menit 76–90+ atau `null`, tidak melebihi total gol masing-masing.

Timestamp wajib menyertakan zona waktu. Duplikasi ID, skor negatif, nilai nonfinite, cakupan 120 menit, serta campuran provider xG ditolak. Field statistik opsional yang hilang diperlakukan sebagai `null`, bukan nol. Ringkasan xGD hanya memakai pasangan xG/xGA lengkap. Tren xGD hanya dihitung jika kelima pasang tersedia. Riwayat yang lebih pendek tetap diringkas dengan `window_complete=false`; riwayat tanpa laga layak ditolak.

Alat mengasumsikan semua baris benar-benar milik `team`; cocokkan ID tim pada tahap pengumpulan. Penyediaan timestamp dan sumber oleh pengguna tidak otomatis membuktikan kebenaran datanya.

## Kalkulator Poisson

```sh
python skills/superanalyst/scripts/stats.py poisson --home-rate 1.6 --away-rate 1.2
```

Laju di atas adalah contoh sintetis. Input adalah ekspektasi gol waktu normal untuk laga target, dengan dasar estimasi di luar kalkulator. Keluaran meliputi 1X2, BTTS, clean sheet tiap tim, 0–0, lima skor teratas, dan sisa massa probabilitas yang dipotong secara numerik.

Asumsi: gol kedua tim Poisson independen. Grid diperpanjang hingga tail tiap tim di bawah `1e-12`; probabilitas 1X2/skor dinormalisasi pada grid tersebut. BTTS dan clean sheet memakai formula analitik. Rentang laju 0–100 adalah batas komputasi, bukan rekomendasi nilai untuk sepak bola. `calibrated=false` selalu dicantumkan karena alat tidak membuktikan kalibrasi model pembentuk lajunya.

## Evaluasi forecast dan rekonstruksi historis

```sh
python skills/superanalyst/scripts/evaluate.py examples/predictions.synthetic.jsonl
```

JSONL berarti satu objek JSON per baris. Contoh siap jalan ada di folder `examples/`. Setiap record memuat:

| Field | Jenis/aturan |
| --- | --- |
| `prediction_id`, `match_id` | ID snapshot dan laga |
| `mode` | `forecast` (bawaan) atau `retrospective_reconstruction`; tidak digabung dalam kelompok evaluasi |
| `competition`, `model_version`, `horizon` | Kelompok eksperimen; horizon adalah label yang dipilih sebelum evaluasi |
| `synthetic` | true/false; keduanya dievaluasi terpisah |
| `scope` | `90m` |
| `as_of`, `recorded_at`, `kickoff_at`, `features_available_at` | ISO 8601 ber-offset; urutan waktu diverifikasi |
| `decision` | `predict`, `observe`, atau `insufficient_data` |
| `p_1x2` | Untuk predict: objek dengan tepat `home`, `draw`, `away`, masing-masing 0–1 dan total 1 |
| `p_btts` | Untuk predict: probabilitas 0–1 |
| `reason` | Wajib untuk observe/insufficient_data; probabilitas harus null/tidak diisi |
| `result` | null untuk belum final, atau objek hasil di bawah |

Untuk rekonstruksi yang dibuat sesudah pertandingan, **jangan isi `recorded_at` dengan waktu masa lalu**. Sebagai gantinya, isi `reconstructed_at` dengan waktu eksekusi sebenarnya, `point_in_time_verified` (boolean), dan `reconstruction_notes` yang menjelaskan sumber dan batas uji. Wajib `as_of < kickoff_at <= reconstructed_at`. `features_available_at` boleh null jika waktu ketersediaan aslinya tidak dibuktikan; nilai yang diisi harus tetap sebelum cutoff. Rekonstruksi bukan pengganti arsip forecast yang benar-benar dibuat saat itu.

Objek `result` berisi `status="completed"`, `scope="90m"`, `home_goals`, `away_goals`, `finished_at`, dan `source_url`. Dalam mode rekonstruksi saja, `finished_at` boleh null dengan `completed_date_utc` (YYYY-MM-DD) bila sumber tidak membuktikan presisi jam. Skor waktu normal tetap digunakan bila pertandingan berlanjut ke extra time; waktu selesai boleh waktu penutupan laga penuh. Pertandingan batal/void tidak diberi hasil palsu. Simpan alasannya pada arsip dan jangan menganggapnya kekalahan prediksi.

Record dapat menyertakan field tambahan seperti `sources`, `data_version`, `lineup_status`, `parameters`, `revision_of`, dan `reason`; pertahankan untuk audit meski evaluator tidak membacanya. Evaluator awal memerlukan 1X2 **dan** BTTS untuk `predict`. Forecast hanya BTTS perlu perluasan schema/evaluator sebelum dimasukkan; jangan mengarang 1X2 untuk mengisi field.

Keluaran dikelompokkan menurut model, horizon, kompetisi, synthetic, dan mode. Laporan menampilkan rentang menit aktual ke kickoff agar label horizon bisa diperiksa; toleransi horizon tidak ditebak oleh alat. Evaluator menolak dua snapshot laga yang sama pada kelompok yang sama. Pilih satu snapshot menurut aturan eksperimen terlebih dahulu.

Dalam repo Superanalyst, contoh kasus nyata dapat diperiksa dengan:

```sh
python backtests/ucl-2025-final/run.py verify
python skills/superanalyst/scripts/evaluate.py backtests/ucl-2025-final/scored-reconstruction.jsonl
```

Folder kasus menyimpan data, spesifikasi, prediksi tanpa hasil, checksum, label hasil, dan evaluasi terpisah. Checksum dibuat pada waktu rekonstruksi sebenarnya; itu tidak membuktikan kebutaan terhadap hasil historis. Runner menolak menimpa snapshot yang sudah ada.

Laporan mencakup jumlah dipertimbangkan/diprediksi/dilewati/belum final, cakupan, Brier, log loss, dan sepuluh bin kalibrasi. Kelompok tanpa hasil yang dapat dinilai menghasilkan metrik `null`. Data contoh yang sangat kecil hanya membuktikan format dan perhitungan, bukan mutu prediksi nyata.

## Pemeriksaan

```sh
python -m unittest discover -s tests -v
```

Tes memeriksa identitas probabilitas, data hilang, pemilihan waktu, konsistensi sumber xG, scoring, pemisahan eksperimen, dan penolakan data yang bocor setelah cutoff. Gunakan juga validator skill yang tersedia di lingkungan Codex setelah mengubah frontmatter atau struktur skill.
