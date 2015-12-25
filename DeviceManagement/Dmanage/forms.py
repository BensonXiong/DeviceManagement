from django import forms
from Dmanage.models import Device

class DeviceForm(forms.ModelForm):
    owner = forms.CharField(max_length=128,label="Your name")
    sn = forms.CharField(max_length=128,widget=forms.HiddenInput(),validators=[])
    class Meta:
        model = Device
        fields = ('owner','sn',)
        
    def clean(self):
        cleaned_data = self.cleaned_data