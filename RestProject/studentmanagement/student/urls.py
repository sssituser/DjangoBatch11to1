from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import Student
router = DefaultRouter()
router.register(r'students',Student)
urlpatterns=[
    path('',include(router.urls)),
]