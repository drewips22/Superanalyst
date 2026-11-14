# Jurnal keputusan v1.2

Ditinjau 14 November 2026. Berlaku untuk snapshot baru v0.4.3+, melengkapi [protokol keputusan v1.1](decision-quality.md). Metode UNL, jendela lima laga, koefisien, resep UCL, serta pilihan pada arsip lama dipertahankan. Ini perbaikan konsistensi dan pencatatan; belum ada klaim peningkatan akurasi.

## Memakai keputusan yang sama

Mulai dari snapshot yang benar-benar tersedia. Bila cutoff, data dan metode sama, tampilkan kembali pilihan tersimpan. Jangan menghasilkan pilihan berbeda hanya karena pengguna meminta tabel atau gambar baru. Teks, gambar dan evaluasi memakai satu snapshot yang sama, termasuk `focus_target` per laga (`1x2`, `btts`, `total_2_5`, atau null). Fokus hanya boleh menunjuk target yang memiliki pilihan aktif.

Jika arsip dari chat lain tidak dapat diakses, jelaskan batasnya dan gunakan teks/lampiran yang tersedia sebagai transkripsi dengan asal yang jelas. Jangan mengklaim sudah memuat arsip, sumber, atau pengaturan model yang tidak tersedia. Jurnal bukan sinkronisasi otomatis lintas chat.

Input yang berubah menjadi versi baru. Penilaian ulang atas bukti lama juga boleh dilakukan bila memang diminta atau ditemukan kekeliruan; catat sebagai `reassessment` yang disengaja. Tetap pertahankan keluaran awal untuk evaluasi. Pembaruan setelah kickoff tidak menjadi pengganti forecast sebelum laga.

## Alasan setiap revisi

Catat sebelum/sesudah untuk pilihan, keyakinan, status, fokus dan skenario skor yang berubah. Setiap perubahan diberi satu kategori:

| Kategori | Yang perlu dibuktikan |
|---|---|
| `new_information` | Fakta baru, URL, waktu tersedia setelah cutoff lama dan sebelum cutoff baru |
| `lineup_confirmation` | Sumber XI resmi, perkiraan sebelumnya, peran yang terkonfirmasi dan dampak pada target |
| `data_correction` | Data yang keliru, koreksi bersumber dan akibatnya pada keputusan |
| `reassessment` | Alasan menafsirkan ulang bukti lama; jangan menyebutnya kabar mendadak |
| `scope_change` | Alasan menambah/mengeluarkan laga pada snapshot baru; snapshot lama tetap dinilai utuh |

Berita lama yang baru dibaca tetap memakai waktu publikasi aslinya. Waktu pengambilan tidak mengubahnya menjadi berita baru. Bila waktu tersedia tidak diketahui, simpan null dan jangan mengklaim kebaruan yang sudah terverifikasi.

Untuk XI, bandingkan perkiraan dengan susunan aktual: pemain/peran, pengganti, perkiraan menit dan target yang terdampak. Konfirmasi pemain yang sudah diperkirakan tampil dapat mengurangi ketidakpastian, tetapi tidak otomatis menaikkan peluang gol atau membatalkan pola sebelumnya. Pemain menyerang di kedua XI tidak otomatis berarti BTTS; nama bek kuat tidak otomatis berarti clean sheet. Perubahan keyakinan tetap perlu alasan khusus target.

## Waktu dan bukti rekaman

Bedakan cutoff informasi, waktu berkas dicatat, dan waktu jawaban/gambar diterbitkan. Jangan menulis “sudah dibekukan sebelum kickoff” hanya karena waktu yang diinginkan ditulis pada jawaban. Catat waktu aktual saat berkas berhasil dibuat; periksa kickoff aktual bila berbeda dari jadwal. Bila bukti rekaman sebelum laga tidak dapat diperiksa, beri status waktu belum terverifikasi.

Alat [decision_journal.py](../scripts/decision_journal.py) memakai waktu UTC eksekusi sebenarnya, menolak rekaman setelah kickoff terjadwal yang diberikan, memeriksa hash input, dan menolak menimpa berkas yang ada. Mengubah jadwal dalam revisi juga memerlukan alasan bersumber. Hash membuktikan kesamaan berkas terhadap hash itu; hash lokal sendiri bukan bukti publikasi, keaslian sumber, atau stempel waktu dari pihak ketiga. Hasil laga disimpan terpisah.

## Bentuk laporan pembaruan

Tampilkan ID snapshot, cutoff, waktu pencatatan dan status XI, lalu tabel:

| Laga/target | Sebelumnya | Sekarang | Kategori | Perubahan bukti dan alasan |
|---|---|---|---|---|

Pilihan yang tetap tidak perlu ditafsirkan ulang dari nol. Laporkan cakupan keputusan per target, misalnya empat pilihan total dari sembilan laga, serta observasi dan hasil yang belum final. Jangan menjumlahkan beberapa versi satu laga sebagai sampel independen. Pilihan yang dicabut tetap ada di penilaian versi sebelumnya; jangan memilih versi terbaik setelah hasil diketahui. Nilai fokus yang telah ditetapkan, bukan fokus pengganti yang kebetulan benar.

## Alat dan contoh sintetis

Format dasar forecast tetap `qualitative-forecast-v2`. Tambahkan `focus_target` dan `analysis_method` pada tiap baris. Input jurnal memuat `as_of`, `profile`, `facts` dan sumber ber-ID dengan URL, `available_at` (boleh null), serta `retrieved_at`. Untuk persahabatan tambahkan [konteks per tim](friendly-context.md).

Contoh berikut hanya data sintetis. Tanggal kickoff jauh di masa depan dipakai agar contoh pencatatan tidak perlu memalsukan waktu komputer. Tidak ada pertandingan nyata atau klaim akurasi dalam contoh ini. Jalankan dari akar paket/repo dan gunakan path keluaran baru setiap kali:

```sh
python skills/superanalyst/scripts/decision_journal.py record examples/journal-forecast.synthetic.json examples/journal-inputs.synthetic.json --out runs/journal-demo/initial.json
python skills/superanalyst/scripts/decision_journal.py reuse runs/journal-demo/initial.json examples/journal-inputs.synthetic.json
```

Pembaruan nyata memakai `record forecast-baru.json inputs-baru.json --previous jurnal-awal.json --review alasan-revisi.json --out jurnal-baru.json`. Jurnal baru menyimpan hash pendahulunya. `changes` pada berkas review harus menyebut setiap pasangan `match_id`/`target` yang berubah tepat sekali, kategori `kind`, alasan `reason`, dan `source_ids` yang relevan. Konfirmasi XI memerlukan `lineup_delta` dengan `team`, `player`, `expected`, `confirmed`, `impact`. Penilaian ulang memerlukan `intentional_reassessment: true`. Penambahan/pengurangan laga memakai target `scope` dan kategori `scope_change`.

```json
{
  "intentional_reassessment": true,
  "changes": [{
    "match_id": "synthetic-journal-1",
    "target": "btts",
    "kind": "reassessment",
    "reason": "Penafsiran ulang bukti sintetis yang saling bertentangan",
    "source_ids": ["synthetic-preview"]
  }]
}
```

`grade jurnal.json outcomes.json` menerima format hasil 90 menit alat arsip v0.4.2 dan menambahkan penilaian fokus serta cakupan. Tidak menghitung Brier/log loss tanpa probabilitas. Bila eksekusi tidak tersedia, terapkan pencatatan yang sama pada tabel/file yang dapat disimpan; nyatakan pemeriksaan mesin belum dijalankan. Jangan menyatakan ada jurnal tersimpan hanya karena template sudah terisi di jawaban.
