from django.db import models

# Create your models here.
class Student(models.Model):
    stuname=models.CharField(max_length=40)
    stuage = models.IntegerField()
    stuqual = models.CharField(max_length=40)
    stuemail = models.EmailField(unique=True)
   



