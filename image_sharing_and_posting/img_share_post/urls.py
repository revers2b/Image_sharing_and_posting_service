from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('new_user/', views.new_user, name="new_user"),
]
