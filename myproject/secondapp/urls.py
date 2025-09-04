from django.urls import path
from secondapp import views
urlpatterns=[
    path('index/',views.index),
    path('contact/',views.contact),
]