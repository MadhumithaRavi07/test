# tests/test_models.py

from yourapp.models import Product
from django.test import TestCase

class ProductModelTest(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product",
            description="Test Description",
            price=100,
            category="Test Category",
            availability=True
        )

    def test_read_product(self):
        product = Product.objects.get(name="Test Product")
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.description, "Test Description")
