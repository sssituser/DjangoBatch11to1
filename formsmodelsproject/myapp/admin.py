from django.contrib import admin
from myapp.models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['empId','empName','empSal','empDept']
admin.site.register(Employee,EmployeeAdmin)
