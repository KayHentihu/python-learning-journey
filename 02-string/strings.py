print("Tantangan 1")

nama = "kay"
print(nama.upper()) # .upper() untuk buat huruf kapital/ uppercase

print("Tantangan 2")

nama = "KAY"
print(nama.lower()) # .lower() untuk buat huruf lowercase

print("Tantangan 3")

nama = "   Kay   "
print(nama.strip()) # .strip() menghapus whitespace di awal dan akhir, bukan spasi di tengah.

print("Tantangan 4")

kalimat = "Saya suka Java"
print(kalimat.replace("Java", "Python")) # .replace("yang_mau_diganti", "penggantinya")

print("Tantangan 5")

email = "kay@example.com"

# .split("@") → memisahkan string berdasarkan "@"
# [0] → mengambil bagian pertama dari hasil split

print(email.split("@")[0]) # split() dulu → [0] kemudian

print("Tantangan FINAL")

nama = "   kay   "

print(nama.strip().upper()) 

