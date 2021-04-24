from django.shortcuts import render
from .models import Entries

def home(request):
    # print(Entries.objects.all())
    words = Entries.objects.all()
    return render(request, 'dict_words/home.html', {'words': words})