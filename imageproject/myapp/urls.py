from django.urls import path
from myapp import views

urlpatterns =[
    path("",views.reg_employee,name="reg_employee"),
    path("employees/",views.showEmployees,name="getEmployees"),
]  

