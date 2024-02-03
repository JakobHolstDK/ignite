from django.contrib import admin

from .models import host, SElinuxEvent, Setroubleshoot

admin.site.register(host)
admin.site.register(SElinuxEvent)
admin.site.register(Setroubleshoot)



# Register your models here.
