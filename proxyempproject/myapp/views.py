from django.shortcuts import render
from myapp.forms import EmployeeForm
from myapp.models import Employee
# Create your views here.

def register_view(request):
    EmpForm = EmployeeForm()
    if(request.method == 'POST'):
        EmpForm = EmployeeForm(request.POST)
        if EmpForm.is_valid():
            EmpForm.save()
    return render(request,'myapp/Register.html',{'EmpForm':EmpForm})

def employees(request):
    emp_list = Employee.objects.all()
    return render(request,'myapp/Employees.html',{'emp_list':emp_list})
