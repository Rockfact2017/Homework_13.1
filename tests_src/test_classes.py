import unittest

from classes import Category, Product


class TestCategory(unittest.TestCase):

    def test_init(self):
        category = Category("Clothing", "A category of clothing products", ["T-shirt", "Jeans", "Dress"])
        self.assertEqual(category.name, "Clothing")
        self.assertEqual(category.description, "A category of clothing products")
        self.assertEqual(category.products, ["T-shirt", "Jeans", "Dress"])
        self.assertEqual(Category.total_categories, 1)
        self.assertEqual(Category.total_unique_products, 3)

    def test_add_product(self):
        category = Category("Clothing", "A category of clothing products", ["T-shirt", "Jeans", "Dress"])
        category.add_product("Sweater")
        self.assertEqual(category.products, ["T-shirt", "Jeans", "Dress", "Sweater"])
        self.assertEqual(Category.total_unique_products, 4)

    def test_remove_product(self):
        category = Category("Clothing", "A category of clothing products", ["T-shirt", "Jeans", "Dress"])
        category.remove_product("Jeans")
        self.assertEqual(category.products, ["T-shirt", "Dress"])
        self.assertEqual(Category.total_unique_products, 2)


class TestProduct(unittest.TestCase):

    def test_init(self):
        product = Product("T-shirt", "A basic cotton T-shirt", 10.00, 20)
        self.assertEqual(product.name, "T-shirt")
        self.assertEqual(product.description, "A basic cotton T-shirt")
        self.assertEqual(product.price, 10.00)
        self.assertEqual(product.quantity_in_stock, 20)

    def test_add_to_stock(self):
        product = Product("T-shirt", "A basic cotton T-shirt", 10.00, 20)
        product.add_to_stock(10)
        self.assertEqual(product.quantity_in_stock, 30)

    def test_remove_from_stock(self):
        product = Product("T-shirt", "A basic cotton T-shirt", 10.00, 20)
        product.remove_from_stock(5)
        self.assertEqual(product.quantity_in_stock, 15)
