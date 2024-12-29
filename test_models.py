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

    def test_update_product(self):
        self.product.price = 200
        self.product.save()
        updated_product = Product.objects.get(name="Test Product")
        self.assertEqual(updated_product.price, 200)
