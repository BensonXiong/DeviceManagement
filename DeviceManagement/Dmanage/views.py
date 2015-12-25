from django.shortcuts import render
from Dmanage.models import Device
from Dmanage.forms import DeviceForm
from django.http.response import HttpResponse, HttpResponseRedirect

import util

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
            return HttpResponseRedirect('/list')
      
        
    else:      
        device.owner = ""
        form = DeviceForm(instance = device)  
        print form  
    return render(request,'Dmanage/borrow_device_form.html',{'form':form,'device':device})
    

def return_device(request):
    sn = request.GET.get('sn')
    deviceInstance = Device.objects.get(sn=sn)
    if(deviceInstance.owner != 'system'):      
        deviceInstance.owner = 'system'
        deviceInstance.returnAt = util.getLocalTime()
        deviceInstance.save();
    return HttpResponse('200')

