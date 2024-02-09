from django.shortcuts import render
from .models import host, message, suggestion
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def host_list(request):
    try:
        host_entries = host.objects.all()
    except host.DoesNotExist:
        host_entries = {}
    return render(request, 'host_list.html', {'host_entries': host_entries})

@csrf_exempt
def message_list(request, pk=None):
    if pk:
        messages = message.objects.filter(hostname=pk)
    else:
        messages = message.objects.all()
    return render(request, 'message_list.html', {'messages': messages})

@csrf_exempt
def suggestion_list(request, pk=None, message=None):
    suggestions = suggestion.objects.all()
    return render(request, 'suggestion_list.html', {'suggestions': suggestions})

