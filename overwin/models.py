from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class GamePlayer(models.Model):
    battle_tag = models.CharField(max_length=32)
    def __str__(self):
        return self.battle_tag

class User(AbstractUser):
    pass

class FavoriteGamePlayer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game_player = models.ForeignKey(GamePlayer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.game_player.battle_tag}"
