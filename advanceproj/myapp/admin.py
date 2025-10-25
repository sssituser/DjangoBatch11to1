from django.contrib import admin
from myapp.models import Teacher1,Student1,ConactInfo1
# Register your models here.
class StudentAdmin1(admin.ModelAdmin):
    list_display=['name','email','address','rollno','marks']
class TeacherAdmin1(admin.ModelAdmin):
   list_display=['name','email','address','subject','salary']
class ContactInfo1Admin(admin.ModelAdmin):
    list_display=['name','email','address']
admin.site.register(Teacher1,TeacherAdmin1)
admin.site.register(Student1,StudentAdmin1)
admin.site.register(ConactInfo1,ContactInfo1Admin)
