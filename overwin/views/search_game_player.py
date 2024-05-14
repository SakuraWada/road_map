from django.views import generic
from ..models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404

@method_decorator(login_required, name="dispatch")
class GamePlayerSearchView(generic.ListView):
    template_name = "overwin/search_game_player.html"
    #検索時の動作
    def get_queryset(self):
        query = self.request.GET.get('query')

        if query:
            game_player_list = GamePlayer.objects.filter(battle_tag__icontains=query)
        else:
            game_player_list = GamePlayer.objects.all()
        return game_player_list
    #お気に入り追加時の動作
    def post(self, request, *args, **kwargs):
        favorite_game_player_ids = request.POST.getlist('favorite_player')
        for game_player_id in favorite_game_player_ids:
            game_player = get_object_or_404(GamePlayer, id=game_player_id)
            favorite, created = FavoriteGamePlayer.objects.get_or_create(user=request.user, game_player=game_player)
        return self.get(request, *args, **kwargs)