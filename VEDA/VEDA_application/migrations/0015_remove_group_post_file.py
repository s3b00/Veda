# Generated by Django 3.2.3 on 2021-05-14 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VEDA_application', '0014_group_post_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group_post',
            name='file',
        ),
    ]