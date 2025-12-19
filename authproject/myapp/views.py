from django.shortcuts import render

from django.contrib.auth.decorators import login_required

# Create your views here.
def home_view(request):
    return render(request,'myapp/home.html')

@login_required
def javaexam_view(request):
    return render(request,'myapp/javaexam.html')

def pythonexam_view(request):
    return render(request,'myapp/pythonexamp.html')
