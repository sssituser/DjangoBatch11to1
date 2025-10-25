from django.contrib import admin
from myapp.models import *
# Register your models here.
admin.site.register(Person)
admin.site.register(Employee)
admin.site.register(Manager)