from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.landing, name="landing"),
    path("blog/", views.blog, name="blog"),
    path("blog/<str:pk>", views.single_blog, name="single_blog"),
    path("registeration_choice", views.registration_choice, name="registration_choice"),
    path("login_choice", views.login_choice, name="login_choice")
]