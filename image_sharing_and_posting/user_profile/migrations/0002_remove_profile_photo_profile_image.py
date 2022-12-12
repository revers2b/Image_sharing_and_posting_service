# Generated by Django 4.1.3 on 2022-12-12 01:03

from django.db import migrations, models
import user_profile.models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='photo',
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default/user.jpg', max_length=255, upload_to=user_profile.models.Profile.image_upload_to),
        ),
    ]
