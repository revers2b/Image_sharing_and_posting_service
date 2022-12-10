from django.shortcuts import render
from django.contrib.auth import get_user_model, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from . import models, serializers

User = get_user_model

def home(request):
    template = "image_sharing_and_posting/home.html"
    return render(request, template)

def profile(request):
    template = "image_sharing_and_posting/Profile.html"
    return render(request, template)

def register(response):
    form = UserCreationForm()
    return render(response, "image_sharing_and_posting/register.html", {"form":form})
