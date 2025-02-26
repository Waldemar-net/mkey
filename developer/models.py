from django.db import models

# Create your models here.
class Developers(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    image = models.ImageField(upload_to="goods_images",blank=True, null=True, verbose_name="Изображение")

    class Meta:
        db_table = 'developers'
        verbose_name = 'Разработчик'
        verbose_name_plural = 'Разработчики'
    def __str__(self):
        return self.name 