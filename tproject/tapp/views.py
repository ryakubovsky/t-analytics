from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from . import models
import requests, json, os, random
from django.conf import settings
from yaml import load


with open(os.path.join(settings.BASE_DIR, 'tapp/config.yaml')) as f:
    config = load(f)

# Create your views here.

YANDEX_KEY_ID = config['yandex']['YANDEX_KEY_ID']
YANDEX_SECRET_KEY = config['yandex']['YANDEX_SECRET_KEY']


def get_clients(request, user_id):
    if request.method == "POST":
        client_name = request.POST['client_name']

        all_clients = models.Client.objects.all()
        all_client_id = [client.client_id for client in all_clients]
        client_id = random.choice(list(set(range(1000)) - set(all_client_id)))

        client = models.Client(client_name=client_name, client_id=client_id, user_id=user_id)
        client.save()
    all_clients = models.Client.objects.all()
    return render(request, 'tapp/clients.html', context={"all_clients": all_clients})


def delete_client(request, user_id, client_id):
    client = models.Client.objects.get(user_id=user_id)
    client.delete()
    return HttpResponseRedirect(reverse('tapp:get_clients', args=(user_id, )))


def get_clients_info(request, user_id, client_id):
    try:
        yandex_direct = models.YandexDirect.objects.all().filter(user_id=user_id)
        client = models.Client.objects.get(client_id=client_id)
        context = {"yandex_direct": yandex_direct, "client": client.client_name, "user_id": user_id,
                   "client_id": client_id}
    except (KeyError, models.YandexDirect.DoesNotExist):
        client = models.Client.objects.get(user_id=user_id)
        context = {"client": client.client_name, "user_id": user_id,
                   "client_id": client_id}
    return render(request, 'tapp/client_info.html', context=context)


def about_yandex_direct(request, user_id, client_id):
    yandex = models.YandexDirect.objects.all().filter(user_id=user_id)
    return render(request, 'tapp/about_yandex_direct.html', context={"yandex": yandex})


def yandex_code(request):
    url = f"https://oauth.yandex.ru/authorize/?response_type=code&client_id={YANDEX_KEY_ID}"
    return HttpResponseRedirect(url)


def yandex_token(request):
    code = request.GET['code']
    headers = {"grant_type": "authorization_code", "code": code, "client_id": YANDEX_KEY_ID,
              "client_secret": YANDEX_SECRET_KEY}
    response = requests.post("https://oauth.yandex.ru/token", headers).json()
    passport = requests.get('https://login.yandex.ru/info', params={"format": "json",
                                                                    "oauth_token": response['access_token']}).json()

    data = {"login": passport['login'], "last_name": passport['last_name'], "first_name": passport['first_name'],
             "token": response['access_token'], "user_id": passport['id'], 'email': passport['default_email']}

    user = models.User.objects.get(pk=1)

    try:
        person = models.YandexDirect.objects.get(user_email=data['email'])
        person.token = data['token']
        person.save()
    except (KeyError, models.YandexDirect.DoesNotExist):
        models.YandexDirect.objects.create(token=data['token'], user_first_name=data['first_name'],
                                            user_last_name=data['last_name'], user_email=data['email'],
                                            user_id=user.user_id)

    return HttpResponseRedirect(reverse('tapp:get_clients', args=(user.user_id,)))










