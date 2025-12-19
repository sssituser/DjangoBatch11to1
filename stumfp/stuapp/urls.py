from django.urls import path
from stuapp import views

urlpatterns = [
    path('', views.StudentCreateView.as_view(), name='addStudent'),
    path('students/', views.StudentListView.as_view(), name='stulist'),
    path('update/<int:pk>/', views.StudentUpdateView.as_view(), name='editstudent'),
    path('show/<int:pk>/', views.StudentDetailView.as_view(), name='showstudent'),
    path('del/<int:pk>/', views.StudentDeleteView.as_view(), name='deletestudent'),
]

