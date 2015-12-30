from django.contrib import admin
from Dmanage.models import Device,History
from django.contrib.admin.templatetags.admin_list import date_hierarchy
from django.contrib.admin.templatetags.admin_modify import prepopulated_fields_js
# Register your models here.
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name','type','version','model','imei','sn','owner')
    search_fields = ('name','type')
    prepopulated_fields = {'slug':('sn',)}

class HistoryAdmin(admin.ModelAdmin):
    list_display = ('device','owner','action','dateAt')
    search_fields = ('owner',)

admin.site.register(Device,DeviceAdmin)
admin.site.register(History,HistoryAdmin)