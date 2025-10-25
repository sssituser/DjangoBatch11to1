from django.db import models

# Create your models here.
class Employee(models.ManyToOneRel):
    empId = models.IntegerField()
    empName = models.CharField(max_length=30)
    empSal = models.FloatField()
    empDept = models.CharField(max_length=30)