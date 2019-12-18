from django import forms
from . import models
import random


class AddClientForm(forms.Form):
    # all_clients = models.Client.objects.all()
    # all_client_id = [client.client_id for client in all_clients]
    client_name = forms.CharField(max_length=256)
    client_id = forms.IntegerField()
    user_id = forms.IntegerField()
    # client_id = random.choice(list(set(range(1000)) - set(all_client_id)))

