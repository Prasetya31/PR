# Input ukuran matriks
baris = int(input("Masukkan jumlah baris: "))
kolom = int(input("Masukkan jumlah kolom: "))

# Input matriks pertama
matrik1 = []
print("Masukkan elemen-elemen matriks pertama:")
for i in range(baris):
    row = []
    for p in range(kolom):
        elemen = int(input(f"Masukkan elemen matriks pertama [{i+1},{p+1}]: "))
        row.append(elemen)
    matrik1.append(row)

# Input matriks kedua
matrik2 = []
print("Masukkan elemen-elemen matriks kedua:")
for i in range(baris):
    row = []
    for p in range(kolom):
        elemen = int(input(f"Masukkan elemen matriks kedua [{i+1},{p+1}]: "))
        row.append(elemen)
    matrik2.append(row)

# Penjumlahan matriks
matrik3 = []
for i in range(baris):
    temp = []
    for p in range(kolom):
        temp.append(matrik1[i][p] + matrik2[i][p])
    matrik3.append(temp)

# Menampilkan hasil penjumlahan
print("Hasil penjumlahan matriks:")
for row in matrik3:
    print(row)