from django.shortcuts import render
from myapp.forms import Student

# Create your views here.
def Student_view(request):
    stud_form = Student()
    form_dict ={'form':stud_form}

    if request.method == "POST":
        form = Student(request.POST)
        if form.is_valid():
            print("Stuent ID : ",form.cleaned_data["stuId"])
            print("Student Name",form.cleaned_data["stuName"])
            print("Student Age",form.cleaned_data["stuAge"])
            print("Student Marks",form.cleaned_data["stuMarks"])

    return render(request,'myapp/index.html',form_dict)
