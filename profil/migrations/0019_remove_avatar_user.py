# Generated by Django 3.2.5 on 2021-07-27 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0018_auto_20210727_0723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avatar',
            name='user',
        ),
    ]
