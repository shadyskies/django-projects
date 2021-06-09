from django.urls import path
from .views import add_to_cart, remove_from_cart

urlpatterns = [
    path('add_to_cart/<int:pk>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:pk>/', remove_from_cart, name='remove_from_cart')
]