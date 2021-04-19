def display_kontak(daftar_kontak):
    for kontak in daftar_kontak:
        print("------------------------")
        print(f"nama : {kontak['nama']}")
        print(f"telp : {kontak['telp']}")
    print("------------------------")

def tambah_kontak(daftar_kontak):
    print("------------------------")
    nama = input("Masukan nama : ")
    telp = input("Masukan telp : ")
    daftar_kontak.append({"nama":nama, "telp":telp})
    print("kontak berhasil ditambahkan")
    print("------------------------")

def hapus_kontak(daftar_kontak):
    print("------------------------")
    nama = input("Nama yang akan dihapus : ")
    index = -1
    for i in range(0, len((daftar_kontak))):
        kontak = daftar_kontak[i]
        if nama == kontak["nama"]:
            index = i
            break

    if index == -1:
        print("Kontak tidak tersedia")
    else:
        del daftar_kontak[index]
        print("Kontak telah dihapus")

    print("------------------------")

def cari_kontak(daftar_kontak):
    print("------------------------")
    nama_cari = input("Cari berdasarkan nama : ")
    ada = False

    for kontak in daftar_kontak:
        nama = kontak["nama"]
        if nama.lower().find(nama_cari.lower()) > -1:
            ada = True
            print("------------------------")
            print(f"nama : {kontak['nama']}")
            print(f"telp : {kontak['telp']}")

    if not ada:
        print("Kontak tidak tersedia")

    print("------------------------")