from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserRegistrationForm, SeriesCreateForm, ArticleCreateForm, SeriesUpdateForm, ArticleUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .decorators import user_is_superuser
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
        template_name='image_sharing_and_posting/home.html',
        context={"objects": matching_series}
        )

def article(request, series: str, article: str):
    matching_article = Article.objects.filter(series__slug=series, article_slug=article).first()
    
    return render(
        request=request,
        template_name='image_sharing_and_posting/article.html',
        context={"object": matching_article}
        )

@user_is_superuser
def new_post(request):
    if request.method == "POST":
        form = ArticleCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(f"{form.cleaned_data['series'].slug}/{form.cleaned_data.get('article_slug')}")

    else:
         form = ArticleCreateForm()

    return render(
        request=request,
        template_name='image_sharing_and_posting/new_record.html',
        context={
            "object": "Article",
            "form": form
            }
        )

@user_is_superuser
def new_series(request):
    if request.method == "POST":
        form = ArticleCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(f"{form.cleaned_data['series'].slug}/{form.cleaned_data.get('article_slug')}")

    else:
         form = ArticleCreateForm()

    return render(
        request=request,
        template_name='image_sharing_and_posting/new_record.html',
        context={
            "object": "Article",
            "form": form
            }
        )

@user_is_superuser
def series_update(request, series):
    matching_series = ArticleSeries.objects.filter(slug=series).first()

    if request.method == "POST":
        form = SeriesUpdateForm(request.POST, request.FILES, instance=matching_series)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    
    else:
        form = SeriesUpdateForm(instance=matching_series)

        return render(
            request=request,
            template_name='image_sharing_and_posting/new_record.html',
            context={
                "object": "Series",
                "form": form
                }
            )

@user_is_superuser
def series_delete(request, series):
    matching_series = ArticleSeries.objects.filter(slug=series).first()

    if request.method == "POST":
        matching_series.delete()
        return redirect('/')
    else:
        return render(
            request=request,
            template_name='image_sharing_and_posting/confirm_delete.html',
            context={
                "object": matching_series,
                "type": "Series"
                }
            )

@user_is_superuser
def article_update(request, series, article):
    matching_article = Article.objects.filter(series__slug=series, article_slug=article).first()

    if request.method == "POST":
        form = ArticleUpdateForm(request.POST, request.FILES, instance=matching_article)
        if form.is_valid():
            form.save()
            return redirect(f'/{matching_article.slug}')
    
    else:
        form = ArticleUpdateForm(instance=matching_article)

        return render(
            request=request,
            template_name='image_sharing_and_posting/new_record.html',
            context={
                "object": "Article",
                "form": form
                }
            )

@user_is_superuser
def article_delete(request, series, article):
    matching_article = Article.objects.filter(series__slug=series, article_slug=article).first()

    if request.method == "POST":
        matching_article.delete()
        return redirect('/')
    else:
        return render(
            request=request,
            template_name='image_sharing_and_posting/confirm_delete.html',
            context={
                "object": matching_article,
                "type": "article"
                }
            )