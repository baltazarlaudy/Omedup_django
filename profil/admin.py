from django.contrib import admin
from .models import Profile, Profession


# Register your models here.
@admin.register(Profile)
class AdminProfil(admin.ModelAdmin):
    list_display = ['user', 'slug']


@admin.register(Profession)
class AdminProfession(admin.ModelAdmin):
    list_display = ['profession', 'slug']
    prepopulated_fields = { 'slug': ('slug',) }
