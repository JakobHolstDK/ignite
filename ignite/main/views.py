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
  create_response = client.secrets.kv.v2.get.secret(
    path=path,
  )
  if create_response.status_code == 200:
    print("Vault secret found")
    return True
  else:
    print("Vault secret not found")
  return  False



@csrf_exempt
def MainView(request):
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    sessionkey = request.META['CSRF_COOKIE']
    while not r.exists(sessionkey):
        print("waiting for session key")
        checkvault(sessionkey)
    print("session key found")

    try:
        tenant_entries = tenant.objects.all()
    except tenant.DoesNotExist:
        tenant_entries = {}
    return render(request, 'MainView.html', {'tenant': tenant_entries})
