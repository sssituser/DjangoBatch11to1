from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hi Iam Index page from second app");

def contact(request):
    return HttpResponse("Hi Iam contact page from second app");