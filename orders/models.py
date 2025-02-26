from itertools import product
from tabnanny import verbose
from django.db import models
from goods.models import Products

from users.models import User

class OrderitemQueryset(models.QuerySet):

    def total_price(self):
        return sum(cart.products_price() for cart in self)
    
class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_DEFAULT, verbose_name='Пользователь', default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')
    email_delivery_adress = models.CharField(null=True, blank=True, verbose_name="Email")
    is_paid = models.BooleanField(default=False, verbose_name="Оплачено")
    status = models.CharField(max_length=50, default="В обработке", verbose_name="Статус заказа")

    class Meta:
        db_table = 'order'
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"Заказ № {self.pk}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name="Заказ")
    product = models.ForeignKey(Products, on_delete=models.SET_DEFAULT, null=True, verbose_name="Продукт", default=None)
    name = models.CharField(max_length=150, verbose_name="Название")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Цена")
    keys = models.CharField(null=True, blank=True, verbose_name="Ключ")
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата продажи')
    

    class Meta:
        db_table = "order_items"
        verbose_name = 'Проданный товар'
        verbose_name_plural = "Проданные товары"

    objects = OrderitemQueryset.as_manager()

    def products_price(self):
        return self.price
    
    def __str__(self):
        return f"Игра {self.name} | Заказ № {self.order.pk}"