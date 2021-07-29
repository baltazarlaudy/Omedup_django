from django.db import models
from profil.models import Profile
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


# Create your models here.
class AccountManager(BaseUserManager):
    def create_user(self, nom, prenom, age, email, password=None):
        if not email:
            raise ValueError('Veuillez entrer une email valide')
        user = self.model(
            nom = nom,
            prenom = prenom,
            age = age,
            email = self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, nom, prenom, age, email, password=None):
        user = self.create_user(
            nom = nom,
            prenom = prenom,
            age = age,
            email = email,
            password = password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user


# Account class
class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique = True, verbose_name = 'Email:')
    nom = models.CharField(max_length = 200, verbose_name = 'Nom:')
    prenom = models.CharField(max_length = 200, verbose_name = 'Prenom:')
    age = models.DateField(verbose_name = 'Date de naissance:')
    is_active = models.BooleanField(default = True)
    is_patient = models.BooleanField(default = True)
    is_doctor = models.BooleanField(default = False)
    is_pharmacian = models.BooleanField(default = False)
    is_biologist = models.BooleanField(default = False)
    is_hospital = models.BooleanField(default = False)
    is_pharmacy = models.BooleanField(default = False)
    is_clinic = models.BooleanField(default = False)
    is_laboratory = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)
    is_admin = models.BooleanField(default = False)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nom', 'prenom', 'age']

    def __str__(self):
        return self.nom

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_profile(self):
        profile = Profile.objects.get(user = self.id)
        return profile
