from django.urls import path
from . import views
#url patter
app_name = 'account'
urlpatterns = [
    path('registration', views.registration_view, name="registration"),
    path('dashboard', views.dashboard, name='dashboard')
]