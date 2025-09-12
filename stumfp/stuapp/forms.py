from django import forms
from stuapp.models import Student

class StudentForm(forms.ModelForm):
    StuId = forms.IntegerField(label='Student ID')
    StuName = forms.CharField(label='Student Name')
    StuMarks = forms.IntegerField(label='Marks')
    class Meta:
        model = Student
        fields = '__all__'