from django.db import models
from pip._vendor.cachecontrol.heuristics import LastModified

class Device(models.Model):
    type_choices = (('Android':'And'),('Iphone':'Ios'),)
    type = models.CharField(max_length=128,)
    name = models.CharField(max_length=128)
    version = models.CharField(max_length=128)
    model = models.CharField(max_length=128)
    imei = models.CharField(max_length=128,unique=True)
    sn = models.CharField(max_length=128,unique=True)
    originOwner = models.CharField(max_length=128,blank=True)
    borrower = models.CharField(max_length=128,blank=True)
    borrowedAt = models.DateTimeField(blank=True)
    returnAt = models.DateTimeField(blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    LastModifiedAt = models.DateTimeField(auto_now=True)
    