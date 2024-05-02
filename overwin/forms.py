from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password",)
