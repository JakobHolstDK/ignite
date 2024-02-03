from django.shortcuts import render
from .models import host
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def HostList(request):
    try:
        host_entries = host.objects.all()
    except host.DoesNotExist:
        host_entries = {}
    return render(request, 'host_list.html', {'host_entries': host_entries})
