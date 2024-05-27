from .models import Recruitment
from django import forms

class RecruitmentForm(forms.ModelForm):
    class Meta:
        model = Recruitment
        fields = ['max_recruit_member', 'comment']