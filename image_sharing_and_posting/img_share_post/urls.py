from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name = "image_sharing_and_posting/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = "image_sharing_and_posting/logout.html"), name='logout'),
    path("new_series", views.new_series, name="series-create"),
    path("new_post", views.new_post, name="post-create"),
    path("<series>", views.series, name="series"),
    path("<series>/update", views.series_update, name="series_update"),
    path("<series>/delete", views.series_delete, name="series_delete"),
    path("<series>/<article>", views.article, name="article"),
    path("<series>/<article>/update", views.article_update, name="article_update"),
    path("<series>/<article>/delete", views.article_delete, name="article_delete"),
]