print("Challenge 1 — Cari angka genap")

angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Tugasnya: gunakan for untuk menampilkan hanya angka genap.

for nilai in angka:
    if nilai % 2 == 0:
        print (nilai)
        

print("Challenge 2 — Jumlahkan angka")

angka = [1, 2, 3, 4, 5]

# Tugasnya:
# Gunakan for untuk menghitung jumlah seluruh angka.

jumlah = 0
for nilai in angka:
    jumlah += nilai
print (jumlah)


print("Challenge 3 — Cari nilai terbesar")

angka = [12, 5, 27, 8, 19]

# Tugasnya:
# Gunakan for untuk mencari angka terbesar.

terbesar = 0
for nilai in angka:
    if nilai > terbesar:
        terbesar = nilai
print (terbesar)


print("FINAL CHECKPOINT — 06")

angka = [12, 5, 27, 8, 19, 30, 14]

# Tugasnya:
# Cari jumlah angka genap dari List tersebut.

jumlah = 0
for nilai in angka:
    if nilai % 2 == 0:
        jumlah += nilai
print (jumlah)
