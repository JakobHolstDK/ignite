from django.contrib import admin
from .models import tenant, service, enabled_service

admin.site.register(tenant)
admin.site.register(service)
admin.site.register(enabled_service)  



# Register your models here.
