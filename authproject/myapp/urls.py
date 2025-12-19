from django.urls import path
from myapp import views
urlpatterns=[
    path('',views.home_view),
    path('javaexam/',views.javaexam_view),
    path('pythonexam/',views.pythonexam_view),
   
]