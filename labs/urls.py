from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.lab_home, name='lab_home'),
]
