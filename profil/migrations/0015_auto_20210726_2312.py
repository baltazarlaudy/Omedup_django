# Generated by Django 3.2.5 on 2021-07-27 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0014_auto_20210726_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='profil/avatar'),
        ),
        migrations.DeleteModel(
            name='Avatar',
        ),
    ]
