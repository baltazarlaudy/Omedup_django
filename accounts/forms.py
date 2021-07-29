from django import forms
from .models import Account


# class form
class DateInput(forms.DateInput):
    input_type = 'date'


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label = 'Password', max_length = 200, widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Password confirmation', max_length = 200, widget = forms.PasswordInput)
    age = forms.DateField(widget = DateInput)

    class Meta:
        model = Account
        fields = ['nom', 'prenom', 'age', 'email', 'password', 'password2']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Les deux mots de pass ne sont pas identique')
        return cd['password2']


# class form edit account
class AccountEditForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['nom', 'prenom', 'age']

        widgets = {
            'nom': forms.TextInput(),
            'prenom': forms.TextInput(),
            'age': DateInput(),
        }

