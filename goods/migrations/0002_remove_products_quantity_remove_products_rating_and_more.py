# Generated by Django 4.2.16 on 2024-11-23 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='products',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='products',
            name='category',
        ),
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.ManyToManyField(to='goods.categories', verbose_name='Категория'),
        ),
    ]
