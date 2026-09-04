print("Challenge 1 — Tampilkan nomor + buah")

buah = ["Apel", "Mangga", "Jeruk", "Pisang"]

# Target:

# 0 - Apel
# 1 - Mangga
# 2 - Jeruk
# 3 - Pisang

for index, nilai in enumerate(buah):
    print(f"{index} - {nilai}")
    

print("Challenge 2 — Mulai dari nomor 1")

buah = ["Apel", "Mangga", "Jeruk", "Pisang"]

# Target:
# Sekarang ubah output menjadi:

# 1 - Apel
# 2 - Mangga
# 3 - Jeruk
# 4 - Pisang

for index, nilai in enumerate(buah, 1):
    print(f"{index} - {nilai}")
    

print("FINAL CHECKPOINT — 09")

buah = ["Apel", "Mangga", "Jeruk", "Pisang", "Durian"]

# Target:
# Tampilkan hanya buah yang posisinya mulai dari nomor 2:

# 2 - Mangga
# 3 - Jeruk
# 4 - Pisang
# 5 - Durian

for index, nilai in enumerate(buah, 1):
    if index >= 2:
        print(f"{index} - {nilai}")