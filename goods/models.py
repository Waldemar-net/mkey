from email.policy import default
from enum import unique
from logging.config import valid_ident
from tabnanny import verbose
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.templatetags.i18n import language
from django.urls import reverse
from django.utils.text import slugify

from publisher.models import Publishers
from developer.models import Developers



class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    is_displayed = models.BooleanField(default=False, verbose_name='Отображать')
    
    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
        
    def __str__(self):
        return self.name
class Genre(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    
    class Meta:
        db_table = 'genre'
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        
    def __str__(self):
        return self.name
class Availability(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    
    class Meta:
        db_table = 'availability'
        verbose_name = 'Наличие'
        verbose_name_plural = 'Наличие'
    def __str__(self):
        return self.name
    
class Platforms(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    
    class Meta:
        db_table = 'platforms'
        verbose_name = 'Платформу'
        verbose_name_plural = 'Платформы'
    def __str__(self):
        return self.name
 

class OCSystem(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    
    class Meta:
        db_table = 'system'
        verbose_name = 'Операционная система'
        verbose_name_plural = 'Операционные системы'
    def __str__(self):
        return self.name
    
class ProcessorPC(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    
    class Meta:
        db_table = 'processor'
        verbose_name = 'Процессор'
        verbose_name_plural = 'Процессоры'
    def __str__(self):
        return self.name    
    
class RAMPC(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    
    class Meta:
        db_table = 'ram'
        verbose_name = 'Оперативная память'
        verbose_name_plural = 'Оперативная память'
    def __str__(self):
        return self.name 

class VideoCard(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    
    class Meta:
        db_table = 'videocard'
        verbose_name = 'Видеокарты'
        verbose_name_plural = 'Видеокарта'
    def __str__(self):
        return self.name 

class Direx(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    
    class Meta:
        db_table = 'direx'
        verbose_name = 'Directx'
        verbose_name_plural = 'Directx'
    def __str__(self):
        return self.name 

class Disk(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    
    class Meta:
        db_table = 'disk'
        verbose_name = 'Место на диске'
        verbose_name_plural = 'Место на диске'
    def __str__(self):
        return self.name 
    

class Languages(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    
    class Meta:
        db_table = 'languages'
        verbose_name = 'Языковую поддержку'
        verbose_name_plural = 'Языковая поддержка'
    def __str__(self):
        return self.name
    
class Region(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    
    class Meta:
        db_table = 'region'
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы активации'
    def __str__(self):
        return self.name
    
class Services(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    
    class Meta:
        db_table = 'services'
        verbose_name = 'Сервис'
        verbose_name_plural = 'Сервисы активации'
        
    def __str__(self):
        return self.name
    


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to="goods_images",blank=True, null=True, verbose_name="Изображение")
    poster = models.ImageField(upload_to="goods_images",blank=True, null=True, verbose_name="Постер")
    is_displayed = models.BooleanField(default=False, verbose_name='Отображать на главном экране')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name="Цена")
    discount = models.DecimalField(default=0.00,blank=True, null=True, max_digits=7, decimal_places=0, verbose_name="Скидка в %")
    category = models.ManyToManyField(to=Categories, verbose_name="Категория")
    genry = models.ManyToManyField(Genre,verbose_name="Жанр")
    platform = models.ForeignKey(to=Platforms,on_delete=models.PROTECT, verbose_name="Платформа", blank=True, null=True)
    availabilitys = models.ForeignKey(to=Availability, on_delete=models.PROTECT, verbose_name="Наличие игры", blank=True, null=True)
    datas = models.DateField(blank=True, null=True, verbose_name="Даты выхода")
    system = models.ForeignKey(to=OCSystem,on_delete=models.PROTECT, verbose_name="Операционная система", blank=True, null=True)
    processor = models.ForeignKey(to=ProcessorPC,on_delete=models.PROTECT, verbose_name="Процессор", blank=True, null=True)
    rampc = models.ForeignKey(to=RAMPC, on_delete=models.PROTECT, verbose_name="Оперативная память", blank=True, null=True)
    videocard = models.ForeignKey(to=VideoCard, on_delete=models.PROTECT, verbose_name="Видеокарта", blank=True, null=True)
    direx = models.ForeignKey(to=Direx, on_delete=models.PROTECT, verbose_name="Directx", blank=True, null=True)
    disk = models.ForeignKey(to=Disk, on_delete=models.PROTECT, verbose_name="Необходимое место на диске", blank=True, null=True)
    languages = models.ForeignKey(to=Languages,on_delete=models.PROTECT, verbose_name="Языковая поддержка", blank=True, null=True)
    region = models.ForeignKey(to=Region, on_delete=models.PROTECT, verbose_name="Регион активации", blank=True, null=True)
    services = models.ForeignKey(to=Services,on_delete=models.PROTECT, verbose_name="Сервис активации", blank=True, null=True)
    additional = models.CharField(max_length=250,unique=False,blank=True, null=True, verbose_name="Дополнительная информация")
    publisher = models.ManyToManyField(to=Publishers, verbose_name="Издатель")
    developer = models.ManyToManyField(to=Developers, verbose_name="Разработчик")
    video = models.CharField(max_length=200, blank=True, null=True, verbose_name="Трейлер")
    
    
    class Meta:
        db_table = 'product'
        verbose_name = 'Игру'
        verbose_name_plural = 'Игры'
        ordering = ("id",)

    def get_absolute_url(self):
           return reverse("catalog:product", kwargs={"product_slug": self.slug})
       
        
    def __str__(self):
       
        return self.name
    
    
 

    def sale_price(self):
        if self.discount:
            return round(self.price - self.price*self.discount/100, 2)
        
        return self.price
        
    
class Gallery(models.Model):
    image = models.ImageField(upload_to="goods_images",blank=True, null=True, verbose_name="Изображения")
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, related_name='images', verbose_name="Скриншоты")   
    
    class Meta:
        verbose_name = 'Скриншот'
        verbose_name_plural = 'Скриншоты'
        
    