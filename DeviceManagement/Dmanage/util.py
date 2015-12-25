from django.utils import timezone

def getLocalTime():
    return timezone.localtime(timezone.now())
    