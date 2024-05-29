from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from ..models import User

class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = " "
    class Meta:
        model = User
        fields = ('username', 'email')

class LoginForm(AuthenticationForm):
    class Meta:
        model = User