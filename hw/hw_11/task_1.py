class Soda:
    def __init__(self, taste=None):
        self.taste = taste

    def get_taste(self):
        if self.taste != None:
            print(f"У вас газировка с {self.taste[:-1].lower() + 'м'} вкусом")
        else:
            print("У вас обычная газировка")


strawberry_soda = Soda("Клубничный")
sparkling_water = Soda()

strawberry_soda.get_taste()
sparkling_water.get_taste()