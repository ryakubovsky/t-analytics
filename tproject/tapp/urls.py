from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

app_name = 'tapp'

urlpatterns = [
    path("uid-<int:user_id>/", views.get_clients, name='get_clients'),
    path("uid-<int:user_id>/cid-<int:client_id>/", views.get_clients_info, name="get_clients_info"),
    path("uid-<int:user_id>/cid-<int:client_id>/delete", views.delete_client, name="delete_client"),
    path("uid-<int:user_id>/cid-<int:client_id>/yandex-direct/", views.about_yandex_direct, name="about_yandex_direct"),
    url(r"^yandex-direct/code/", views.yandex_code, name="yandex_code"),
    url(r"^yandex-direct/token/", views.yandex_token, name="yandex_token"),
    # url(r"^login/yandex/$", views.YandexDirectCode),
    # url(r"^login/yandex/user/", views.YandexDirectUser)
]