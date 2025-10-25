from django.urls import path
from myapp import views
urlpatterns = [
    path('',views.register_view),
    path('employees/',views.employees,name="emp_list"),
]