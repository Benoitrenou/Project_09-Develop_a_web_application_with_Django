# Generated by Django 3.2.9 on 2021-11-27 16:10

from django.db import migrations, models
import pathlib


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0007_alter_ticket_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=pathlib.PureWindowsPath('C:/Users/benoi/Documents/GitHub/projet_09/LITReview/media')),
        ),
    ]
