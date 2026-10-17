from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import RegisterForm


@login_required
def user_home(request):
    return render(request, 'home.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('user_home')

    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('user_home')

    return render(request, 'register.html', {'form': form})
