from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProfilForm, ProfileAvatarForm
from accounts.models import Account
from accounts.forms import AccountEditForm
from .models import Profile, Image
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse, HttpResponse


# Create your views here.
@login_required()
def profile_view(request, slug):
    data = get_object_or_404(Profile, slug = slug)
    context = {
        'section': 'profile',
        'profile': data
    }
    return render(request, 'profil/profil.html', context)


# edit profil
@login_required()
def profile_edit(request, slug):
    data = get_object_or_404(Profile, slug = slug)
    data1 = get_object_or_404(Account, id = request.user.id)
    if request.method == 'POST':
        form = ProfilForm(request.POST, request.FILES, instance = data)
        form_account = AccountEditForm(request.POST, instance = data1)
        if form.is_valid() and form_account.is_valid():
            form.save()
            form_account.save()
            messages.success(request, 'Modification effectue')
        else:
            messages.error(request, 'Profil non modifier a cause d\'une erreur')
    else:
        form = ProfilForm(instance = data)
        form_account = AccountEditForm(instance = data1)
    context = {
        'section': 'profil',
        'profile': data,
        'form': form,
        'form_account': form_account,
    }
    return render(request, 'profil/profil_edit.html', context)


@login_required()
def upload_avatar(request, slug):
    data = get_object_or_404(Profile, slug = slug)
    if request.method == 'POST':
        form = ProfileAvatarForm(request.POST, request.FILES)
        if form.is_valid():
            form_image = form.save(commit = False)
            form_image.profile = Profile.objects.get(id = data.id)
            form_image.save()
            messages.success(request, 'Photo Modifier')
        else:
            messages.error(request, 'Erreur inconnu, la photo n\est pas modifier')
    form = ProfileAvatarForm()
    context = {
        'form_avatar': form,
        'profile': data
    }
    return render(request, 'profil/profil_edit.html', context)

#edit profil avatar
@login_required()
def edit_avatar(request, slug):

    data = get_object_or_404(Image, slug=slug)
    if request.method == "POST":
        form = ProfileAvatarForm(request.POST, request.FILES, instance = data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Photo modifié;')
            return redirect('profile:edit', slug = data.profile.slug)
        else:
            return HttpResponse('error')
    form = ProfileAvatarForm(instance = data)
    context = {
        'form_avatar': form,
        'image': data
    }
    return render(request, 'profil/profil_edit.html', context)