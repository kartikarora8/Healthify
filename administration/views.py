from django.shortcuts import render
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
    return render(request, 'administration/login_choice.html')
