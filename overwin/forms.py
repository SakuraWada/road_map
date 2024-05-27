from django.contrib.auth.forms import UserCreationForm
from .models import User,Recruitment
from django import forms

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')

class RecruitmentForm(forms.ModelForm):
    class Meta:
        model = Recruitment
        fields = ['max_recruit_member', 'comment']
