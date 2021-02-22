from django.db import models

from users.models import User


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


class Review(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name="reviews")
    title = models.ForeignKey(Title,
                              on_delete=models.CASCADE,
                              related_name="reviews")
    text = models.TextField()
    score = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField("Дата добавления",
                                   auto_now_add=True,
                                   db_index=True)

    class Meta:
        ordering = ['-created']
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'],
                name='unique_review'
            )]


class Comment(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name="comments")
    review = models.ForeignKey(Review,
                               on_delete=models.CASCADE,
                               related_name="comments")
    text = models.TextField()
    created = models.DateTimeField("Дата добавления",
                                   auto_now_add=True,
                                   db_index=True)
