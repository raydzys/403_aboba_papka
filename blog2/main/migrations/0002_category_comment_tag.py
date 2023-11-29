# Generated by Django 4.2.7 on 2023-11-15 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название категории, ограниченный 100 символами', max_length=100, unique=True)),
                ('description', models.TextField(blank=True, help_text='Описание категории', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(help_text='Автор комментария, ограниченный 50 символами', max_length=50)),
                ('text', models.TextField(help_text='Текст комментария')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Дата и время создания комментария')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Дата и время последнего обновления комментария')),
            ],
        ),
        migrations.CreateModel(
            name='tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Имя тега, ограниченное 50 символами', max_length=50, unique=True)),
                ('description', models.TextField(blank=True, help_text='Описание тега', null=True)),
            ],
        ),
    ]