# Generated by Django 4.2.16 on 2024-11-23 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_remove_products_quantity_remove_products_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='discount',
            field=models.DecimalField(blank=True, decimal_places=0, default=0.0, max_digits=7, null=True, verbose_name='Скидка в %'),
        ),
    ]
