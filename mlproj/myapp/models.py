from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=30)
    age = models.IntegerField()
class Employee(Person):
    eno = models.IntegerField()
    esal = models.FloatField
class Manager(Employee):
    exp= models.ImageField()
    team_sizze = models.IntegerField()