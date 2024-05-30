from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from ..models import User

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')

class LoginForm(AuthenticationForm):
    class Meta:
        model = User

class AccountInfoUpdateForm(UserChangeForm):
    #TODO パスワードの変更処理
    password = None
    class Meta:
        model = User
        fields = ('username', 'email')