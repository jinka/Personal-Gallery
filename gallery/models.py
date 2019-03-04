from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=40)

    class Meta:
        ordering = ['category_name']

    def __str__(self):
        return self(category_name)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()


class Location(models.Model):
    location_name = models.CharField(max_length=40)

    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

class Image(models.Model):
    image=models.ImageField(upload_to = '')
    image_name=models.CharField(max_length=100)
    image_description=models.CharField(max_length=100)
    image_location=models.ForeignKey(Location, null=True)
    image_category=models.ManyToManyField(Category)

    class Meta:
        ordering = ['image_name']

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def images_all(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def search_by_location(cls,image_location):
        image = cls.objects.filter(location=image_location)
        return image
