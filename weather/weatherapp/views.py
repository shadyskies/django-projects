from django.shortcuts import render
from .retrieve_openweather import retrieve
from rest_framework import viewsets, permissions
from .models import WeatherModel
from .serializers import WeatherSerializer


def home(request):
    retrieved = retrieve()
    context = {
        "retrieved": retrieved
    }
    return render(request, "weatherapp/home.html", context=context)


class WeatherViewSet(viewsets.ModelViewSet):
    queryset = WeatherModel.objects.all().order_by('id')
    serializer_class = WeatherSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] #toggle auth to view api route