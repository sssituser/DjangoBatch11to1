from django.urls import path
from myapp import views

urlpatterns =[
    path('',views.home,name='home'),
    path('register/',views.register,name='signup'),
    path('login/',views.login,name='signin'),
]