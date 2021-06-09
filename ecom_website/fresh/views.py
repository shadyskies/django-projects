from django.shortcuts import render
from .models import Products, Insta_images, Blog_model
from django.template import RequestContext
from orders.models import OrderItem, Order, Cart
from django.contrib.auth.decorators import login_required


# TODO: implement rating
def index(request):
    blogs = Blog_model.objects.all()
    return render(request, 'fresh/index.html',{"blogs":blogs})


@login_required
def shop(request):
    cart = Cart.objects.get(user=request.user)
    cart_item = OrderItem.objects.filter(cart=cart)
    insta_images = Insta_images.objects.all()
    products = Products.objects.all()
    return render(request, 'fresh/shop.html', {"insta_images": insta_images, "products": products, "cart_item": cart_item})


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
    cart = Cart.objects.get(user=request.user)
    cart_item = OrderItem.objects.filter(cart=cart)
    context = {
        'insta_images': insta_images,
        'cart_item': cart_item
    }
    return render(request, 'fresh/base.html', context=context)
