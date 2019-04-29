from __future__ import unicode_literals  
from django.db import models 
from django import forms

from phonenumber_field.modelfields import PhoneNumberField
from localflavor.us.models import USPostalCodeField, USStateField, USSocialSecurityNumberField, USZipCodeField
from localflavor.in_.forms import INAadhaarNumberField
from localflavor.in_.in_states import STATE_CHOICES
from django_countries import countries
import pytz
COUNTRY_CHOICES = tuple(countries)
TIMEZONE_CHOICES = tuple((choice, choice) for choice in pytz.common_timezones)
GENDER_CHOICES = (
				('',''),
				('male','Male'),
				('female', 'Female'),
			)
class Candidate(models.Model):    
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=50) # for creating varchar column  
    release_date = models.DateField()           # for creating date column  
    num_stars = models.IntegerField()
    postal_code = USPostalCodeField()
class Student(models.Model): 
    candidate_registration_no = models.SlugField()
    first_name = models.CharField(max_length=20) 
    middle_name= models.CharField(max_length=10)	
    last_name  = models.CharField(max_length=30) 	
    email      = models.EmailField(max_length=50)  
    age        = models.IntegerField()
    image      = models.ImageField()	
    DOB        = models.DateField()
    gender    = models.CharField(max_length=10, choices=GENDER_CHOICES)
    state    =   models.CharField(max_length=20, choices=STATE_CHOICES)
    country  =   models.CharField(max_length=20, choices=COUNTRY_CHOICES)
    address_line_1 = models.TextField(max_length=50)
    address_line_2 = models.TextField(max_length=30)
    zipcode = USZipCodeField()
    phone_number = PhoneNumberField()
    resume = models.FileField()
	