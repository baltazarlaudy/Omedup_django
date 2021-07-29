from django.urls import path
from . import views

#name for patterns
app_name = 'base'

#url patterns for base
urlpatterns = [
    path('', views.home_view, name='home')
]