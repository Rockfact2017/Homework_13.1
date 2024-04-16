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


def test_category_add_product(category):
    """Тест для проверки корректности добавления продукта в категорию."""
    new_product = Product("Skirt", "A stylish skirt", 25.00, 12)
    category.add_product(new_product)
    assert len(category.products) == 4
    assert Category.total_unique_products == 4


def test_product_create_product(product):
    """Тест для проверки корректности создания нового продукта."""
    new_product = Product.create_product("Shorts", "A pair of comfortable shorts", 15.00, 18)
    assert new_product.name == "Shorts"
    assert new_product.description == "A pair of comfortable shorts"
    assert new_product.price == 15.00
    assert new_product.quantity_in_stock == 18


def test_product_add_product(product):
    """Тест для проверки корректности добавления продукта к существующему продукту."""
    new_product = Product.add_product("T-shirt", "A basic cotton T-shirt", 12.00, 15, [product])
    assert new_product.name == "T-shirt"
    assert new_product.description == "A basic cotton T-shirt"
    assert new_product.price == 12.00
    assert new_product.quantity_in_stock == 35


def test_product_set_price(product):
    """Тест для проверки корректности изменения цены продукта."""
    product.price = 15.00
    assert product.price == 15.00


def test_product_set_price_invalid(product):
    """Тест для проверки корректности обработки некорректного значения цены продукта."""
    with pytest.raises(ValueError):
        product.price = -10.00
