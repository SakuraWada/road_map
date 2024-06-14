from django.views import generic
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from ..models import GamePlayer, FavoriteGamePlayer
from ..utils import fetch_data_from_api

@method_decorator(login_required, name="dispatch")
class GamePlayerSearchView(generic.ListView):
    template_name = "overwin/search_game_player/index.html"
    #検索時の動作
    def get_queryset(self):
        query = self.request.GET.get('query')

        if query:
            search_query = query.replace('#','-')

            #apiからデータを取得
            params    = {'name':search_query, 'limit': 200}
            json_data = fetch_data_from_api("players", params)

            #データのフィルタリング
            game_player_list = [
                {
                    'player_id'  : player['player_id']  , #（例）player-1234
                    'name'       : player['name']       , #（例）player#1234
                    'namecard'   : player['namecard']   ,
                    'title'      : player['title']      ,
                    'career_url' : player['career_url'] ,
                    'blizzard_id': player['blizzard_id'],
                }
                for player in json_data['results']
            ]

        else:
            game_player_list = []

        return game_player_list

    #お気に入り追加時の動作
    def post(self, request, *args, **kwargs):
        ## （例）player#1234"
        game_player_name = request.POST.get('game_player_name')

        ##GamePlayerモデルに登録されていないプレイヤーの場合モデルに登録
        if not GamePlayer.objects.filter(battle_tag=game_player_name).exists():
            game_player = GamePlayer(battle_tag=game_player_name)
            game_player.save()

        ##FavoriteGamePlayerモデルに登録
        add_game_player_name = GamePlayer.objects.get(battle_tag=game_player_name)
        favorite, created = FavoriteGamePlayer.objects.get_or_create(user=request.user, game_player=add_game_player_name)

        if created:
            is_favorite = True
        else:
            favorite.delete()
            is_favorite = False

        return JsonResponse({'is_favorite': is_favorite})

