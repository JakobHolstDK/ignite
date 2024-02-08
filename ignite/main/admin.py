from django.contrib import admin
from .models import tenant, service, enabled_service, TutorialCategory, TutorialSeries, Tutorial

admin.site.register(tenant)
admin.site.register(service)
admin.site.register(enabled_service)  
admin.site.register(TutorialCategory)
admin.site.register(TutorialSeries)
admin.site.register(Tutorial)




# Register your models here.
