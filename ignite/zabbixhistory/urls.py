from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import ZabbixDataType0_list, ZabbixDataType1_list, ZabbixDataType2_list, ZabbixDataType3_list, ZabbixDataType4_list, ZabbixDataType0ViewSet, ZabbixDataType1ViewSet, ZabbixDataType2ViewSet, ZabbixDataType3ViewSet, ZabbixDataType4ViewSet

routes = routers.DefaultRouter()
routes.register('datatype0', ZabbixDataType0ViewSet)
routes.register('datatype1', ZabbixDataType1ViewSet)
routes.register('datatype2', ZabbixDataType2ViewSet)
routes.register('datatype3', ZabbixDataType3ViewSet)
routes.register('datatype4', ZabbixDataType4ViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('datatype0', ZabbixDataType0_list, name='ZabbixDataType0_list'),
    path('datatype1', ZabbixDataType1_list, name='ZabbixDataType1_list'),
    path('datatype2', ZabbixDataType2_list, name='ZabbixDataType2_list'),
    path('datatype3', ZabbixDataType3_list, name='ZabbixDataType3_list'),
    path('datatype4', ZabbixDataType4_list, name='ZabbixDataType4_list'),
    path('api/', include(routes.urls)),
]



