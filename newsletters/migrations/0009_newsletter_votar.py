# Generated by Django 2.2.24 on 2021-11-24 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletters', '0008_auto_20211123_2222'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='votar',
            field=models.CharField(default='', max_length=30, verbose_name='Election type'),
        ),
    ]
