from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.http import HttpResponse

User = get_user_model

def home(request):
    template = "image_sharing_and_posting/home.html"
    return render(request, template)

def profile(request):
    template = "image_sharing_and_posting/Profile.html"
    return render(request, template)