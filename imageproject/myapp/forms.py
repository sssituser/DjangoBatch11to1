from django import forms
from myapp.models import Employee
class EmployeeForm(forms.ModelForm):
    EmpId = forms.IntegerField();
    EmpName = forms.CharField(max_length=30)
    EmpImage = forms.ImageField()
    EmpDept = forms.CharField(max_length=30)
    class Meta:
        model=Employee
        fields = '__all__'

