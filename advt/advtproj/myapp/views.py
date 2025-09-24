
from django.shortcuts import render

def base_view(request):
    return render(request,'myapp/base.html')

def home_view(request):
    return render(request,'myapp/home.html')

def register_view(request):
    return render(request,'myapp/register.html')

def login_view(request):
    return render(request,'myapp/login.html')