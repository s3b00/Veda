# Generated by Django 3.2.3 on 2021-05-17 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VEDA_application', '0020_auto_20210517_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='description',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]