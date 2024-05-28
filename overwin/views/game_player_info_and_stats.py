from ..models import GamePlayer
from django.views import generic
from ..utils import fetch_data_from_api, rate_calculation, seconds_to_hour_and_minutes
import math

class GamePlayerInfoView(generic.TemplateView):
    template_name = 'overwin/game_player_info.html'

    def fetch_player_info_by_battle_tag(self):
        battle_tag = self.request.GET.get('battle_tag')
        battle_tag_to_fetch = battle_tag.replace("#","-")

        try:
            #推薦レベル、ランク、アイコン、バナー、称号
            fetch_player_info_summary = fetch_data_from_api(f"players/{battle_tag_to_fetch}/summary", params=None)

            player_info ={
                'avatar':           fetch_player_info_summary['avatar'],
                'namecard':         fetch_player_info_summary['namecard'],
                'title':            fetch_player_info_summary['title'],
                'endorsement':      fetch_player_info_summary['endorsement'],
                'tank_rank_cs' :    fetch_player_info_summary['competitive']['console']['tank'],
                'damage_rank_cs' :  fetch_player_info_summary['competitive']['console']['damage'],
                'support_rank_cs' : fetch_player_info_summary['competitive']['console']['support'],
            }

        # todo: APIエラーになったときの処理
        except Exception:
            pass
        # todo: 200じゃなかったときの処理
        # if response.status_code != 200:
        #     pass

        return player_info

    def fetch_player_hero_info_by_battle_tag(self):
        battle_tag = self.request.GET.get('battle_tag')
        battle_tag_to_fetch = battle_tag.replace("#","-")

        try:
            #ヒーローごとの簡単なスタッツを取得
            fetch_hero_stats_summary = fetch_data_from_api(f"players/{battle_tag_to_fetch}/stats/summary", params={'gamemode':'competitive'})

            heroes_stats_summary_dict = fetch_hero_stats_summary["heroes"]
            #TODO:ヒーローの画像も入れる

            player_hero_info = {}

            for hero_name, hero_stats in heroes_stats_summary_dict.items():
                time_played = seconds_to_hour_and_minutes(hero_stats["time_played"])
                win_rate = hero_stats["winrate"]

                kill_count = hero_stats["average"].get("eliminations", 0)
                death_count = hero_stats["average"].get("deaths", 0)
                kill_count_divide_death_count = rate_calculation(kill_count,death_count,2)

                average_damage = int(hero_stats["average"].get("damage", 0))

                player_hero_info[hero_name] = {
                    "time_played" :                   time_played,
                    "win_rate" :                      win_rate,
                    "kill_count_divide_death_count" : kill_count_divide_death_count,
                    "average_damage" :                average_damage,
                }

        # todo: APIエラーになったときの処理
        except Exception:
            pass
        # todo: 200じゃなかったときの処理
        # if response.status_code != 200:
        #     pass
        return player_hero_info

    def get_context_data(self, **kwargs):
        #親のget_context_dataを呼び出している。基本的なコンテキストデータが入っている
        context = super().get_context_data(**kwargs)
        battle_tag = self.request.GET.get('battle_tag')
        if battle_tag:
            player = GamePlayer.objects.filter(battle_tag=battle_tag).first()
            context['player'] = player
            context['player_info'] = self.fetch_player_info_by_battle_tag()
            context['player_hero_info'] = self.fetch_player_hero_info_by_battle_tag()
        return context
