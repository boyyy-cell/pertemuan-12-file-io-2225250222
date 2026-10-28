
# Latihan 6: Menangani ValueError

try:
    nilai = float(input("Masukkan nilai mahasiswa: "))
    print(f"Nilai yang dimasukkan: {nilai}")
except ValueError:
    print("Error: Masukkan angka yang valid.")
