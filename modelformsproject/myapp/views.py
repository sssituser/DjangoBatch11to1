from django.shortcuts import render
from myapp.forms import StudentForm

def getStudents(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
           form.save(commit=True)
           print("Record Inserted Successfully...")
    else:
        form = StudentForm()
    # Always return a response
    return render(request, 'myapp/index.html', {'stuForm': form})

def getStuList(request):