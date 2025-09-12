from django.shortcuts import render,redirect
from stuapp.forms import StudentForm
from stuapp.models import Student
# Create your views here.
def index(request):
    stuForm = StudentForm()
    stu_dict ={'stuForm':stuForm}
    if request.method == 'POST':
        stuForm = StudentForm(request.POST)
        if stuForm.is_valid():
            stuForm.save(commit=True)
            return redirect('stulist')
    return render(request,'stuapp/index.html',stu_dict)

def getStudents(request):
    stu_list = Student.objects.all()
    stu_list_dict = {'stu_list':stu_list}
    return render(request,'stuapp/students.html',stu_list_dict)

def editStudent(request):
    return render(request,'stuapp/editstu.html')

def showStudent(request):
   return render(request,'stuapp/showstu.html')

def delStudent(request):
    return render(request,'stuapp/deleteStudent.html')
