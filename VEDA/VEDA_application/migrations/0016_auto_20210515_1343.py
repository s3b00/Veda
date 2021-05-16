# Generated by Django 3.2.3 on 2021-05-15 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('VEDA_application', '0015_remove_group_post_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VEDA_application.group')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='note',
            name='discipline',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='VEDA_application.discipline'),
        ),
    ]