# List   → bisa diubah
buah = ["Apel", "Mangga", "Jeruk"]

# Tuple  → tidak bisa diubah
buah = ("Apel", "Mangga", "Jeruk")

# keduanya memanggil berdasarkan index

print("Tantangan 1")
buah = ("Apel", "Mangga", "Jeruk")
print(buah[1])

print("Tantangan 2")
buah = ("Apel", "Mangga", "Jeruk", "Pisang")

print(len(buah))

print("Tantangan 4 — Looping Tuple")
buah = ("Apel", "Mangga", "Jeruk", "Pisang")

for i in range(len(buah)):
    print(buah[i])
