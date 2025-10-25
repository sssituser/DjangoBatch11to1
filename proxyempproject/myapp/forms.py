from django import forms
from myapp.models import Employee

class EmployeeForm(forms.ModelForm):
    EmpId = forms.IntegerField(label="Employee ID")
    EmpName = forms.CharField(max_length=30,label="Employee Name")
    EmpSal = forms.IntegerField(label="Employee Salary")
    class Meta:
        model = Employee
        fields = '__all__'