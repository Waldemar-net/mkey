from django.shortcuts import render

# Create your views here.
from unicodedata import category
from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404
from django.views.generic.edit import FormMixin
from django.views.generic import DetailView
from django.urls import reverse
from publisher.models import Publishers
from goods.models import Products
from users.models import User



def publisher(request, publisher_name_slug):
    page = request.GET.get('page', 1)
    publisher_obj = Publishers.objects.get(slug=publisher_name_slug)
    products = Products.objects.filter(publisher=publisher_obj)

    paginator = Paginator(products, 12)
    current_page = paginator.page(page)

    context = {
        "title": "MKEY - Издатели",
        'products': current_page,
        'slug_url' : publisher_name_slug,
        'publisher': publisher_obj,
    }
    return render(request, "publisher/publisher.html", context=context)

def publishers(request):
    page = request.GET.get('page', 1)
    publishers = Publishers.objects.all()
    products = Products.objects.all()

    paginator = Paginator(publishers, 8)
    current_page = paginator.page(page)
    context = {
        "title": "MKEY - Все издатели",
        'publishers': current_page,
        'products' : products,
        'publishers_int' : publishers
    }
    return render(request, "publisher/publishers.html", context=context)





