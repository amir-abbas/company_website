from django.db import models
from multi_email_field.fields import MultiEmailField

class AboutUs(models.Model):
    text=models.CharField(max_length=1000,blank=False)
    image=models.ImageField(upload_to=None,width_field=500,height_field=500,blank=True)

class Customer(models.Model):
    text=models.CharField(max_length=100,blank=False)
    image=models.ImageField(upload_to=None,height_field=500,width_field=500)
    sample=models.URLField(max_length=128,blank=True,db_index=False)

class Product(models.Model):
    text=models.CharField(max_length=100)
    image=models.ImageField(upload_to=None,width_field=500,height_field=500)

class ContactWithUs(models.Model):
    text=models.CharField(max_length=1000)
    image=models.ImageField(upload_to=None,width_field=500,height_field=500,blank=False)
    email=MultiEmailField()