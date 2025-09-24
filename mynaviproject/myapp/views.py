from django.shortcuts import render

# Create your views here.
def navbar(request):
    return render(request,'myapp/navbarex.html')

def home(request):
    return render(request,'myapp/home.html')

def login(request):
    return render(request,'myapp/login.html')

def register(request):
    return render(request,'myapp/register.html')
def about(request):
    return render(request,'myapp/about.html')
def contact(request):
    return render(request,'myapp/contact.html')