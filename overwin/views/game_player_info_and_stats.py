from ..models import *
from ..forms import *
from django.views import generic
from ..utils import fetch_data_from_api

class GamePlayerInfoView(generic.TemplateView):
    template_name = 'overwin/game_player_info.html'


    def fetch_info_by_battle_tag(self):
        battle_tag = self.request.GET.get('battle_tag')
        battle_tag_to_fetch = battle_tag.replace("#","-")

        try:
            #推薦レベル、ランク、アイコン、バナー、称号
            fetch_player_info_summary = fetch_data_from_api(f"players/{battle_tag_to_fetch}/summary", params=None)
            #ヒーローごとの簡単なスタッツ
            #TODO ヒーロー情報も含める
            fetch_hero_stats_summary = fetch_data_from_api(f"players/{battle_tag_to_fetch}/stats/summary", params=None)

            #TODO 非公開時の処理

            #データの作成
            player_info ={
                'username': fetch_player_info_summary['username'],
                'avatar': fetch_player_info_summary['avatar'],
                'namecard': fetch_player_info_summary['namecard'],
                'title': fetch_player_info_summary['title'],
                'endorsement': fetch_player_info_summary['endorsement']
            }

# todo: APIエラーになったときの処理
        except Exception:
            pass
# todo: 200じゃなかったときの処理
        # if response.status_code != 200:
        #     pass

        return player_info

    def get_context_data(self, **kwargs):
        #親のget_context_dataを呼び出している。基本的なコンテキストデータが入っている
        context = super().get_context_data(**kwargs)
        battle_tag = self.request.GET.get('battle_tag')
        if battle_tag:
            player = GamePlayer.objects.filter(battle_tag=battle_tag).first()
            context['player'] = player
            context['player_data'] = self.fetch_info_by_battle_tag()
        return context
