# Generated by Django 3.2.9 on 2022-01-03 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='Date',
            field=models.DateField(default='1998-05-06'),
            preserve_default=False,
        ),
    ]
