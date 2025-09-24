from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.AddEmployee),
    path('emps/',views.Employeesview,name='emplist')
   
]