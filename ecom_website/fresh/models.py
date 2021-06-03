from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=30)
    p_id = models.IntegerField(primary_key=True)
    price = models.IntegerField(blank=False, null=False)
    discount = models.BooleanField(default=False)
    image = models.ImageField()
