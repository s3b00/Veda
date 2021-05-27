from django.urls import path, re_path

from . import views
from VEDA import settings

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    re_path('^login$', views.login_view, name="login"),               # страница авторизации
    re_path('^registration$', views.register, name="register"),       # страница регистрации
    re_path('^group/(?P<pk>\S+)$', views.group, name="group"),       # страница конкретной группы, доступ по ключу
    re_path('^group_enter/(?P<pk>\d+?)$', views.group_enter, name="group_enter"),       # страница для входа в группу по id
    re_path('^group_out/(?P<pk>\d+?)$', views.group_out, name="group_out"),       # страница для выхода из группы по id
    re_path('^group_create$', views.create_group, name="create_group"),       # страница создания группы
    re_path('^group_post/(?P<pk>\d+?)$', views.group_post, name="group_post"),       # страница создания поста для группы
    re_path('^group_search$', views.group_search, name="group_search"),       # поиск группы по уникальному идентификатору
    re_path('^set_status_group/(?P<pk>\d+?)$', views.update_status_group, name="update_status_group"),       # обновление статуса пользователя в группе (модератор/слушатель)
    re_path('^kick_user_group/(?P<pk>\d+?)$', views.kick_user, name="kick_user"),       # кик пользователя из группы
    re_path('^get_results/(?P<pk>\d+?)$', views.get_results, name="get_results"),       # получить ведомость на электронную почту
    re_path('^set_sheet/(?P<pk>\d+?)$', views.set_lesson, name="set_sheet"),       # изменить состояние записи урока (или удалить)
    re_path('^add_sheet/(?P<pk>\d+?)$', views.add_lesson, name="add_sheet"),       # добавить в расписание новый урок
    re_path('^add_discipline/(?P<pk>\d+?)$', views.add_discipline, name="add_discipline"),       # добавить новый предмет в дисциплины группы
    re_path('^remove_discipline/(?P<pk>\d+?)$', views.remove_discipline, name="remove_discipline"),       # удалить  предмет из дисциплин группы
    re_path('^recover$', views.recover, name="recover"),              # восстановление пароля
    re_path('^logout$', views.logout_view, name="logout"),            # выход из учетной записи
    re_path('^settings$', views.settings, name="settings"),           # переход в настройки учетной записи
    re_path('^update_user/(?P<pk>\d+?)$', views.update_user, name="update_user"),           # обновление настроек пользователя
    re_path('^update_password/(?P<pk>\d+?)$', views.update_password, name="update_password"),           # обновление пароля пользователя
    re_path('^update_father$', views.update_father, name="update_father"),           # обновление информации об отце пользователя
    re_path('^update_mother$', views.update_mother, name="update_mother"),           # обновление информации об матери пользователя
    re_path('^update_userpic$', views.update_userpic, name="update_userpic"),           # обновление аватарки пользователя
    re_path('^faq$', views.faq, name="faq"),                          # страница о проекте и ответы на вопросы
    re_path('^profile/(?P<pk>\d+?)$', views.profile, name="profile"), # страница конкретного пользователя
    re_path('^post$', views.post, name="post"),                       # урл создания поста админа
    re_path('^notification/(?P<pk>\d+?)$', views.remove_notification, name="remove_notification"),        # урл удаления уведомления
    re_path('^add_notes/(?P<pk_group>\d+)/(?P<pk_user>\d+)', views.add_note, name="add_note"),        # урл добавления оценки в группу
    re_path('^remove_notes/(?P<pk>\d+)$', views.remove_note, name="remove_note"),        # урл добавления оценки в группу
    re_path('^notice/(?P<pk>\d+?)$', views.add_notice, name="add_notice"),                                # урл создания объявления в группе
    re_path('^remove_notice/(?P<pk>\d+?)$', views.remove_notice, name="remove_notice"),                   # урл удаления задачи пользователю из группы
    re_path('^add_task/(?P<pk>\d+?)$', views.add_task, name="add_task"),                                  # урл добавления задачи из группы
    re_path('^update_task/(?P<pk>\d+?)$', views.update_task, name="update_task"),                         # урл обновления статуса задачи из группы
    re_path('^remove_task/(?P<pk>\d+?)$', views.remove_task, name="remove_task"),                         # урл удаления задачи из группы
    path('', views.index, name="index")        # главная страница
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
