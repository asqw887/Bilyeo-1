from django.contrib.auth.models import AbstractUser
from django.db import models


class Myuser(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    rev_star = models.IntegerField() 
    nickname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)    # real name 
    number = models.IntegerField()