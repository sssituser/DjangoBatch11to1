from django.contrib import admin

# Register your models here.
from myapp.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display= ['rollnao','name','dob','marks','email','phone','address']
admin.site.register(Student,StudentAdmin)
