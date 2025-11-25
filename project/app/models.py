from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    contact=models.IntegerField()
    image=models.ImageField(upload_to='image/')
    document=models.FileField(upload_to='file/')
    password=models.CharField(max_length=50)
 
    def __str__(self):
        return self.name
    
class Query(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    query=models.CharField(max_length=225)
    

class itames(models.Model):
    name=models.CharField(max_length=50)
    fess=models.IntegerField()
       