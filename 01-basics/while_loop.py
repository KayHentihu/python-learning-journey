i = 1
while i <= 5:
    print(i)
    i += 1
    
# tantangan
i = 5
while i >= 1:
    print(i)
    i -= 1
    
i = 2
while i <= 10:
    print(i)
    i += 2
    
password_benar = "python123"
valid = False
while not valid:
    input_password = input("Masukkan Password anda : ")
    if input_password == password_benar:
        print(f"Login berhasil!!")
        valid = True
        break
    else:
        print(f"Gagal, coba lagi!!")
    