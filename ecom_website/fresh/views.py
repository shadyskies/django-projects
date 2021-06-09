from django.shortcuts import render
from .models import Products, Insta_images, Blog_model
from django.template import RequestContext
from orders.models import OrderItem, Order, Cart
from django.contrib.auth.decorators import login_required


# TODO: implement rating
@login_required
def index(request):
    blogs = Blog_model.objects.all()
    cart_obj = Cart.objects.get(user=request.user)
    cart_item = OrderItem.objects.filter(cart=cart_obj)
    context = {
        "cart_obj": cart_obj,
        "cart_item": cart_item,
        "blogs": blogs
    }
    return render(request, 'fresh/index.html',context=context)


@login_required
def shop(request):
    cart_obj = Cart.objects.get(user=request.user)
    cart_item = OrderItem.objects.filter(cart=cart_obj)
    context = {
        "cart_obj": cart_obj,
        "cart_item": cart_item
    }
    return render(request, 'fresh/shop.html', context=context)


def cart(request):
    cart_obj = Cart.objects.get(user=request.user)
    order_item = OrderItem.objects.filter(cart=cart_obj)
    context = {
        "cart_obj": cart_obj,
        "cart_item": order_item
    }
    return render(request, 'fresh/cart.html', context=context)


def shop_detail(request, pk):
    products = Products.objects.all()[:5]
    cart_obj = Cart.objects.get(user=request.user)
    order_item = OrderItem.objects.filter(cart=cart_obj)

    # specific item to display
    prod_item_sp = Products.objects.get(p_id=pk)
    context = {
        "products": products,
        "cart_obj": cart_obj,
        "cart_item": order_item,
        "sp": prod_item_sp
    }
    return render(request, 'fresh/shop-detail.html', context=context)


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
