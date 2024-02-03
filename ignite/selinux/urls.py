from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import HostList


routes = routers.DefaultRouter()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hostlist/', HostList, name='host-list'),
    path('api/', include(routes.urls)),
]

