class Hero: # Template
    # class variable
    jumlah_hero = 0

    def __init__(self, inputName, inputPower):
        # instance variable
        self.name = inputName
        self.power = inputPower
        Hero.jumlah_hero += 1

    def siapa(self):
        print(f"namaku adalah {self.name}")

    def powerUp(self, up):
        self.power += up

    def getPower(self):
        return self.power

hero1 = Hero("sniper", 100)
hero2 = Hero("mario", 200)

hero1.siapa()
hero1.powerUp(66)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero1.power)