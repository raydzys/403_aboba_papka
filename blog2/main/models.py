from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
class Comment(models.Model):
    author = models.CharField(max_length=50, help_text='Автор комментария, ограниченный 50 символами')
    text = models.TextField(help_text='Текст комментария')
    created_at = models.DateTimeField(auto_now_add=True, help_text='Дата и время создания комментария')
    updated_at = models.DateTimeField(auto_now=True, help_text='Дата и время последнего обновления комментария')
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, help_text='Имя тега, ограниченное 50 символами')
    description = models.TextField(blank=True, null=True, help_text='Описание тега')
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text='Название категории, ограниченный 100 символами')
    description = models.TextField(blank=True, null=True, help_text='Описание категории')
class User(models.Model):
    name = models.CharField(max_length=50)

class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)

class Comment(models.Model):
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    article = models.ForeignKey('Article', on_delete=models.SET_NULL, null=True, blank=True)

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True, unique=True)
    description = models.TextField()
