from django.shortcuts import redirect, render
from .models import blogs, Tag

def landing(request):
    return render(request, "administration/landing.html")

def blog(request):
    articles = blogs.objects.all()
    return render(request, "administration/blogs.html", {'blogs' : articles})

def single_blog(request,pk):
    article = blogs.objects.get(id=pk)
    return render(request, "administration/single_blog.html", {'blog' : article})

def registration_choice(request):
    return render(request, 'administration/register_choice.html')

def login_choice(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if(username=="RohanMittal"):
            return redirect('dashboard')
        elif(username=="lalpathlab"):
            return redirect('lab_home')
        elif(username=="Aviral Nagpal"):
            return redirect('self_doc')
    return render(request, 'administration/login.html')
