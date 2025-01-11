from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('accounts/register/', views.UserRegistrationView.as_view(), name='register'),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(), name='logout'),
    path('accounts/', views.profile_view.as_view(template_name='profile.html'), name='profile'),
]
