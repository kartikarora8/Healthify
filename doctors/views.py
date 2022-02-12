from django.shortcuts import render
from .models import Doctor
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
import math, random

def doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors/doctors.html', {'doctors' : doctors})

def doc_profile(request, pk):
    profile = Doctor.objects.get(id=pk)
    return render(request, 'doctors/doc_profile.html', {'profile' : profile})

def self_doc(request):
    profile = Doctor.objects.get(name="Aviral Nagpal")
    return render(request, 'doctors/self_doc.html', {'profile' : profile})
