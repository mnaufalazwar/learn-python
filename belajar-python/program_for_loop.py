banyak = int(input("berapa banyak data?"))

nama = []
umur = []

for i in range(0, banyak):
    print(f"data ke {i}")
    input_nama = input("Nama : ")
    input_umur = input("Umur : ")

    nama.append(input_nama)
    umur.append(input_umur)

for i in range(0, len(nama)):
    print(f"Nama : {nama[i]} Umur : {umur[i]}")