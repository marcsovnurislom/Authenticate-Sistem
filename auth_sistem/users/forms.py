from django.forms import ModelForm, TextInput, DateInput, EmailInput, PasswordInput

from .models import User


class UsersForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'birth_date', 'password1', 'password2']

        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username',
            }),
            "first_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First name',
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last name',
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'example@example.com',
            }),
            'birth_date': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'гггг-дд-мм',
            }),
            'password1': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password',
            }),
            'password2': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirm password',
            }),

        }