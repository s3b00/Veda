from django.contrib import admin
from django.urls import path, re_path, include

from . import views
from VEDA import settings

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    re_path('^login$', views.login_view, name="login"),               # страница авторизации
    re_path('^registration$', views.register, name="register"),       # страница регистрации
    re_path('^group/(?P<pk>\d+?)$', views.group, name="group"),       # страница конкретной группы, доступ по ключу
    re_path('^recover$', views.recover, name="recover"),              # восстановление пароля
    re_path('^logout$', views.logout_view, name="logout"),            # выход из учетной записи
    re_path('^settings$', views.settings, name="settings"),           # переход в настройки учетной записи
    re_path('^faq$', views.faq, name="faq"),                          # страница о проекте и ответы на вопросы
    re_path('^profile/(?P<pk>\d+?)$', views.profile, name="profile"), # страница конкретного пользователя
    re_path('^post$', views.post, name="post"),                       # урл создания поста админа
    path('', views.index, name="index")                            # главная страница
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()