from django.test import TestCase
from your_project.models import Product  # Import your Product model

class ProductModelTest(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name="Sample Product",
            description="This is a sample product.",
            price=100.00,
            category="Electronics",
            availability="In Stock"
        )

    def test_read_product(self):
        product = Product.objects.get(id=self.product.id)
        self.assertEqual(product.name, "Sample Product")

    def test_update_product(self):
        self.product.price = 120.00
        self.product.save()
        updated_product = Product.objects.get(id=self.product.id)
        self.assertEqual(updated_product.price, 120.00)

    def test_delete_product(self):
        product_count_before = Product.objects.count()
        self.product.delete()
        product_count_after = Product.objects.count()
        self.assertEqual(product_count_before - 1, product_count_after)

    def test_list_all_products(self):
        products = Product.objects.all()
        self.assertTrue(products.exists())

    def test_find_product_by_name(self):
        product = Product.objects.get(name="Sample Product")
        self.assertEqual(product.description, "This is a sample product.")

    def test_find_product_by_category(self):
        products = Product.objects.filter(category="Electronics")
        self.assertTrue(products.exists())

    def test_find_product_by_availability(self):
        products = Product.objects.filter(availability="In Stock")
        self.assertTrue(products.exists())
