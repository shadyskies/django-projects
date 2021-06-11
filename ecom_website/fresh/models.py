from django.db import models
from PIL import Image
from django.core.validators import MaxValueValidator, MinValueValidator


class Products(models.Model):
    name = models.CharField(max_length=30)
    p_id = models.AutoField(primary_key=True)
    price = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    discount = models.BooleanField(default=False)
    image = models.ImageField()
    rating = models.IntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(10)])
    num_sold = models.IntegerField(default=0, blank=True)
    quantity_available = models.PositiveIntegerField(default=100)

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.width > 370 or img.height > 350:
            output_size = (370, 350)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def  __str__(self):
        return f"Product: {self.name} id:[{self.p_id}]"


class Insta_images(models.Model):
    image = models.ImageField(upload_to='images/')
    href = models.URLField(max_length=128)

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.width > 400 or img.height > 400:
            output_size = (400, 400)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Blog_model(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/blog/')
