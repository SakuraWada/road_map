from django.contrib.auth.forms import AuthenticationForm
from models import *

class LoginForm(AuthenticationForm):
    class Meta:
        model = User