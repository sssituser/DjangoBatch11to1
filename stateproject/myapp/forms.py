from django import forms
from myapp.models import User

class LoginForm(forms.Form):
    name=forms.CharField(max_length=100)    
    
    
