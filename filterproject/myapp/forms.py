from myapp.models import Employee
from django import forms
class EmployeeForm(forms.ModelForm):
    EmpId = forms.IntegerField()
    EmpName = forms.CharField(max_length=30)
    EmpJoinDate = forms.DateField()
    class Meta:
        model=Employee
        fields='__all__'

