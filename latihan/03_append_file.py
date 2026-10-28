
# Latihan 3: Menambahkan Isi File

with open("data/catatan.txt", "a", encoding="utf-8") as file:
    file.write("Belajar menambahkan isi file.\n")

print("Isi file berhasil ditambahkan.")
