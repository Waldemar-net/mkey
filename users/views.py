from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from carts.models import Cart
from developer.models import Developers
from goods.forms import AddProductsForm
from goods.models import RAMPC, Categories, Direx, Disk, Genre, Languages, OCSystem, Platforms, ProcessorPC, Products, Region, Services
from publisher.models import Publishers
from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm, DataForm
from users.models import User
from django.core.mail import send_mail
from .forms import PasswordResetForm
import random
from django.template.loader import render_to_string
import string


def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('main:index'))
    
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            session_key = request.session.session_key

            if user:
                auth.login(request, user)
                

                if session_key:
                  
                    cart_user = Cart.objects.filter(user=user)
                    cart_guest = Cart.objects.filter(session_key=session_key)

                    
                    for item_guest in cart_guest:
                        item_user = cart_user.filter(product=item_guest.product).first()
                        if not item_user:
                            
                            item_guest.user = user
                            item_guest.save()
                            

                if request.POST.get('next', None):
                    return HttpResponseRedirect(request.POST.get('next'))
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()
        
    context = {
        'title' : 'MKEY - Авторизация',
        'form' : form
    }
    return render(request, 'users/login.html', context)

def registration(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('main:index'))

    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()

            session_key = request.session.session_key

            user = form.instance
            auth.login(request, user)

            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)

           
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()
        
    context = {
        'title' : 'MKEY - Регистрация',
        'form' : form
        
    }
    return render(request, 'users/registration.html', context)
@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)
        
    context = {
        'title' : 'MKEY - Профиль',
        'form' : form
    }
    return render(request, 'users/profile.html', context)


@login_required
def data(request):
    if request.method == "POST":
        form = DataForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
         
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')

            if password1 and password1 == password2:
                user.set_password(password1)
            user.save()

            return HttpResponseRedirect(reverse('users:data'))
    else:
        form = DataForm(instance=request.user)
        
    context = {
        'title': 'MKEY - Личные данные',
        'form': form
    }
    return render(request, 'users/data.html', context)

@login_required
def logout(request): 
    auth.logout(request)
    
    return redirect(reverse("main:index"))

def users_cart(request):
    context = {
        'title':'MKEY - Корзина'
    }
    return render(request, 'users/users_cart.html', context)

def my_orders(request):
    context = {
        'title':'MKEY - Мои заказы'
    }
    return render(request, 'users/my_orders.html', context)

def generate_random_password(length=8):
    """Генерация случайного пароля."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))
def password_reset(request):
    context = {
        'title': 'MKEY - Восстановление пароля',
    }
    
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
                new_password = generate_random_password()
                user.set_password(new_password)
                user.save()
                html_message = render_to_string('users/email_template.html', {
                    'new_password': new_password,
                })
                send_mail(
                    'Дорогой игрок, мы сбросили тебе пароль',
                    'Это текстовое содержимое письма, если HTML не поддерживается.',
                    'no-reply@mkey.top',
                    [email],
                    fail_silently=False,
                    html_message=html_message,
                )
                messages.success(request, 'Новый пароль был отправлен на ваш адрес электронной почты.')
                return redirect('users:login')  # Перенаправление на страницу входа
            except User.DoesNotExist:
                messages.error(request, 'Пользователь с таким адресом электронной почты не найден.')
    else:
        form = PasswordResetForm()
    
    context['form'] = form  # Добавляем форму в контекст
    return render(request, 'users/password_reset.html', context)

def add_product(request):
    product = Products.objects.all()
    category = Categories.objects.all()
    genres = Genre.objects.all()
    platform = Platforms.objects.all()
    system = OCSystem.objects.all()
    rampc = RAMPC.objects.all()
    directx_list = Direx.objects.all()
    disk_list = Disk.objects.all()
    languages_list = Languages.objects.all()
    region_list = Region.objects.all()
    services_list = Services.objects.all()
    publishers_list = Publishers.objects.all()
    developers_list = Developers.objects.all()
    processor_list = ProcessorPC.objects.all()

    context = {
        'title' : 'MKEY - Добавить игру',
        'product':product,
        'category' : category,
        'genres' : genres,
        'platform' : platform,
        'system' : system,
        'rampc' : rampc,
        'directx_list' : directx_list,
        'disk_list' : disk_list,
        'languages_list' : languages_list,
        'region_list' : region_list,
        'services_list' : services_list,
        'publishers_list' : publishers_list,
        'developers_list' : developers_list,
        'processor_list' : processor_list,
    }
    return render(request, "goods/add-game.html", context=context)

def add_new_game(request):
    if request.method == 'POST':
        form = AddProductsForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.name = form.cleaned_data['name']
            product.slug = form.cleaned_data['slug']
            product.description = form.cleaned_data['description']
            product.image = form.cleaned_data['image']
            product.poster = form.cleaned_data['poster']
            product.is_displayed = form.cleaned_data['is_displayed']
            product.price = form.cleaned_data['price']
            product.discount = form.cleaned_data['discount']
            product.category.set(form.cleaned_data['category'])
            product.genry.set(form.cleaned_data['genry'])
            product.platform = form.cleaned_data['platform']
            product.availabilitys = form.cleaned_data['availabilitys']
            product.datas = form.cleaned_data['datas']
            product.system = form.cleaned_data['system']
            product.processor = form.cleaned_data['processor']
            product.rampc = form.cleaned_data['rampc']
            product.videocard = form.cleaned_data['videocard']
            product.direx = form.cleaned_data['direx']
            product.disk = form.cleaned_data['disk']
            product.languages = form.cleaned_data['languages']
            product.region = form.cleaned_data['region']
            product.services = form.cleaned_data['services']
            product.additional = form.cleaned_data['additional']
            product.publisher.set(form.cleaned_data['publisher'])
            product.developer.set(form.cleaned_data['developer'])
            product.video = form.cleaned_data['video']
            product.save()
            return redirect(reverse('goods:add-product')) 
    else:
        form = AddProductsForm()
    
    return render(request, 'goods/add-new-game.html', {'form': form})
