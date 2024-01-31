from django.contrib import admin

# Register your models here.

from .models import ZabbixDataType0, ZabbixDataType1, ZabbixDataType2, ZabbixDataType3, ZabbixDataType4

admin.site.register(ZabbixDataType0)
admin.site.register(ZabbixDataType1)
admin.site.register(ZabbixDataType2)
admin.site.register(ZabbixDataType3)
admin.site.register(ZabbixDataType4)

