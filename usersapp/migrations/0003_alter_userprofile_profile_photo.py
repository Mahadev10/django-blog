# Generated by Django 4.0.6 on 2022-07-24 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersapp', '0002_alter_userprofile_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_photo',
            field=models.ImageField(blank=True, default='users/default_user.png', null=True, upload_to='users/'),
        ),
    ]
