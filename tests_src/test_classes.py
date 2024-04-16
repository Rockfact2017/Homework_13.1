
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


def test_product_init(product):
    """Тест для проверки корректности инициализации экземпляра класса Product."""
    assert product.name == "T-shirt"
    assert product.description == "A basic cotton T-shirt"
    assert product.price == 10.00
    assert product.quantity_in_stock == 20



