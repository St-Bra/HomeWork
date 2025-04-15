class Bus:
    """Класс Автобус с пассажирами и скоростью."""

    def __init__(self, max_seats, max_speed):
        self.speed = 0  # Начальная скорость 0
        self.max_seats = max_seats  # Максимальное количество мест
        self.max_speed = max_speed  # Максимальная скорость
        self.passengers = {}  # Словарь {фамилия: место}
        self.free_seats = list(range(1, max_seats + 1))  # Список свободных мест

    def board(self, surname):
        """Посадка пассажира. Если есть места, добавляем в словарь."""
        if self.free_seats:
            seat = self.free_seats.pop(0)  # Берём первое свободное место
            self.passengers[surname] = seat
            print(f"{surname} сел на место {seat}.")
        else:
            print("Нет свободных мест!")

    def disembark(self, surname):
        """Высадка пассажира."""
        if surname in self.passengers:
            seat = self.passengers.pop(surname)
            self.free_seats.append(seat)
            self.free_seats.sort()
            print(f"{surname} покинул автобус.")
        else:
            print(f"{surname} не найден в автобусе.")

    def change_speed(self, delta):
        """Изменение скорости."""
        new_speed = self.speed + delta
        if 0 <= new_speed <= self.max_speed:
            self.speed = new_speed
            print(f"Скорость изменена: {self.speed} км/ч.")
        else:
            print("Ошибка: выход за пределы допустимой скорости!")

    def __contains__(self, surname):
        """Проверка, есть ли пассажир в автобусе."""
        return surname in self.passengers

    def __iadd__(self, surname):
        """Оператор += для посадки."""
        self.board(surname)
        return self

    def __isub__(self, surname):
        """Оператор -= для высадки."""
        self.disembark(surname)
        return self

    def show_passengers(self):
        """Вывод списка пассажиров."""
        print("Пассажиры автобуса:", self.passengers)


# Пример использования
bus = Bus(5, 100)

bus.board("Иванов")
bus.board("Петров")
bus.board("Сидоров")

bus.change_speed(50)
bus.change_speed(-10)

print("Иванов" in bus)  # True

bus += "Смирнов"  # Посадка
bus -= "Иванов"  # Высадка

bus.show_passengers()