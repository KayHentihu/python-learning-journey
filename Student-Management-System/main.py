from crud import lihat_mahasiswa, tambah_mahasiswa, edit_mahasiswa, hapus_mahasiswa
from storage import load_data, save_data

mahasiswa = []      
   
def menu():
    while True:
        print("============ MENU ==============")
        print("1. Tambah Mahasiswa")
        print("2. Lihat Mahasiswa")
        print("3. Edit Mahasiswa")
        print("4. Hapus Mahasiswa")
        print("0. Keluar")
        print("================================")
        pilih = int(input("Pilih menu: "))
        
        match pilih:
            case 1:
                tambah_mahasiswa(mahasiswa)
                save_data(mahasiswa)
            case 2:
                lihat_mahasiswa(mahasiswa)
            case 3:
                edit_mahasiswa(mahasiswa)
                save_data(mahasiswa)
            case 4:
                hapus_mahasiswa(mahasiswa)
                save_data(mahasiswa)
            case 0:
                print("\nProgram selesai, Terima kasih")
                return 

load_data(mahasiswa)
menu()
