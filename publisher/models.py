from django.db import models

# Create your models here.
class Publishers(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    image = models.ImageField(upload_to="goods_images",blank=True, null=True, verbose_name="Изображение")

    class Meta:
        db_table = 'publishers'
        verbose_name = 'Издателя'
        verbose_name_plural = 'Издатели'
    def __str__(self):
        return self.name  

