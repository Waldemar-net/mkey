from genericpath import exists
from urllib import response
from django.contrib import sessions
from django.shortcuts import redirect, render

from django.http import JsonResponse
from django.template.loader import render_to_string

from carts.models import Cart
from carts.utils import get_user_carts
from goods.models import Products
from users.views import users_cart

def cart_add(request):

    product_id = request.POST.get("product_id")
    
    product = Products.objects.get(id=product_id)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)
        if carts.exists():
            is_product_added = True
        else:
            Cart.objects.create(user=request.user, product=product)
            is_product_added = False
    else:
        carts = Cart.objects.filter(session_key=request.session.session_key, product=product)
        if carts.exists():
            is_product_added = True
        else:
            Cart.objects.create(session_key=request.session.session_key, product=product)
            is_product_added = False

        
    
    
    user_cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "carts/includes/included_cart.html", {"carts":user_cart}, request=request
    )
    response_data = {
        'message' : "Товар добавлен в корзину",
        "cart_items_html" : cart_items_html,
        "is_product_added": is_product_added,
    }

    return JsonResponse(response_data)


def cart_remove(request):
    cart_id = request.POST.get("cart_id")

    cart = Cart.objects.get(id=cart_id)
    cart.delete()

    user_cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "carts/includes/included_cart.html", {"carts":user_cart}, request=request
    )

    response_data = {
        "message" : "Товар удален",
        "cart_items_html" : cart_items_html,
    }

    return JsonResponse(response_data)
    

