import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DeviceManagement.settings')

import django
django.setup()

from Dmanage.models import Device

def populate():
    and_device = add_device('Android','name1','version1','model1','imei1','sn1')
    
    ios_device = add_device('Iphone','name2','version2','model2','imei2','sn2')
    
    for d in Device.objects.all():
        print "-{0}".format(str(d))
    
def add_device(type,name,version,model,imei,sn):
    d = Device.objects.get_or_create(type=type,name=name,version=version,model=model,imei=imei,sn=sn)[0]  
    return d

if __name__ == '__main__':
    print "Starting popluation script"
    populate()