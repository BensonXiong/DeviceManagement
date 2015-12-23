from django.contrib import admin
from Dmanage.models import Device
from django.contrib.admin.templatetags.admin_list import date_hierarchy
from django.contrib.admin.templatetags.admin_modify import prepopulated_fields_js
# Register your models here.
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name','type','slug','createdAt')
    search_fields = ('name','type')
    prepopulated_fields = {'slug':('sn',)}

admin.site.register(Device,DeviceAdmin)