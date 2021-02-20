from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Title(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    year = models.IntegerField()

    def __str__(self):
        return self.name


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
