from django.contrib import admin
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    re_path('^index$', views.index, name="index"),
    re_path('^login$', views.login, name="login"),
    re_path('^registration$', views.register, name="register"),
    re_path('^recover$', views.recover, name="recover"),
    re_path('^faq$', views.faq, name="faq"),
    re_path('', views.template)
]
