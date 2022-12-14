# Generated by Django 4.0.6 on 2022-10-31 13:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_user_profileimage_alter_post_headline'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='User_followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='User_follwoing', to=settings.AUTH_USER_MODEL),
        ),
    ]
