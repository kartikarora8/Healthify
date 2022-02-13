from django.shortcuts import render, redirect
from .models import Doctor,Special
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
import math, random
from patient.models import patient
from django.db.models import Q
from labs.models import report


def doctors(request):
    doctors = Doctor.objects.all()
    search_query = ''
    special = ''
    if request.GET.get('text'):
        search_query = request.GET.get('text')
        special = Special.objects.filter(name__icontains=search_query)
        doctors = Doctor.objects.distinct().filter(Q(name__icontains=search_query) | Q(short_intro__icontains=search_query) | Q(special__in=special))
    return render(request, 'doctors/doctors.html', {'doctors' : doctors,'search_query' : search_query})

def doc_profile(request, pk):
    profile = Doctor.objects.get(id=pk)
    patients = patient.objects.get(name="Rohan Gupta")
    return render(request, 'doctors/doc_profile.html', {'profile' : profile, "patient" : patients})

def self_doc(request):
    profile = Doctor.objects.get(name="Aviral Nagpal")
    return render(request, 'doctors/self_doc.html', {'profile' : profile})

def find_patient(request):
    return render(request, 'doctors/find_patient.html')

def otp_page(request):
    if request.method == "POST":
        otp = request.POST.get('otp')
        if(otp=="RohanMittal"):
            return redirect('dashboard')
        elif(otp=="lalpathlab"):
            return redirect('lab_home')
    return render(request, 'doctors/otp_page.html')

def otp_result(request):
    patients = patient.objects.get(name="Rohan Gupta")
    doctors = Doctor.objects.get(name="Aviral Nagpal")
    reports = report.objects.filter(adhar=patients.adhar)
    return render(request, "doctors/otp_result.html",{'patient' : patients, "reports" : reports, 'doctor' : doctors})

def inbox(request):
    return render(request, 'doctors/inbox.html')
