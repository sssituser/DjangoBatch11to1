from django.contrib import admin
from myapp.models import Employee
# Register your models here.
class EmpoyeAdmin(admin.ModelAdmin):
    list_display=['eno','ename','esal']
admin.site.register(Employee,EmpoyeAdmin)
