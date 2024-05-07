from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")

class LoginForm(AuthenticationForm):
    class Meta:
        model = User