from django.views import generic
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from ..models import GamePlayer, FavoriteGamePlayer
from ..utils import fetch_data_from_api, convert_text

@method_decorator(login_required, name="dispatch")
class GamePlayerSearchView(generic.ListView):
    template_name = "overwin/search_game_player/index.html"
    #検索時の動作
    def get_queryset(self):
        query = self.request.GET.get('query')

        if not query:
            return []

        #apiからデータを取得
        params    = {'name':query, 'limit': 200}
        json_data = fetch_data_from_api("players", params)

        game_player_list = []
        for player in json_data['results']:
            try:
                game_player = GamePlayer.objects.get(battle_tag=player['name'])
                is_favorite = game_player.is_favorite(self.request.user)
            except GamePlayer.DoesNotExist:
                is_favorite = False
            if convert_text(query) not in convert_text(player["name"]):
                continue
            game_player_data = {
                    'player_id'  : player['player_id']  , #（例）player-1234
                    'name'       : player['name']       , #（例）player#1234
                    'namecard'   : player['namecard']   ,
                    'title'      : player['title']      ,
                    'career_url' : player['career_url'] ,
                    'blizzard_id': player['blizzard_id'],
                    'is_favorite': is_favorite,
            }
            game_player_list.append(game_player_data)


        return game_player_list

    #お気に入り追加時の動作
    def post(self, request, *args, **kwargs):
        ## （例）player#1234"
        game_player_name = request.POST.get('game_player_name')
        is_favorite = request.POST.get('is_favorite') == 'true'

        ## GamePlayerモデルに登録されていないプレイヤーの場合モデルに登録
        game_player, created = GamePlayer.objects.get_or_create(battle_tag=game_player_name)

        if is_favorite:
            FavoriteGamePlayer.objects.get_or_create(user=request.user, game_player=game_player)
        else:
            FavoriteGamePlayer.objects.filter(user=request.user, game_player=game_player).delete()

        return JsonResponse({'status': 'success'})

