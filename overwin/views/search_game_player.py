from django.views import generic
from ..models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404,redirect

class GamePlayerSearchView(generic.ListView):
    template_name = "overwin/search_player.html"
    def get_queryset(self):
        query = self.request.GET.get('query')

        if query:
            game_player_list = Game_Player.objects.filter(battle_tag__icontains=query)
        else:
            game_player_list = Game_Player.objects.all()
        return game_player_list

@login_required
def favorite_game_player(request):
    player = get_object_or_404(GamePlayer, pk=request.user.pk)
    request.user.favorite_.add(player)
    return render(request, 'overwin/account_info.html')