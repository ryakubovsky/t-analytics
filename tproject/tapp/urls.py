from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views


app_name = 'tapp'
urlpatterns = [
    url(r"^$", views.index),
    url(r"^VKAuth/", views.VKAuth),
    url(r"^YandexDirect/", views.YandexDirectAuth),
]