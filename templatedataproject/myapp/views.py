from django.shortcuts import render
from myapp.models import Employee
from django.contrib.auth.decorators import login_required

@login_required
def getEmployees(request):
    emp_list=Employee.objects.all()
    my_dict = {'emp_list':emp_list}
    return render(request,'myapp/index.html',my_dict)