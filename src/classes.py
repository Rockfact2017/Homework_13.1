class Category:
    name: str
    description: str
    products: list
    total_categories: int = 0
    total_unique_products: int = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.total_categories += 1
        Category.total_unique_products += len(set(products))

    def add_product(self, product):
        if not isinstance(product, Product) and not issubclass(type(product), Product):
            raise TypeError("В категорию можно добавлять только объекты класса Product и его наследников.")

        self.__products.append(product)

    @property
    def list_of_products(self):
        return "\n".join(
            [f"{product.name}, {product.price} руб. Остаток: {product.quantity_in_stock} шт." for product in
             self.__products])

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self.__products)} шт."

    def __len__(self):
        return len(self.__products)


class Product:
    name: str
    description: str
    price: float
    quantity_in_stock: int

    def __init__(self, name, description, price, quantity_in_stock):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity_in_stock = quantity_in_stock

    @classmethod
    def create_product(cls, name, description, price, quantity_in_stock):
        return cls(name, description, price, quantity_in_stock)

    @classmethod
    def add_product(cls, name, description, price, quantity_in_stock, products):
        for product in products:
            if product.name == name:
                product.quantity_in_stock += quantity_in_stock
                if product.price < price:
                    product.price = price
                return product
        return cls(name, description, price, quantity_in_stock)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена введена некорректно.")
        else:
            if self.__price > new_price:
                confirmation = input("Цена товара понижается. Подтвердите действие (y/n): ")
                if confirmation == "y":
                    self.__price = new_price
                else:
                    print("Действие отменено.")
            else:
                self.__price = new_price

            if self.__price < self.old_price:
                self.old_price = self.__price

    def __call__(self):
        return self.__price

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity_in_stock} шт."

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты класса Product и его наследников.")

        if not isinstance(self, type(other)):
            raise TypeError("Можно складывать только товары одного класса.")

        return self() * self.quantity_in_stock + other() * other.quantity_in_stock


class Smartphone(Product):
    def __init__(self, name, description, price, quantity_in_stock, performance, model, internal_memory, color):
        super().__init__(name, description, price, quantity_in_stock)
        self.performance = performance
        self.model = model
        self.internal_memory = internal_memory
        self.color = color

class Grass(Product):
    def __init__(self, name, description, price, quantity_in_stock, country_of_origin, germination_period, color):
        super().__init__(name, description, price, quantity_in_stock)
        self.country_of_origin = country_of_origin
        self.germination_period = germination_period
        self.color = color


# Создаем категорию "Электроника и другое"
electronics_and_others = Category("Электроника", "Категория товаров, связанных с электроникой", [])

# Создаем смартфон
smartphone = Smartphone("iPhone 14 Pro", "Новый iPhone 14 Pro", 1000.00, 10, "Высокая", "iPhone 14 Pro", 128, "Черный")

# Добавляем смартфон в категорию
electronics_and_others.add_product(smartphone)

# Создаем траву газонную
grass = Grass("Трава газонная", "Трава для газона", 15.00, 20, "Россия", "14 дней", "Зеленый")

# Добавляем траву газонную в категорию
electronics_and_others.add_product(grass)

# Выводим список продуктов в категории
print(electronics_and_others.list_of_products)


# class CategoryProducts:
#     def __init__(self, category, product):
#         self.product = product
#         self.category = category
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index < len(self.category.products):
#             product = self.category.products[self.index]
#             self.index += 1
#             return product
#         else:
#             raise StopIteration


