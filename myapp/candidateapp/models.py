from __future__ import unicode_literals  
from django.db import models 
from django import forms
from phonenumber_field.modelfields import PhoneNumberField
class Countries(models.Model):
     country_name = models.CharField(max_length=20) 
     def __str__(self):
         return self.country_name
class Candidate(models.Model):    
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=50) # for creating varchar column  
    release_date = models.DateField()                        # for creating date column  
    num_stars = models.IntegerField()
class Student(models.Model):  
    first_name = models.CharField(max_length=20)  
    last_name  = models.CharField(max_length=30)  
    email      = models.EmailField(max_length=50)  
    age        = models.IntegerField()
    image      = models.ImageField()	
    DOB        = models.DateField()
    zipcode =    models.SlugField()
    phone_number = PhoneNumberField()
    resume = models.FileField()
    countries = models.ForeignKey(Countries, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.first_name + self.last_name + self.contact + self.email + self.age