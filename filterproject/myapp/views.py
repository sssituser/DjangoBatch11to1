from django.shortcuts import render
from myapp.models import Employee
# Create your views here.

def getEmployees(request):
    Emp_List = Employee.objects.all();
    Emp_Dict = {'Emp_List':Emp_List}
    return render(request,'myapp/index.html',Emp_Dict)
                  
