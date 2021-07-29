from django import forms
from .models import Profile, Image


class ProfilForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['sexe', 'address', 'pays', 'departement', 'status', 'profession', 'assurance']
        widgets = {
            'sexe': forms.Select(attrs = { 'class': 'form-control' })
        }


class ProfileAvatarForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['avatar']
