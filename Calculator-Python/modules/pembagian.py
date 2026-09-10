def pembagian(angka_a, angka_b):
    try:    
        hasil = angka_a / angka_b
        return hasil
    except ZeroDivisionError:
        return "Error, tidak bisa dibagi dengan 0 !!" 
