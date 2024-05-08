from django.views import generic
from ..models import *

class PlayerSearchView(generic.ListView):
    template_name = "overwin/search_player.html"
    def get_queryset(self):
        query = self.request.GET.get('query')

        if query:
            game_player_list = Game_Player.objects.filter(battle_tag__icontains=query)
        else:
            game_player_list = Game_Player.objects.all()
        return game_player_list