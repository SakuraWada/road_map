from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from ..models import User

class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = " "
    class Meta:
        model = User
        fields = ('username', 'email')

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = " "
    class Meta:
        model = User
class AccountInfoUpdateForm(UserChangeForm):
    #TODO パスワードの変更処理
    password = None
    class Meta:
        model = User
        fields = ('username', 'email')
