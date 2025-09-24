from django.shortcuts import render,redirect
from myapp.forms import EmployeeForm
# Create your views here.
def home(request):
    empForm = EmployeeForm();
    if request.method == "POST":
      return redirect('signin')
    return render(request,'myapp/home.html',{'empForm':empForm})

def register(request):
    return render(request,'myapp/register.html')

def login(request):
    return render(request,'myapp/login.html')
