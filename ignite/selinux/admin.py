from django.contrib import admin

from .models import host, SElinuxEvent, Setroubleshoot, message, suggestion

admin.site.register(host)
admin.site.register(SElinuxEvent)
admin.site.register(Setroubleshoot)
admin.site.register(message)
admin.site.register(suggestion)




# Register your models here.
