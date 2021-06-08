from django.shortcuts import render
from .models import Products, Insta_images, Blog_model
from django.template import loader, RequestContext
from orders.models import OrderItem, Order, Cart


#TODO: look into context processing
# using context processor to handle same contexts
def insta_images_context(request):
    insta_images = Insta_images.objects.all()
    return{
        'insta_images': insta_images
    }


# TODO: implement rating
def index(request):
    insta_images = Insta_images.objects.all()
    blogs = Blog_model.objects.all()
    products = Products.objects.all()[:4]
    context = {}
    return render(request, 'fresh/index.html', {"insta_images": insta_images, 'blogs': blogs, "products": products})


def shop(request):
    insta_images = Insta_images.objects.all()
    products = Products.objects.all()
    return render(request, 'fresh/shop.html', {"insta_images": insta_images, "products": products})


def cart(request):
    cart_obj = Cart.objects.get(user=request.user)
    order_item = OrderItem.objects.filter(cart=cart_obj)
    context = {
        "cart_obj": cart_obj,
        "order_item": order_item
    }
    return render(request, 'fresh/cart.html', context=context)


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