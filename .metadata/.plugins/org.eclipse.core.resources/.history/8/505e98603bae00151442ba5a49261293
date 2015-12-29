from django.shortcuts import render
from Dmanage.models import Device,History
from Dmanage.forms import DeviceForm
from django.http.response import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.core.serializers.json import DateTimeAwareJSONEncoder
from django.template.context_processors import request
from django.db import transaction
from django.core import serializers


import util
import json
from DmanageConstant import *

# Create your views here.
def index(request):
    _device = Device.objects.order_by('-name')
    paginator = Paginator(_device,DmanageConstant['PaginatorSize'])
    page = request.GET.get('page')
    try:
        pageResult = paginator.page(page)       
    except PageNotAnInteger:
        pageResult = paginator.page(1)
    except EmptyPage:
        pageResult = Paginator.page(Paginator.num_pages)
    context_dict = {'PageResults':pageResult,'devices':_device}    
    return render(request,'Dmanage/device_list.html',context_dict)

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

def device_history(request,device_sn_slug):
    _device = Device.objects.get(sn=device_sn_slug)
    _history = History.objects.filter(device__id=_device.id)
    paginator = Paginator(_history,DmanageConstant['PaginatorSize'])
    page = request.GET.get('page')
    try:
        pageHistory = paginator.page(page)       
    except PageNotAnInteger:
        pageHistory = paginator.page(1)
    except EmptyPage:
        pageHistory = Paginator.page(Paginator.num_pages)
    context_dict = {'historys':pageHistory,'device':_device}    
    return render(request,'Dmanage/device_history.html',context_dict)


def bootstrap(request):
    return render(request,'Dmanage/bootstrap.html',{})

def bootstrap_table_data(request):
    currentPage = request.GET.get('offset')
    limit = request.GET.get('limit')
    _device = Device.objects.all()
    paginator = Paginator(_device,limit)
    try:
        pageHistory = paginator.page(currentPage)
    except PageNotAnInteger:
        pageHistory = paginator.page(1)
    except EmptyPage:
        pageHistory = paginator.page(paginator.num_pages)
    total = paginator.count
    rows = util.preJsonEncode(pageHistory.object_list.values('name','version','model','imei','borrowedAt','returnAt','slug'))
    jData =  {"total":total,"rows":rows}
    return HttpResponse(json.dumps(jData,cls=util.JSONDateTimeEncoder), content_type="application/json")  
