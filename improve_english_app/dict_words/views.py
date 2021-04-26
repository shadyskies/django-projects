from django.shortcuts import render
from .models import Entries
from .retrieve_random_words import get_words, get_sentence, search


def home(request):
    # print(Entries.objects.all())
    val = list(get_words())
    print(val)
    # get_sentence(val)
    return render(request, 'dict_words/home.html', {'words': val})


def search_view(request, word):
    val = list(search(word))
    return render(request, 'dict_words/search.html', {'words': val})
# TODO: implement missing word func
