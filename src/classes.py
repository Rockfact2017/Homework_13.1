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
        return self() * self.quantity_in_stock + other() * other.quantity_in_stock


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


