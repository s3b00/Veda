# Generated by Django 3.2.3 on 2021-05-24 12:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('hobbies', models.CharField(blank=True, max_length=100, null=True)),
                ('day_of_birthday', models.DateField(null=True)),
                ('adress', models.CharField(blank=True, max_length=50, null=True)),
                ('vk', models.TextField(blank=True)),
                ('instagram', models.TextField(blank=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=50, null=True)),
                ('userpic', models.ImageField(default='default.png', null=True, upload_to='userpics')),
            ],
            options={
                'ordering': ['user__last_name', 'user__first_name'],
            },
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('tag', models.CharField(max_length=40, null=True)),
                ('hNotices', models.BooleanField()),
                ('hTasks', models.BooleanField()),
                ('hSheet', models.BooleanField()),
                ('listeners', models.ManyToManyField(blank=True, related_name='listeners', to='VEDA_application.Client')),
                ('moderators', models.ManyToManyField(blank=True, related_name='moderators', to='VEDA_application.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('middlename', models.CharField(max_length=30)),
                ('job', models.CharField(blank=True, max_length=60, null=True)),
                ('date_of_birthday', models.DateField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('date_of_create', models.DateTimeField(auto_now_add=True)),
                ('date_of_completion', models.DateTimeField(null=True)),
                ('status', models.IntegerField(choices=[(0, '???????? ????????????????????'), (1, '??????????????')])),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VEDA_application.group')),
                ('receiver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='VEDA_application.client')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=100)),
                ('date_of_create', models.DateTimeField(auto_now_add=True)),
                ('priority', models.IntegerField(choices=[(1, 'Personal'), (2, 'System notification'), (3, 'Group tasks'), (4, 'Group post'), (5, 'Admin post')])),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VEDA_application.client')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=250)),
                ('date_of_create', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='VEDA_application.client')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VEDA_application.group')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_receive', models.DateField()),
                ('value', models.CharField(blank=True, max_length=10)),
                ('description', models.CharField(blank=True, max_length=50)),
                ('discipline', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='VEDA_application.discipline')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VEDA_application.group')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VEDA_application.client')),
            ],
            options={
                'ordering': ['date_of_receive'],
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')])),
                ('discipline', models.CharField(max_length=40)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VEDA_application.group')),
            ],
        ),
        migrations.CreateModel(
            name='Group_post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('date_of_create', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='VEDA_application.client')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VEDA_application.group')),
            ],
            options={
                'ordering': ['-date_of_create'],
            },
        ),
        migrations.AddField(
            model_name='discipline',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VEDA_application.group'),
        ),
        migrations.AddField(
            model_name='client',
            name='father',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='father', to='VEDA_application.parent'),
        ),
        migrations.AddField(
            model_name='client',
            name='mother',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mother', to='VEDA_application.parent'),
        ),
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Admin_post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('date_of_create', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='VEDA_application.client')),
            ],
            options={
                'ordering': ['-date_of_create'],
            },
        ),
    ]
