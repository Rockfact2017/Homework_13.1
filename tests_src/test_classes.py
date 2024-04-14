import pytest

from classes import Category
from classes import Product

@pytest.fixture
def category():
    """Фикстура для создания экземпляра класса Category с корректными данными."""
    return Category(
        "Clothing",
        "A category of clothing products",
        [
            Product("T-shirt", "A basic cotton T-shirt", 10.00, 20),
            Product("Jeans", "A pair of denim jeans", 20.00, 15),
            Product("Dress", "A stylish dress", 30.00, 10),
        ],
    )


@pytest.fixture
def product():
    """Фикстура для создания экземпляра класса Product с корректными данными."""
    return Product("T-shirt", "A basic cotton T-shirt", 10.00, 20)


def test_category_init(category):
    """Тест для проверки корректности инициализации экземпляра класса Category."""
    assert category.name == "Clothing"
    assert category.description == "A category of clothing products"
    assert len(category.products) == 3
    assert Category.total_categories == 1
    assert Category.total_unique_products == 3


def test_category_add_product(category):
    """Тест для проверки метода add_product класса Category."""
    category.add_product(Product("Sweater", "A warm and cozy sweater", 25.00, 12))
    assert len(category.products) == 4
    assert Category.total_unique_products == 4


def test_category_remove_product(category):
    """Тест для проверки метода remove_product класса Category."""
    category.remove_product("Jeans")
    assert len(category.products) == 2
    assert Category.total_unique_products == 2


def test_product_init(product):
    """Тест для проверки корректности инициализации экземпляра класса Product."""
    assert product.name == "T-shirt"
    assert product.description == "A basic cotton T-shirt"
    assert product.price == 10.00
    assert product.quantity_in_stock == 20


def test_product_add_to_stock(product):
    """Тест для проверки метода add_to_stock класса Product."""
    product.add_to_stock(10)
    assert product.quantity_in_stock == 30


def test_product_remove_from_stock(product):
    """Тест для проверки метода remove_from_stock класса Product."""
    product.remove_from_stock(5)
    assert product.quantity_in_stock == 15
