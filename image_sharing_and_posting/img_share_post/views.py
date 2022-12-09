from django.shortcuts import render
from django.contrib.auth import get_user_model
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

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.AllowAny]

    def delete(self, request, *args, **kwargs):
        user = User.objects.filter(pk=request.user.pk)
        if user.exists():
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError(('User does not exist.'))
