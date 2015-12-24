import os
from time import timezone
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DeviceManagement.settings')

import django
django.setup()

from Dmanage.models import Device,History
from django.utils import timezone

def populate():
    and_device = add_device('Android','name1','version1','model1','imei1','sn1')
    sn = and_device.sn
    add_history(sn, 'owner1', 'checkin', timezone.localtime(timezone.now()))
    add_history(sn, 'owner2', 'checkout', timezone.localtime(timezone.now()))
    
    ios_device = add_device('Iphone','name2','version2','model2','imei2','sn2')
    sn = ios_device.sn
    add_history(sn, 'owner3', 'checkin', timezone.localtime(timezone.now()))
    add_history(sn, 'owner4', 'checkout', timezone.localtime(timezone.now()))
    
    
    for d in Device.objects.all():
        print "-{0}".format(str(d))
    
def add_device(type,name,version,model,imei,sn):
    d = Device.objects.get_or_create(type=type,name=name,version=version,model=model,imei=imei,sn=sn)[0]  
    return d

def add_history(sn,owner,action,dateAt):
    d = Device.objects.get(sn=sn)
    h = History.objects.get_or_create(device=d,owner=owner,action=action,dateAt=dateAt)[0]  
    return h

if __name__ == '__main__':
    print "Starting popluation script"
    populate()