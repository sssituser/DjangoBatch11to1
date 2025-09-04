from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("<h1> Hi Iam home page from  firstapp</h1")

def about(request):
    return HttpResponse("<h1> Hi Iam about page from firstapp</h1>")
