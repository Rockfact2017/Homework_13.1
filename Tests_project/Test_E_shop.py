import pytest

class Category:
    name: str
    description: str
    products: list
    total_categories: int = 0
    total_unique_products: int = 0


    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.total_categories += 1
        Category.total_unique_products += 1


class Product:
    name: str
    description: str
    price: float
    quantity_in_stock: int

    def __init__(self, name, description, price, quantity_in_stock):
        self.name = name
        self.description = description
        self.price = price
        self.quantity_in_stock =quantity_in_stock


def test_category_initialization():
    category = Category("Electronics", "All things electronic", [])
    assert category.name == "Electronics"
    assert category.description == "All things electronic"
    assert category.products == []
    assert Category.total_categories == 1
    assert Category.total_unique_products == 0


def test_product_initialization():
    product = Product("iPhone 15", "The latest iPhone", 999.99, 10)
    assert product.name == "iPhone 15"
    assert product.description == "The latest iPhone"
    assert product.price == 999.99
    assert product.quantity_in_stock == 10


def test_category_product_count():
    category = Category("Electronics", "All things electronic", [])
    product1 = Product("iPhone 15", "The latest iPhone", 999.99, 10)
    product2 = Product("Macbook Pro", "The latest Macbook Pro", 1299.99, 5)
    category.products.append(product1)
    category.products.append(product2)
    assert len(category.products) == 2
    assert Category.total_unique_products == 2


def test_category_count():
    category1 = Category("Electronics", "All things electronic", [])
    category2 = Category("Clothing", "All things clothing", [])
    assert Category.total_categories == 2
