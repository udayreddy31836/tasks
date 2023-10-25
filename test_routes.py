from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from your_project.models import Product  # Import your Product model
from your_project.serializers import ProductSerializer  # Import your ProductSerializer

class ProductRoutesTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.product = Product.objects.create(
            name="Sample Product",
            description="This is a sample product.",
            price=100.00,
            category="Electronics",
            availability="In Stock"
        )
        self.product_data = {
            'name': 'New Product',
            'description': 'This is a new product.',
            'price': 150.00,
            'category': 'Clothing',
            'availability': 'Out of Stock',
        }
        self.url = reverse('product-list')

    def test_read_product(self):
        response = self.client.get(reverse('product-detail', args=[self.product.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_product(self):
        response = self.client.put(reverse('product-detail', args=[self.product.id]), self.product_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_product(self):
        response = self.client.delete(reverse('product-detail', args=[self.product.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_list_all_products(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_products_by_name(self):
        response = self.client.get(self.url, {'name': 'Sample Product'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_products_by_category(self):
        response = self.client.get(self.url, {'category': 'Electronics'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_products_by_availability(self):
        response = self.client.get(self.url, {'availability': 'In Stock'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
