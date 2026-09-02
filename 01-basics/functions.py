def sapa():  # ini fungsi nya
    print("Hello, Kay!")

sapa() # ini pemanggilan fungsinya

# tantangan

print("Tantangan 1")
def perkenalan():
    print(f"Halo, nama saya Kay")
    print(f"Saya mahasiswa Informatika")
    
perkenalan()

print("Tantangan 2 — Function dengan Parameter")
def sapa(nama):
    print(f"Halo, {nama}!")
    
sapa("Kay")

print("Tantangan 3")
def tambah(a, b):
    print(a + b)
    
tambah(10, 5)

print("Tantangan 4 — return")
def kali(a, b):
    return a * b
    
hasil = kali(4, 5)
print(hasil)

print("FUNCTIONS — FINAL CHECKPOINT")
def cek_nilai(nilai):
    if nilai >= 75:
        return "Lulus"
    else:
        return "Tidak Lulus"
    
hasil = cek_nilai(80)
print(hasil)