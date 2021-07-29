# Generated by Django 3.2.5 on 2021-07-23 23:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0007_auto_20210723_1911'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession', models.CharField(max_length=20)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(choices=[('ETUDIANT', 'Etudiant'), ('CHOMEUR', 'Chomeur'), ('JE TRAVAIL', 'Je travail')], default='Chomage', max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Profession', to='profil.profession'),
        ),
    ]