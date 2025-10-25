from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

def add_employee(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_employees')
    return render(request, 'index.html', {'form': form})

def show_employees(request):
    employees = Employee.objects.select_related('department').all()
    return render(request, 'show_employees.html', {'employees': employees})

