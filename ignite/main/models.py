from django.db import models

class tenant(models.Model):
    tenant = models.CharField(max_length=128, primary_key=True)
    logo = models
    about = models.TextField()
    adress = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    email = models.EmailField()
    website = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tenant
    
    class Meta:
        db_table = 'tenant'
        verbose_name = 'tenant'
        verbose_name_plural = 'tenants'
        ordering = ['tenant']

class service(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'service'
        verbose_name = 'service'
        verbose_name_plural = 'services'
        ordering = ['name']

class enabled_service(models.Model):
    tenant = models.ForeignKey(tenant, on_delete=models.CASCADE)
    service = models.ForeignKey(service, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tenant
    
    class Meta:
        db_table = 'enabled_service'
        verbose_name = 'enabled_service'
        verbose_name_plural = 'enabled_services'
        ordering = ['tenant']


