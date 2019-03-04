from django.db import models

class Location(models.Model):
    location_name = models.CharField(max_length=40)

    def __str__(self):
        return self.location_name

class Category(models.Model):
    category_name = models.CharField(max_length=40)

class Image(models.Model):
    image=models.ImageField(upload_to = '')
    image_name=models.CharField(max_length=100)
    image_description=models.CharField(max_length=100)
    image_location=models.ForeignKey(Location, null=True)
    image_category=models.ManyToManyField(Category)

    def __str__(self):
        return self.image_name

    @classmethod
    def images_all(cls):
        images = cls.objects.filter()
        return images

    class Meta:
        ordering = ['image_name']

    def save_image(self):
        self.save()

