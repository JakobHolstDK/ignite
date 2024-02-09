import pprint
import os
import redis
import json



from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import tenant, service, enabled_service



# Create your views here.


@csrf_exempt
def MainView(request):
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r.set('foo', 'bar')
    pprint.pprint(request.META['CSRF_COOKIE'])
    


    try:
        tenant_entries = tenant.objects.all()
    except tenant.DoesNotExist:
        tenant_entries = {}
    return render(request, 'MainView.html', {'tenant': tenant_entries})
