# Generated by Django 3.2.3 on 2021-05-25 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VEDA_application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group_post',
            name='post_file_field',
            field=models.FileField(blank=True, null=True, upload_to='group_files'),
        ),
    ]