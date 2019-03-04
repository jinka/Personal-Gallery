from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=40)

    def __str__(self):
        return self

class Location(models.Model):
    location_name = models.CharField(max_length=40)

    def __str__(self):
        return self.location_name
    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

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
        images = cls.objects.all()
        return images

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

