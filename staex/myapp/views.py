from myapp.forms import LoginForm
from django.shortcuts import redirect, render


def login_view(request):
    form =LoginForm()
    if request.method == 'POST':
        form= LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['name']
            response = redirect('main_view')
            response.set_cookie('uname', uname)
            return response 
    return render(request, 'myapp/login.html', {'form': form})
    
def main_view(request):
    uname = request.COOKIES.get('uname')
    return render(request, 'myapp/main.html', {'uname': uname}) 

