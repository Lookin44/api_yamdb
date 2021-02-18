from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='категория')
    slug = models.SlugField(primary_key=True, unique=True, verbose_name='уникальное имя')

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=200, verbose_name='жанр')
    slug = models.SlugField(primary_key=True, unique=True, verbose_name='уникальное имя')

    def __str__(self):
        return self.name
