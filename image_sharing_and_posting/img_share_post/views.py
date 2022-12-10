from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from . import models, serializers
from .forms import UserRegistrationForm

User = get_user_model

def home(request):
    template = "image_sharing_and_posting/home.html"
    return render(request, template)

def profile(request):
    template = "image_sharing_and_posting/Profile.html"
    return render(request, template)

def register(request):
    template = "image_sharing_and_posting/register.html"
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')

        else:
            for error in list(form.errors.values()):
                print(request, error)

    else:
        form = UserRegistrationForm()

    return render(request, template, context={"form": form})