from django.shortcuts import render, redirect
from .forms import RegistrationForm


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Normally save user to DB here
            return redirect("success")
    else:
        form = RegistrationForm()
    return render(request, "accounts/register.html", {"form": form})


def success(request):
    return render(request, "accounts/success.html")
