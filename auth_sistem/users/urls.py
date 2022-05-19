from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.createUser, name='createUser'),
    path('user_home/', views.user_home, name='user_home'),
    path('', views.login, name='login'),
]