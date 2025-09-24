from django.db import models

# Create your models here.
class Employee(models.Model):
    Eid = models.IntegerField()
    Ename = models.CharField(max_length=30)
    Esal = models.FloatField()