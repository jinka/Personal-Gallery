from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=40)

    class Meta:
        ordering = ['category_name']

    def __str__(self):
        return self.category_name

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
    def update_image(cls, id, description):
        cls.objects.filter(id=id).update(description = description)

    @classmethod
    def images_all(cls):
        images = cls.objects.all()
        return images


    @classmethod
    def search_by_location(cls,search_location):
        location_result = cls.object.filter(image_location__image__icontains=location)
        return location_result

        images_name = cls.objects.filter(image_name__icontains=search_image)
        return images_name

    @classmethod
    def search_by_category(cls,search_category):
        images = cls.objects.filter(image_category__category_name__icontains=search_category)
        return images
