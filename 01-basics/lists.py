# manual
buah1 = "Apel"
buah2 = "Mangga"
buah3 = "Jeruk"

# sudah di lists
buah = ["Apel", "Mangga", "Jeruk"]

#tantangan
print("tantangan 1")
buah = ["Apel", "Mangga", "Jeruk", "Pisang"]
print(buah)

print("tantangan 2")
buah = ["Apel", "Mangga", "Jeruk", "Pisang"]
print(buah[2])

print("tantangan 3")
buah = ["Apel", "Mangga", "Jeruk", "Pisang"]
print(buah[3])

print("tantangan 4")
buah = ["Apel", "Mangga", "Jeruk", "Pisang"]
buah[2] = "Semangka"
print(buah)

print("tantangan 5")
buah = ["Apel", "Mangga", "Semangka", "Pisang"]
buah.append("Durian")
print(buah)

print("tantangan 6")
buah = ["Apel", "Mangga", "Semangka", "Pisang", "Durian"]
buah.remove("Mangga")
print(buah)

print("tantangan 7")
buah = ["Apel", "Mangga", "Semangka", "Pisang"]
print(len(buah))

print("tantangan 8")
buah = ["Apel", "Mangga", "Semangka", "Pisang"]
for i in range(len(buah)):
    print(buah[i])
    
#alternatif
print("Cara alternatif")
for buah_item in buah:
    print(buah_item)
    
print("tantangan 9")
buah = ["Apel", "Mangga", "Semangka", "Pisang"]
for i in range(len(buah)):
    print(f"{i} - {buah[i]}")