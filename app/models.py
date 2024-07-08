from django.db import models
# Create your models here.
class Table(models.Model):
    name=models.TextField(max_length=50)
    flavour=models.TextField(max_length=200)
    topings=models.TextField(max_length=200)
    address=models.TextField(max_length=250)
    phno=models.TextField(max_length=20)
    time=models.TextField(max_length=50)
    quantity=models.TextField(max_length=200)


class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=12)
    
