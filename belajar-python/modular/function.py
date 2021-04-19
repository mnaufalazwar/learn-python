def say_hello(nama):
    return f"Hello {nama}"

def total(*list_angka):
    hasil = 0
    for val in list_angka:
        hasil = hasil + val
    return hasil

