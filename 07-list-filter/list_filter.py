print("Challenge 1 — Cari nilai di atas 10")

angka = [5, 12, 7, 20, 3, 15, 8]

# Tugas:
# gunakan for + if untuk menampilkan angka yang lebih besar dari 10.

for nilai in angka:
    if nilai > 10:
        print (nilai)


print("Challenge 2 — Hitung berapa yang lolos")

angka = [5, 12, 7, 20, 3, 15, 8]

# Tugas:
# Hitung ada berapa angka yang lebih besar dari 10.

jumlah = 0

for nilai in angka:
    if nilai > 10:
        jumlah += 1
print(jumlah)


print("Challenge 3 — Filter + jumlah")

angka = [5, 12, 7, 20, 3, 15, 8]

# Tugas:
# Jumlahkan hanya angka yang lebih besar dari 10.

jumlah = 0

for nilai in angka:
    if nilai > 10:
        jumlah += nilai
print(jumlah)


print("FINAL CHECKPOINT — 07")

angka = [4, 15, 7, 22, 10, 31, 8, 18]

# Tugas:
# Cari jumlah semua angka genap yang lebih besar dari 10.

jumlah = 0

for nilai in angka:
    if nilai > 10 and nilai % 2 == 0:
        jumlah += nilai
print(jumlah)