# -*- coding=gb18030 -*-
from django.shortcuts import render
from Dmanage.models import Device,History
from Dmanage.forms import DeviceForm
from django.http.response import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.core.serializers.json import DateTimeAwareJSONEncoder
from django.template.context_processors import request
from django.db import transaction
from django.core import serializers
from DmanageConstant import *

import util
import json





# Create your views here.

def borrowDeviceForm(request,device_sn_slug):
    device = Device.objects.get(sn=device_sn_slug)
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        
        if form.is_valid():
            with transaction.atomic():
                owner = form.cleaned_data['owner']
                sn = form.cleaned_data['sn']
                deviceInstance = Device.objects.get(sn=sn)
                deviceInstance.borrowedAt = util.getLocalTime()
                deviceInstance.returnAt = None
                deviceInstance.owner = owner
                deviceInstance.save()
            
                _history = History.objects.create(device=deviceInstance)
                _history.action = DmanageConstant['CheckIn']
                _history.owner = owner
                _history.dateAt = deviceInstance.borrowedAt
                _history.save()
            return HttpResponseRedirect('/list')
      
        
    else:      
        device.owner = ""
        form = DeviceForm(instance = device)  
        print form  
    return render(request,'Dmanage/borrow_device_form.html',{'form':form,'device':device})
    

def return_device(request):
    sn = request.GET.get('sn')
    deviceInstance = Device.objects.get(sn=sn)
    owner = deviceInstance.owner
    if(deviceInstance.owner != DmanageConstant['SystemUser']):      
        deviceInstance.owner = DmanageConstant['SystemUser']
        deviceInstance.returnAt = util.getLocalTime()
        deviceInstance.save();
        
        _history = History.objects.create(device=deviceInstance)
        _history.action = DmanageConstant['CheckOut']
        _history.owner = owner
        _history.dateAt = deviceInstance.borrowedAt
        _history.save()
    return HttpResponse('200')


def list(request):
    return render(request,'Dmanage/device_list.html',{})

def device_history(request,device_sn_slug):
    return render(request,'Dmanage/device_history.html',{'slug':device_sn_slug})

def list_data(request):
    currentPage = int(request.GET.get('offset'))
    limit = int(request.GET.get('limit'))
    currentPage = currentPage /limit + 1
    search = request.GET.get('search')
    if (isinstance(currentPage, int)):
        currentPage = currentPage +1
    if (search):
        searchSql = 'name like "%{0}%" or version like "%{0}%"'.format(search)
        _device = Device.objects.extra(where=[searchSql])
    else:
        _device = Device.objects.all()
    paginator = Paginator(_device,limit)
    try:
        pageHistory = paginator.page(currentPage)
    except PageNotAnInteger:
        pageHistory = paginator.page(1)
    except EmptyPage:
        pageHistory = paginator.page(paginator.num_pages)
    total = paginator.count
    rows = util.preJsonEncode(pageHistory.object_list.values('name','version','model','imei','owner','borrowedAt','returnAt','slug'))
    jData =  {"total":total,"rows":rows}
    return HttpResponse(json.dumps(jData,cls=util.JSONDateTimeEncoder), content_type="application/json")  

def device_history_data(request,device_sn_slug):
    currentPage = int(request.GET.get('offset'))
    limit = int(request.GET.get('limit'))
    currentPage = currentPage /limit + 1
    _device = Device.objects.get(sn=device_sn_slug)
    _history = History.objects.filter(device__id=_device.id)
    paginator = Paginator(_history,limit)
    try:
        pageHistory = paginator.page(currentPage)       
    except PageNotAnInteger:
        pageHistory = paginator.page(1)
    except EmptyPage:
        pageHistory = paginator.page(paginator.num_pages)
    total = paginator.count
    rows = util.preJsonEncode(pageHistory.object_list.values('device','owner','action','dateAt'))
    jData =  {"total":total,"rows":rows}
    return HttpResponse(json.dumps(jData,cls=util.JSONDateTimeEncoder), content_type="application/json")  
