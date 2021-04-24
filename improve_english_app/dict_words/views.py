from django.shortcuts import render
from .models import Entries
from .retrieve_random_words import get_words

def home(request):
    # print(Entries.objects.all())
    val = list(get_words())
    print(val)
    return render(request, 'dict_words/home.html', {'words': val})