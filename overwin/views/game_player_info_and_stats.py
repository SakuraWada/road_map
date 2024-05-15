from ..models import *
from ..forms import *
from django.views import generic
from urllib.parse import unquote


class GamePlayerInfoView(generic.TemplateView):
    template_name = 'overwin/game_player_info.html'
# todo:コンテキストの処理とAPIから取得する関数を別にする
    def get_context_data(self, **kwargs):
        #親のget_context_dataを呼び出している。基本的なコンテキストデータが入っている
        context = super().get_context_data(**kwargs)
        battle_tag = self.request.GET.get('battle_tag')
        if battle_tag:
            # breakpoint()
            player = GamePlayer.objects.filter(battle_tag=battle_tag).first()
            context['player'] = player
        return context