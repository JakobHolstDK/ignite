import pprint
import os
import redis
import json
import hvac



from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import tenant, service, enabled_service



# Create your views here.
def checkvault(path):
  ign8_vault_url  = os.environ.get("VAULT_URL", "https://vault.openknowit.com")
  ign8_vault_token = os.environ.get("VAULT_TOKEN", "s.5Y9pZ4x6y3sZ4y3s")
  client = hvac.Client(
    url=ign8_vault_url,
    token=ign8_vault_token,
  )
  read_response = client.secrets.kv.v2.read_secret_version(path=path)
  pprint.pprint(read_response['data']['data'])
  try:
     machineid = read_response['data']['data']['machineid']
  except:
     machineid = "unknown"
  
  if machineid != "unknown":
    print("Vault secret found : we have a login from machineid: " + machineid)
    return True
  else:
    print("Vault secret not found")
  return  False



@csrf_exempt
def MainView(request):
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    try:
        sessionkey = request.META['CSRF_COOKIE']
    except:
        sessionkey = "unknown"
        tenant_entries = {}
        return render(request, 'MainView.html', {'tenant': tenant_entries})

    while not r.exists(sessionkey):
        print("waiting for session key")
        if checkvault(sessionkey):
            r.set(sessionkey, "session key found", ex=600)
    print("session key found")

    try:
        tenant_entries = tenant.objects.all()
    except tenant.DoesNotExist:
        tenant_entries = {}
    return render(request, 'MainView.html', {'tenant': tenant_entries})
