from django.shortcuts import render
from .models import Products


def index(request):
    return render(request, 'fresh/index.html', {})


def shop(request):
    return render(request, 'fresh/shop.html', {})


def cart(request):
    return render(request, 'fresh/cart.html', {})


def checkout(request):
    return render(request, 'fresh/cart.html')


def contact(request):
    return render(request, 'fresh/contact.html')


def gallery(request):
    return render(request, 'fresh/gallery.html')


def wishlist(request):
    return render(request, 'fresh/wishlist.html')


def base(request):
    return render(request, 'fresh/base.html')