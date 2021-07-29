from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import auth
import uuid


# Create your models here.

# pression
class Profession(models.Model):
    profession = models.CharField(max_length = 20)
    slug = models.SlugField()

    def __str__(self):
        return self.profession

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.profession)
        super(Profession, self).save(*args, **kwargs)


# profil model
class Profile(models.Model):
    CHOICES_COUNTRY = (
        ('HAITI', 'haiti'),
        ('AUTRE', 'autre')
    )
    DEPARTEMENT_CHOICES = (
        ('OUEST', 'Ouest'),
        ('GRAND\'ANSE', 'Grand\'anse'),
        ('SUD', 'Sud'),
        ('NORD', 'Nord'),
        ('NORD OUEST', 'Nord ouest'),
        ('NORD EST', 'Nord est'),
        ('SUD OUEST', 'Sud ouest'),
        ('ARTIBONITE', 'Artibonite'),
        ('CENTRE', 'Centre'),
        ('NIPPES', 'Nippes'),
    )
    STATUS_CHOICES = (
        ('ETUDIANT', 'Etudiant'),
        ('CHOMEUR', 'Chomeur'),
        ('JE TRAVAIL', 'Je travail')
    )
    ASSURANCE_CHOICES = (
        ('OUI', 'Oui'),
        ('NON', 'Non')
    )
    SEXE_CHOICES = (
        ('HOMME', 'Homme'),
        ('FEMME', 'Femme'),
        ('AUTRE', 'Autre'),
        ('CHOIX', 'Choix')
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name = 'user', on_delete = models.CASCADE)
    slug = models.SlugField()
    address = models.CharField(max_length = 250, null = True)
    pays = models.CharField(max_length = 10, choices = CHOICES_COUNTRY, default = 'haiti')
    departement = models.CharField(max_length = 20, choices = DEPARTEMENT_CHOICES, default = 'Ouest')
    profession = models.ManyToManyField(Profession, related_name = 'Profession', null = True)
    status = models.CharField(max_length = 200, choices = STATUS_CHOICES, default = 'Chomage')
    assurance = models.CharField(max_length = 10, choices = ASSURANCE_CHOICES, default = 'Non')
    sexe = models.CharField(max_length = 10, choices = SEXE_CHOICES, default = 'Choix')

    def __str__(self):
        return self.user.nom

    def get_absolute_url(self):
        return reverse('profile:index', args = [self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(str(uuid.uuid4()))
        super(Profile, self).save(*args, **kwargs)

    # get avatar profil
    def get_avatar(self):
        avatar = Image.objects.get(profile = self.id)
        return avatar


# image clas for profile
class Image(models.Model):
    avatar = models.ImageField(upload_to = 'profil/avatar', null = True)
    profile = models.OneToOneField(Profile, on_delete = models.CASCADE, related_name = 'profile')
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(uuid.uuid4())
        super(Image, self).save(*args, **kwargs)

    def __str__(self):
        return self.avatar
