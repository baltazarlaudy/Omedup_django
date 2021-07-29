from django.urls import path
from . import views
#url patterns
app_name = 'profile'
urlpatterns = [
    path('<str:slug>/', views.profile_view, name='index'),
    path('profile/<str:slug>/edit', views.profile_edit, name='edit'),
    path('profile/upload_image/<str:slug>', views.upload_avatar, name='upload_avatar'),
    path('profile/image/edit/<str:slug>', views.edit_avatar, name='edit_avatar'),
]