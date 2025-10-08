from django import forms
from .models import Student
class StudentForm(forms.ModelForm):
    name=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    age=forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))           
    photo=forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))   
    enrollment_date=forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    class Meta:
        model = Student
        fields = '__all__'
