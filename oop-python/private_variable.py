class Hero:
    #class variable
    jumlah = 0

    def __init__(self, name, health):
        #object variable
        self.name = name
        self.health = health

        # private variable
        self.__private = "privatecuy"

        # protected variable
        self._protected = "protectedcuy"


lina = Hero("lina", 100)

print(lina.__dict__)
