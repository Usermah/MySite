from django.db import models

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    phone = models.CharField(max_length=15)


    def __str__(self):
        return self.name
