# Generated by Django 4.2.5 on 2023-09-27 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_remove_task_photos_task_photos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]
