from django.shortcuts import render, redirect

from .forms import UsersForm
from .models import User


def user_home(request):
    return render(request, 'home.html')


def createUser(request):
    error = ''
    usera = ''
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        email_bool = True
        if User.objects.filter(email=email):
            email_bool = True
        else:
            email_bool = False
        username = request.POST.get('username')
        username_bool = True
        if User.objects.filter(username=username):
            username_bool = True
        else:
            username_bool = False
        form = UsersForm(request.POST)
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if form.is_valid():
            if not username_bool:
                if not email_bool:
                    if password1 == password2:
                        form.save()
                        usera = User.objects.filter(email=email)
                        return redirect('user_home')
                    else:
                        error = 'Пароли не совпадают'
                else:
                    error = 'Такой email адресс уже существует.'
            else:
                error = 'Такoe имя пользователя уже существует.'
        else:
            error = 'Поля не заполнены корректно'

    form = UsersForm

    data = {
        "form": form,
        "error": error,
        "user": usera,
    }

    return render(request, 'register.html', data)


def login(request):
    error = ''
    usera = ''
    if request.method == 'POST':
        form = UsersForm(request.POST)
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        first_name = request.POST.get('first_name')
        if email != '' and username != '' and password1 != '' and password2 != '':
            if User.objects.filter(username=username):
                if User.objects.filter(email=email):
                    if User.objects.filter(password1=password1):
                        if password1 == password2:
                            usera = User.objects.get(username=username)
                            return redirect('user_home')
                        else:
                            error = 'Пароли не совпадают'
                    else:
                        error = 'Невильный пароль'
                else:
                    error = 'Такой email адресс не существует.'
            else:
                error = 'Такoe имя пользователя не существует.'
        else:
            error = 'Поля не заполнены корректно'

    form = UsersForm

    data = {
        "form": form,
        "error": error,
        'user': usera,
    }
    return render(request, 'login.html', data)



