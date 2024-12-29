# tests/test_routes.py

from rest_framework.test import APITestCase
from rest_framework import status
from yourapp.models import Product

class ProductRouteTest(APITestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product",
            description="Test Description",
            price=100,
            category="Test Category",
            availability=True
        )

    def test_read_product(self):
        response = self.client.get(f"/api/products/{self.product.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Test Product")
