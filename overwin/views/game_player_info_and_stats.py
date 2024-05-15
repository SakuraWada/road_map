from ..models import *
from ..forms import *
from django.views import generic
import requests

class GamePlayerInfoView(generic.TemplateView):
    template_name = 'overwin/game_player_info.html'

    def get_context_data(self, **kwargs):
        #親のget_context_dataを呼び出している。基本的なコンテキストデータが入っている
        context = super().get_context_data(**kwargs)
        battle_tag = self.request.GET.get('battle_tag')
        if battle_tag:
            player = GamePlayer.objects.filter(battle_tag=battle_tag).first()
            context['player'] = player
        return context

    def fetch_stats_by_battle_tag(self):
        battle_tag = self.request.GET.get('battle_tag')
        battle_tag_to_fetch = battle_tag.replace("#","-")
        api_url = f'https://overfast-api.tekrop.fr/players/{battle_tag_to_fetch}/summary'

        try:
            response = requests.get(api_url)
# todo: APIエラーになったときの処理
        except Exception:
            pass
# todo: 200じゃなかったときの処理
        if response.status_code != 200:
            pass

        stats = response.json()
        return stats
