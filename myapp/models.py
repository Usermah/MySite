from django.db import models

# Create your models here.
class Student(models.Model):
    name= models.CharField(max_length=30)
    cell_no = models.CharField(max_length=15)
    dob = models.DateField()
    email= models.EmailField()