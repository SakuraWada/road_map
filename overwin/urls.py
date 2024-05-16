from django.urls import path
from .views.mypage import MyPageView
from .views.account_register_and_login import AccountRegisterView, LoginView, LogoutView
from .views.game_player_info_and_stats import GamePlayerInfoView
from .views.search_game_player import GamePlayerSearchView
from .views.favorite_game_player import FavoritePlayerView
from .views.account_info import show_account_info,update_account_info,delete_account


app_name = "overwin"
urlpatterns = [
    #mypage関連
    path('mypage/',               MyPageView.as_view(),           name='mypage'),
    #accountのログイン、登録関連
    path('account_register/',     AccountRegisterView.as_view(),  name='account_register'),
    path('',                      LoginView.as_view(),            name='login'),
    path('logout/',               LogoutView.as_view(),           name='logout'),
    #個人戦績
    path('game_player_info/',     GamePlayerInfoView.as_view(),   name='game_player_info'),
    #プレイヤー検索
    path('search_game_player/',   GamePlayerSearchView.as_view(), name='search_game_player'),
    #お気に入りプレイヤー表示
    path('favorite_game_player/', FavoritePlayerView.as_view(),   name='favorite_game_player'),
    #アカウント情報関連
    path('account_info/',         show_account_info,              name='account_info'),
    path('account_info/update/',  update_account_info,            name='account_info_update'),
    path('account_delete',        delete_account,                 name='account_delete'),
]