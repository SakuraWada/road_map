from django.urls import path, include
from .views import mypage,account_register_and_login,search_favorite_player,account_info

app_name = "overwin"
urlpatterns = [
    path('mypage/', mypage.MyPageView.as_view(), name='mypage'),
    path('account_register/', account_register_and_login.AccountRegisterView.as_view(), name='account_register'),
    path('',account_register_and_login.LoginView.as_view(), name='login'),
    path('logout/',account_register_and_login.LogoutView.as_view(), name='logout'),
    path('search_player/',search_favorite_player.PlayerSearchView.as_view(), name='search_player'),
    path('account_info/', account_info.show_account_info, name='account_info'),
    path('account_info/update/', account_info.update_account_info, name='account_info_update'),
    path('account_delete', account_info.delete_account, name='account_delete'),
]