from django.shortcuts import render
from .models import patient

def dashboard(request):
    patients = patient.objects.get(name="Rohan Gupta")
    return render(request, "patient/dashboard.html",{'patient' : patients})
