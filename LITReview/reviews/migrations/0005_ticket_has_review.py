# Generated by Django 3.2.9 on 2021-11-22 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_alter_ticket_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='has_review',
            field=models.BooleanField(default=False),
        ),
    ]
