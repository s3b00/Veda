# Generated by Django 3.2.3 on 2021-05-13 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VEDA_application', '0009_auto_20210513_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='tag',
            field=models.CharField(max_length=40, null=True),
        ),
    ]