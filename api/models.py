from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='категория')
    slug = models.SlugField(
        primary_key=True,
        unique=True,
        verbose_name='уникальное имя'
    )

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=200, verbose_name='жанр')
    slug = models.SlugField(
        primary_key=True,
        unique=True,
        verbose_name='уникальное имя'
    )

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=200, verbose_name='название')
    year = models.IntegerField()
    description = models.TextField(verbose_name='описание')
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='категория',
        related_name='titles',
    )

    genre = models.ManyToManyField(
        Genre,
        related_name='titles',
    )
