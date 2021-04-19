class Mangga:

    def __init__(self, nama, jumlah):
        self.nama = nama
        self.jumlah = jumlah

    def __repr__(self):
        return f"ini {self.nama}"

    #__str__
    #__add__


a = Mangga("hahaha", 100)

print(a)