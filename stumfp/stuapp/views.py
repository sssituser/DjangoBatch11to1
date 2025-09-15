from django.shortcuts import render,redirect,get_object_or_404
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


def editStudent(request, id):
    stu = get_object_or_404(Student, id=id)   # Fetch student by ID
  
    if request.method == 'POST':
        stu_Form = StudentForm(request.POST, instance=stu)  # Bind form with POST data and existing student
        if stu_Form.is_valid():
            stu_Form.save()   # Save updated data
            return redirect('stulist')
    else:
        stu_Form = StudentForm(instance=stu)  # Pre-fill form with existing student data
    return render(request, 'stuapp/editstu.html', {'stu_Form': stu_Form})




def showStudent(request,id):
    stu = get_object_or_404(Student,id=id);
    return render(request,'stuapp/showstu.html',{'stu':stu})

def delStudent(request,id):
    stu = get_object_or_404(Student,id=id)
    if request.method == 'POST':
        stu.delete()
        return redirect('stulist')
    return render(request,'stuapp/deleteStudent.html',{'stu':stu})
