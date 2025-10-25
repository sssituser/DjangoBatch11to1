from django.db import models

# Create your models here.
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    # One Department → Many Employees
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')

    def __str__(self):
        return self.name
