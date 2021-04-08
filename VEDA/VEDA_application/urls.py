from django.contrib import admin
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    re_path('', views.template)
]
