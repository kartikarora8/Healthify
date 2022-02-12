from django.shortcuts import redirect, render
from patient.models import patient

def lab_home(request):
    if request.method == 'POST':
        user = request.POST.get('adhar')
        return redirect('search_patient', pk=user)
    return render(request, 'labs/lab_home.html')

def search_patient(request, pk):
    user_profile = patient.objects.get(adhar=pk)
    print(user_profile)
    return render(request, 'labs/search_patient.html', {'user_profile' : user_profile})


