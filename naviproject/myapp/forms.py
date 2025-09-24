from django import forms

class EmployeeForm(forms.Form):
    EmpId = forms.IntegerField()
    EmpName = forms.CharField(max_length=30)
    EmpSal = forms.IntegerField()