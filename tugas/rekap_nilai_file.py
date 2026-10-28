
# Tugas Pertemuan 12: Rekap Nilai Mahasiswa

def baca_data(nama_file):
    data = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor, baris in enumerate(file, start=1):
                baris = baris.strip()

                if not baris:
                    continue

                try:
                    bagian = baris.split(",")

                    if len(bagian) != 2:
                        raise ValueError("Format baris tidak sesuai")

                    nim = bagian[0].strip()
                    nilai = float(bagian[1].strip())

                    data.append({"nim": nim, "nilai": nilai})

                except ValueError:
                    print(f"Baris {nomor} tidak valid, dilewati: {baris}")

    except FileNotFoundError:
        print(f"Error: File {nama_file} tidak ditemukan.")

    return data


def tulis_rekap(nama_file, data):
    with open(nama_file, "w", encoding="utf-8") as file:
        file.write("HASIL REKAP NILAI MAHASISWA\n")
        file.write("===========================\n")

        if not data:
            file.write("Tidak ada data nilai yang valid.\n")
            return

        nilai_list = [mahasiswa["nilai"] for mahasiswa in data]
        jumlah = len(nilai_list)
        rata_rata = sum(nilai_list) / jumlah
        tertinggi = max(nilai_list)
        terendah = min(nilai_list)
        lulus = sum(1 for nilai in nilai_list if nilai >= 60)

        file.write(f"Jumlah data valid: {jumlah}\n")
        file.write(f"Rata-rata nilai: {rata_rata:.2f}\n")
        file.write(f"Nilai tertinggi: {tertinggi:g}\n")
        file.write(f"Nilai terendah: {terendah:g}\n")
        file.write(f"Jumlah mahasiswa lulus: {lulus}\n")

    print(f"Rekap berhasil disimpan ke {nama_file}.")


def main():
    data = baca_data("data/nilai.txt")
    tulis_rekap("data/hasil_rekap.txt", data)


if __name__ == "__main__":
    main()
