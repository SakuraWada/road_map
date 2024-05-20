from ..models import *
from ..forms import *
from django.views import generic
from ..utils import fetch_data_from_api
import math

class GamePlayerInfoView(generic.TemplateView):
    template_name = 'overwin/game_player_info.html'


    def seconds_to_hour_and_minutes(self, seconds):
        hours = math.floor(seconds / 3600)
        minutes = math.floor((seconds % 3600) / 60)
        return f"{hours:02d}:{minutes:02d}"

    def kill_count_divide_death_count(self,kill_count,death_count):
        try:
            divided_num = round((kill_count / death_count),2)
        except ZeroDivisionError:
            divided_num = "-"
        return divided_num


    def fetch_player_info_by_battle_tag(self):
        battle_tag = self.request.GET.get('battle_tag')
        battle_tag_to_fetch = battle_tag.replace("#","-")

        try:
            #推薦レベル、ランク、アイコン、バナー、称号
            fetch_player_info_summary = fetch_data_from_api(f"players/{battle_tag_to_fetch}/summary", params=None)

            #データの作成
            player_info ={
                'avatar':           fetch_player_info_summary['avatar'],
                'namecard':         fetch_player_info_summary['namecard'],
                'title':            fetch_player_info_summary['title'],
                'endorsement':      fetch_player_info_summary['endorsement'],
                'tank_rank_cs' :    fetch_player_info_summary['competitive']['console']['tank'],
                'damage_rank_cs' :  fetch_player_info_summary['competitive']['console']['damage'],
                'support_rank_cs' : fetch_player_info_summary['competitive']['console']['support'],
                # 'tank_rank_pc' :    fetch_player_info_summary['competitive']['pc']['tank'],
                # 'damage_rank_pc' :  fetch_player_info_summary['competitive']['pc']['damage'],
                # 'support_rank_pc' : fetch_player_info_summary['competitive']['pc']['support'],
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
            #ヒーローごとの簡単なスタッツ
            fetch_hero_stats_summary = fetch_data_from_api(f"players/{battle_tag_to_fetch}/stats/summary", params={'gamemode':'competitive'})
            heroes_stats_summary_dict = fetch_hero_stats_summary["heroes"]
            #ヒーローの画像
            # fetch_hero_portrait = 

            player_hero_info = {}

            for hero_name, hero_stats in heroes_stats_summary_dict.items():
                kill_count = hero_stats["average"].get("eliminations", 0)
                death_count = hero_stats["average"].get("deaths", 0)
                kill_count_divide_death_count = self.kill_count_divide_death_count(kill_count,death_count)

                time_played = self.seconds_to_hour_and_minutes(hero_stats["time_played"])
                win_rate = hero_stats["winrate"]
                average_damage = int(hero_stats["average"].get("damage", 0))

                player_hero_info[hero_name] = {
                    "kill_count_divide_death_count" : kill_count_divide_death_count,
                    "time_played" :                   time_played,
                    "win_rate" :                      win_rate,
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
