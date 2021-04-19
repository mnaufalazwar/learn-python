class Hero:

    def __init__(self, name, health):
        self.__name = name
        self.__health = health

    def getName(self):
        return self.__name

    @property
    def info(self):
        return f"info = name : {self.__name}, health : {self.__health}"

    @property
    def health(self):
        pass

    @health.getter
    def health(self):
        return self.__health

    @health.setter
    def health(self, val):
        self.__health = val

    @health.deleter
    def health(self):
        self.__health = None

    def cobaPanggilGetter(self):
        print(f"coba panggil {self.health}")


sniper = Hero("sniper", 1000)

print(sniper.info)
print(sniper.health)

sniper.health = 666
print(sniper.info)
print(sniper.health)

del sniper.health
print(sniper.info)
print(sniper.health)

sniper.cobaPanggilGetter()
