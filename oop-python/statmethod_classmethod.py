class Hero:
    __jumlah = 0

    def __init__(self, name):
        self.__name = name
        Hero.__jumlah += 1

    #method untuk object, tidak untuk class
    def getJumlah(self):
        return Hero.__jumlah

    #method untuk class, tidak untuk onject
    def getJumlahc():
        return Hero.__jumlah

    #static method (decorator) -> untuk object dan class
    @staticmethod
    def getJumlahStatic():
        return Hero.__jumlah

    #class method
    @classmethod
    def getJumlahClass(cls):
        return cls.__jumlah




sniper = Hero("sniper")
print(sniper.getJumlah())
print(Hero.getJumlahc())
print(Hero.getJumlahStatic())
print(sniper.getJumlahStatic())
print(Hero.getJumlahClass())
