from django.db import models

# Create your models here.
class Empoyee(models.Model):
    empId = models.IntegerField()
    empName = models.CharField(max_length=30)
    empSal = models.FloatField()
class Student(models.Model):
      stuId = models.IntegerField()
      stuName = models.CharField(max_length=30)
      stuMarks = models.IntegerField()
    
    
