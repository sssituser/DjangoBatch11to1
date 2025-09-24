from django.shortcuts import render
from myapp.forms import EmployeesForm
# Create your views here.

def Add_Student(request):
    if request.method == 'POST':
        form=EmployeesForm(request.POST)
        if form.is_valid():
           form.save(commit=True)
           print('Employee Added Successfully..')
    else:
        form = EmployeesForm()
    # Always return a response
    return render(request, 'myapp/index.html', {'empForm': form})





