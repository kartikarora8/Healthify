from django.shortcuts import render
from .models import patient
from labs.models import report
from doctors.models import Doctor

def dashboard(request):
    patients = patient.objects.get(name="Rohan Gupta")
    doctors = Doctor.objects.get(name="Aviral Nagpal")
    reports = report.objects.filter(adhar=patients.adhar)
    return render(request, "patient/dashboard.html",{'patient' : patients, "reports" : reports, 'doctor' : doctors})

def my_activity(request):
    patients = patient.objects.get(name="Rohan Gupta")
    return render(request, "patient/my_activity.html", {'patient' : patients})
