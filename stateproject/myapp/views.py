from django.shortcuts import render, redirect
from myapp.forms import LoginForm

def logn_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            response = redirect('second_view')  # Redirect instead of render
            response.set_cookie('uname', name, max_age=86400)
            return response
    return render(request, 'myapp/login.html', {'form': form})

def second_view(request):
    name = request.COOKIES.get('uname', 'Guest')
    return render(request, 'myapp/second.html', {'name': name})
