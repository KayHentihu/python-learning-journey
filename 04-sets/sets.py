# Set tidak menyimpan duplikat.
angka = {1, 2, 2, 3, 3, 4}

print(angka) # output {1, 2, 3, 4}

print("Tantangan 1 — Set & Duplikat")
# Set tidak menyimpan duplikat.
angka = {1, 2, 2, 3, 3, 4}

print(angka) # output {1, 2, 3, 4}

print("Tantangan 2 — Tambah Data")

buah = {"Apel", "Mangga", "Jeruk"}
# tambahkan "Pisang" ke dalam set

buah.add("Pisang")
print(buah)

print("Challenge 3 — Hapus Data")

buah = {"Apel", "Mangga", "Jeruk", "Pisang"}

# hapus "Mangga"

buah.remove("Mangga")
print(buah)

print("Challenge 4 — Operasi Set")

angka1 = {1, 2, 3, 4}
angka2 = {3, 4, 5, 6}

# | = Union / gabungan
# output {1, 2, 3, 4, 5, 6}
print(angka1 | angka2) 

# & = Intersection / irisan
# output {3, 4}
print(angka1 & angka2)

print("FINAL CHECKPOINT — SET")

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Tugasmu:
# 1. Buat Set yang berisi semua angka dari a dan b tanpa duplikat.

# 2. Buat Set yang berisi angka yang sama-sama ada di a dan b.

# 💡 Petunjuk: tadi kita baru belajar | dan &.

print(a | b)
print(a & b)