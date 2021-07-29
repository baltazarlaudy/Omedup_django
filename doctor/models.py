from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
# speciality model
class Speciality(models.Model):
    title = models.CharField(max_length = 200, unique = True)
    slug = models.SlugField(unique = True)

    class Meta:
        verbose_name_plural = 'Specialities'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Speciality, self).save(*args, *kwargs)


# doctor class
class Doctor(models.Model):
    speciality = models.ForeignKey(Speciality, related_name = 'speciality', on_delete = models.CASCADE)
    profile = models.OneToOneField(settings.AUTH_USER_MODEL, related_name = 'profile', on_delete = models.CASCADE)
    description = models.TextField(null = True)
    clinique = models.CharField(null = True, max_length = 200)
    hopital = models.CharField(null = True, max_length = 200)




    def __str__(self):
        return self.profile.nom
