def jumlahkan(x, *list_angka):
    total = 0
    for i in list_angka:
        total = total + i
    print(f"total = {total}")
    return (list_angka, total)


list_angka, total = jumlahkan(1,2,3,4,5,6)

print(type(list_angka))
print(type(total))

print(f"list_angka = {list_angka} \ntotal = {total}")