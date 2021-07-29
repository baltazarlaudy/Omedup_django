from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
def home_view(request):
    context = {
        'data':'data'
    }
    return render(request, 'base/home.html', context)