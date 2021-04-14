from django.contrib import admin
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    re_path('^login$', views.login, name="login"),                  # страница авторизации
    re_path('^registration$', views.register, name="register"),     # страница регистрации
    re_path('^recover$', views.recover, name="recover"),            # восстановление пароля
    re_path('^faq$', views.faq, name="faq"),                        # страница о проекте и ответы на вопросы
    re_path('', views.index, name="index")                          # главная страница
]
