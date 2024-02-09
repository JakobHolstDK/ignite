from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import host_list, message_list


routes = routers.DefaultRouter()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hostlist/', host_list, name='host_list'),
    path('messages/<pk>', message_list, name='message_list'),
    path('messages/', message_list, name='messages_list'),
    path('api/', include(routes.urls)),
]

