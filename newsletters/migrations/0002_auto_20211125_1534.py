# Generated by Django 3.2.9 on 2021-11-25 20:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('newsletters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='suscrito',
            field=models.ManyToManyField(related_name='news', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='imagen',
            field=models.ImageField(null=True, upload_to='fotos'),
        ),
    ]
