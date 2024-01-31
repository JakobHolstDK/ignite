from django.db import models

class ZabbixDataType0(models.Model):
    id = models.AutoField(primary_key=True)
    clock = models.DateTimeField(null=False)
    host_name = models.CharField(max_length=255, null=False)
    item_id = models.IntegerField(null=False)
    item_name = models.CharField(max_length=255, blank=True, null=True)
    ns = models.BigIntegerField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)  # Using FloatField for double precision
    data_type = models.IntegerField(blank=True, null=True)
    class Meta:
        db_table = 'zabbixdatatype0'
        verbose_name = 'ZabbixDataType0'
        verbose_name_plural = 'ZabbixDataType0'
        ordering = ['host_name']

class ZabbixDataType1(models.Model):
    id = models.AutoField(primary_key=True)
    clock = models.DateTimeField()
    host_name = models.CharField(max_length=255)
    item_id = models.IntegerField()
    item_name = models.CharField(max_length=255, blank=True, null=True)
    ns = models.BigIntegerField(blank=True, null=True)
    value = models.BigIntegerField(blank=True, null=True)
    data_type = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'zabbixdatatype1'
        verbose_name = 'ZabbixDataType1'
        verbose_name_plural = 'ZabbixDataType1'
        ordering = ['host_name']

class ZabbixDataType2(models.Model):
    id = models.AutoField(primary_key=True)
    clock = models.DateTimeField(null=False)
    host_name = models.CharField(max_length=255, null=False)
    item_id = models.IntegerField(null=False)
    item_name = models.CharField(max_length=255, blank=True, null=True)
    ns = models.BigIntegerField(blank=True, null=True)
    value = models.BigIntegerField(blank=True, null=True)
    data_type = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'zabbixdatatype2'
        verbose_name = 'ZabbixDataType2'
        verbose_name_plural = 'ZabbixDataType2'
        ordering = ['host_name']

class ZabbixDataType3(models.Model):
    id = models.AutoField(primary_key=True)
    clock = models.DateTimeField(null=False)
    host_name = models.CharField(max_length=255, null=False)
    item_id = models.IntegerField(null=False)
    item_name = models.CharField(max_length=255, blank=True, null=True)
    ns = models.BigIntegerField(blank=True, null=True)
    value = models.BigIntegerField(blank=True, null=True)
    data_type = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'zabbixdatatype3'
        verbose_name = 'ZabbixDataType3'
        verbose_name_plural = 'ZabbixDataType3'
        ordering = ['host_name']


class ZabbixDataType4(models.Model):
    id = models.AutoField(primary_key=True)
    clock = models.DateTimeField(null=False)
    host_name = models.CharField(max_length=255, null=False)
    item_id = models.IntegerField(null=False)
    item_name = models.CharField(max_length=255, blank=True, null=True)
    ns = models.BigIntegerField(blank=True, null=True)
    fsname = models.CharField(max_length=512, null=False)
    options = models.CharField(max_length=512, blank=True, null=True)
    bytes_used = models.BigIntegerField(blank=True, null=True)
    bytes_free = models.BigIntegerField(blank=True, null=True)
    bytes_total = models.BigIntegerField(blank=True, null=True)
    bytes_pused = models.FloatField(blank=True, null=True)
    bytes_pfred = models.FloatField(blank=True, null=True)
    fstype = models.CharField(max_length=24, blank=True, null=True)
    inodes_used = models.BigIntegerField(blank=True, null=True)
    inodes_free = models.BigIntegerField(blank=True, null=True)
    inodes_total = models.BigIntegerField(blank=True, null=True)
    inodes_pused = models.FloatField(blank=True, null=True)
    inodes_pfree = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'zabbixdatatype4'
        verbose_name = 'ZabbixDataType4'
        verbose_name_plural = 'ZabbixDataType4'
        ordering = ['host_name']
        

               
        
        
        