from django.shortcuts import render
from myapp import views
from myapp.models import Student
# Create your views here.
def getStudents(request):
    stud_list = Student.objects.all()
    student_dict = {'stu_list':stud_list}
    return render(request,'myapp/index.html',student_dict)

