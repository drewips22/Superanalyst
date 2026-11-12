# Model penelitian terlatih

Ditinjau 12 November 2026. Model ini memperbaiki baseline gol lima laga pada rekonstruksi UCL dua musim uji, dengan batas sumber yang tetap penting. Keunggulan terhadap pasar dan kalibrasi untuk forecast langsung belum dibuktikan.

## Resep yang terpilih

Lihat [kebijakan mesin](../assets/validated-policy.json) dan [laporan lengkap](../../../backtests/ucl-model-upgrade-v1/review.md).

| Target | Resep | Bukti yang tersedia |
| --- | --- | --- |
| 1X2 | Poisson kekuatan serangan/pertahanan tim dan lawan, kandang, form10, istirahat/kepadatan jadwal, proxy poin fase UCL | Log loss 1,0033 → 0,9211 pada 378 laga uji |
| BTTS | Laju gol dari rerata GF/GA jendela 20 laga tercakup | Brier 0,2541 → 0,2451 |
| Over 2,5 | Poisson kekuatan serangan/pertahanan dan intercept kompetisi | Brier 0,2348 → 0,2226 |

Resep dipilih pada 125 laga validasi 2023/24, lalu dinilai pada seluruh 378 laga utama UCL 2024/25 dan 2025/26 dengan skor 90 menit. Masing-masing target membaik di kedua musim. Tidak memilih ulang varian yang kebetulan terbaik setelah hasil uji diketahui.

## Batas penggunaan pada laga baru

- Cakupan empiris adalah sepak bola klub pria UCL fase utama/knockout, hasil 90 menit dan cutoff T-24 jam. Liga/horizon lain memerlukan pengujian tersendiri; jangan mengutip angka di atas sebagai jaminan di luar cakupan.
- Lima laga terbaru tetap ditampilkan untuk pembacaan pola. Model dapat memakai jendela lebih panjang; tampilkan denominator dan kompetisi yang benar-benar tercakup.
- Gunakan riwayat terbaru yang tersedia sebelum cutoff dan pasang ulang model. Parameter bulanan 2024–2026 yang disimpan dalam studi adalah artefak replay, bukan rating saat ini. Data yang tidak lengkap/stale harus memengaruhi status analisis.
- Pelatihan historis memakai empat tahun data terakhir dengan bobot waktu paruh 365 hari, regularisasi serangan/pertahanan dan kompetisi. Ikuti spesifikasi eksperimen untuk mengulangnya; perubahan bobot/jadwal pelatihan merupakan varian baru.
- Jika memakai model berbeda untuk tiga target, beri nama model masing-masing. Probabilitas BTTS dan clean sheet harus berasal dari model gol yang sama ketika memakai identitas probabilitasnya; jangan merangkai marginal lintas model menjadi satu distribusi gabungan.
- Proxy poin fase UCL mengukur hasil/kemajuan fase yang sudah terjadi, bukan intensitas psikologis. Efek kandang dipelajari dalam model, bukan dikalikan 35%. Tidak ada penalti absensi 22% atau bonus degradasi 18%.

## Fitur yang diuji dan belum dipromosikan

H2H tiga tahun dan jarak antarkota diuji sebagai tambahan di validasi, tetapi tidak memperbaiki varian form10 + istirahat. Pertahankan sebagai konteks/hipotesis; jangan menyatakan efeknya selalu nol. Jarak adalah garis lurus kota kandang yang sudah teramati ke kota pertandingan, bukan rute aktual.

[Studi tambahan xG](../../../backtests/xg-domestic-2015-v1/review.md) berada pada dua liga pria 2015/16. Campuran gol+xG membaik untuk pemenang, tetapi perubahan jendela juga berpengaruh; kontrol jendela sama ditandai posthoc. BTTS dan total gol berbasis xG murni tidak membaik. Jangan mengaktifkannya otomatis untuk UCL modern.

Absensi berbobot peran dan pasar belum memiliki arsip yang cukup untuk pengujian prediktif pada cohort ini. Ketersediaan tool validasi bukan bukti akurasi fitur. [Status lengkap](../../../backtests/ucl-model-upgrade-v1/coverage-status.json).

## Arsip konteks sebelum cutoff

`scripts/research/context.py` menyediakan fungsi validasi untuk:

- Pengumuman pemain: `match_id`, `team_id`, `player_id`, `status`, `announced_at`, `source_url`. Estimasi `expected_minutes_if_available` perlu `minutes_reference_cutoff` sebelum cutoff. Role yang tidak diketahui tetap tidak diketahui; berita absen lama mungkin sudah tercermin dalam performa tim.
- Line-up: sebelas ID berbeda, `official=true`, cap waktu pengumuman dan sumber. XI yang diumumkan sesudah cutoff tidak boleh masuk prediksi lebih awal.
- Quote pasar: pertandingan, kontrak, scope, provider, kelompok sumber independen, waktu observasi, probabilitas/bid–ask dan depth bila ada. Tiga quote dari satu sumber dasar tidak menjadi tiga pembanding independen. Quote setelah cutoff atau kontrak berbeda dikeluarkan.
- Diagnosis hasil: simpan dugaan keberuntungan beserta bukti sesudah laga. Label hasil tetap sama, kekalahan tetap dihitung, dan tidak ada penyesuaian prediksi surut.

Validasi struktur/waktu tidak membuktikan timestamp yang diberikan benar. Verifikasi publikasi sumber dan catat `retrieved_at` sebenarnya. Untuk dugaan anomali T-30 menit, buat eksperimen horizon terpisah dan arsip sebelum kickoff; grafik harga saja tidak membuktikan informasi internal.

## Menjalankan penelitian dan replay

Alat dasar tetap memakai pustaka standar. Fit model penelitian memakai NumPy/SciPy untuk gradien analitik dan optimasi L-BFGS. Dari akar repo:

```sh
python -m pip install -r requirements-research.txt
python backtests/ucl-model-upgrade-v1/replay.py
python backtests/xg-domestic-2015-v1/replay.py
python -m unittest discover -s tests -v
```

Replay memeriksa probabilitas dari fitur/model serta skor yang disimpan, tanpa corpus penuh. Untuk mereproduksi fit asli, diperlukan ekspor lokal yang cocok dengan checksum manifest. Sumber yang diunduh ulang bisa berubah; jangan mengganti arsip lama agar cocok.

Kolektor historis yang disertakan:

```sh
python skills/superanalyst/scripts/research/collect_history.py --output data/research-v1
python skills/superanalyst/scripts/research/coordinates.py --matches data/research-v1/matches.jsonl --output data/research-v1/geography
python skills/superanalyst/scripts/research/collect_xg.py --output data/statsbomb-xg-v1
```

Kolektor tersebut ditujukan untuk rentang studi yang tercatat, bukan layanan live. Jangan menjalankan `prepare/validate/grade` di folder yang sudah dibekukan. Untuk percobaan baru, buat direktori eksperimen baru, salin runner/spesifikasi yang relevan, tetapkan identitas serta periode baru, kemudian jalankan tahapan `prepare → validate → predict-test → grade`. Versikan helper yang berubah agar checksum kasus lama tetap berlaku.
