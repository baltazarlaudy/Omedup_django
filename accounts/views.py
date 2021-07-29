from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from accounts.models import Account
from profil.models import Profile


# Create your views here.
@login_required()
def dashboard(request):
    id = request.user.id
    data = get_object_or_404(Account, id=id)
    context = {
        'section': 'dashboard',
        'account': data,
    }
    return render(request, 'account/dashboard.html', context)


# registration view
def registration_view(request):
    if request.user.is_authenticated:
        return redirect('account:dashboard')
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit = False)
            # set password
            new_user.set_password(
                form.cleaned_data['password']
            )
            # save user
            new_user.save()
            Profile.objects.create(
                user = new_user
            )
            return redirect('base:home')
    else:
        form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'registration/registration.html', context)
