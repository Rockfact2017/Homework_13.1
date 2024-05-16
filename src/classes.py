from abc import ABC, abstractmethod

class LoggingMixin:
    """
    Миксин для логирования создания объектов.
    Выводит в консоль сообщение о создании объекта.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(f"{self.__repr__()} создан.")  # Логирование создания объекта

    def __repr__(self):
        """
        Возвращает строковое представление объекта с его атрибутами.
        """
        attributes = ', '.join([f"{key}={value}" for key, value in self.__dict__.items()])
        return f"{self.__class__.__name__}({attributes})"

class AbstractProduct(ABC):
    """
    Абстрактный класс для продуктов.
    Определяет основные свойства и методы, которые должны быть реализованы в подклассах.
    """
    name: str
    description: str
    price: float
    quantity_in_stock: int

    @abstractmethod
    def __init__(self, name, description, price, quantity_in_stock):
        """
        Инициализирует объект продукта.
        """
        self.name = name
        self.description = description
        self._price = price
        self.quantity_in_stock = quantity_in_stock

    @abstractmethod
    def __str__(self):
        """
        Возвращает строковое представление продукта.
        """
        pass

    @property
    def price(self):
        """
        Возвращает цену продукта.
        """
        return self._price

    @price.setter
    def price(self, new_price):
        """
        Устанавливает новую цену продукта.
        Если цена понижается, запрашивает подтверждение.
        """
        if new_price <= 0:
            print("Цена введена некорректно.")  # Проверка корректности цены
        else:
            if self._price > new_price:
                confirmation = input("Цена товара понижается. Подтвердите действие (y/n): ")
                if confirmation == "y":
                    self._price = new_price
                else:
                    print("Действие отменено.")  # Отмена действия при отказе
            else:
                self._price = new_price

    def __call__(self):
        """
        Возвращает цену продукта при вызове объекта.
        """
        return self._price

    @abstractmethod
    def __add__(self, other):
        """
        Осуществляет сложение двух продуктов одного типа.
        """
        pass

class Product(LoggingMixin, AbstractProduct):
    """
    Класс, представляющий общий продукт.
    """
    def __init__(self, name, description, price, quantity_in_stock):
        super().__init__(name, description, price, quantity_in_stock)

    @classmethod
    def create_product(cls, name, description, price, quantity_in_stock):
        """
        Создает новый продукт.
        """
        return cls(name, description, price, quantity_in_stock)

    @classmethod
    def add_product(cls, name, description, price, quantity_in_stock, products):
        """
        Добавляет продукт к списку продуктов, увеличивая количество,
        если продукт с таким именем уже существует.
        """
        for product in products:
            if product.name == name:
                product.quantity_in_stock += quantity_in_stock
                if product.price < price:
                    product.price = price
                return product
        return cls(name, description, price, quantity_in_stock)

    def __str__(self):
        """
        Возвращает строковое представление продукта.
        """
        return f"{self.name}, {self._price} руб. Остаток: {self.quantity_in_stock} шт."

    def __add__(self, other):
        """
        Складывает количество на складе двух продуктов одного типа.
        """
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты класса Product и его наследников.")

        if not isinstance(self, type(other)):
            raise TypeError("Можно складывать только товары одного класса.")

        return self() * self.quantity_in_stock + other() * other.quantity_in_stock

class Smartphone(Product):
    """
    Класс, представляющий смартфон.
    """
    def __init__(self, name, description, price, quantity_in_stock, performance, model, internal_memory, color):
        super().__init__(name, description, price, quantity_in_stock)
        self.performance = performance
        self.model = model
        self.internal_memory = internal_memory
        self.color = color

    def __add__(self, other):
        """
        Складывает количество на складе двух смартфонов.
        """
        if not isinstance(other, Smartphone):
            raise TypeError("Можно складывать только объекты класса Smartphone.")

        return self() * self.quantity_in_stock + other() * other.quantity_in_stock

class Grass(Product):
    """
    Класс, представляющий газонную траву.
    """
    def __init__(self, name, description, price, quantity_in_stock, country_of_origin, germination_period, color):
        super().__init__(name, description, price, quantity_in_stock)
        self.country_of_origin = country_of_origin
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        """
        Складывает количество на складе двух видов газонной травы.
        """
        if not isinstance(other, Grass):
            raise TypeError("Можно складывать только объекты класса Grass.")

        return self() * self.quantity_in_stock + other() * other.quantity_in_stock

class Category:
    """
    Класс, представляющий категорию продуктов.
    """
    name: str
    description: str
    products: list
    total_categories: int = 0
    total_unique_products: int = 0

    def __init__(self, name, description, products):
        """
        Инициализирует объект категории.
        """
        self.name = name
        self.description = description
        self.__products = products
        Category.total_categories += 1
        Category.total_unique_products += len(set(products))

    def add_product(self, product):
        """
        Добавляет продукт в категорию.
        """
        if not isinstance(product, Product) and not issubclass(type(product), Product):
            raise TypeError("В категорию можно добавлять только объекты класса Product и его наследников.")

        self.__products.append(product)

    @property
    def list_of_products(self):
        """
        Возвращает список продуктов в категории в виде строки.
        """
        return "\n".join(
            [f"{product.name}, {product.price} руб. Остаток: {product.quantity_in_stock} шт." for product in
             self.__products])

    def __str__(self):
        """
        Возвращает строковое представление категории.
        """
        return f"{self.name}, количество продуктов: {len(self.__products)} шт."

    def __len__(self):
        """
        Возвращает количество продуктов в категории.
        """
        return len(self.__products)




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


