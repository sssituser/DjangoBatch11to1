from django.shortcuts import render,redirect
from myapp.forms import EmployeeForm
from myapp.models import Employee

# Create your views here.

def AddEmployee(request):
    empForm = EmployeeForm()
    if request.method == 'POST':
        empForm = EmployeeForm(request.POST)
        if empForm.is_valid():
            empForm.save(commit=True)
            print("Employee Registred Successfully")
            empForm = EmployeeForm()
            return redirect("emplist")
    return render(request,'myapp/index.html',{'form':empForm})

def Employeesview(request):
    emp_list = Employee.objects.all();
    emp_dict ={'emp_list':emp_list}
    return render(request,'myapp/EmployeesInfo.html',emp_dict)

  