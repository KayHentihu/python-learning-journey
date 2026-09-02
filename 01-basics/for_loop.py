for i in range(5):
    print(i)
    
for i in range(2, 7): # range(start, stop pakai metode <)
    print(i)
    
for i in range(1, 11):
    print(f"10 * {i} = {10 * i}")
    
for i in range(0, 11, 2): # range(start, stop, step)
    print(i)
    
for i in range(10, 0, -1): # sama seperti tadi tapi decrement
    print(i)
    
# tantangan
for i in range(2, 11, 2):
    print(i)
    
for i in range(1, 11):
    print(f"{i} x 2 = {i * 2}")
    
for i in range(1, 11):
    print(f"{i} x 5 = {i * 5}")
    
jumlah = 0
for i in range(1, 11):
    jumlah = jumlah + i
print(jumlah)

jumlah = 0
for i in range(2, 11, 2):
    jumlah += i
print(jumlah)

jumlah = 0
for i in range(1, 10, 2):
    jumlah += i
print(jumlah)