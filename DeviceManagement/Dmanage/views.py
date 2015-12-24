from django.shortcuts import render
from Dmanage.models import Device
from Dmanage.forms import DeviceForm
from django.http.response import HttpResponse
from django.utils import timezone

# Create your views here.
def index(request):
    devices_list = Device.objects.order_by('-name')
    context_dict = {'devices':devices_list}
    return render(request,'Dmanage/device_list.html',context_dict)

def borrowDevice(request,device_sn_slug):
    device = Device.objects.get(sn=device_sn_slug)
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        
        if form.is_valid():
            pass
        
    else:
        form = DeviceForm(instance = device)  
        print form  
    return render(request,'Dmanage/borrow_device.html',{'form':form})

def borrow_Device(request):
    if request.method == 'POST':
        print request
        form = DeviceForm(request.POST)
        
        if form.is_valid():
            pass
        
    else:
        form = DeviceForm()    
    return render(request,'Dmanage/borrow_device.html',{'form':form})


def return_device(request):
    sn = request.GET.get('sn')
    deviceInstance = Device.objects.get(sn=sn)
    deviceInstance.owner = 'system'
    deviceInstance.returnAt = timezone.localtime(timezone.now())
    deviceInstance.save();
    return HttpResponse('200')