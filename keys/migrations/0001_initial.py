# Generated by Django 4.2.16 on 2024-10-21 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keys', models.CharField(max_length=250, unique=True, verbose_name='Ключ')),
                ('activated_key', models.BooleanField(default=False, verbose_name='Активирован')),
                ('created_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления ключа')),
                ('datas', models.DateField(blank=True, null=True, verbose_name='Даты активации')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.products', verbose_name='Игра')),
            ],
            options={
                'verbose_name': 'Игровые ключи',
                'verbose_name_plural': 'Игровые ключи',
                'db_table': 'key',
            },
        ),
    ]
