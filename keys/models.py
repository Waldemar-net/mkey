from django.db import models
from goods.models import Products
from users.models import User

class Keys(models.Model):
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Игра')
    keys = models.CharField(max_length=250, unique=True, verbose_name="Ключ")
    activated_key = models.BooleanField(default=False, verbose_name='Активирован')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления ключа')
    datas = models.DateField(blank=True, null=True, verbose_name="Даты активации")

    class Meta:
        db_table = 'key'
        verbose_name = "Игровые ключи"
        verbose_name_plural = "Игровые ключи"

    #objects = CartQueryset().as_manager()

    def __str__(self):
        return f'{self.product.name}'
