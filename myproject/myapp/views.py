from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def home(request):
    date  = datetime.datetime.now()
    h = int(date.strftime('%H'))
    res = '<h1> Hi guest '
    if h<12 :
        res += ' Good morning !!!'
    elif h<16:
        res+= ' Good Afternoon !!!'
    elif h<21:
        res += ' Good Evenging !!!'
    else:
        res += ' Good night !!!'
    res +='</h1><hr>'
    res +='<h1> Server time is : '+str(date)+'</h1>'
    return HttpResponse(res)
def register(request):
    res ="<h1>Register Here</h1>"
    return HttpResponse(res)
def login(request):
    res = "<h1> Login here </h1>"
    return HttpResponse(res)
    



