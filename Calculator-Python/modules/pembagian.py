def pembagian(angka_a, angka_b):
    try:    
        hasil = float(angka_a) / float(angka_b)
        return hasil
    except ZeroDivisionError:
        return "Error, tidak bisa dibagi dengan 0 !!" 
