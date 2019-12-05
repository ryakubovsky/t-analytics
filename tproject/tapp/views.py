from django.shortcuts import render
from django.http import HttpResponse
from . import models
import requests
import json

# Create your views here.

def index(request):
    return HttpResponse("Hello world!")


def VKAuth(request):
    all_objects = models.VKAuth.objects.get(id=1)
    try:
        code = request.GET['code']
        token = requests.get(f"https://oauth.vk.com/access_token/?client_id={all_objects.vkUserId}&client_secret={all_objects.clientSecret}&redirect_uri=http://127.0.0.1:8001/tapp/VKAuth/&code={code}")
        all_objects.vkToken = token.json()['access_token']
        all_objects.save
        return render(request, 'tapp/VKAuth.html', {"all_objects": all_objects, "code": token.json()['access_token']})
    except:
        return render(request, 'tapp/VKAuth.html', {"all_objects": all_objects, "code": "Нет кода"})
