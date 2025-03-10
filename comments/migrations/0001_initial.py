# Generated by Django 4.2.16 on 2024-10-21 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('created_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'db_table': 'comments_user',
            },
        ),
        migrations.CreateModel(
            name='CommentsResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.TextField(blank=True, null=True, verbose_name='Ответ')),
                ('created_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comments.comments', verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Ответ на комментарий',
                'verbose_name_plural': 'Ответы на комментарии',
                'db_table': 'comments_response',
            },
        ),
    ]
