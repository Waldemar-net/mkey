from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from developer.models import Developers
from developer.views import developer
from goods.models import Categories, Genre, Products
from django.conf.urls import handler404
from main.forms import ContactForm
from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings
import pas
import publisher
from publisher.models import Publishers



def index(request):
   
    categories = Categories.objects.filter(is_displayed=True).exclude(slug='all')
    products_by_category = {category: [] for category in categories}

    for product in Products.objects.filter(is_displayed=True):
        for category in product.category.all():
            if category in products_by_category:
                products_by_category[category].append(product)

    context = {
        'title': 'MKEY - Магазин игр',
        'products_by_category': products_by_category,
        'categories': categories
    }
    return render(request, 'main/index.html', context)

def mains(request):
    context = {
        'title':'MKEY - Магазин игр'
    }
    return render(request, 'main/main.html', context)

def agreement(request):
    context = {
        'title':'MKEY - Пользовательское соглашение',

    }
    return render(request, 'main/user-agreement.html', context)


def privacy(request):
    context = {
        'title':'MKEY - Политика конфиденциальности',
        
        
    }
    return render(request, 'main/privacy.html', context)

def support(request):
    context = {
        'title':'MKEY - Техническая поддержка',
        
        
    }
    return render(request, 'main/support.html', context)

def support_send(request):
    context = {
        'title':'MKEY - Отправить запрос',
        
        
    }
    return render(request, 'main/support-send.html', context)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            problem = form.cleaned_data['problem']
            email = form.cleaned_data['email']
            order_number = form.cleaned_data['order_number']

            subject = f'Новое обращение от {name}'
            message = f'Имя: {name}\nОписание: {problem}\nEmail: {email}\nНомер заказа: {order_number}'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = ['support@mkey.top']

            try:
                send_mail(subject, message, from_email, recipient_list)
                return redirect(reverse('main:support'))
            except Exception as e:
                return render(request, 'main/support.html', {'form': form, 'error': str(e)})  # Обработка ошибки
    else:
        form = ContactForm()

    return render(request, 'main/support.html', {'form': form})

def handler500(request):
    return render(request, '500.html', status=500)

def get_404(request):
    context = {
        'title':'MKEY - Страница не найдена',
    }
    return render(request, 'main/404.html', context)

def custom_404_view(request, exception):
    return render(request, 'main/404.html', status=404)

@login_required
def admin_panel(request):
    context = {
        'title':'MKEY - Административная панель',
    }
    return render(request, 'main/admin-panel.html', context)

@login_required
def admin_panel_game_add(request):
    context = {
        'title':'MKEY - Административная панель',
    }
    return render(request, 'main/add-game.html', context)

@login_required
def add_game(request):
    if request.method == 'POST':
        url = request.POST.get('url') 
        classes_to_parse = ['b-card__table-value', 'b-card__table-title', 'b-breadcrumbs__item', 'b-card__tabdescription', 'b-card__subinfo-item']
    
        pas.parse_website(url, classes_to_parse)

    context = {
        'title':'MKEY - Административная панель',
    }
    return render(request, 'main/add-game.html', context)

def mob_menu_catalog(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '')


    category = Categories.objects.filter(is_displayed=True)
    developer = Developers.objects.all()
    publisher = Publishers.objects.all()
    genre = Genre.objects.all()
    context = {
        'title':'MKEY - Каталог игр',
        'category' : category,
        'developer' : developer,
        'publisher' : publisher,
        'genre' : genre
    }
    
    if 'Mobi' in user_agent or 'Android' in user_agent:
        return render(request, 'main/menu-mobail.html', context) # Отображение мобильного меню
    else:
        return redirect('main:index')