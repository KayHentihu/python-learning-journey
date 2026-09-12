def validasi_nama(nama):
    nama_tanpa_spasi = nama.replace(" ", "")
    
    if len(nama.strip()) == 0:
        print("\nNama tidak boleh kosong!!")
        return False
    if not nama_tanpa_spasi.isalpha():
        print("\nNama tidak boleh angka!!")
        return False
    return True

def validasi_nim(nim, mahasiswa, mahasiswa_edit):
    if not nim.isdigit():
        print("\nNIM harus berupa angka!!")
        return False
    
    for data in mahasiswa:
        if nim == data.nim and data != mahasiswa_edit:
            print("\nNIM ini sudah ada!!")
            return False   
        
    return True
    
def validasi_semester(semester):
    semester_tanpa_spasi = semester.replace(" ", "")
    if len(semester.strip()) == 0:
        print("\nSemester tidak boleh kosong!!")
        return False
    if semester_tanpa_spasi.isalpha():
        print("\nSemester harus berupa angka!!")
        return False
    if int(semester) < 1 or int(semester) > 9:
        print("\nSemester tidak valid!!")
        return False
    return True   
