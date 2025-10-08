from django.contrib import admin
from myapp.forms import EmployeeForm
from myapp.models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display =["EmpId","EmpName","EmpImage","EmpDept"]
admin.site.register(Employee,EmployeeAdmin)
