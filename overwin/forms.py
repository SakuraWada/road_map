from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from django import forms

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')

class RecruitmentForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email')

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = " "
    class Meta:
        model = User