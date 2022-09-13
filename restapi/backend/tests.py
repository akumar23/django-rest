from itertools import product
from django.test import TestCase 
from products.models import Product

class TestCase(TestCase):
    def testPost(self):
        product = Product(title="Newest Product")
        self.assertEqual(product.title, "Newest Product")
        self.assertEqual(product.content, None)
        self.assertEqual(product.price, 99.99)