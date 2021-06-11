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

    # TODO: check if available

    cart_obj = Cart.objects.get(user=request.user)
    # if orderitem exists
    if OrderItem.objects.filter(cart=cart_obj, product=prod).exists():
        order_item_obj = OrderItem.objects.get(cart=cart_obj, product=prod)
        order_item_obj.quantity += 1
        order_item_obj.price += prod.price

    #if orderitem doesnt exist
    else:
        order_item_obj = OrderItem(product=prod, cart=cart_obj, price=prod.price)

    cart_obj.subtotal += prod.price
    cart_obj.updated = datetime.now()
    order_item_obj.save()
    cart_obj.save()

    return redirect('/shop/')


@login_required
def remove_from_cart(request, pk):
    prod = get_object_or_404(Products, p_id=pk)
    cart_obj = get_object_or_404(Cart, user=request.user)
    order_item_obj = OrderItem.objects.filter(cart=cart_obj, product=prod)
    cart_obj.subtotal -= order_item_obj[0].price
    order_item_obj.delete()
    cart_obj.save()
    return redirect('/cart/')