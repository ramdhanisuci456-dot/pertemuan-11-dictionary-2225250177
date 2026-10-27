def cari_mahasiswa(data, nim):
    return data.get(nim)


def rata_rata_nilai(data):
    if len(data) == 0:
        return 0

    total = 0
    for info in data.values():
        total += info["nilai"]

    return total / len(data)


data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}

# 1. Mencari data mahasiswa
print("=== PENCARIAN MAHASISWA ===")

nim = "A003"
hasil = cari_mahasiswa(data_mahasiswa, nim)

if hasil is not None:
    print(f"NIM: {nim}")
    print(f"Data: {hasil}")
else:
    print("Data tidak ditemukan")

# Menguji NIM yang tidak tersedia
print("\nMencari NIM A999:")
hasil = cari_mahasiswa(data_mahasiswa, "A999")

if hasil is not None:
    print(hasil)
else:
    print("Data tidak ditemukan")

# 2. Menambahkan mahasiswa baru
print("\n=== MENAMBAHKAN MAHASISWA ===")

data_mahasiswa["A006"] = {
    "nama": "Fajar",
    "kelas": "B",
    "nilai": 80
}

print("Mahasiswa baru berhasil ditambahkan.")

# 3. Mengubah nilai mahasiswa
print("\n=== MENGUBAH NILAI ===")

data_mahasiswa["A002"]["nilai"] = 82

print("Nilai Budi berhasil diubah menjadi 82.")

# 4. Menampilkan seluruh data mahasiswa
print("\n=== SELURUH DATA MAHASISWA ===")

for nim, info in data_mahasiswa.items():
    print(
        f"NIM: {nim}, "
        f"Nama: {info['nama']}, "
        f"Kelas: {info['kelas']}, "
        f"Nilai: {info['nilai']}"
    )

# 5. Menghitung rata-rata nilai
print("\n=== RATA-RATA NILAI ===")

rata_rata = rata_rata_nilai(data_mahasiswa)
print(f"Rata-rata nilai mahasiswa: {rata_rata:.2f}")