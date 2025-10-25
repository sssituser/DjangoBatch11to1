from django.db import models

# Create your models here.


class CustomerManager1(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(EmpSal__gte=15000)

    
class CustomerManager2(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(EmpSal__lte=15000)
    
class CustomerManager3(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by("EmpId")
    
class Employee(models.Model):
    EmpId =models.IntegerField()
    EmpName = models.CharField(max_length=30)
    EmpSal = models.IntegerField()
    objects = CustomerManager2()
    
    
class ProxyEmployee1(Employee):
    objects = CustomerManager2()
    class Meta:
        proxy=True

class ProxyEmployee2(Employee):
    objects = CustomerManager3()
    class Meta:
        proxy=True
