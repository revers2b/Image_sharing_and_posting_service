from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    template = "image_sharing_and_posting/home.html"
    context = {}
    return render(request, template, context)