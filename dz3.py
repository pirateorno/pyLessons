class soda:
    def __init__(self, add = ""):
        self.add = add

    def show_my_drink(self, add):
        if add != "":
            print(f"Газована вода з {add}")
        else:
            print("Звичайна газована вода")

cola = soda("cola")
water = soda()

cola.show_my_drink(cola.add)
water.show_my_drink(water.add)
