from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from VEDA_application.models import Admin_post, Notification

def template(request):
    return render(request, 'main_template.html', context={
        'groups': models.Group.objects.all()
    })


def index(request):
    """ Основная страница сайта, где расположены
        группы пользователя, их новости и блог разработчика """

    if request.method == 'GET':
        return render(request, 'index.html', context={
            'admin_posts': models.Admin_post.objects.all(),
            'l_groups': models.Group.objects.filter(listeners__user__username=request.user.username),                     # группы, где есть текущий пользователь
            'm_groups': models.Group.objects.filter(moderators__user__username=request.user.username),                     # группы, где есть текущий пользователь
            'group_posts': models.Group_post.objects.filter(group__listeners__user__username=request.user.username),    # посты в группах, в которых находится пользователь
            'notifications': models.Notification.objects.filter(receiver__user__username=request.user.username),        # уведомления для пользователя
            'tasks': models.Task.objects.filter(receiver__user__username=request.user.username)                         # задачи из группа для пользователя
        })


def logout_view(request):
    """ View для выхода из аккаунта авторизированного пользователя, в любом случае 
        (даже если не авторизирован пользователь) - возвращает на основную страницу """


    logout(request)
    return HttpResponseRedirect(reverse('index'))


def login_view(request):
    """ Страница входа в учетную запись пользователя, должна обрабатывать
        сохранение, вход и переходы на главную страницу, восстановление пароля
        и регистрацию пользователя """

    if request.method == 'GET':
        return render(request, 'login.html', context={

        })
    if request.method == "POST":
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'login.html', context={
                'error': True
        })


def register(request):
    """ Страница регистрации, обрабатывает выдачу формы для ввода данных
        нового пользователя, а также принимает POST запрос на создание нового пользователя """

    if request.method == "GET":
        return render(request, 'register.html', context={

        })
    if request.method == "POST":
        try:
            user = User.objects.create_user(username=request.POST.get('username'), 
                email=request.POST.get('email'), 
                first_name=request.POST.get('firstname'), 
                last_name=request.POST.get('secondname'), 
                password=request.POST.get('password'))
                
            user.client.hobbies = request.POST.get('hobbies')
            user.client.day_of_birthday = request.POST.get('dob')
            user.client.adress = request.POST.get('address')
            user.client.gender = request.POST.get('gender')
            user.client.status = ""

            user.save()

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
        except Exception as e:
            return render(request, 'register.html', context={
                'error': e
            })
    

def profile(request, pk):
    """ Отдает страницу профиля, и, в случае, если это профиль пользователя, то может принять
        UPDATE запрос на изменение данных профиля """

    if request.method == "GET":
        client = get_object_or_404(models.Client, pk=pk)
        groups = models.Group.objects.filter(listeners__user__username=client.user.username)

        return render(request, 'profile.html', context={
            'client': client,
            'groups': groups
        })


def post(request):
    """ Страница конкретного поста блога (как группы, так и разработчика), может быть POST,
        тогда создает новый пост в области создания """

    if request.method == "GET":
        return render(request, 'post.html', context={

        })
    if request.method == "POST":
        if request.user.is_staff:
            newPost = Admin_post(author=request.user.client, article=request.POST.get('article'), text=request.POST.get('content'))
            newPost.save()
        return HttpResponseRedirect(reverse('index'))  


def group(request, pk):
    """ Страница, отображающая всю основную информацию о комнате группы, принимает POST,
        чтобы создать страницу группы, UPDATE для изменения данных """

    if request.method == "GET":
        group = get_object_or_404(models.Group, pk=pk)

        return render(request, 'group.html', context={
            'group': group,
            'listeners': group.listeners.all(),
            'moderators': group.moderators.all(),
            'notices': models.Notice.objects.filter(group__id=group.id),
            'tasks': models.Task.objects.filter(group__id=group.id),
            'posts': models.Group_post.objects.filter(group__id=group.id),
        })


def faq(request):
    """ Страница ответов на основные вопросы к проекту """

    if request.method == "GET":
        return render(request, 'faq.html', context={

        })


def settings(request):
    """ Страница просмотра и изменения настроек пользователя """

    if request.method == "GET":
        return render(request, 'settings.html', context={

        })


def recover(request):
    """ Страница восстановления пароля пользователя """

    if request.method == "GET":
        return render(request, 'recover.html', context={

        })


def create_group(request):
    """ Страница создания комнаты группы """

    if request.method == "GET":
        return render(request, 'create_group.html', context={

        })


@login_required
def remove_notification(request, pk):
    """ Вьюшка для удаления уведомления """

    if request.method == "GET":
        notification = get_object_or_404(Notification, pk=pk)
        notification.delete()
        return HttpResponseRedirect(reverse('index'))  


@login_required
def add_notice(request, pk):
    """ Вьюшка для удаления уведомления """

    if request.method == "POST":
        group = get_object_or_404(models.Group, pk=pk)
        notice = models.Notice(group=group, author=request.user.client, message=request.POST.get('message'))
        notice.save()

        return HttpResponseRedirect(reverse('group', args=[group.id]))  
