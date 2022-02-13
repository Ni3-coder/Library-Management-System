from django.db import models

class asignup(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=8)

class book(models.Model):
    bname = models.CharField(max_length=50)
    writer = models.CharField(max_length=50)
    quantity = models.IntegerField()

def __str__(self):
    return self.bname




