from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import User


class BootstrapMixin:
    """Adds Bootstrap's form-control class to every widget."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault('class', 'form-control')


class RegisterForm(BootstrapMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'birth_date']
        labels = {
            'username': 'Имя пользователя',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }


class LoginForm(BootstrapMixin, AuthenticationForm):
    pass
