from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))               
    pimage = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))    
    class Meta:
        model = Product
        fields = '__all__'