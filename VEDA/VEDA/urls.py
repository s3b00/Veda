from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin', admin.site.urls),
    re_path('', include('VEDA_application.urls')) # пересылает на VEDA_apllication и его урлы
]
