# Pertemuan 11 - Dictionary/Map

**Nama:** Suci Ramadhani  
**NIM:** 2225250177  
**Kelas:** 3B  
**Program Studi:** Pendidikan Matematika FKIP Untirta  
**Mata Kuliah:** Algoritma dan Pemrograman

## Tujuan
Mempelajari penggunaan dictionary untuk menyimpan dan mengelola data dalam bentuk pasangan key-value, mengakses data berdasarkan key, serta mengolah data mahasiswa menggunakan Python.

## Struktur Data
Program menggunakan dictionary dengan NIM sebagai key utama. Setiap value berisi dictionary yang menyimpan nama, kelas, dan nilai mahasiswa.

Contoh:
```python
"A001": {"nama": "Ayu", "kelas": "A", "nilai": 85}
```

## Daftar Latihan
1. `01_dasar_dictionary.py` — Membuat dan mengakses dictionary.
2. `02_akses_get.py` — Mengakses data menggunakan `get()`.
3. `03_manipulasi_dictionary.py` — Menambah, mengubah, dan menghapus data.
4. `04_iterasi_dictionary.py` — Menelusuri key dan value menggunakan `items()`.
5. `05_dictionary_bersarang.py` — Menggunakan dictionary bersarang.
6. `06_fungsi_dictionary.py` — Membuat fungsi pencarian data.

## Program Praktik
File `praktik/data_mahasiswa.py` digunakan untuk:
- Mencari data mahasiswa berdasarkan NIM.
- Menampilkan pesan jika NIM tidak ditemukan.
- Menambahkan mahasiswa baru.
- Mengubah nilai mahasiswa.
- Menampilkan seluruh data mahasiswa.
- Menghitung rata-rata nilai mahasiswa.

## Cara Menjalankan
Jalankan setiap file melalui terminal VS Code menggunakan perintah Python.

Contoh menjalankan latihan:
```bash
python latihan/01_dasar_dictionary.py
```

Contoh menjalankan program praktik:
```bash
python praktik/data_mahasiswa.py
```

## Test Case

| No. | Pengujian | Hasil yang Diharapkan |
|---|---|---|
| 1 | Mencari NIM A003 | Data Citra ditampilkan |
| 2 | Mencari NIM A999 | Data tidak ditemukan |
| 3 | Mengubah nilai A002 | Nilai berubah menjadi 82 |
| 4 | Menambahkan NIM A006 | Data Fajar berhasil ditambahkan |
| 5 | Menampilkan seluruh data | Semua data mahasiswa ditampilkan |
| 6 | Menghitung rata-rata | Rata-rata nilai 83,50 |

## Refleksi
Pada praktikum ini, saya mempelajari bahwa dictionary memudahkan pencarian data berdasarkan key. Saya juga memahami penggunaan `get()` untuk menangani key yang tidak tersedia, `items()` untuk menampilkan pasangan key-value, serta fungsi untuk memisahkan proses pencarian dan perhitungan rata-rata nilai.