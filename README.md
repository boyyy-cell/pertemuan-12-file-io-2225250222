
# Pertemuan 12 — File I/O dan Error Handling Python

## Identitas
- Nama: Farid Syahputra
- NIM: 2225250222
- Kelas: 3F
- Mata Kuliah: Algoritma dan Pemrograman

## Tujuan
1. Memahami cara membaca dan menulis file menggunakan Python.
2. Memahami mode file `r`, `w`, dan `a`.
3. Memproses data dari file teks.
4. Menangani FileNotFoundError dan ValueError.
5. Membuat program rekap nilai mahasiswa.

## Struktur Proyek
- `data/`: menyimpan file input dan hasil rekap.
- `latihan/`: menyimpan enam file latihan.
- `tugas/rekap_nilai_file.py`: program utama.
- `README.md`: dokumentasi proyek.

## Format Data
Data nilai disimpan dalam format NIM,nilai.

Contoh:
A001,85
A002,78
A003,92

## Cara Menjalankan
Jalankan dari folder utama proyek menggunakan terminal:

`python tugas/rekap_nilai_file.py`

## Penanganan Error
- FileNotFoundError: menangani file yang tidak ditemukan.
- ValueError: melewati data dengan nilai bukan angka atau format yang salah.
- Baris kosong dilewati saat membaca data.

## Hasil Pengujian

| Pengujian | Hasil yang Diharapkan | Status |
|---|---|---|
| Membaca data nilai | Data valid berhasil dibaca | Berhasil |
| Nilai berisi abc | Baris dilewati | Berhasil |
| Menghitung rata-rata | 83.40 | Berhasil |
| Nilai tertinggi | 92 | Berhasil |
| Nilai terendah | 74 | Berhasil |
| Jumlah mahasiswa lulus | 5 | Berhasil |

## Refleksi
Saya belajar membaca, menulis, dan mengolah data dari file menggunakan Python. Saya juga memahami bahwa error dapat ditangani menggunakan try-except agar program tidak langsung berhenti ketika menemukan data yang salah.

## Catatan Pengerjaan
Proyek ini mencakup latihan membaca, menulis, menambahkan isi file, memproses baris, dan menangani error menggunakan Python.

## Pengujian GitHub
Kode sumber dan dokumentasi disimpan dalam repository GitHub pada branch main.
