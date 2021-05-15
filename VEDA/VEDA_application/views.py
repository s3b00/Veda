from django.core.checks import messages
from django.dispatch.dispatcher import receiver
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from VEDA_application.models import Admin_post, Client, Discipline, Group, Group_post, Lesson, Note, Notice, Notification, Task

import json

from datetime import datetime

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
            'group_posts_listener': models.Group_post.objects.filter(group__listeners__user__username=request.user.username),    # посты в группах, в которых находится пользователь
            'group_posts_moderator': models.Group_post.objects.filter(group__moderators__user__username=request.user.username),    # посты в группах, в которых находится пользователь
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
            print(e)
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
            'sheet': models.Lesson.objects.filter(group__id=group.id),
            'disciplines': models.Discipline.objects.filter(group__id=group.id),
            'days': range(1, 32),
            'notes': Note.objects.filter(group__id=group.id)
        })


@login_required
def create_group(request):
    """ Страница создания комнаты группы """

    if request.method == "GET":
        return render(request, 'create_group.html', context={

        })
    elif request.method == "POST":
        data = json.loads(request.body)

        group = Group.objects.create(
            name = data['name'],
            tag = data['tag'],
            hNotices = data['hNotices'],
            hTasks = data['hTasks'],
            hSheet = data['hSheet'],
        )

        group.moderators.add(request.user.client)
        group.save()

        notification = Notification.objects.create(
            receiver=request.user.client,
            message=f'Вы создали группу {group.name}',
            priority=2
        )

        disciplines = []

        for lmo in data['mo']:
            if lmo not in disciplines:
                disciplines.append(lmo)

            lesson = Lesson(
                group=group,
                discipline=lmo,
                day=1,
            )
            
            lesson.save()
        
        for lt in data['tu']:
            if lt not in disciplines:
                disciplines.append(lt)

            lesson = Lesson(
                group=group,
                discipline=lt,
                day=2
            )
            
            lesson.save()

        for lwe in data['we']:
            if lwe not in disciplines:
                disciplines.append(lwe)

            lesson = Lesson(
                group=group,
                discipline=lwe,
                day=3
            )
            
            lesson.save()
   
        for lth in data['th']:
            if lth not in disciplines:
                disciplines.append(lth)

            lesson = Lesson(
                group=group,
                discipline=lth,
                day=4
            )
            
            lesson.save()
        
        for lfr in data['fr']:
            if lfr not in disciplines:
                disciplines.append(lfr)

            lesson = Lesson(
                group=group,
                discipline=lfr,
                day=5
            )
            
            lesson.save()

        for lsa in data['sa']:
            if lsa not in disciplines:
                disciplines.append(lsa)

            lesson = Lesson(
                group=group,
                discipline=lsa,
                day=6
            )
            
            lesson.save()
        
        for lsu in data['su']:
            if lsu not in disciplines:
                disciplines.append(lsu)

            lesson = Lesson(
                group=group,
                discipline=lsu,
                day=7
            )
            
            lesson.save()
        
        for discipline in disciplines:
            new_discipline = Discipline.objects.create(
                group = group,
                name = discipline
            )

        return HttpResponseRedirect(reverse('create_group'))


def group_enter(request, pk):
    """ Вью для входа в группу конкретного пользователя в группу под РК """

    if request.method == "POST":
        group = get_object_or_404(Group, pk=pk)

        group.listeners.add(request.user.client)
        group.save()

        moderators = group.moderators.all()

        for moderator in moderators:
            notification = Notification.objects.create(
                receiver = moderator,
                message = f'@{request.user.username} зашел в группу #{group.name}',
                priority = 2
            )

        return HttpResponseRedirect(reverse('index'))


def group_out(request, pk):
    """ Вью для выхода пользователя из группы """

    if request.method == "POST":
        group = get_object_or_404(Group, pk=pk)
        
        if request.user.client in group.listeners.all():
            group.listeners.remove(request.user.client)
        elif request.user.client in group.moderators.all():
            group.moderators.remove(request.user.client)
        
        group.save()

        moderators = group.moderators.all()

        for moderator in moderators:
            notification = Notification.objects.create(
                receiver = moderator,
                message = f'@{request.user.username} вышел из группы #{group.name}',
                priority = 2
            )

        return HttpResponseRedirect(reverse('index'))


def group_post(request, pk):
    """ Вью для создания постов в группе """

    if request.method == "POST":
        group = get_object_or_404(Group, pk=pk)

        group_post = Group_post.objects.create(
            group = group,
            article = request.POST.get('article'),
            text = request.POST.get('text'),
            author = request.user.client,
        )

        if request.FILES['file']:
            file = request.FILES['file']
            group_post.file.save()
            group_post.save()

        for listener in group.listeners.all():
            notification = Notification.objects.create(
                receiver = listener,
                message = f'В группе #{group.name} новый пост!',
                priority = 4
            )
        
        for moderator in group.moderators.all():
            notification = Notification.objects.create(
                receiver = moderator,
                message = f'В группе #{group.name} новый пост!',
                priority = 4
            )
        
        return HttpResponseRedirect(reverse('group', args=[pk]))



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


@login_required
def add_task(request, pk):
    """ Вью для добавления задачи пользователю в конкретной группе """

    if request.method=="POST":
        group = get_object_or_404(Group, pk=pk)
        user = get_object_or_404(Client, pk=request.POST.get('user'))

        task = Task.objects.create(
            group = group,
            receiver = user,
            content = request.POST.get('content'),
            status = 0
        )

        notification = Notification.objects.create(
            receiver = user,
            message = f"Вам пришла новая задача в группе #{group.name}",
            priority = 3
        )

        return HttpResponseRedirect(reverse('group', args=[pk]))


@login_required
def update_task(request, pk):
    """ Вью для изменения статуса выполнения задачи в конкретной группе """

    if request.method == "POST":
        task = get_object_or_404(Task, pk=pk)

        if task.status == 0:
            task.status = 1
        else:
            task.status = 0
        
        task.date_of_completion = datetime.now()

        task.save()

        return HttpResponseRedirect(reverse('group', args=[task.group.id]))


@login_required
def remove_task(request, pk):
    """  Вью для удаления задачи из конкретной группы """

    pass


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


@login_required
def remove_notice(request, pk):
    """ Вьюшка для удаления уведомления """

    if request.method == "POST":
        notice = get_object_or_404(Notice, pk=pk)
        group = get_object_or_404(Group, pk=notice.group.id)
        
        notice.delete()

        return HttpResponseRedirect(reverse('group', args=[group.id]))  
