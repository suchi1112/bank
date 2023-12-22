

from django.db import models

# Create your models here.

class Form(models.Model):
        name = models.CharField(max_length=40, unique=True)
        date = models.DateField()
        age = models.IntegerField()
        gender = models.CharField(max_length=20, unique=True)
        mobilenumber = models.CharField(max_length=10)
        email = models.EmailField(unique=True)
        address = models.CharField(max_length=100, unique=True)
        district = models.CharField(max_length=100, blank=True, null=True)
        branch = models.CharField(max_length=100, blank=True, null=True)
        account = models.CharField(max_length=20, unique=True)
        material = models.CharField(max_length=20, blank=True, null=True)



