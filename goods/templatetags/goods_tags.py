from itertools import product
from unicodedata import category
from django import template
from django.template.defaultfilters import length
from django.utils.http import urlencode

from carts.models import Cart
from comments.models import Comments
from developer.models import Developers
from keys.models import Keys
from orders.models import Order, OrderItem
from publisher.models import Publishers
from goods.models import Categories, Genre, Services, Products

register = template.Library()


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.simple_tag()
def tag_categories():
    return Categories.objects.all()

@register.simple_tag()
def tag_products():
    new_category = Categories.objects.filter(name='Новинки').first()
    
    if new_category:
        products = Products.objects.filter(category=new_category)
        return products
    else:
        return Products.objects.none()
    

@register.simple_tag()
def tag_products_like():
    new_category = Categories.objects.filter(name='Лучший выбор').first()
    
    if new_category:
        products = Products.objects.filter(category=new_category)
        return products
    else:
        return Products.objects.none()
    
@register.simple_tag()
def tag_products_sale():
    new_category = Categories.objects.filter(name='Скидки').first()
    
    if new_category:
        products = Products.objects.filter(category=new_category)
        return products
    else:
        return Products.objects.none()
    
@register.simple_tag()
def tag_products_podbor():
    new_category = Categories.objects.filter(name='Подборки').first()
    
    if new_category:
        products = Products.objects.filter(category=new_category)
        return products
    else:
        return Products.objects.none()

@register.simple_tag()
def tag_publisher():
    return Publishers.objects.all()

@register.simple_tag()
def tag_developer():
    return Developers.objects.all()

@register.simple_tag()
def tag_genre():
    return Genre.objects.all()

@register.simple_tag()
def tag_Services():
    return Services.objects.all()

@register.simple_tag()
def tag_Key(product):
    keys = Keys.objects.filter(product=product)
    if any(not key.activated_key for key in keys):
        return True
    else:
        return False

@register.simple_tag()
def tag_Orders(user):
    orders = Order.objects.filter(user=user)
    order_items = OrderItem.objects.filter(order__in=orders)
    return order_items

@register.simple_tag()
def tag_OrderStatus(user):
    orders = Order.objects.filter(user=user)
    
    return orders

@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)

@register.simple_tag()
def tag_GetCart(product):
    carts_game = Cart.objects.filter(product=product)
    if carts_game.exists():
        return False
    else:
        return True
    
@register.simple_tag()
def tag_Comments(product):
    comments = Comments.objects.filter(product=product)
    return comments

@register.simple_tag()
def tag_LenGameDeveloper(developer):
    int_product = Products.objects.filter(developer=developer)
    return int_product

@register.simple_tag()
def tag_LenGamePublisher(publisher):
    int_product = Products.objects.filter(publisher=publisher)
    return int_product

@register.filter
def game_declension(count):
    if count % 10 == 1 and count % 100 != 11:
        return f"{count} Игра"
    elif 2 <= count % 10 <= 4 and not (12 <= count % 100 <= 14):
        return f"{count} Игры"
    else:
        return f"{count} Игр"