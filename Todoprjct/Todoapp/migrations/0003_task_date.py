# Generated by Django 4.2.3 on 2023-07-15 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todoapp', '0002_rename_task_task_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2023-07-15'),
            preserve_default=False,
        ),
    ]