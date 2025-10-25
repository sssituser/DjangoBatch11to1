# from django.db import models

# # Create your models here.
# class ConactInfo(models.Model):
#     name = models.CharField(max_length=30)
#     email = models.EmailField()
#     address = models.CharField(max_length=30)
#     class Meta:
#         abstract = True
        
# class Student(ConactInfo):
#     rollno = models.IntegerField()
#     marks = models.IntegerField()
# class Teacher(ConactInfo):
#     subject = models.CharField(max_length=30)
#     salary = models.IntegerField()
from django.db import models

# Create your models here.
class ConactInfo1(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=30)
        
class Student1(ConactInfo1):
    rollno = models.IntegerField()
    marks = models.IntegerField()
class Teacher1(ConactInfo1):
    subject = models.CharField(max_length=30)
    salary = models.IntegerField()
    