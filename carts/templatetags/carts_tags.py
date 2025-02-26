from atexit import register
from django import template

from carts.models import Cart
from carts.utils import get_user_carts
from keys.models import Keys

register = template.Library()

@register.simple_tag()
def user_carts(request):
    return get_user_carts(request)

@register.simple_tag()
def tag_Key(product):
    keys = Keys.objects.filter(product=product)
    if any(not key.activated_key for key in keys):
        return True
    else:
        return False
    

    