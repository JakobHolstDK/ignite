
from .models import ZabbixDataType0, ZabbixDataType1, ZabbixDataType2, ZabbixDataType3, ZabbixDataType4

from rest_framework import serializers

class ZabbixDataType0Serializer(serializers.ModelSerializer):
    class Meta:
        model = ZabbixDataType0
        fields = '__all__'

class ZabbixDataType1Serializer(serializers.ModelSerializer):
    class Meta:
        model = ZabbixDataType1
        fields = '__all__'

class ZabbixDataType2Serializer(serializers.ModelSerializer):
    class Meta:
        model = ZabbixDataType2
        fields = '__all__'

class ZabbixDataType3Serializer(serializers.ModelSerializer):
    class Meta:
        model = ZabbixDataType3
        fields = '__all__'

class ZabbixDataType4Serializer(serializers.ModelSerializer):
    class Meta:
        model = ZabbixDataType4
        fields = '__all__'


