from django.db import models


class User(models.Model):
    username = models.CharField('Username', max_length=50)
    first_name = models.CharField('First Name', max_length=50)
    last_name = models.CharField('Last Name', max_length=50)
    email = models.EmailField('Email', max_length=100)
    birth_date = models.DateField('Date')
    password1 = models.CharField('Password1', max_length=25)
    password2 = models.CharField('Password2', max_length=25)

    def __str__(self):
        return f"{self.first_name}  {self.last_name}"

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

