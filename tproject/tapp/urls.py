from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views


app_name = 'social'
urlpatterns = [
    # url(r"^$", views.index),
    url(r"^VKAuth/", views.VKAuth),
    url(r"^YandexDirect/", views.YandexDirectAuth),
    url(r'', include('social_django.urls'))
]