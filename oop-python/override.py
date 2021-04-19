class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def showInfo(self):
        print(f"{self.name} dengan Health {self.health}")


class Hero_intelligent(Hero):
    def __init__(self, name):
        super().__init__(name, 100)

    def showInfo(self):
        print(f"{self.name} dengan tipe intelligent")



class Hero_strength(Hero):
    def __init__(self, name):
        super().__init__(name, 100)


lina = Hero_intelligent("lina")
axe = Hero_strength("axe")

lina.showInfo()
axe.showInfo()

# print(help(lina))