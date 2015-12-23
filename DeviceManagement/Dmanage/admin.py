from django.contrib import admin
from Dmanage.models import Device
from django.contrib.admin.templatetags.admin_list import date_hierarchy
# Register your models here.
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name','type','createdAt')
    search_fields = ('name','type')
    date_hierarchy = 'createdAt'

admin.site.register(Device,DeviceAdmin)