print("Challenge 1 — Tabel Perkalian")

# Tugas:
# Coba buat program yang menghasilkan:
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# ...
# 2 x 1 = 2
# 2 x 2 = 4
# ...
# 3 x 3 = 9

for i in range(1, 11, 1):
    for j in range(1, 11, 1):
        print(f"{i} x {j} = {i * j}")
        

print("Challenge 2 — Pola Bintang")

# Tugas:
# Sekarang kita pakai nested loop untuk membuat:
# *
# **
# ***
# ****
# *****

for i in range(0, 6, 1):
    for j in range(0, i, 1):
        print("*", end="")  # end="" membuat print() tidak pindah baris.
    print()


print("FINAL CHECKPOINT — 08")

# Tugas:
# Kita bikin pola angka:
# 1
# 12
# 123
# 1234
# 12345

for i in range(1, 7):
    for j in range(1, i):
        print(j, end="")  # end="" membuat print() tidak pindah baris.
    print()
