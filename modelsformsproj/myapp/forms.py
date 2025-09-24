from django import forms
from myapp.models import Employee

class EmployeesForm(forms.ModelForm):
    Eid = forms.IntegerField()
    Ename = forms.CharField(max_length=30)
    Esal = forms.FloatField()
    class Meta:
        model=Employee
        fields = '__all__'
        widgets = {
            'Eid': forms.NumberInput(attrs={'placeholder': 'Enter Employee ID'}),
            'Ename': forms.TextInput(attrs={'placeholder': 'Enter Employee Name'}),
            'Esal': forms.NumberInput(attrs={'placeholder': 'Enter Salary'}),
        }