print("Challenge 1 — Cek buah")

buah = ["Apel", "Mangga", "Jeruk", "Pisang"]

# Target:
# Cek apakah "Mangga" ada di dalam List.

print ("Mangga" in buah)


print("Challenge 2 — not in")

buah = ["Apel", "Mangga", "Jeruk", "Pisang"]

# Target:
# Cek apakah "Durian" tidak ada di dalam List.

print ("Durian" not in buah)


print("Challenge 3 — Gabungkan dengan if")

buah = ["Apel", "Mangga", "Jeruk", "Pisang"]

nama_buah = input("Cari buah: ")

# Target:
# Kalau buah ada → tampilkan "Buah ditemukan"
# Kalau tidak ada → tampilkan "Buah tidak ditemukan".

if nama_buah in buah:
    print ("Buah ditemukan")
else:
    print ("Buah tidak ditemukan")


print("FINAL CHECKPOINT — 10")

buah = ["Apel", "Mangga", "Jeruk", "Pisang"]

nama_buah = input("Cari buah: ")

# Tugas:
# Kalau buah ditemukan, tampilkan:
# Buah ditemukan pada daftar.
# Kalau tidak ditemukan:
# Buah tidak ada dalam daftar.

ketemu = False

for nilai in buah:
    nilai = nilai.lower()
    
    if nama_buah.lower() in nilai:
        print ("Buah ditemukan pada daftar.")
        ketemu = True
        break
        
if not ketemu:
    print ("Buah tidak ada dalam daftar.")
