from django.shortcuts import render
from rest_framework import viewsets
from .models import ZabbixDataType0, ZabbixDataType1, ZabbixDataType2, ZabbixDataType3, ZabbixDataType4

from .serializers import ZabbixDataType0Serializer, ZabbixDataType1Serializer, ZabbixDataType2Serializer, ZabbixDataType3Serializer, ZabbixDataType4Serializer

class ZabbixDataType0ViewSet(viewsets.ModelViewSet):
    queryset = ZabbixDataType0.objects.all()
    serializer_class = ZabbixDataType0Serializer

class ZabbixDataType1ViewSet(viewsets.ModelViewSet):
    queryset = ZabbixDataType1.objects.all()
    serializer_class = ZabbixDataType1Serializer

class ZabbixDataType2ViewSet(viewsets.ModelViewSet):
    queryset = ZabbixDataType2.objects.all()
    serializer_class = ZabbixDataType2Serializer

class ZabbixDataType3ViewSet(viewsets.ModelViewSet):
    queryset = ZabbixDataType3.objects.all()
    serializer_class = ZabbixDataType3Serializer

class ZabbixDataType4ViewSet(viewsets.ModelViewSet):
    queryset = ZabbixDataType4.objects.all()
    serializer_class = ZabbixDataType4Serializer



def ZabbixDataType0_list(request):
    type0_entries = ZabbixDataType0.objects.all()
    print(type0_entries)

    return render(request, 'ZabbixDataType0_list.html', {'type0_entries': type0_entries})

def ZabbixDataType1_list(request):
    type1_entries = ZabbixDataType1.objects.all()
    return render(request, 'ZabbixDataType1_list.html', {'type1_entries': type1_entries})

def ZabbixDataType2_list(request):
    type2_entries = ZabbixDataType2.objects.all()
    return render(request, 'ZabbixDataType2_list.html', {'type2_entries': type2_entries})
# Create your views here.
def ZabbixDataType3_list(request):
    type3_entries = ZabbixDataType3.objects.all()
    return render(request, 'ZabbixDataType3_list.html', {'type3_entries': type3_entries})

def ZabbixDataType4_list(request):
    type4_entries = ZabbixDataType4.objects.all()
    return render(request, 'ZabbixDataType4_list.html', {'type4_entries': type4_entries})