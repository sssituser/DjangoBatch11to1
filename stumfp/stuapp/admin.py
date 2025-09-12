from django.contrib import admin
from stuapp.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display =['StuId','StuName','StuMarks']
admin.site.register(Student,StudentAdmin)


