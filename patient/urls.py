from unicodedata import name
from django import views
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path("my_activity",views.my_activity, name="my_activity")
]