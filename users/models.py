from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Django's built-in user (hashed passwords) plus a birth date."""

    email = models.EmailField('Email', unique=True)
    birth_date = models.DateField('Дата рождения', null=True, blank=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.get_full_name() or self.username
