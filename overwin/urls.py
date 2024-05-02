from django.urls import path
from .views import mypage,account_register_and_login

app_name = "overwin"
urlpatterns = [
    path('', mypage.MyPageView.as_view(), name='mypage'),
    path('account_register/', account_register_and_login.AccountRegisterView.as_view(), name='account_register'),
]