from django.contrib.auth.models import User, AnonymousUser
from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.dispatch import receiver


class Parent(models.Model):
    """ Модель родителя предназначается для того, чтобы куратор
        имел доступ к данным об родителях пользователя группы """


    surname = models.CharField(max_length=30)       # Фамилия
    name = models.CharField(max_length=30)          # Имя
    middlename = models.CharField(max_length=30)    # Отчество
    job = models.CharField(max_length=60)           # Место работы
    date_of_birthday = models.DateField(null=True)  # Дата рождения
    phone = models.CharField(max_length=20)         # Номер телефона


class Client(models.Model):
    """ Модель клиента расширяет возможности модели пользователя,
        появляется дополнительные поля родителей, статуса, хобби и тому подобное """


    def __str__(self):
        return self.user.username

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )   # Связь один-к-одному с пользователем                        

    father = models.ForeignKey(
        Parent, 
        on_delete=models.SET_NULL,
        null=True,
        related_name='father'
    ) # Связь с родителем внешним ключем

    mother =  models.ForeignKey(
        Parent, 
        on_delete=models.SET_NULL,
        null=True,
        related_name='mother'
    ) # Связь с родителем внешним ключом

    status = models.CharField(max_length=100)                       # Поле статуса (отображается в профиле пользователя)
    hobbies = models.CharField(max_length=100)                      # Поле хобби (используется куратором и отображается в профиле)
    day_of_birthday = models.DateField(null=True)                   # Поле дня рождения (используется куратором и отображается в профиле)
    adress = models.CharField(max_length=50)                        # Поле адреса (используется только куратором и не виден в профиле)
    userpic = models.ImageField(upload_to='userpics', null=True)    # Аватар пользователя


# Два метода ниже - позволяет создавать клиента сразу, когда меняется пользователь (основа клиента)
@receiver(post_save, sender=User)
def create_user_client(sender, instance, created, **kwargs):
    if created:
        Client.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_client(sender, instance, **kwargs):
    instance.client.save()


class Notification(models.Model):
    """ Класс уведомлений, предназначенный для того,
        чтобы пользователи на страницах сайта могли отслеживать
        действия, которые могут его о чем-либо проинформировать
    """


    receiver = models.ForeignKey(Client, on_delete=models.CASCADE)  # Получатель уведомления
    message = models.CharField(max_length=100)                      # Сообщение уведомления
    date_of_create = models.DateTimeField(auto_now_add=True)        # Дата и время создания уведомления
    priority = models.IntegerField(choices=(                        
        (1, 'Personal'),
        (2, 'System notification'),
        (3, 'Group tasks'),
        (4, 'Group post'),
        (5, 'Admin post'),
    )) 
    """ Приоритет уведомления, где: 
        1. Личные уведомления (подписка, удаление из группы и т.п.)
        2. Системные уведомления (технические работы, баг и т.п.)
        3. Задачи группы (выполнена, закрыта, открыта)
        4. Посты группы (новый пост)
        5. Посты админов (обновления разработчиков в блоге)
    """


class Group(models.Model):
    """ Модель группы предназначена для выполнения главной
        функции проекта - выделения учебных групп и их оформления
    """


    def __str__(self):
            return self.name

    moderators = models.ManyToManyField(
        Client, 
        related_name='moderators',
        blank=True,
    ) # Количество модераторов не ограничено, связаны внешней таблицей с Client

    listeners = models.ManyToManyField(
        Client, 
        related_name='listeners',
        blank=True,
    ) # Количество подписчиков не ограничено, связаны внешней таблицей с Client

    name = models.CharField(max_length=40)              # Название группы
    shedule = models.FileField(upload_to='shedules')    # Расписание группы
    ratings =  models.FileField(upload_to='ratings')    # Оценки в группе
    sheet = models.FileField(upload_to='sheets')        # Вся ведомость по группе


class Group_post(models.Model):
    """ Пост конкретной группы предназначен для оформления всех
        постов под конкретную группу в связке по таблице Group
    """


    def __str__(self):
        return self.group.name + " " + self.article

    group = models.ForeignKey(
        Group, 
        on_delete=models.CASCADE
    ) # Группа-автор

    author = models.ForeignKey(
        Client,
        on_delete=models.SET_NULL,
        null=True
    ) # Автор поста, может отсутствовать

    article = models.CharField(max_length=50)                   # Заголовок поста
    text = models.TextField()                                   # Сообщение поста, неограниченное количество знаков
    date_of_create = models.DateTimeField(auto_now_add=True)    # Дата и время публикации поста


class Admin_post(models.Model):
    """ Модель поста админа сделана исключительно для блога
        администраторов в целях удобства коммуникации с сообществом проекта """


    def __str__(self):
            return self.author.user.username + " " + self.article

    author = models.ForeignKey(
        Client,
        on_delete=models.SET_NULL,
        null=True
    ) # Автор поста, может отсутствовать

    article = models.CharField(max_length=50)                   # Заголовок поста
    text = models.TextField()                                   # Сообщение поста, неограниченное количество знаков
    date_of_create = models.DateTimeField(auto_now_add=True)    # Дата и время публикации поста


class Task(models.Model):
    """ Модель задач хранит сообщение для выполнения
        конкретному пользователю, закрепляется датой выполнения и статусом """


    def __str__(self):
            return self.group.name + " " + self.content

    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
    ) # Группа с задачами

    receiver = models.ForeignKey(
        Client,
        on_delete=models.SET_NULL,
        null=True
    ) # Ответственный за задачу, может отсутствовать

    content = models.CharField(max_length=100)                      # Содержание задачи
    date_of_create = models.DateTimeField(auto_now_add=True)        # Дата открытия задачи
    date_of_completion = models.DateTimeField()                     # Дата срока для завершения
    status = models.IntegerField(choices=(
        (0, 'Ждет выполнения'),
        (1, 'Сделано')
    ))                                                              
    """ Статус выполнения задачи, где:
        0. Не выполнена
        1. Выполнена 
    """
