from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *
from django import forms

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')

class LoginForm(AuthenticationForm):
    class Meta:
        model = User

class RecruitmentForm(forms.ModelForm):
    class Meta:
        model = Recruitment
        fields = ['max_recruit_member', 'comment']
