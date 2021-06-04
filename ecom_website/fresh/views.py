from django.shortcuts import render
from .models import Products, Insta_images
from django.template import loader, RequestContext


#TODO: look into context processing
# using context processor to handle same contexts
def insta_images_context(request):
    insta_images = Insta_images.objects.all()
    return{
        'insta_images': insta_images
    }


def index(request):
    insta_images = Insta_images.objects.all()
    return render(request, 'fresh/index.html', {"insta_images": insta_images})


def shop(request):
    insta_images = Insta_images.objects.all()
    return render(request, 'fresh/shop.html', {"insta_images": insta_images})


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
    insta_images = Insta_images.objects.all()
    for i in insta_images:
        print(i.image)
        print(i.href)
    context = {
        'insta_images': insta_images
    }
    print(insta_images)
    return render(request, 'fresh/base.html', context=context)