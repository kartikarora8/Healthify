from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.lab_home, name='lab_home'),
    path('search_patient/<str:pk>', views.search_patient, name='search_patient'),
]
