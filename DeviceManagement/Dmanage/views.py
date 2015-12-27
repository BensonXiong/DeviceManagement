from django.shortcuts import render
from Dmanage.models import Device,History
from Dmanage.forms import DeviceForm
from django.http.response import HttpResponse, HttpResponseRedirect,\
    JsonResponse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


import util
import json
from django.template.context_processors import request

# Create your views here.
def index(request):
    devices_list = Device.objects.order_by('-name')
    context_dict = {'devices':devices_list}
    return render(request,'Dmanage/device_list.html',context_dict)

def borrowDeviceForm(request,device_sn_slug):
    device = Device.objects.get(sn=device_sn_slug)
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        
        if form.is_valid():
            owner = form.cleaned_data['owner']
            sn = form.cleaned_data['sn']
            deviceInstance = Device.objects.get(sn=sn)
            deviceInstance.borrowedAt = util.getLocalTime()
            deviceInstance.returnAt = None
            deviceInstance.owner = owner
            deviceInstance.save()
            
            _history = History.objects.create(device=deviceInstance)
            _history.action = 'checkin'
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
    if(deviceInstance.owner != 'system'):      
        deviceInstance.owner = 'system'
        deviceInstance.returnAt = util.getLocalTime()
        deviceInstance.save();
        
        _history = History.objects.create(device=deviceInstance)
        _history.action = 'checkout'
        _history.owner = owner
        _history.dateAt = deviceInstance.borrowedAt
        _history.save()
    return HttpResponse('200')

def device_history(request,device_sn_slug):
    _device = Device.objects.get(sn=device_sn_slug)
    _history = History.objects.filter(device__id=_device.id)
    paginator = Paginator(_history,5)
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

def bootstrap_json(request):
    jData =   [{
    "id":"10001",
    "invited_name": "a",
    "invited_phone": "15018735211",
    "invited_email": "zhangsan@163.com",
    "inviter_name": "b",
    "inviter_org": "c",
    "invite_time": "",
    "status": "e",
  }]
    return HttpResponse(json.dumps(jData), content_type="application/json")  
