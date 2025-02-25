from django import template
from django.utils.http import urlencode

from developer.models import Developers
from keys.models import Keys
from orders.models import Order
from publisher.models import Publishers
from goods.models import Categories, Genre, Services, Products

register = template.Library()


