from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from .enum import Role

class GamePlayer(models.Model):
    battle_tag = models.CharField(max_length=32, unique=True)
    def __str__(self):
        return self.battle_tag

    def is_favorite(self, user):
        return FavoriteGamePlayer.objects.filter(user=user, game_player=self).exists()


class User(AbstractUser):
    pass


class FavoriteGamePlayer(models.Model):
    user        = models.ForeignKey(User,       on_delete=models.CASCADE)
    game_player = models.ForeignKey(GamePlayer, on_delete=models.CASCADE, to_field='battle_tag')

    def __str__(self):
        return f"{self.user.username} - {self.game_player.battle_tag}"

class Recruitment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='募集者')

    max_recruit_member = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(4),
        ],
        verbose_name='募集人数',
    )

    current_member_count = models.PositiveIntegerField(default=0)
    tank_role_num        = models.IntegerField(default=0)
    damage_role_num      = models.IntegerField(default=0)
    support_role_num     = models.IntegerField(default=0)
    comment              = models.TextField(max_length=64, blank=True, null=True,verbose_name='コメント')

    @property
    def possible_to_entry(self):
        return self.current_member_count < self.max_recruit_member


class JoinMember(models.Model):
    recruitment        = models.ForeignKey(Recruitment, on_delete=models.CASCADE)
    join_member        = models.ForeignKey(User,        on_delete=models.CASCADE)
    message = models.TextField(blank=True, null=True)

    role = models.CharField(
        max_length=16,
        choices=Role.choices(),
        default=Role.FREE_ROLE.key,
    )

    is_approved = models.BooleanField(default=False)