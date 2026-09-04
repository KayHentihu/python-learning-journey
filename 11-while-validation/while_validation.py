print("Challenge 1 — Minta input sampai benar")

# Tugas:
# Buat program yang terus meminta angka sampai user memasukkan angka positif.

# Contoh:

# Masukkan angka: -5
# Angka harus positif!

# Masukkan angka: -2
# Angka harus positif!

# Masukkan angka: 10
# Angka diterima!
valid = False
while not valid:
    angka = int(input("Masukkan angka : "))
    
    if angka <= 0:  
        print ("Angka harus positif!")
    else:
        print ("Angka diterima")
        valid = True
    

print ("Challenge 2 — Validasi Password")

# Tugas
# Buat program yang terus meminta password sampai password yang dimasukkan benar.

# 🎯 Target

# Password yang benar: python123
# Contoh:
# Masukkan password: halo
# Password salah!

# Masukkan password: belajar
# Password salah!

# Masukkan password: python123
# Password benar!

password_benar = "python123"

valid = False
while not valid:
    input_password = input("Masukkan password : ")
    
    if input_password == password_benar:
        print ("Password benar!")
        valid = True
    else:
        print ("Password salah, coba lagi!")
        
        
print ("Challenge 3")

# Tugas
# Buat program yang meminta nilai 0–100 
# terus-menerus sampai user memasukkan nilai yang valid.

# Contoh:

# Masukkan nilai: 120
# Nilai tidak valid!

# Masukkan nilai: -5
# Nilai tidak valid!

# Masukkan nilai: 85
# Nilai diterima!

valid = False
while not valid:
    nilai = int(input("Masukkan nilai: "))
    if nilai >= 0 and nilai <= 100:
        print("Nilai diterima")
        valid = True
    else:
        print("Nilai tidak valid!")


print("Challenge FINAL")

# Tugas
# Buat program registrasi username sederhana.

# Aturannya:

# Username tidak boleh kosong.
# Username minimal 3 karakter.
# Program terus meminta username sampai valid.
# Gunakan while + boolean.
# Jangan gunakan break.

# Contoh:

# Masukkan username: 
# Username tidak boleh kosong!

# Masukkan username: ab
# Username terlalu pendek!

# Masukkan username: kay
# Username diterima!

valid = False

while not valid:
    username = input("Masukkan username: ")
    if username == "":
        print("Username tidak boleh kosong!")
    elif len(username) < 3:
        print("Username terlalu pendek!")
    else:
        print("Username diterima!")
        valid = True