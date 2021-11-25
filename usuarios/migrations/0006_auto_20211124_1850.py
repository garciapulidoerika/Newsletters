# Generated by Django 2.2.24 on 2021-11-24 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletters', '0012_auto_20211124_1850'),
        ('usuarios', '0005_remove_usuario_sucribir_a'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='suscribir',
            field=models.ManyToManyField(related_name='newsletters', to='newsletters.Newsletter'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=models.CharField(default='', max_length=100),
        ),
    ]