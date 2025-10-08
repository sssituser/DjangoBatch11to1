from django.shortcuts import render,redirect
from myapp.forms import EmployeeForm
from myapp.models import Employee
# Create your views here.
def reg_employee(request):
    form=EmployeeForm()
    if request.method =='POST':
        form = EmployeeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('getEmployees')
    return render(request,'myapp/register.html',{'form':form})

def showEmployees(request):
    Employees = Employee.objects.all()
    return render(request,'myapp/emplist.html',{'employees':Employees})    
