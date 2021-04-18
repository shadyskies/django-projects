from django.urls import path, include
from .views import home, WeatherViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'weather', WeatherViewSet)

urlpatterns = [
    path("", home, name="home"),
    path("api_home/", include(router.urls)),
    path("api_auth/", include('rest_framework.urls', namespace='weather-api-home')),
]