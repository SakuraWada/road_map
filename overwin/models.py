from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    slug = models.SlugField(unique=True)

class Game_Player(models.Model):
    battle_tag = models.CharField(max_length=32)
    def __str__(self):
        return self.battle_tag

class Favorite_Game_Player(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    game_player_id = models.ForeignKey(Game_Player, on_delete=models.CASCADE)
    # favorite_game_player = models.ManyToManyField(Game_Player, verbose_name='お気に入りプレイヤー',blank=True)
    def __str__(self):
        return self.User.username

