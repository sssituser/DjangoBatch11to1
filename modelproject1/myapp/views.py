from django.shortcuts import render
from myapp.models import Student
# Create your views here.
def getStdents(request):
    stud_list =Student.objects.all();
    stud_dict ={'stud_list':stud_list}
    return render(request,'myapp/index.html',stud_dict)
