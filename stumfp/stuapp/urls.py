from django.urls import path
from stuapp import views

urlpatterns =[
    path('',views.index,name='addStudent'),
    path('students/',views.getStudents,name='stulist'),
    path('update/',views.editStudent,name='editstudent'),
    path('show/',views.showStudent,name='showstudent'),
    path('del/',views.delStudent,name='deletestudent'),
    
]
