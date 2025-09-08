from django.db import models

# Create your models here.
class Student(models.Model):
    rollno = models.IntegerField()
    name = models.CharField(max_length=30)
    dob = models.DateField()
    marks = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    address = models.TextField()
class Employee(models.Model):
    eid=models.IntegerField()
    ename=models.CharField(max_length=30)
    esal = models.FloatField()
