from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.doctors, name="doctors"),
    path('profile/<str:pk>', views.doc_profile, name="doc_profile"),
    path('self_doc/', views.self_doc, name="self_doc"),
    path('find_patient/', views.find_patient, name="find_patient"),
    path('otp_page/', views.otp_page, name="otp_page"),
    path('otp_result/', views.otp_result, name="otp_result"),
    path('inbox/', views.inbox, name="inbox"),
]