from django.contrib import admin
from myapp.models import Student,Empoyee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['empId','empName','empSal']
class StudentAdmin(admin.ModelAdmin):
    list_display=['stuId','stuId','stuMarks']
admin.site.register(Empoyee,EmployeeAdmin)
admin.site.register(Student,StudentAdmin)