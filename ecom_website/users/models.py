from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from fresh.models import Products
from orders.models import OrderItem, Order


class Profile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=300, default='India')
    city = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=15, default='')
    image = models.ImageField(upload_to='images/profile_images/', blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(null=True)
    user_id = models.AutoField(primary_key=True)

    def __str__(self):
        return f"{self.username} Profile"

