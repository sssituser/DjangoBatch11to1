from django.contrib import admin
from myapp.models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['EmpId','EmpName','EmpJoinDate']
admin.site.register(Employee,EmployeeAdmin)

