class Hero:

    def __init__(self, name, health):
        self.__name = name
        self.__health = health


class Hero_1(Hero):
    pass


lina = Hero("lina", 100)
nana = Hero_1("nana", 666)

print(lina.__dict__)
print(nana.__dict__)
print(help(nana))
