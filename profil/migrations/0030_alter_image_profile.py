# Generated by Django 3.2.5 on 2021-07-27 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0029_alter_image_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='profil.profile'),
        ),
    ]
