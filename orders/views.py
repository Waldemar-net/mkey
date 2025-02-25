
from importlib.metadata import requires
import random
from django.contrib import messages
from django.db import transaction
from django.forms import ValidationError
from django.shortcuts import redirect, render
from django.db.models import Count
from django.utils import timezone
from carts.models import Cart
from keys.models import Keys
from orders.forms import CreateOrderForm
from orders.models import Order, OrderItem

def create_order(request):
    if request.method == "POST":
        form = CreateOrderForm(data=request.POST)
        
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_items = Cart.objects.filter(user=user)
                    if cart_items.exists():
                        order = Order.objects.create(
                            user = user,
                            email_delivery_adress=form.cleaned_data['email'],
                        )
                        import random

                        for cart_item in cart_items:
                            product = cart_item.product
                            name = cart_item.product.name
                            price = cart_item.product.sale_price()
                            keys_product = Keys.objects.filter(product=product, activated_key=False)
                            if any(not key.activated_key for key in keys_product):
                                free_keys = Keys.objects.filter(product=product, activated_key=False)
                                if not free_keys.exists():
                                    raise ValidationError(f'На данный момент ключей нет {product.name}')
                                key = random.choice(free_keys)

                            
                                OrderItem.objects.create(
                                    order=order,
                                    product=product,
                                    name=name,
                                    price=price,
                                    keys=key.keys,
                                )

                                
                                key.activated_key = True
                                key.datas = timezone.now()
                                key.user = user
                                key.save()

                                
                                cart_item.delete()
                            else:
                                ...
                            
                            

                        messages.success(request,'Заказ оформлен!')
                        return redirect("user:users-cart")
            except ValidationError as e:
                    messages.success(request, str(e))
                    print('False')
                    return redirect('user:users-cart')
            
        
            
        context = {
            'title' : "Оформление заказа",
            'form' : form,
        }
    else:
        initial = {
                "first_name" : request.user.first_name,
                "last_name" : request.user.last_name,
                "username" : request.user.username,
                'email' : request.user.username,
            }    
        form = CreateOrderForm(initial=initial)
    return render(request, 'users/users_cart.html')