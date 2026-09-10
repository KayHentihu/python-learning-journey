from modules.penjumlahan import penjumlahan
from modules.pengurangan import pengurangan
from modules.perkalian import perkalian
from modules.pembagian import pembagian
from modules.modulus import modulus
from modules.tunggu_enter import tunggu_enter

def menu_calculator():
    
    while True:
        try:          
            print("===== KALKULATOR SEDERHANA =====")
            print("1. Penjumlahan")
            print("2. Pengurangan")
            print("3. Perkalian")
            print("4. Pembagian")
            print("5. Modulus")
            print("0. Keluar")
            print("--------------------------------")
            pilihan = int(input("Pilih menu (0-5): "))
            
            if pilihan > 0 and pilihan <= 5:  
                angka_a = int(input("Masukkan angka pertama: "))
                angka_b = int(input("Masukkan angka kedua: "))
                           
            match pilihan:
                
                case 1:
                    operasi = penjumlahan
                    simbol = "+"
                case 2:
                    operasi = pengurangan
                    simbol = "-"
                case 3:
                    operasi = perkalian
                    simbol = "x"
                case 4:
                    operasi = pembagian
                    simbol = "/"
                case 5:
                    operasi = modulus
                    simbol = "%"
                case 0:
                    print("\nProgram berakhir, Terima kasih!")
                    return
                case _:
                    print("\nAngka tidak valid, tolong masukkan angka (0-5)")
                    tunggu_enter()
                    continue
            
            hasil = operasi(angka_a, angka_b)
            print(f"\nHasil dari {angka_a} {simbol} {angka_b} = {hasil}")
            tunggu_enter()
                    
        except ValueError:
            print("\nInput tidak valid, tolong masukkan angka!!")    
            tunggu_enter()
