from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from models import User
from forms import CustomForm

class UserRegisterForm(CustomForm, UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')

class LoginForm(CustomForm, AuthenticationForm):
    class Meta:
        model = User