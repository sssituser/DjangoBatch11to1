from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_employee, name='add_employee'),
    path('employees/', views.show_employees, name='show_employees'),
]
