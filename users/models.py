from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    ROLE = [
        (USER, 'user'),
        (MODERATOR, 'moderator'),
        (ADMIN, 'admin')
        ]

    password = models.CharField(max_length=50, blank=True)
    email = models.EmailField(unique=True, blank=False)
    bio = models.TextField(blank=True)
    username = models.CharField(max_length=50, unique=True, blank=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    role = models.CharField(
        max_length=10,
        choices=ROLE,
        default=USER
    )
