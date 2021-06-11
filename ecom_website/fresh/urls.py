from django.urls import path, include
from .views import index, shop, cart, about, checkout, contact, gallery, wishlist, base, shop_detail, UserViewSet, ProductViewSet
# rest_framework
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)


urlpatterns = [
    path('', index, name='index'),
    path('shop/', shop, name='shop'),
    path('shop_detail/<int:pk>', shop_detail, name='shop_detail'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('gallery/', gallery, name='gallery'),
    path('wishlist/', wishlist, name='wishlist'),
    path('base/', base, name='base'),
    path('about/', about, name='about'),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
]