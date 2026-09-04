print ("Challenge 1")
# Tugas
# Kita punya:

# angka = [1, 2, 3, 4, 5]

# Buat list baru yang berisi setiap angka dikali 2.

# Target output:

# [2, 4, 6, 8, 10]

angka = [1, 2, 3, 4, 5]

hasil = [nilai * 2 for nilai in angka] # [sesuatu for nilai in angka if kondisi]
print(hasil)


print ("Challenge 2")
# Tugas
# Diberikan:
# angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Buat list baru yang hanya berisi angka genap.
# Target:
# [2, 4, 6, 8, 10]

angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

hasil = [nilai for nilai in angka if nilai % 2 == 0] # [sesuatu for nilai in angka if kondisi]
print(hasil)


print ("Challenge 3")
# Tugas
# Diberikan:
# angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Buat list baru yang berisi kuadrat dari angka yang lebih besar dari 5.
# Target:
# [36, 49, 64, 81, 100]
# Jadi yang diproses hanya:
# 6 → 36
# 7 → 49
# 8 → 64
# 9 → 81
# 10 → 100

angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

hasil = [nilai**2 for nilai in angka if nilai > 5] # [sesuatu for nilai in angka if kondisi]
print(hasil)


print ("Challenge FINAL")
# Tugas
# Diberikan:
# nama = ["kay", "andi", "budi", "alex", "putra"]
# Buat list baru yang berisi nama dengan panjang 4 karakter atau lebih, dan semuanya diubah menjadi huruf kapital.
# Target:
# ["KAY", "ANDI", "BUDI", "ALEX", "PUTRA"]
# ⚠️ Tapi perhatikan: kay panjangnya 3, jadi seharusnya tidak masuk.
# Jadi target yang benar sebenarnya:
# ["ANDI", "BUDI", "ALEX", "PUTRA"]

nama = ["kay", "andi", "budi", "alex", "putra"]

hasil = [nilai.upper() for nilai in nama if len(nilai) >= 4] # [sesuatu for nilai in angka if kondisi]
print(hasil)