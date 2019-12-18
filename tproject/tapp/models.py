from django.db import models

# Create your models here.


class YandexDirect(models.Model):
    token = models.CharField(max_length=256)
    client_id = models.CharField(max_length=256)
    user_first_name = models.CharField(max_length=256)
    user_last_name = models.CharField(max_length=256)
    user_email = models.CharField(max_length=256)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    user_id = models.IntegerField()

    def __str__(self):
        return f"{self.user_first_name} {self.user_last_name}"


class User(models.Model):
    user_name = models.CharField(max_length=256)
    user_surname = models.CharField(max_length=256)
    user_create = models.DateTimeField(auto_now_add=True)
    user_update = models.DateTimeField(auto_now=True)
    user_id = models.IntegerField()

    def __str__(self):
        return f"{self.user_name} {self.user_surname}"


class Client(models.Model):
    client_name = models.CharField(max_length=256)
    client_id = models.IntegerField()
    user_id = models.IntegerField()

    def __str__(self):
        return self.client_name


