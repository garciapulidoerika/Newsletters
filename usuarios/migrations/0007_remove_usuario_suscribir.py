# Generated by Django 3.2.9 on 2021-11-25 03:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_auto_20211124_1850'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='suscribir',
        ),
    ]