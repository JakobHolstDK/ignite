from django.db import models

class metadata(models.Model):
    tenant = models.CharField(max_length=128, primary_key=True)
    logo = models
    def __str__(self):
        return self.tenant
    
    class Meta:
        db_table = 'host'
        verbose_name = 'host'
        verbose_name_plural = 'hosts'
        ordering = ['hostname']