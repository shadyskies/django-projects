from django.shortcuts import render
from .retrieve_openweather import retrieve


def home(request):
    retrieved = retrieve()
    context = {
        "retrieved": retrieved
    }
    return render(request, "weatherapp/home.html", context=context)