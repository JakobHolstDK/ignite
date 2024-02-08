import pprint

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import tenant, service, enabled_service

# Create your views here.


@csrf_exempt
def MainView(request):
    pprint.pprint(request)
    try:
        tenant_entries = tenant.objects.all()
    except tenant.DoesNotExist:
        tenant_entries = {}
    return render(request, 'MainView.html', {'tenant': tenant_entries})
