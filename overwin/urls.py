from django.urls import path, include
from .views import mypage,account_register_and_login,search_favorite_player

app_name = "overwin"
urlpatterns = [
    path('', mypage.MyPageView.as_view(), name='mypage'),
    path('account_register/', account_register_and_login.AccountRegisterView.as_view(), name='account_register'),
    path('login/',account_register_and_login.LoginView.as_view(), name='login'),
    path('logout/',account_register_and_login.LogoutView.as_view(), name='logout'),
    path('search_player/',search_favorite_player.PlayerSearchView.as_view(), name='search_player')
]