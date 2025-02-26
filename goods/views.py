from unicodedata import category
from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404
from django.views.generic.edit import FormMixin
from django.views.generic import DetailView



from goods.models import Products, Genre, Categories
from goods.utils import q_search


def catalog(request, category_slug=None):
    
    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    genry = request.GET.get('genry', None)
    query = request.GET.get('q', None)
    
    
    
    if category_slug == 'all':
        goods = Products.objects.all() 
        if genry and genry != "Все":
            goods = goods.filter(genry__name=genry) 
    elif query:
        goods = q_search(query)
    elif category_slug:
        goods = Products.objects.all() 
        goods = goods.filter(category__slug=category_slug) 
        if genry and genry != "Все": 
            goods = goods.filter(genry__name=genry) 
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))
    
    if on_sale:
        goods = goods.filter(discount__gt = 0)
        
    
    if order_by and order_by != "default":
        goods = goods.order_by(order_by)
        
    
    genre = Genre.objects.all()
    
    paginator = Paginator(goods, 12)
    current_page = paginator.page(page)
    
    
    context = { 
        "title": "MKEY - каталог товаров",
        "goods": current_page,
        "slug_url": category_slug,
        "genre" : genre,
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    context = {
        'title':f"Купить {product}",
        'product':product
    }
    return render(request, "goods/product.html", context=context)

def genry(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    context = {
        'product':product
    }
    return render(request, "goods/genry.html", context=context)

    
