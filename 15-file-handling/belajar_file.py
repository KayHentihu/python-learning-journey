from models import Mahasiswa

mahasiswa = []

with open("mahasiswa.txt", "w") as file:
    for data in mahasiswa:
        nim, nama, semester = data
        file.write(f"{nim}|{nama}|{semester}\n")
    
with open("mahasiswa.txt", "a") as file:
    file.write("\nIpit")
    
# with open("mahasiswa.txt", "r") as file:
#     data = file.readlines()
    
#     for baris in data:
#         baris = baris.strip()
#         hasil = baris.split("|")
#         nim, nama, semester = hasil
        
#         data_mahasiswa = Mahasiswa(nim, nama, semester)
#         mahasiswa.append(data_mahasiswa)
    
#     for data in mahasiswa:
#         print(data.nim)
#         print(data.nama)
#         print(data.semester)
        
# data = "001|kay|3"

# hasil = data.split("|")

# nim, nama, semester = hasil

# print(nim)
# print(nama)
# print(semester)