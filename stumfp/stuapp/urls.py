from django.urls import path
from stuapp import views


urlpatterns =[
    path('',views.index,name='addStudent'),
    path('students/',views.getStudents,name='stulist'),
    path('update/<int:id> ',views.editStudent,name='editstudent'),
    path('show/<int:id>',views.showStudent,name='showstudent'),
    path('del/<int:id>',views.delStudent,name='deletestudent'),
    
]

