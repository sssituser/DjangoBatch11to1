from django import forms
from myapp.models import Student
class StudentForm(forms.ModelForm):
    stuId = forms.IntegerField()
    stuName = forms.CharField(max_length=30)
    stuMarks = forms.IntegerField()
    class Meta:
            model = Student
            fields = '__all__'
