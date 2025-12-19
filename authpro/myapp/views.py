from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
def home_page_view(request):
    return render(request,'my/home.html')
@login_required
def java_exams_view(request):
    return render(request,'my/javaexams.html')
@login_required
def python_exams_view(request):
    return render(request,'myapp/pythonexams.html')
@login_required
def aptitude_exams_view(request):
    return render(request,'myapp/aptitudeexams.html')
def logout_view(request):
    return render(request,'my/logout.html')

from myapp.forms import SignUpForm
from django.http import HttpResponseRedirect
def signup_view(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        #form.save()
        user = form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/signup.html',{'form':form})
