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
    re_path('^group_enter/(?P<pk>\d+?)$', views.group_enter, name="group_enter"),       # страница конкретной группы, доступ по ключу
    re_path('^group_out/(?P<pk>\d+?)$', views.group_out, name="group_out"),       # страница конкретной группы, доступ по ключу
    re_path('^group_create$', views.create_group, name="create_group"),       # страница создания группы
    re_path('^group_post/(?P<pk>\d+?)$', views.group_post, name="group_post"),       # страница создания группы
    re_path('^recover$', views.recover, name="recover"),              # восстановление пароля
    re_path('^logout$', views.logout_view, name="logout"),            # выход из учетной записи
    re_path('^settings$', views.settings, name="settings"),           # переход в настройки учетной записи
    re_path('^faq$', views.faq, name="faq"),                          # страница о проекте и ответы на вопросы
    re_path('^profile/(?P<pk>\d+?)$', views.profile, name="profile"), # страница конкретного пользователя
    re_path('^post$', views.post, name="post"),                       # урл создания поста админа
    re_path('^notification/(?P<pk>\d+?)$', views.remove_notification, name="remove_notification"),                       # урл создания поста админа
    re_path('^notice/(?P<pk>\d+?)$', views.add_notice, name="add_notice"),                                               # урл создания объявления в группе
    re_path('^remove_notice/(?P<pk>\d+?)$', views.remove_notice, name="remove_notice"),                                  # урл удаления объявления из группы
    path('', views.index, name="index")                            # главная страница
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()