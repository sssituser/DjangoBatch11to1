from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from myapp.forms import SignUpForm
# Create your views here.
@login_required
def home(request):
    return render(request,'myapp/home.html')
def java(request):
    return render(request,'myapp/java.html')

def python(request):
    return render(request,'myapp/python.html')

def register(request):
    form = SignUpForm()
    if form.is_valid():
        form=SignUpForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        print("welcome..............")
        return render(request,'accounts/login/')
    return render(request,'myapp/register.html',{'form':form})
