class Hero:

    def __init__(self, name, health, power, armor):
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor

    def serang(self, lawan):
        print(self.name + " menyerang " + lawan.name)
        lawan.diserang(self, self.power)

    def diserang(self, lawan, attack_lawan):
        print(self.name + " diserang " + lawan.name)
        self.health -= attack_lawan
        print(f"health {self.name} sisa {self.health}")


sniper = Hero("sniper", 100, 10, 100)
rikimaru = Hero("rikimaru", 100, 5, 100)

sniper.serang(rikimaru)
rikimaru.serang(sniper)
