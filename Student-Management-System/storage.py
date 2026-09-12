from models import Mahasiswa

def load_data(mahasiswa):
    try:
        with open("mahasiswa.txt", "r") as file:
            data = file.readlines()
            
            for baris in data:
                baris = baris.strip("\n")
                hasil = baris.split("|")
                
                nim, nama, semester = hasil
                
                data_mahasiswa = Mahasiswa(nim, nama, semester)
                mahasiswa.append(data_mahasiswa)
    except FileNotFoundError:
        with open("mahasiswa.txt", "w") as file:
            pass
        
def save_data(mahasiswa):
    with open("mahasiswa.txt", "w") as file:
        for data in mahasiswa:
            file.write(f"{data.nim}|{data.nama}|{data.semester}\n")
