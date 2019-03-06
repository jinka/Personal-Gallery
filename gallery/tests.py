from django.test import TestCase
from . models import Image,Category,Location

# Create your tests here.
class CategoryTestClass(TestCase):
    def setup(self):
        self.animal = Category(category_name = 'Animals')

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.animal,Category))

