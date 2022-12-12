from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name = "image_sharing_and_posting/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = "image_sharing_and_posting/logout.html"), name='logout'),
]
