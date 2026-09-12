from models import Mahasiswa
from validation import validasi_nim, validasi_nama, validasi_semester

def lihat_mahasiswa(mahasiswa):
    if len(mahasiswa) == 0:
        print("\nData masih kosong!")
        return
    
    for data in mahasiswa:
        print(f"NIM      : {data.nim}")
        print(f"Nama     : {data.nama}")
        print(f"Semester : {data.semester}\n")

def tambah_mahasiswa(mahasiswa):
    nim = input("Masukkan NIM      : ")
    if not validasi_nim(nim, mahasiswa, None):
        return
    
    nama = input("Masukkan Nama     : ")
    if not validasi_nama(nama):
        return
 
    
    semester = input("Masukkan Semester : ")
    
    if not validasi_semester(semester):
        return
    
    data_baru = Mahasiswa(nim, nama, semester)

    mahasiswa.append(data_baru)
    
    print("\nData berhasil ditambahkan!\n")
 
def edit_mahasiswa(mahasiswa):
    lihat_mahasiswa(mahasiswa)
    
    cari = input("Masukkan Nim yang ingin di edit: ")
    for data in mahasiswa:
        if cari == data.nim:
            nim_baru = input("Masukkan NIM (edit): ")
            
            if not validasi_nim(nim_baru, mahasiswa, data):
                return
            
            nama_baru = input("Masukkan Nama (edit): ")
            if not validasi_nama(nama_baru):
                return
            
            semester_baru = input("Masukkan semester (edit): ")
            if not validasi_semester(semester_baru):
                return
            
            data.nama = nama_baru
            data.nim = nim_baru
            data.semester = semester_baru
            print("\nData berhasil di edit!!")
            return
        
    print("\nNim tidak ditemukan!!")

def hapus_mahasiswa(mahasiswa):
    lihat_mahasiswa(mahasiswa)
        
    cari = input("Masukkan Nim yang ingin di hapus: ")
    for data in mahasiswa:
        if cari == data.nim:
            mahasiswa.remove(data)
            print("\nData berhasil di Hapus!!")
            return
        
    print("\nNIM tidak ditemukan!!")

