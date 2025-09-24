from django import forms
from myapp.models import Employee


class EmployeeForm(forms.ModelForm):
    empId = forms.IntegerField()
    empName = forms.CharField(max_length=30)
    empSal = forms.FloatField()
    empDept = forms.CharField(max_length=30)
    class Meta:
        model = Employee
        fields ='__all__'