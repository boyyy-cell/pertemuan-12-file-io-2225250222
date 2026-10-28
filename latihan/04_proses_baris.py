
# Latihan 4: Memproses Baris File

with open("data/nilai.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()

        if baris:
            data = baris.split(",")
            nim = data[0]
            nilai = data[1]
            print(f"NIM: {nim}, Nilai: {nilai}")
