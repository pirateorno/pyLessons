class Human:
    weight =  65
    Old = 80
    endurance = 100
    def __init__(self):
        print("Human")
        print("weight", self.weight)
        print("Old", self.Old)
        print("endurance", self.endurance)

class Elves(Human):
    Old = 500
    endurance = 897
    mana = 45
    def __init__(self):
        print("Elves")
        print("weight", self.weight)
        print("Old", self.Old)
        print("endurance", self.endurance)
        print("mana", self.mana)

class hobbyt(Human):
    endurance = 50
    def __init__(self):
        print("Elves")
        print("weight", self.weight)
        print("Old", self.Old)
        print("endurance", self.endurance)

a = Human()
b = Elves()
c = hobbyt()