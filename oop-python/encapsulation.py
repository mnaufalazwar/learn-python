class Hero:

    def __init__(self, name, health):
        self.__name = name
        self.__health = health

    #getter
    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

    #setter
    def setHealth(self, val):
        self.__health = val


sniper = Hero("sniper", 100)

print(sniper.__dict__)