from django.contrib.auth.models import User, AnonymousUser
from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.dispatch import receiver
from django.urls import reverse
from django.utils import tree


class Parent(models.Model):
    """ Модель родителя предназначается для того, чтобы куратор
        имел доступ к данным об родителях пользователя группы """


    surname = models.CharField(max_length=30)       # Фамилия
    name = models.CharField(max_length=30)          # Имя
    middlename = models.CharField(max_length=30)    # Отчество
    job = models.CharField(max_length=60, blank=True, null=True)           # Место работы
    date_of_birthday = models.DateField(null=True, blank=True)  # Дата рождения
    phone = models.CharField(max_length=20, blank=True, null=True)         # Номер телефона


class Client(models.Model):
    """ Модель клиента расширяет возможности модели пользователя,
        появляется дополнительные поля родителей, статуса, хобби и тому подобное """


    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )   # Связь один-к-одному с пользователем                        

    father = models.ForeignKey(
        Parent, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='father'
    ) # Связь с родителем внешним ключем

    mother =  models.ForeignKey(
        Parent, 
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='mother'
    ) # Связь с родителем внешним ключом

    status = models.CharField(max_length=100, blank=True, null=True)             # Поле статуса (отображается в профиле пользователя)
    hobbies = models.CharField(max_length=100, blank=True, null=True)            # Поле хобби (используется куратором и отображается в профиле)
    day_of_birthday = models.DateField(null=True)         # Поле дня рождения (используется куратором и отображается в профиле)
    adress = models.CharField(max_length=50, blank=True, null=True)              # Поле адреса (используется только куратором и не виден в профиле)

    #socials
    vk = models.TextField(blank=True)
    instagram = models.TextField(blank=True)

    gender = models.CharField(choices=(
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ), max_length=50, null=True)                          # Пол пользователя в формате первой буквы             
    userpic = models.ImageField(upload_to='userpics', null=True, default="default.png")    # Аватар пользователя

    def __str__(self):
            # format: s3boo
            return self.user.username
    

    class Meta:
        ordering = ['user__last_name', 'user__first_name']


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

    class Meta:
        ordering = ['-id']


class Group(models.Model):
    """ Модель группы предназначена для выполнения главной
        функции проекта - выделения учебных групп и их оформления
    """


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
    tag = models.CharField(max_length=40, null=True)              # Тег для поиска

    hNotices = models.BooleanField()    # видимость блока объявлений
    hTasks = models.BooleanField()      # видимость блока задач
    hSheet = models.BooleanField()      # видимость блока расписания, ведомости, успеваемости

    def __str__(self):
        # format: П-41
        return self.name

    def get_absolute_url(self):
        # Возвращает ссылку на конкретный профиль группы
        return reverse('group', args=[str(self.id)])


class Lesson(models.Model):
    """ Модель для загрузки расписания группы """

    group = models.ForeignKey(Group, on_delete=models.CASCADE)  # група, для которой записывается урок в расписании
    day = models.IntegerField(choices=(
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday'),
        (6, 'Saturday'),
        (7, 'Sunday'),
    ), blank=False, null=False) # день, в котороый проходит текущее занятие
    discipline = models.CharField(max_length=40, null=False, blank=False) # наименования для конкретного занятия


class Discipline(models.Model):
    """ Модель для представления дисциплины, которая используется в группе и по ней ведут оценки """

    group = models.ForeignKey(Group, on_delete=models.CASCADE)  # группа для предмета, по которому идет ведомость
    name = models.CharField(max_length=50, blank=False, null=False) # название предмета

    def __str__(self):
        # format: КПиЯП
        return self.name


    class Meta:
        # сортировка по имени
        ordering = ['name']


class Note(models.Model):
    """ Модель для записей результатов/оценок учащихся в группе """

    group = models.ForeignKey(Group, on_delete=models.CASCADE)  # группа, где поставлена оценка
    receiver = models.ForeignKey(Client, on_delete=models.CASCADE)  # пользователь, которому поставлена оценка
    date_of_receive = models.DateField(blank=False, null=False) # дата оценки
    value = models.CharField(max_length=10, blank=True) # значение оценки (10, н-ка, неуд и т.п.)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, null=True) # предмет, по которому поставлена оценка
    description = models.CharField(max_length=50, blank=True)

    def __str__(self):
        # format: s3boo 9
        return self.receiver.user.username + " " + self.value

    class Meta:
        # сортировка по дате получения оценки
        ordering = ['date_of_receive']


class Group_post(models.Model):
    """ Пост конкретной группы предназначен для оформления всех
        постов под конкретную группу в связке по таблице Group
    """


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
    # file_field = models.FileField(null=True, blank=True, upload_to='files'),      # Файл приложение к посту
    post_file_field = models.FileField(null=True, blank=True, upload_to='group_files')

    def __str__(self):
        # format: П-41 Первый пост
        return self.group.name + " " + self.article


    class Meta():
        # сортировка по дате создания в обратном порядке
        ordering = ['-date_of_create']

    

class Admin_post(models.Model):
    """ Модель поста админа сделана исключительно для блога
        администраторов в целях удобства коммуникации с сообществом проекта """


    author = models.ForeignKey(
        Client,
        on_delete=models.SET_NULL,
        null=True
    ) # Автор поста, может отсутствовать

    article = models.CharField(max_length=50)                   # Заголовок поста
    text = models.TextField()                                   # Сообщение поста, неограниченное количество знаков
    date_of_create = models.DateTimeField(auto_now_add=True)    # Дата и время публикации поста


    def __str__(self):
        # format: s3boo First_post
        return self.author.user.username + " " + self.article


    class Meta():
        # сортировка по дате создания в обратном порядке
        ordering = ['-date_of_create']


class Task(models.Model):
    """ Модель задач хранит сообщение для выполнения
        конкретному пользователю, закрепляется датой выполнения и статусом """


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
    date_of_completion = models.DateTimeField(null=True)                     # Дата срока для завершения
    status = models.IntegerField(choices=(
        (0, 'Ждет выполнения'),
        (1, 'Сделано')
    ))                                                              
    """ Статус выполнения задачи, где:
        0. Не выполнена
        1. Выполнена 
    """


    def __str__(self):
        # format: П-41 Продать почку
        return self.group.name + " " + self.content


    class Meta:
        # сортировка в обратном порядке создания
        
        ordering = ['-id']


class Notice(models.Model):
    """ Модель для объявлений, которые делают модераторы в группах """


    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
    ) # Группа для объявления

    author = models.ForeignKey(
        Client,
        on_delete=models.SET_NULL,
        null=True
    ) # Автор объявления (среди модераторов) 

    message = models.CharField(max_length=250)                      # Содержание объявления
    date_of_create = models.DateTimeField(auto_now_add=True)        # Дата публикации


    def __str__(self):
        return self.message
