from django.db import models
from users.models import User
from goods.models import Products

class Comments(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь')
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Игра')
    comments = models.TextField(blank=True, null=True, verbose_name='Комментарий')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        db_table = "comments_user"
        verbose_name = 'Комментарий'
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return f"Комментарий № {self.pk}"

class CommentsResponse(models.Model):
    comment = models.ForeignKey(to=Comments, on_delete=models.CASCADE, verbose_name="Комментарий")
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь')
    response = models.TextField(blank=True, null=True, verbose_name='Ответ')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        db_table = "comments_response"
        verbose_name = 'Ответ на комментарий'
        verbose_name_plural = "Ответы на комментарии"

    def __str__(self):
        return f"Ответ  {self.comment}"