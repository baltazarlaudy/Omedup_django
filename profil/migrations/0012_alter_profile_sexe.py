# Generated by Django 3.2.5 on 2021-07-24 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0011_alter_profile_profession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='sexe',
            field=models.CharField(choices=[('HOMME', 'Homme'), ('FEMME', 'Femme'), ('AUTRE', 'Autre'), ('CHOIX', 'Choix')], default='Choix', max_length=10),
        ),
    ]
