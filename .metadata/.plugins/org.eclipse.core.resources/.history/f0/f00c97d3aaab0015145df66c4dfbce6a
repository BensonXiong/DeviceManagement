from django.db import models
from django.template.defaultfilters import slugify
from django.db.models.fields.related import ForeignKey

class Device(models.Model):
    TYPE_CHOICES = (('Android','And'),('Iphone','Ios'))
    type = models.CharField(max_length=128,choices=TYPE_CHOICES)
    name = models.CharField(max_length=128)
    version = models.CharField(max_length=128)
    model = models.CharField(max_length=128)
    imei = models.CharField(max_length=128,unique=True)
    sn = models.CharField(max_length=128,unique=True)
    owner = models.CharField(max_length=128,blank=True)
    borrowedAt = models.DateTimeField(blank=True,null=True)
    returnAt = models.DateTimeField(blank=True,null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    LastModifiedAt = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=128,unique=True)
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.sn)
        super(Device,self).save(*args,**kwargs)
    
    def __str__(self):
        return self.name
    

class History(models.Model):
    device = ForeignKey(Device)
    owner = models.CharField(max_length=128)
    action = models.CharField(max_length=128)
    dateAt = models.DateTimeField(blank=True,null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    LastModifiedAt = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return models.Model.__str__(self)
    
    