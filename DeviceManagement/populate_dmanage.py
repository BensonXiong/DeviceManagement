import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DeviceManagement.settings')

import django
django.setup()

from Dmanage.models import Device

def populate():
    pass
    
def add_device():
    pass    

if __name__ == '__main__':
    print "Starting popluation script"
    populate()