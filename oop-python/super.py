class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def showInfo(self):
        print(f"{self.name} dengan health = {self.health}")


class Hero_2(Hero):
    def __init__(self, name):
        # Hero.__init__(name, 100)
        super().__init__(name, 100)
        super().showInfo()


lina = Hero_2("lina")
print(lina.__dict__)