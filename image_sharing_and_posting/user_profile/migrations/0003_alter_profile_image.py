# Generated by Django 4.1.3 on 2022-12-12 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_remove_profile_photo_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(max_length=255, upload_to='user_profile/photos', verbose_name='image'),
        ),
    ]
