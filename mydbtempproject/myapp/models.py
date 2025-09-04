from django.db import models

# Create your models here.
class Student(models.Model):
    stuId = models.IntegerField()
    stuName = models.CharField(max_length=30)
    stuMarks = models.IntegerField()
