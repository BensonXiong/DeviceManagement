from django.db import models
from pip._vendor.cachecontrol.heuristics import LastModified

class Device(models.Model):
    type = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    version = models.CharField(max_length=128)
    model = models.CharField(max_length=128)
    imei = models.CharField(max_length=128,unique=True)
    sn = models.CharField(max_length=128,unique=True)
    originOwner = models.CharField(max_length=128)
    borrower = models.CharField(max_length=128)
    borrowedAt = models.DateTimeField()
    returnAt = models.DateTimeField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField()
    LastModifiedAt = models.DateTimeField(auto_now=True)
    