print("Challenge 1 — Validasi Nilai")

nilai = int(input("Masukkan nilai: "))

# Tugas:
# Kalau nilai 0–100 → tampilkan "Nilai valid"
# Kalau di luar 0–100 → tampilkan "Nilai tidak valid"

if nilai >= 0 and nilai <= 100:
    print ("Nilai valid")
else:
    print ("Nilai tidak valid")
    

print("Challenge 2 — Validasi Nama")

nama = input("Masukkan nama: ")

# Tugas:
# Kalau nama tidak kosong → "Nama valid"
# Kalau nama kosong → "Nama tidak boleh kosong"

if nama == "":
    print ("Nama tidak boleh kosong")
else:
    print ("Nama valid")
    

print("Challenge 3 — Sedikit lebih realistis")

nama = input("Masukkan nama: ")

# Tugas:
# Misalnya user memasukkan: "   kay"
# Program harus tetap menganggapnya nama valid, tetapi: "kay"

if nama.strip() == "":
    print ("Nama tidak boleh kosong")
else:
    print (nama.strip())
    print ("Nama valid")
    

print("FINAL CHECKPOINT — 05")

username = input("Masukkan username: ")

# Tugas:
# Username harus minimal 3 karakter
# Kalau kurang dari 3 → "Username terlalu pendek"
# Kalau 3 karakter atau lebih → "Username valid"

if len(username) >= 3:
    print ("Username valid")
else:
    print ("Username terlalu pendek")
    