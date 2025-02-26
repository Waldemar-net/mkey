from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='Изображение')
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=0, verbose_name="Скидка в %")
    
    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'
        
    def __str__(self):
        return self.username