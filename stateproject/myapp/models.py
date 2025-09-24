from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30,primary_key=True)
    emaild =  models.EmailField(max_length=40,unique=True)
    image = models.ImageField(upload_to='myapp/images/')
    password = models.CharField(max_length=30)
    confirmPassword = models.CharField(max_length=30)