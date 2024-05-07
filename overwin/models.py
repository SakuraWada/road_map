from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass

class Player(models.Model):
    battle_tag = models.CharField(max_length=32)
    favorite_players = models.ManyToManyField('Player', related_name='favorited_by')

