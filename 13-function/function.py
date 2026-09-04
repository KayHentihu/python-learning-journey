print("Challenge 1 — Dua Parameter + Return")
# Tugas:
# Buat function bernama hitung_luas yang menerima:
# panjang
# lebar
# Function tersebut harus mengembalikan (return) luas persegi panjang.
# Contoh pemakaian:
# hasil = hitung_luas(10, 5)
# print(hasil)
# Target output: 50

def hitung_luas(panjang, lebar):
    return panjang * lebar

print(hitung_luas(10, 5))


print("Challenge 2 — Function dengan Kondisi")
# Tugas:
# Buat function:
# cek_nilai(nilai)
# Aturannya:
# Jika nilai >= 75 → return "Lulus"
# Jika nilai < 75 → return "Tidak Lulus"
# Contoh:
# print(cek_nilai(80))
# print(cek_nilai(60))
# Target:
# Lulus
# Tidak Lulus

def cek_nilai(nilai):
    if nilai >= 75:
        return "Lulus"
    else:
        return "Tidak Lulus"

print(cek_nilai(80))
print(cek_nilai(60))


print("Challenge 3 — Function dengan Default Parameter")
# Tugas:
# Buat function:
# def sapa(nama="Kay"):
# Function tersebut harus mengembalikan:
# Halo, Kay!
# jika dipanggil tanpa argumen:
# print(sapa())
# Tetapi kalau dipanggil:
# print(sapa("Andi"))
# hasilnya:
# Halo, Andi!

def sapa(nama = "kay"):
    return f"Halo {nama}!"

print(sapa())
print(sapa("Andi"))


print("Challenge FINAL")
# Tugas:
# Buat function:
# hitung_diskon(harga, diskon=10)
# Aturannya:
# harga = harga barang
# diskon = persentase diskon, default 10%
# Function mengembalikan harga setelah diskon
# Contoh:
# print(hitung_diskon(100000))
# Target:
# 90000.0
# Kalau:
# print(hitung_diskon(100000, 20))
# Target:
# 80000.0
# 💡 Rumusnya:
# harga setelah diskon = harga - (harga × diskon / 100)

def hitung_diskon(harga, diskon = 10):
    hasil = harga - (harga * diskon / 100)
    return hasil

print(hitung_diskon(10000))
print(hitung_diskon(10000, 20))