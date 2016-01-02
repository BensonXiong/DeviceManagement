"""DeviceManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url,patterns
from django.contrib import admin
from Dmanage import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^borrowDeviceForm/$',views.borrowDeviceForm,name='borrowDeviceForm'),
    url(r'^return_device/$',views.return_device,name='returnDevice'),
    url(r'^list/$',views.list,name='list'),
    url(r'^list/(?P<device_sn_slug>\w+)/history/$',views.device_history,name='device_history'),
    url(r'^list/data$',views.list_data,name='list_data'),
    url(r'^list/(?P<device_sn_slug>\w+)/history/data$',views.device_history_data,name='device_history_data'),
    url(r'^login/$', views.user_login, name='login'), 
]
