from django.urls import path
from .views.mypage import MyPageView
from .views.account_register_and_login import AccountRegisterView, LoginView, LogoutView
from .views.game_player_info_and_stats import GamePlayerInfoView
from .views.search_game_player import GamePlayerSearchView
from .views.favorite_game_player import FavoritePlayerView
from .views.account_info import AccountInfoView,UpdateAccountInfoView,DeleteAccountInfoView
from .views.party_recruitment import RecruitmentListView,PartyRecruitmentCreateView,PartyRecruitmentDetailView,PartyRecruitmentDeleteView, PartyRecruitmentUpdateView


app_name = "overwin"
urlpatterns = [
    #mypage関連
    path('mypage/',               MyPageView.as_view(),               name='mypage'),
    #accountのログイン、登録関連
    path('account-register/',     AccountRegisterView.as_view(),      name='account_register'),
    path('',                      LoginView.as_view(),                name='login'),
    path('logout/',               LogoutView.as_view(),               name='logout'),
    #個人戦績
    path('game-player-info/',     GamePlayerInfoView.as_view(),       name='game_player_info'),
    #プレイヤー検索
    path('search-game-player/',   GamePlayerSearchView.as_view(),     name='search_game_player'),
    #お気に入りプレイヤー表示
    path('favorite-game-player/', FavoritePlayerView.as_view(),       name='favorite_game_player'),
    #アカウント情報関連
    path('account-info/',         AccountInfoView.as_view(),                  name='account_info'),
    path('account-info/update/',  UpdateAccountInfoView.as_view(),                name='account_info_update'),
    path('account-info/delete/',        DeleteAccountInfoView.as_view(),                     name='account_delete'),
    #パーティー募集
    path('party-recruitment/',            RecruitmentListView.as_view(),        name='party_recruitment_list'),
    path('party-recruitment/create/',          PartyRecruitmentCreateView.as_view(), name='party_recruitment_create'),
    path('party-recruitment/<int:pk>/delete/', PartyRecruitmentDeleteView.as_view(), name='party_recruitment_delete'),
    path('party-recruitment/<int:pk>/detail/', PartyRecruitmentDetailView.as_view(), name='party_recruitment_detail'),
    path('party-recruitment/<int:pk>/update/', PartyRecruitmentUpdateView.as_view(), name='party_recruitment_update'),
]
