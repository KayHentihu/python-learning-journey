mahasiswa = {
    "nama": "Kay",
    "umur": 20,
    "jurusan": "Informatika"
}

# key       value
# -------------------------
# nama   →  Kay
# umur   →  20
# jurusan → Informatika

print(mahasiswa["nama"]) # untuk mengambil data, kita menggunakan key, bukan index.

#tantangan
print("Tantangan 1")
mahasiswa = {
    "nama": "Kay",
    "umur": 20,
    "jurusan": "Informatika"
}
print(mahasiswa["jurusan"])

print("Tantangan 2 — Mengubah Value")
mahasiswa = {
    "nama": "Kay",
    "umur": 20,
    "jurusan": "Informatika"
}
mahasiswa["umur"] = 21
print(mahasiswa)

print("Tantangan 3 — Menambah data")
mahasiswa = {
    "nama": "Kay",
    "umur": 20,
    "jurusan": "Informatika"
}
mahasiswa["semester"] = 3
print(mahasiswa)

print("Tantangan 4 — Looping Dictionary")
mahasiswa = {
    "nama": "Kay",
    "umur": 20,
    "jurusan": "Informatika"
}

for key in mahasiswa:
    print(f"{key} : {mahasiswa[key]}")