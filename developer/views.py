from django.shortcuts import redirect, render

# Create your views here.
from unicodedata import category
from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404
from django.views.generic.edit import FormMixin
from django.views.generic import DetailView
from django.urls import reverse

from goods.models import Products
from developer.models import Developers


def developer(request, developer_name_slug):
    
    
    developer_obj = Developers.objects.get(slug=developer_name_slug)
    products = Products.objects.filter(developer=developer_obj)

    paginator = Paginator(products, 12)
    page = request.GET.get('page')
    current_page = paginator.get_page(page)

    context = {
        "title": "MKEY - Разработчики",
        'products': current_page,
        'slug_url' : developer_name_slug,
        'developer': developer_obj,
    }
    return render(request, "developer/developer.html", context=context)

def developers(request):
    
    developers = Developers.objects.all()
    products = Products.objects.all()

    paginator = Paginator(developers, 8)
    page = request.GET.get('page')
    current_page = paginator.get_page(page)

    context = {
        "title": "MKEY - Разработчики",
        'developers': current_page,
        'products' : products,
        'developers_int' : developers
    }
    return render(request, "developer/developers.html", context=context)




