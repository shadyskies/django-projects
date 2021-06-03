from django.urls import path, include
from .views import index, shop, cart, checkout, contact, gallery, wishlist, base


urlpatterns = [
    path('', index, name='index'),
    path('shop/', shop, name='shop'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('gallery/', gallery, name='gallery'),
    path('wishlist/', wishlist, name='wishlist'),
    path('base/', base, name='base'),
]