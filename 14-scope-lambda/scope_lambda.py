print ("Challenge 1 — Scope")
nama = "Kay"  # Global

def sapa():
    nama = "Andi" # Local
    print(nama)

sapa()
print(nama)

# Hasil prediksi output
# Andi 
# kay


print ("Challenge 2 — Scope")
def hitung():
    angka = 10 # Local variabel
    print(angka) # bisa -> 10

hitung()
# print(angka) # tidak bisa karena tidak ada variabelnya

# Hasil prediksi output
# 10
# error


print ("Challenge 3 — Lambda")
# Tugas:
# Buat function kecil untuk menghitung kuadrat sebuah angka.
# Target:
# kuadrat(5)
# menghasilkan:
# 25
# Tapi kali ini jangan gunakan def.
# 💡 Gunakan pola:
# nama = lambda parameter: hasil

kuadrat = lambda angka: angka**2

print(kuadrat(5))


print ("Challenge FINAL — Gabungkan Lambda + List")
# Tugas:
# Diberikan:
# angka = [1, 2, 3, 4, 5]
# Buat lambda bernama kuadrat untuk menghitung kuadrat.
# Kemudian gunakan list comprehension untuk menghasilkan kuadrat dari semua angka.
# Target:
# [1, 4, 9, 16, 25]
# 💡 Kamu sudah mempelajari dua-duanya secara terpisah:
# kuadrat = lambda angka: angka ** 2
# dan:
# hasil = [sesuatu for nilai in angka]
# Sekarang tinggal gabungkan.

angka = [1, 2, 3, 4, 5]

kuadrat = lambda angka: angka**2

hasil = [kuadrat(nilai) for nilai in angka]
print(hasil)
