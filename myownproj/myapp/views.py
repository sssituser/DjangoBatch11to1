from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect to a success page or another view
    else:
        form = ProductForm()
    return render(request, 'myapp/register.html', {'form': form})
def product_list(request):
    products = Product.objects.all()
    return render(request, 'myapp/products.html', {'products': products})