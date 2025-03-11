class Product:
    """Класс Товар с закрытыми полями: название, магазин и цена."""

    def __init__(self, name, store, price):
        self.__name = name       # Закрытое поле: название товара
        self.__store = store     # Закрытое поле: магазин
        self.__price = price     # Закрытое поле: цена

    def get_info(self):
        """Метод для получения информации о товаре."""
        return f"{self.__name} продаётся в {self.__store} за {self.__price} руб."


class Warehouse:
    """Класс Склад с закрытым массивом товаров."""

    def __init__(self):
        self.__products = []  # Закрытый список товаров

    def add_product(self, product):
        """Добавление товара в склад."""
        self.__products.append(product)

    def get_product_by_index(self, index):
        """Получение информации о товаре по индексу."""
        if 0 <= index < len(self.__products):
            return self.__products[index].get_info()
        return "Товар с таким индексом отсутствует"

    def get_product_by_name(self, name):
        """Поиск товара по имени."""
        for product in self.__products:
            if product._Product__name == name:
                return product.get_info()
        return "Товар не найден"

    def sort_products(self, key):
        """Сортировка товаров по ключу (названию, магазину, цене)."""
        if key == "name":
            self.__products.sort(key=lambda p: p._Product__name)
        elif key == "store":
            self.__products.sort(key=lambda p: p._Product__store)
        elif key == "price":
            self.__products.sort(key=lambda p: p._Product__price)

    def __add__(self, other):
        """Перегрузка оператора сложения — сумма цен всех товаров."""
        if isinstance(other, Warehouse):
            total_price = sum(p._Product__price for p in self.__products) + \
                          sum(p._Product__price for p in other.__products)
            return total_price
        return NotImplemented


# Пример использования
product1 = Product("Хлеб", "Магнит", 50)
product2 = Product("Молоко", "Пятёрочка", 80)
product3 = Product("Яблоки", "Ашан", 120)

warehouse1 = Warehouse()
warehouse1.add_product(product1)
warehouse1.add_product(product2)

warehouse2 = Warehouse()
warehouse2.add_product(product3)

# Вывод информации
print(warehouse1.get_product_by_index(0))  # Хлеб продаётся в Магнит за 50 руб.
print(warehouse1.get_product_by_name("Молоко"))  # Молоко продаётся в Пятёрочка за 80 руб.

# Сортировка по цене
warehouse1.sort_products("price")
print(warehouse1.get_product_by_index(0))  # Хлеб продаётся в Магнит за 50 руб.

# Сложение складов (общая стоимость всех товаров)
print(warehouse1 + warehouse2)  # 250