from django.db import models

# Create your models here.


class VKAuth(models.Model):
    vkToken = models.CharField(max_length=256)
    vkUserId = models.IntegerField()
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    access = models.CharField(max_length=128)
    clientSecret = models.CharField(max_length=256)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def __dict__(self):
        return {"first_name": self.first_name, "last_name": self.last_name, "vkUserId": self.vkUserId,
                "clientSecret": self.clientSecret, "vkToken": self.vkToken}

