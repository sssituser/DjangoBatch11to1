from django.shortcuts import render
from myapp.models import Student,Empoyee
# Create your views here.
def getData(request):
    emp_list = Empoyee.objects.all();
    stu_list = Student.objects.all();
    my_dict = {'emp_list':emp_list,'stu_list':stu_list}
    return render(request,'myapp/index.html',my_dict)

