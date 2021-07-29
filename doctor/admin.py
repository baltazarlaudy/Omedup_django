from django.contrib import admin
from .models import Speciality, Doctor


# Register your models here.
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['speciality', 'profile']


# speciality admin
@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ['title']
