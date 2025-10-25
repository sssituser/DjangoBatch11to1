from django.shortcuts import render,redirect,get_object_or_404
from myapp.forms import EmployeeForm
from myapp.models import Employee
from django.db.models.aggregates import  Avg,Max,Min,Count,Sum

# Create your views here.
def addEmployee_view(request):
    print('This line Added by view function')
    emp_form = EmployeeForm()
    if request.method == 'POST':
        emp_form = EmployeeForm(request.POST)
        if emp_form.is_valid():
            emp_form.save()
            return redirect("employeelist")
    return render(request,"myapp/empregister.html",{"emp_form":emp_form})



def employeelist_view(request):
    emplist = Employee.objects.all()
    return render(request,'myapp/employeelist.html',{'emplist':emplist})

def aggrigate_view(request):
    avgSal = Employee.objects.all().aggregate(Avg('EmpSal'))
    sumSal = Employee.objects.all().aggregate(Sum('EmpSal'))
    maxSal = Employee.objects.all().aggregate(Max('EmpSal'))
    minSal = Employee.objects.all().aggregate(Min('EmpSal'))
    empCount = Employee.objects.all().aggregate(Count('EmpId'))
    empswitha = Employee.objects.all().filter(EmpName__startswith='a');
    empsewithn = Employee.objects.all().filter(EmpName__endswith='n')
    return render(request,'myapp/aggregate.html',
    {
     'empswitha':empswitha,    
     'empsewithn':empsewithn,
    'avg_Sal':avgSal['EmpSal__avg'],
     'sum_Sal':sumSal['EmpSal__sum'],
     'max_Sal':maxSal['EmpSal__max'],
     'min_Sal':minSal['EmpSal__min'],
     'emp_Count':empCount['EmpId__count']                                            
    })


def filter_view(request):

    return render(request,'myapp/filter.html',{})






def employeeedit_view(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect("employeelist")
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'myapp/editemployee.html', {'emp_form': form})
