from modules.penjumlahan import penjumlahan
from modules.pengurangan import pengurangan
from modules.perkalian import perkalian
from modules.pembagian import pembagian
from modules.modulus import modulus

def menu_calculator():
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
        
        try:
            angka_a = int(input("Masukkan angka pertama: "))
            angka_b = int(input("Masukkan angka kedua: "))
        except ValueError:
            print("Input tidak valid, tolong masukkan angka!!")    
            return
        
        match pilihan:
            
            case 1:
                hasil = penjumlahan(angka_a, angka_b)
            case 2:
                hasil = pengurangan(angka_a, angka_b)
            case 3:
                hasil = perkalian(angka_a, angka_b)
            case 4:
                hasil = pembagian(angka_a, angka_b)
            case 5:
                hasil = modulus(angka_a, angka_b)
        
        print(hasil)
                
    except ValueError:
        print("Input tidak valid, tolong masukkan angka (0-5)!!")    
 