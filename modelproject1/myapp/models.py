from django.db import models

# Create your models here.
class Student(models.Model):
    rollnao=models.IntegerField()
    name = models.CharField(max_length=30)
    dob  = models.DateField()
    marks = models.IntegerField()
    email =models.EmailField()
    phone = models.CharField(max_length=30)
    address = models.TextField()

