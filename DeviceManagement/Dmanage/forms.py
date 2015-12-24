from django import forms
from Dmanage.models import Device

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ('owner',)