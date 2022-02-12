from django.shortcuts import redirect, render
from patient.models import patient
from .forms import ReportForm

def lab_home(request):
    form = ReportForm()
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lab_home')
    return render(request, 'labs/lab_home.html', {"form" : form})




