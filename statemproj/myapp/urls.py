from django.urls import path
from myapp import views
urlpatterns =[
    path('',views.addEmployee_view),
    path('/emplist',views.employeelist_view,name="employeelist"),
    path('/empedit/<int:id>/',views.employeeedit_view,name='emp_edit'),
    path('/aggregate/',views.aggrigate_view,name="aggregate"),
]

