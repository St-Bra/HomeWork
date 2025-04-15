class BeeElephant:
    """Класс ПчёлоСлон с частями пчелы и слона."""

    def __init__(self, bee_part, elephant_part):
        self.bee_part = bee_part           # Часть пчелы
        self.elephant_part = elephant_part  # Часть слона
        self.energy = 50                    # Энергия существа (от 0 до 100)

    def fly(self):
        """Метод, проверяющий, может ли существо летать."""
        return self.bee_part >= self.elephant_part

    def trumpet(self):
        """Метод, издающий звук. Завист от пропорции частей."""
        return "tu-tu-doo-doo" if self.elephant_part >= self.bee_part else "wzzzz"

    def eat(self, food):
        """Метод еды. Если нектар — прибавляет энергию, если трава — отнимает."""
        if food == "nectar":
            self.energy = min(100, self.energy + 10)  # Энергия не превышает 100
        elif food == "grass":
            self.energy = max(0, self.energy - 10)  # Энергия не может быть меньше 0

    def get_info(self):
        """Метод, возвращающий текущие параметры существа."""
        return f"ПчёлоСлон: {self.bee_part} пчела, {self.elephant_part} слон, энергия {self.energy}"


# Пример использования
creature = BeeElephant(5, 10)
print(creature.get_info())  # ПчёлоСлон: 5 пчела, 10 слон, энергия 50

print(creature.fly())  # False (не может летать)
print(creature.trumpet())  # "tu-tu-doo-doo" (как слон)

creature.eat("nectar")
print(creature.get_info())  # Энергия 60

creature.eat("grass")
creature.eat("grass")
print(creature.get_info())  # Энергия 40