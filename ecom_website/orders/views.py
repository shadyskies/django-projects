from django.shortcuts import render
from .models import Order, OrderItem, Cart
from fresh.models import Products
from django.shortcuts import get_object_or_404, redirect
from users.models import Profile
from django.contrib.auth.decorators import login_required
from datetime import datetime


@login_required
def add_to_cart(request, pk):
    prod = get_object_or_404(Products, pk=pk)

    # TODO: use signals to autocreate cart obj on user creation
    # TODO: check if available
    # checking if cart_obj exists
    if Cart.objects.filter(user=request.user).exists():
        # if orderitem exists
        cart_obj = Cart.objects.get(user=request.user)
        order_item_obj = OrderItem.objects.get(cart=cart_obj)
        if OrderItem.objects.filter(product=prod).exists():
            order_item_obj.quantity += 1

        else:
            order_item_obj = OrderItem(product=prod, cart=cart_obj, price=prod.price)

        cart_obj.subtotal += prod.price
        cart_obj.updated = datetime.now()
        order_item_obj.save()
        cart_obj.save()

    else:
        # create Cart obj
        cart_obj = Cart.objects.create(user=request.user)
        oi = OrderItem(product=prod, cart=cart_obj, price=prod.price)
        oi.save()
        cart_obj.subtotal = prod.price
        cart_obj.save()
    return redirect('/shop/')


def remove_from_cart(request, pk):
    prod = get_object_or_404(Products, p_id=pk)
    cart_obj = get_object_or_404(Cart, user=request.user)
    order_item_obj = OrderItem(cart=cart_obj)

    order_item_obj.quantity -= 1
    order_item_obj.price = order_item_obj.get_cost()
    cart_obj.subtotal -= prod.price
    cart_obj.updated = datetime.now()
