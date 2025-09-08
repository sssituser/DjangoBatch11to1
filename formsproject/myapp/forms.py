from django import forms
class Student(forms.Form):
    stuId = forms.IntegerField()
    stuName = forms.CharField(max_length=30)
    stuAge = forms.IntegerField()
    stuMarks = forms.IntegerField()