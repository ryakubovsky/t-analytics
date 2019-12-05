from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r"^$", views.index),
    url(r"^VKAuth/", views.VKAuth),
    url(r"^VKAuth/?client_id=<int:vkUserId>", views.VKAuth)
]