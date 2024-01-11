from django.db import models
from django.contrib.auth.models import User


class UserType(models.Model):
    type_name = models.CharField(max_length=20)

    def __str__(self):
        return self.type_name


class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.OneToOneField(UserType, null=False, on_delete=models.PROTECT)

    def __str__(self):
        return self.user.username

