from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import MainView

routes = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(routes.urls)),
    path('', MainView,  name='ignite' )
]