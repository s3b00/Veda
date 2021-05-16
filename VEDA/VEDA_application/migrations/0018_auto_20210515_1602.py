# Generated by Django 3.2.3 on 2021-05-15 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VEDA_application', '0017_auto_20210515_1432'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['date_of_receive']},
        ),
        migrations.AddField(
            model_name='group',
            name='hNotices',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='hSheet',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='hTasks',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]