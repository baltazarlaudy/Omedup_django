# Generated by Django 3.2.5 on 2021-07-27 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0021_alter_avatar_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(null=True, upload_to='profil/avatar'),
        ),
    ]