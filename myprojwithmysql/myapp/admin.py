from django.contrib import admin
from myapp.models import Student,Employee
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['rollno','name','dob','marks','email','phone','address']
class EmployeeAdmin(admin.ModelAdmin):
    list_display=["eid","ename","esal"]
admin.site.register(Student,StudentAdmin)
admin.site.register(Employee,EmployeeAdmin)