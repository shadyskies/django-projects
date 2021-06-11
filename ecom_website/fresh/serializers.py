from rest_framework import serializers
from .models import Products
from django.contrib.auth.models import User



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Products
        fields = ('name', 'price', 'quantity_available', 'num_sold', 'rating')