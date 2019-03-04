from django.test import TestCase
from . models import Image

# Create your tests here.
class ImageTestClass(TestCase):
    def setup(self):
        self.image1=Image(image="Animal",image_name="Dog",image_description="White Red",image_location="Kenya",image_category="jjjj")


# Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image1,Image))

# Testing Save Mothod
    # def test_save_method(self):
    #     self.image.save_image()
    #     image = Image.objects.all()
    #     self.assertTrue(len(image)>0)