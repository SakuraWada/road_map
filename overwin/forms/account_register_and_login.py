from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from ..models import User
from ..forms_utils import CustomForm

class UserRegisterForm(CustomForm, UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')

class LoginForm(CustomForm, AuthenticationForm):
    class Meta:
        model = User

class AccountInfoUpdateForm(CustomForm, UserChangeForm):
    #TODO パスワードの変更処理
    password = None
    class Meta:
        model = User
        fields = ('username', 'email')