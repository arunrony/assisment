# Generated by Django 4.1.3 on 2022-12-02 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quesapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
    ]
