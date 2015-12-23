from django.shortcuts import render
from Dmanage.models import Device
# Create your views here.
def index(request):
    devices_list = Device.objects.order_by('-name')
    context_dict = {'devices':devices_list}
    return render(request,'Dmanage/device_list.html',context_dict)


def borrowDevice(request,device_sn_slug):
    context_dict={}
    return render(request,'Dmanage/borrow_device.html',context_dict)
