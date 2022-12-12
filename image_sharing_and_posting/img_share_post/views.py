from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Article, ArticleSeries


User = get_user_model

def home(request):
    template = "image_sharing_and_posting/home.html"
    matching_series = ArticleSeries.objects.all()

    return render(request, template, context={"objects": matching_series})

def profile(request):
    template = "image_sharing_and_posting/Profile.html"
    return render(request, template)

def logout(request):
    template = "image_sharing_and_posting/logout.html"
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


@login_required
def logout_cust(request):
    logout(request)
    messages.info(request, "Logged out!")
    return redirect("home")

def login_cust(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello{user.username}!")
                return redirect("home")

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    form = AuthenticationForm()

    return render(request=request, template_name="image_sharing_and_posting/login.html", context={"form": form})

def series(request, series: str):
    matching_series = Article.objects.filter(series__slug=series).all()
    
    return render(
        request=request,
        template_name='main/home.html',
        context={"objects": matching_series}
        )

def article(request, series: str, article: str):
    matching_article = Article.objects.filter(series__slug=series, article_slug=article).first()
    
    return render(
        request=request,
        template_name='main/article.html',
        context={"object": matching_article}
        )