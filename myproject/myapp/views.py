from django.shortcuts import render
from myapp.forms import StudentForm
# Create your views here.
def register(request):
    stu_form = StudentForm()
    if request.method == 'POST':
        stu_form = StudentForm(request.POST,request.FILES)
        if stu_form.is_valid():
            stu_form.save()
            return render(request, 'myapp/show.html',   {'stu_form': stu_form})
    return render(request, 'myapp/register.html', {'stu_form': stu_form})

def show(request):
    return render(request, 'myapp/show.html')

