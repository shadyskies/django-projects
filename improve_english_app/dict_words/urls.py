from django.urls import path, include
from .views import home, search_view


urlpatterns = [
    path('', home, name='home'),
    path('search/<str:word>', search_view, name='search'),
]