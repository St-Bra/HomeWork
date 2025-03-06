class Car:
    def __init__(self, color = None, type = None, year = None):
        self.color = color
        self.type = type
        self.year = year

    def starting_the_car(self):
        print('Автомобиль заведён')

    def car_shutdown(self):
        print('Автомобиль заглушен')

    def car_color(self, color):
        self.color = color

    def car_type(self, type):
        self.type = type

    def car_year(self, year):
        self.year = year

first_car = Car('red', 'sedan', 2025)
first_car.starting_the_car()
first_car.car_type('hatchback')
print(first_car.type)
first_car.car_shutdown()