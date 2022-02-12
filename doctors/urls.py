from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.doctors, name="doctors"),
    path('profile/<str:pk>', views.doc_profile, name="doc_profile"),
    path('self_doc/', views.self_doc, name="self_doc"),
]