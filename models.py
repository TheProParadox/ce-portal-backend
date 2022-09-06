from tkinter import CASCADE
from django.db import models

cities=(
    ('delhi','Delhi'),('Mumbai','Mumbai'),('Hyderabad','Hyderabad'),('Gurgaon','Gurgaon')
)

Competitions=(
    ('dance','Dance'),('Music','music'),('arts','Arts')
)


class Competition(models.Model):
     competitionName = models.CharField(max_length=50,choices=Competitions,default='Arts')

     def __str__(self):
        return self.name



class City(models.Model):
     cityName = models.CharField(max_length=50,choices=cities,default='delhi')
     competitions= models.ManyToManyField(Competition)
     def __str__(self):
        return self.name


class Entry(models.Model):
    name = models.CharField(max_length=50)
    city=models.ForeignKey(City,on_delete=models.CASCADE,choices=cities,default='delhi')
    Competition=models.ForeignKey(Competition,on_delete=models.CASCADE,choices=Competitions,default='Arts')
    Emailid=models.EmailField(max_length=500)
  
    
    def __str__(self):
        return self.name





    
