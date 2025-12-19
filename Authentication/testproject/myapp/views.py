from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from myapp.forms import SignUpForm
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    return render(request,'myapp/home.html')
@login_required
def java(request):
    return render(request,'myapp/java.html')

def signup(request):
    form=SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()
        
        return HttpResponseRedirect('/accounts/login')
        print("Errror if")
    else:
        print("Error else")
        return render(request,'myapp/signup.html',{'form':form})