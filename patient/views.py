from django.shortcuts import render
from .models import patient
from labs.models import report

def dashboard(request):
    patients = patient.objects.get(name="Rohan Gupta")
    reports = report.objects.filter(adhar=patients.adhar)
    return render(request, "patient/dashboard.html",{'patient' : patients, "reports" : reports})
