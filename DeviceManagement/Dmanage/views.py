from django.shortcuts import render
from Dmanage.models import Device,History
from Dmanage.forms import DeviceForm
from django.http.response import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.template.context_processors import request
from django.db import transaction


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
    jData =  {"total":233,"rows":[{"id":1,"name":"Item 1","price":"$1"},{"id":10,"name":"Item 10","price":"$10"},{"id":11,"name":"Item 11","price":"$11"},{"id":12,"name":"Item 12","price":"$12"},{"id":13,"name":"Item 13","price":"$13"},{"id":14,"name":"Item 14","price":"$14"},{"id":15,"name":"Item 15","price":"$15"},{"id":16,"name":"Item 16","price":"$16"},{"id":17,"name":"Item 17","price":"$17"},{"id":18,"name":"Item 18","price":"$18"}]}
    return HttpResponse(json.dumps(jData), content_type="application/json")  
