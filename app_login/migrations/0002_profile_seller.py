# Generated by Django 4.0.4 on 2022-06-18 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='seller',
            field=models.BooleanField(default=False),
        ),
    ]
